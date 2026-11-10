#!/usr/bin/env python3
"""Render the per-release API changes pages from oasdiff's changelog.

`oasdiff changelog -f json` classifies every change between two OpenAPI schemas
as breaking (ERR), a warning (WARN) or informational (INFO), one entry per
change. Its own markdown output lists them by endpoint in schema order, with no
summary and no severity order -- the 8.1.3 release came to some 8,000 lines --
so this script renders the page instead:

- a summary of how many changes of each kind the release brings;
- removed and added endpoints;
- breaking changes, counted by kind, then listed by endpoint: changes to
  requests first, then to responses, and new values in response enums last,
  collapsed;
- warnings, listed by endpoint;
- everything else, collapsed.

Description-only edits are not changelog entries in oasdiff, so they never show
up here; the full structural diff (`oasdiff diff`) is linked for those.

Severity is oasdiff's, with the overrides in `oasdiff-severity-levels.txt`
(passed as `--severity-levels`): removed request fields, query parameters and
optional response fields are breaking for Waldur clients, and the page's
explanation of "breaking" says so. Run oasdiff with that file.

A ``HEAD`` change that repeats a ``GET`` change of the same path is left out:
Django serves a ``HEAD`` for every ``GET`` and the schema mirrors it, so the
change would otherwise be listed twice. A ``HEAD`` that is not such a mirror --
a ``HEAD`` added to an existing ``GET``, or one with its own meaning such as the
existence check on ``/api/openportal-managed-projects/{identifier}/{destination}/``
-- keeps its changes. For the same reason a request-body change, which oasdiff
reports once per media type the endpoint accepts, is listed once, and a change
made the same way on many endpoints (a renamed security scheme, a field of a
shared serializer) is listed once with the number of endpoints.

Usage:

    render_api_changes.py page --changelog changelog.json --version 8.1.4 \
        --previous 8.1.3 --oasdiff-version v1.34.1 \
        [--full-diff full/waldur-openapi-schema-8.1.4-diff-full.md] -o page.md
    render_api_changes.py index --dir docs/integrator-guide/APIs/api-changes

Standard library only: it runs in the plain Python image of the upload job.
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

LEVEL_ERR = 3
LEVEL_WARN = 2

ENDPOINT_ADDED = "endpoint-added"

METHOD_ORDER = {
    method: index
    for index, method in enumerate(
        ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE"]
    )
}

# Changes not tied to one operation (e.g. a removed component schema).
GENERAL = "General"

DIFF_PAGE_RE = re.compile(r"^waldur-openapi-schema-(\d+(?:\.\d+)*)-diff\.md$")

# Usually last in the text, but oasdiff can follow it with other notes, such as
# "(shared schema: ...)".
MEDIA_TYPE_RE = re.compile(r" ?\(media type: ([^)]+)\)")

# The request media types every DRF endpoint with a body accepts. A change
# reported for all of them is listed once with no media type; one reported for
# only some names them.
REQUEST_MEDIA_TYPES = frozenset(
    {"application/json", "application/x-www-form-urlencoded", "multipart/form-data"}
)

# A change made the same way on this many endpoints is listed once.
FOLD_MIN_ENDPOINTS = 10
MANY_ENDPOINTS = "On many endpoints"

# Breaking changes are listed in this order, each group under its own heading.
REQUESTS = "Requests"
RESPONSES = "Responses"
RESPONSE_ENUM_VALUES = "New values in response enums"


def is_endpoint_removal(change) -> bool:
    """Whether ``change`` removes a whole operation or path.

    oasdiff has several such checks, by whether the endpoint was deprecated
    first and whether its sunset date had passed: ``api-removed-*`` for an
    operation, ``api-path-removed-*`` for a path.
    """
    return change["id"].startswith(("api-removed-", "api-path-removed-"))


def version_key(version: str):
    return tuple(int(part) for part in version.split("."))


def endpoint_key(endpoint):
    method, path = endpoint
    if method is None:
        return (1, "", 0)
    return (0, path, METHOD_ORDER.get(method, len(METHOD_ORDER)))


def endpoint_title(endpoint) -> str:
    method, path = endpoint
    if method is None:
        return GENERAL
    return f"`{method} {path}`"


CODE_SPAN_RE = re.compile(r"(`[^`]*`)")


def escape(text: str) -> str:
    """Keep change texts from being read as HTML by Markdown.

    oasdiff quotes names and values in backticks, and Markdown shows a code
    span literally: escaping a ``<`` there would put ``&lt;`` on the page
    (``array<string>``). Only a ``<`` outside a code span is escaped.
    """
    parts = CODE_SPAN_RE.split(text)
    return "".join(
        part if index % 2 else part.replace("<", "&lt;")
        for index, part in enumerate(parts)
    ).strip()


def load_changes(path: Path) -> list:
    # oasdiff prints `[]` for identical schemas; be lenient about empty output.
    changes = json.loads(path.read_text(encoding="utf-8") or "null") or []
    return merge_media_types(drop_mirrored_heads(changes))


def drop_mirrored_heads(changes) -> list:
    """Leave out each ``HEAD`` change that repeats a ``GET`` change of its path."""

    def key(change):
        return (change["id"], change["level"], change.get("path"), change["text"])

    get_changes = {key(c) for c in changes if c.get("operation") == "GET"}
    return [
        c for c in changes if c.get("operation") != "HEAD" or key(c) not in get_changes
    ]


def merge_media_types(changes) -> list:
    """List a change once when oasdiff reports it once per request media type.

    A request-body change comes once for each media type the endpoint accepts,
    with the type in a trailing "(media type: ...)". Entries that differ only in
    that suffix become one, in the position of the first; it names the media
    types unless they are all of ``REQUEST_MEDIA_TYPES``.
    """
    merged = {}
    for change in changes:
        match = MEDIA_TYPE_RE.search(change["text"])
        text = MEDIA_TYPE_RE.sub("", change["text"]) if match else change["text"]
        key = (
            change["id"],
            change["level"],
            change.get("operation"),
            change.get("path"),
            text,
        )
        if key not in merged:
            merged[key] = (dict(change, text=text), [])
        if match:
            merged[key][1].append(match.group(1))

    result = []
    for entry, media_types in merged.values():
        if media_types and set(media_types) != REQUEST_MEDIA_TYPES:
            label = "media type" if len(media_types) == 1 else "media types"
            entry["text"] += f" ({label}: {', '.join(media_types)})"
        result.append(entry)
    return result


def breaking_group(change) -> str:
    """Which part of the breaking changes ``change`` is listed in.

    Requests come first: a client that sends what used to be valid now gets an
    error. Responses next: a client may fail on what it now receives. A new
    value in a response enum breaks only a client that validates enums
    strictly, and such changes are the bulk of most releases, so they come last.
    """
    change_id = change["id"]
    if change_id.startswith("response-"):
        if change_id.endswith("enum-value-added"):
            return RESPONSE_ENUM_VALUES
        return RESPONSES
    return REQUESTS


def group_by_endpoint(changes) -> dict:
    grouped = defaultdict(list)
    for change in changes:
        grouped[(change.get("operation"), change.get("path"))].append(change)
    return grouped


def render_by_endpoint(changes, indent: str = "") -> list:
    """One bold label per endpoint, one line per change.

    Labels, not headings: a release touches hundreds of endpoints, and a heading
    each would bury the page's five sections in its table of contents.

    A change made the same way on ``FOLD_MIN_ENDPOINTS`` or more endpoints is
    listed once, first, with the number of endpoints: renaming a security scheme
    in 8.1.0 removed it from 2,207 endpoints in one go.
    """
    endpoints_by_change = defaultdict(set)
    for change in changes:
        endpoints_by_change[(change["id"], change["text"])].add(
            (change.get("operation"), change.get("path"))
        )
    folded = {
        key
        for key, endpoints in endpoints_by_change.items()
        if len(endpoints) >= FOLD_MIN_ENDPOINTS
    }

    lines = []
    if folded:
        lines += [f"{indent}**{MANY_ENDPOINTS}**", ""]
        for key in sorted(folded, key=lambda k: (-len(endpoints_by_change[k]), k[1])):
            count = len(endpoints_by_change[key])
            lines.append(f"{indent}- {escape(key[1])} ({count:,} endpoints)")
        lines.append("")

    grouped = group_by_endpoint(
        [c for c in changes if (c["id"], c["text"]) not in folded]
    )
    for endpoint in sorted(grouped, key=endpoint_key):
        lines += [f"{indent}**{endpoint_title(endpoint)}**", ""]
        lines += [f"{indent}- {escape(change['text'])}" for change in grouped[endpoint]]
        lines.append("")
    return lines


def render_endpoint_list(changes) -> list:
    endpoints = sorted(
        {(change.get("operation"), change.get("path")) for change in changes},
        key=endpoint_key,
    )
    return [f"- {endpoint_title(endpoint)}" for endpoint in endpoints] + [""]


def kind_label(change_id: str) -> str:
    return change_id.replace("-", " ").capitalize()


def render_page(changes, version, previous, oasdiff_version, full_diff=None) -> str:
    removed = [c for c in changes if is_endpoint_removal(c)]
    added = [c for c in changes if c["id"] == ENDPOINT_ADDED]
    listed_elsewhere = {id(c) for c in removed + added}

    breaking = [c for c in changes if c["level"] >= LEVEL_ERR]
    warnings = [c for c in changes if c["level"] == LEVEL_WARN]
    info = [c for c in changes if c["level"] < LEVEL_WARN]

    breaking_rest = [c for c in breaking if id(c) not in listed_elsewhere]
    warnings_rest = [c for c in warnings if id(c) not in listed_elsewhere]
    info_rest = [c for c in info if id(c) not in listed_elsewhere]

    # Removed endpoints have their own row, so the breaking row counts the rest
    # and adds up with the table under "Breaking changes".
    breaking_endpoints = {
        (c.get("operation"), c.get("path")) for c in breaking_rest if c.get("operation")
    }

    lines = [
        f"# API changes in {version}",
        "",
        f"Changes to the Waldur REST API between **{previous}** and "
        f"**{version}**, computed from the two releases' OpenAPI schemas with "
        f"[oasdiff](https://github.com/oasdiff/oasdiff) {oasdiff_version}.",
        "",
        "**Breaking** changes can break an existing client: a removed endpoint, "
        "field or query parameter, a request field that became required or "
        "stricter, a response that can now hold values it could not before (a "
        "new enum value, a wider type, a field that became optional or "
        "nullable). A removed request field or query parameter is not rejected, "
        "but ignored: the client's value is silently dropped. A removed response "
        "field is breaking even where the schema marks it optional, which it "
        "does only because a client may ask for a subset of fields. "
        "**Warnings** may break a client, depending on how it uses the field.",
        "",
        "A `HEAD` change that repeats the `GET` change of its path is left out. "
        f"A change made the same way on {FOLD_MIN_ENDPOINTS} or more endpoints "
        f"is listed once, under *{MANY_ENDPOINTS}*, with the number of "
        "endpoints.",
        "",
        "| Changes | Count |",
        "|---|---:|",
        f"| Breaking, besides removed endpoints | {len(breaking_rest):,} in "
        f"{len(breaking_endpoints):,} endpoints |",
        f"| Warnings | {len(warnings):,} |",
        f"| Endpoints removed | {len(removed):,} |",
        f"| Endpoints added | {len(added):,} |",
        f"| Other changes | {len(info_rest):,} |",
        "",
    ]
    if full_diff:
        lines += [
            f"The [full schema diff]({full_diff}) lists every difference "
            "between the two schemas, description edits included.",
            "",
        ]

    if not changes:
        lines += ["The API did not change in this release.", ""]
        return "\n".join(lines)

    if removed:
        lines += ["## Endpoints removed", ""] + render_endpoint_list(removed)
    if added:
        lines += ["## Endpoints added", ""] + render_endpoint_list(added)

    if breaking_rest:
        kinds = Counter(c["id"] for c in breaking_rest)
        lines += [
            "## Breaking changes",
            "",
            "| Kind | Count |",
            "|---|---:|",
        ]
        lines += [
            f"| {kind_label(kind)} | {count:,} |"
            for kind, count in sorted(kinds.items(), key=lambda kv: (-kv[1], kv[0]))
        ]
        lines.append("")

        groups = defaultdict(list)
        for change in breaking_rest:
            groups[breaking_group(change)].append(change)
        if groups[REQUESTS]:
            lines += [f"### {REQUESTS}", ""] + render_by_endpoint(groups[REQUESTS])
        if groups[RESPONSES]:
            lines += [f"### {RESPONSES}", ""] + render_by_endpoint(groups[RESPONSES])
        if groups[RESPONSE_ENUM_VALUES]:
            count = len(groups[RESPONSE_ENUM_VALUES])
            lines += [
                f"### {RESPONSE_ENUM_VALUES}",
                "",
                "A response can now hold an enum value it could not before. "
                "This breaks only a client that rejects unknown values.",
                "",
                f'??? note "{count:,} new values in response enums"',
                "",
            ]
            lines += render_by_endpoint(groups[RESPONSE_ENUM_VALUES], indent="    ")

    if warnings_rest:
        lines += ["## Warnings", ""] + render_by_endpoint(warnings_rest)

    if info_rest:
        lines += [
            "## Other changes",
            "",
            f'??? note "{len(info_rest):,} changes that do not break clients"',
            "",
        ]
        lines += render_by_endpoint(info_rest, indent="    ")

    return "\n".join(lines).rstrip() + "\n"


PAGE_TITLE_PREFIX = "# API changes in "
FULL_DIFF_ONLY = " (full structural diff only)"


def render_index(directory: Path) -> str:
    """List the release pages newest first.

    A page rendered before this script existed holds only oasdiff's structural
    diff; it is told apart by its title and marked as such, so the index stays
    right whichever releases have been regenerated.
    """
    pages = {}
    for path in directory.iterdir():
        match = DIFF_PAGE_RE.match(path.name)
        if match:
            title = path.read_text(encoding="utf-8").split("\n", 1)[0]
            pages[match.group(1)] = title.startswith(PAGE_TITLE_PREFIX)
    lines = [
        "# API changes",
        "",
        "What changed in the Waldur REST API in each release, computed from the "
        "OpenAPI schemas of that release and the one before it. Each page opens "
        "with a summary and lists breaking changes first; pages marked *full "
        "structural diff only* were published before that and list every "
        "difference by endpoint.",
        "",
    ]
    lines += [
        f"- [{version}](waldur-openapi-schema-{version}-diff.md)"
        + ("" if pages[version] else FULL_DIFF_ONLY)
        for version in sorted(pages, key=version_key, reverse=True)
    ]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    page = sub.add_parser("page", help="render one release's page")
    page.add_argument("--changelog", type=Path, required=True)
    page.add_argument("--version", required=True)
    page.add_argument("--previous", required=True)
    page.add_argument("--oasdiff-version", required=True)
    page.add_argument("--full-diff", help="relative link to the full diff page")
    page.add_argument("-o", "--output", type=Path, required=True)

    index = sub.add_parser("index", help="render the index of release pages")
    index.add_argument("--dir", type=Path, required=True)

    args = parser.parse_args(argv)

    if args.command == "page":
        content = render_page(
            load_changes(args.changelog),
            args.version,
            args.previous,
            args.oasdiff_version,
            args.full_diff,
        )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content, encoding="utf-8")
    else:
        (args.dir / "index.md").write_text(render_index(args.dir), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
