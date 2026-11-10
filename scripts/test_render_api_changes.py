"""Tests for render_api_changes.py.

Run with: python3 -m unittest discover -s scripts -p 'test_*.py'
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import render_api_changes as rac  # noqa: E402


def change(id_, level, method="GET", path="/api/things/", text=None):
    entry = {"id": id_, "level": level, "text": text or id_}
    if method is not None:
        entry["operation"] = method
        entry["path"] = path
    return entry


def render(changes, **kwargs):
    kwargs.setdefault("full_diff", "full/x-diff-full.md")
    return rac.render_page(changes, "8.1.4", "8.1.3", "v1.34.1", **kwargs)


class RenderPageTest(unittest.TestCase):
    def test_summary_counts_each_kind(self):
        page = render(
            [
                change("api-path-removed-without-deprecation", 3, path="/api/old/"),
                change("endpoint-added", 1, "POST", "/api/new/"),
                change("response-property-became-nullable", 3, path="/api/a/"),
                change("response-property-became-nullable", 3, path="/api/b/"),
                change("response-property-enum-value-added", 2),
                change("response-optional-property-added", 1),
            ]
        )
        # The removed endpoint is breaking too, but has its own row.
        self.assertIn(
            "| Breaking, besides removed endpoints | 2 in 2 endpoints |", page
        )
        self.assertIn("| Warnings | 1 |", page)
        self.assertIn("| Endpoints removed | 1 |", page)
        self.assertIn("| Endpoints added | 1 |", page)
        self.assertIn("| Other changes | 1 |", page)

    def test_breaking_row_adds_up_with_the_kind_table(self):
        page = render(
            [
                change("api-path-removed-without-deprecation", 3, path="/api/old/"),
                change("api-removed-without-deprecation", 3, "DELETE", "/api/gone/"),
                change("response-property-became-nullable", 3, path="/api/a/"),
                change("request-property-removed", 3, "POST", "/api/b/"),
            ]
        )
        kinds = page[page.index("| Kind | Count |") :].split("\n\n")[0]
        total = sum(
            int(line.rsplit("|", 2)[1].strip().replace(",", ""))
            for line in kinds.splitlines()[2:]
        )
        self.assertEqual(total, 2)
        self.assertIn(
            "| Breaking, besides removed endpoints | 2 in 2 endpoints |", page
        )

    def test_change_on_many_endpoints_is_listed_once(self):
        text = "the endpoint scheme security `tokenAuth` was removed from the API"
        many = [
            change("api-security-removed", 3, "GET", f"/api/things-{n}/", text=text)
            for n in range(rac.FOLD_MIN_ENDPOINTS)
        ]
        page = render(many + [change("request-property-removed", 3, "POST", "/api/a/")])
        requests = page[page.index("### Requests") :]
        self.assertIn(
            f"**On many endpoints**\n\n- {text} ({rac.FOLD_MIN_ENDPOINTS} endpoints)",
            requests,
        )
        self.assertEqual(page.count(text), 1)
        self.assertNotIn("/api/things-0/", page)
        # Other changes are still listed by endpoint, after the folded ones.
        self.assertLess(
            requests.index("On many endpoints"), requests.index("`POST /api/a/`")
        )

    def test_change_on_fewer_endpoints_is_listed_by_endpoint(self):
        text = "removed the request property `x`"
        page = render(
            [
                change("request-property-removed", 3, "POST", f"/api/t-{n}/", text=text)
                for n in range(rac.FOLD_MIN_ENDPOINTS - 1)
            ]
        )
        self.assertNotIn("**On many endpoints**", page)
        self.assertEqual(page.count(text), rac.FOLD_MIN_ENDPOINTS - 1)

    def test_sections_come_in_severity_order(self):
        page = render(
            [
                change("response-optional-property-added", 1),
                change("response-property-enum-value-added", 2),
                change("response-property-became-nullable", 3),
                change("endpoint-added", 1, "POST", "/api/new/"),
                change("api-removed-without-deprecation", 3, "DELETE", "/api/x/"),
            ]
        )
        headings = [line for line in page.splitlines() if line.startswith("## ")]
        self.assertEqual(
            headings,
            [
                "## Endpoints removed",
                "## Endpoints added",
                "## Breaking changes",
                "## Warnings",
                "## Other changes",
            ],
        )

    def test_removed_and_added_endpoints_are_not_repeated_by_endpoint(self):
        page = render(
            [
                change("api-path-removed-without-deprecation", 3, path="/api/old/"),
                change("endpoint-added", 1, "POST", "/api/new/"),
            ]
        )
        self.assertEqual(page.count("`GET /api/old/`"), 1)
        self.assertEqual(page.count("`POST /api/new/`"), 1)
        self.assertNotIn("## Breaking changes", page)
        self.assertNotIn("## Other changes", page)

    def test_breaking_changes_are_counted_by_kind(self):
        page = render(
            [
                change("response-property-became-nullable", 3, path="/api/a/"),
                change("response-property-became-nullable", 3, path="/api/b/"),
                change("new-required-request-property", 3, "POST"),
            ]
        )
        self.assertIn("| Response property became nullable | 2 |", page)
        self.assertIn("| New required request property | 1 |", page)
        self.assertLess(
            page.index("became nullable | 2"), page.index("request property | 1")
        )

    def test_endpoints_are_sorted_by_path_then_method(self):
        page = render(
            [
                change("x", 3, "DELETE", "/api/b/"),
                change("x", 3, "POST", "/api/a/"),
                change("x", 3, "GET", "/api/b/"),
                change("x", 3, "GET", "/api/a/"),
            ]
        )
        labels = [line for line in page.splitlines() if line.startswith("**`")]
        self.assertEqual(
            labels,
            [
                "**`GET /api/a/`**",
                "**`POST /api/a/`**",
                "**`GET /api/b/`**",
                "**`DELETE /api/b/`**",
            ],
        )

    def test_changes_without_an_operation_are_grouped_last(self):
        page = render(
            [
                change("api-schema-removed", 1, method=None),
                change("response-optional-property-added", 1, path="/api/z/"),
            ]
        )
        self.assertLess(page.index("`GET /api/z/`"), page.index("**General**"))

    def test_other_changes_are_collapsed(self):
        page = render([change("response-optional-property-added", 1, text="added")])
        block = page[page.index("## Other changes") :]
        self.assertIn('??? note "1 changes that do not break clients"', block)
        self.assertIn("\n    **`GET /api/things/`**", block)
        self.assertIn("\n    - added", block)

    def test_breaking_changes_list_requests_then_responses_then_enum_values(self):
        page = render(
            [
                change("response-property-enum-value-added", 3, path="/api/a/"),
                change("response-property-became-nullable", 3, path="/api/b/"),
                change("request-property-removed", 3, "POST", "/api/c/"),
                change("new-required-request-property", 3, "POST", "/api/d/"),
            ]
        )
        breaking = page[page.index("## Breaking changes") :]
        subheadings = [l for l in breaking.splitlines() if l.startswith("### ")]
        self.assertEqual(
            subheadings,
            ["### Requests", "### Responses", "### New values in response enums"],
        )
        requests = breaking[: breaking.index("### Responses")]
        self.assertIn("`POST /api/c/`", requests)
        self.assertIn("`POST /api/d/`", requests)

    def test_new_response_enum_values_are_collapsed(self):
        page = render(
            [
                change("response-property-enum-value-added", 3, text="added `x`"),
                change("response-property-enum-value-added", 3, text="added `y`"),
            ]
        )
        block = page[page.index("### New values in response enums") :]
        self.assertIn('??? note "2 new values in response enums"', block)
        self.assertIn("\n    - added `x`", block)
        self.assertNotIn("### Requests", page)
        self.assertNotIn("### Responses", page)

    def test_endpoints_are_labels_not_headings(self):
        page = render([change("response-property-became-nullable", 3)])
        self.assertNotIn("####", page)

    def test_angle_brackets_in_code_spans_are_left_alone(self):
        # Markdown shows a code span literally, so `&lt;` there would be
        # printed as is (seen on GET /api/event-consumers/ in 8.1.3).
        page = render([change("x", 3, text="type changed to `array<string>`")])
        self.assertIn("- type changed to `array<string>`", page)
        self.assertNotIn("&lt;", page)

    def test_angle_brackets_outside_code_spans_are_escaped(self):
        page = render([change("x", 3, text="pattern <a> set on `a<b>`")])
        self.assertIn("- pattern &lt;a> set on `a<b>`", page)

    def test_full_diff_link_is_optional(self):
        self.assertIn("[full schema diff](full/x-diff-full.md)", render([]))
        self.assertNotIn("full schema diff", render([], full_diff=None))

    def test_no_changes(self):
        page = render([])
        self.assertIn("The API did not change in this release.", page)
        self.assertNotIn("## ", page)


class LoadChangesTest(unittest.TestCase):
    def test_head_change_that_repeats_get_is_dropped(self):
        changes = rac.drop_mirrored_heads(
            [change("x", 3, "HEAD"), change("x", 3, "GET")]
        )
        self.assertEqual([c["operation"] for c in changes], ["GET"])

    def test_head_change_of_its_own_is_kept(self):
        # A HEAD added to an existing GET, or one that is an existence check,
        # has no GET change to repeat.
        changes = rac.drop_mirrored_heads(
            [
                change("endpoint-added", 1, "HEAD", "/api/debug/x/"),
                change("x", 3, "HEAD", "/api/a/", text="only on HEAD"),
                change("x", 3, "GET", "/api/a/", text="only on GET"),
                change("x", 3, "HEAD", "/api/b/"),
                change("x", 3, "GET", "/api/c/"),
            ]
        )
        self.assertEqual(
            [(c["operation"], c["path"]) for c in changes],
            [
                ("HEAD", "/api/debug/x/"),
                ("HEAD", "/api/a/"),
                ("GET", "/api/a/"),
                ("HEAD", "/api/b/"),
                ("GET", "/api/c/"),
            ],
        )

    def test_load_changes_drops_mirrored_heads(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "changelog.json"
            path.write_text(json.dumps([change("x", 3, "HEAD"), change("x", 3, "GET")]))
            changes = rac.load_changes(path)
        self.assertEqual([c["operation"] for c in changes], ["GET"])

    def test_empty_changelog_means_no_changes(self):
        # oasdiff prints `[]` when the two schemas do not differ.
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "changelog.json"
            for content in ("[]", "null", ""):
                path.write_text(content)
                self.assertEqual(rac.load_changes(path), [])


class MergeMediaTypesTest(unittest.TestCase):
    TEXT = "removed the request property `name`"

    def body_change(self, media_type, text=None, path="/api/things/"):
        return change(
            "request-property-removed",
            3,
            "POST",
            path,
            text=f"{text or self.TEXT} (media type: {media_type})",
        )

    def test_change_for_every_request_media_type_is_listed_once(self):
        merged = rac.merge_media_types(
            [
                self.body_change("application/json"),
                self.body_change("application/x-www-form-urlencoded"),
                self.body_change("multipart/form-data"),
            ]
        )
        self.assertEqual([c["text"] for c in merged], [self.TEXT])

    def test_change_for_some_media_types_names_them(self):
        merged = rac.merge_media_types(
            [
                self.body_change("application/json"),
                self.body_change("multipart/form-data"),
            ]
        )
        self.assertEqual(
            [c["text"] for c in merged],
            [f"{self.TEXT} (media types: application/json, multipart/form-data)"],
        )

    def test_media_type_followed_by_another_note_is_merged(self):
        text = "added the new optional request property `x` (media type: {}) (shared schema: `Y`)"
        merged = rac.merge_media_types(
            [
                change("new-optional-request-property", 1, "POST", text=text.format(m))
                for m in sorted(rac.REQUEST_MEDIA_TYPES)
            ]
        )
        self.assertEqual(
            [c["text"] for c in merged],
            ["added the new optional request property `x` (shared schema: `Y`)"],
        )

    def test_change_for_one_media_type_keeps_it(self):
        merged = rac.merge_media_types([self.body_change("application/json")])
        self.assertEqual(
            [c["text"] for c in merged], [f"{self.TEXT} (media type: application/json)"]
        )

    def test_different_changes_are_not_merged(self):
        merged = rac.merge_media_types(
            [
                self.body_change("application/json"),
                self.body_change("application/json", text="removed `other`"),
                self.body_change("application/json", path="/api/else/"),
                change("response-property-became-nullable", 3, text=self.TEXT),
            ]
        )
        self.assertEqual(len(merged), 4)

    def test_order_follows_the_first_occurrence(self):
        merged = rac.merge_media_types(
            [
                self.body_change("application/json", text="first"),
                self.body_change("application/json", text="second"),
                self.body_change("multipart/form-data", text="first"),
            ]
        )
        self.assertEqual(
            [c["text"].split(" (")[0] for c in merged], ["first", "second"]
        )

    def test_summary_counts_merged_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "changelog.json"
            path.write_text(
                json.dumps(
                    [
                        self.body_change(media_type)
                        for media_type in sorted(rac.REQUEST_MEDIA_TYPES)
                    ]
                )
            )
            page = render(rac.load_changes(path))
        self.assertIn(
            "| Breaking, besides removed endpoints | 1 in 1 endpoints |", page
        )


class RenderIndexTest(unittest.TestCase):
    def test_lists_release_pages_newest_first(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            for name, content in (
                ("waldur-openapi-schema-8.1.3-diff.md", "# API changes in 8.1.3\n"),
                ("waldur-openapi-schema-8.1.10-diff.md", "# API changes in 8.1.10\n"),
                ("waldur-openapi-schema-7.9.0-diff.md", "# API changes in 7.9.0\n"),
                ("index.md", ""),
                (".pages", ""),
            ):
                (directory / name).write_text(content)
            (directory / "full").mkdir()
            index = rac.render_index(directory)
        entries = [line for line in index.splitlines() if line.startswith("- [")]
        self.assertEqual(
            entries,
            [
                "- [8.1.10](waldur-openapi-schema-8.1.10-diff.md)",
                "- [8.1.3](waldur-openapi-schema-8.1.3-diff.md)",
                "- [7.9.0](waldur-openapi-schema-7.9.0-diff.md)",
            ],
        )

    def test_marks_pages_that_hold_only_the_structural_diff(self):
        # Pages published before this renderer have oasdiff's own title.
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "waldur-openapi-schema-8.1.5-diff.md").write_text(
                "# API changes in 8.1.5\n\nSummary\n"
            )
            (directory / "waldur-openapi-schema-8.1.4-diff.md").write_text(
                "# OpenAPI schema diff - 8.1.4\n\n## For version 8.1.4\n"
            )
            index = rac.render_index(directory)
        self.assertIn("- [8.1.5](waldur-openapi-schema-8.1.5-diff.md)\n", index)
        self.assertIn(
            "- [8.1.4](waldur-openapi-schema-8.1.4-diff.md) (full structural diff only)",
            index,
        )
        self.assertNotIn("8.1.3", index)


if __name__ == "__main__":
    unittest.main()
