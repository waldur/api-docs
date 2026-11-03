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
        self.assertIn("| Breaking | 3 in 3 endpoints |", page)
        self.assertIn("| Warnings | 1 |", page)
        self.assertIn("| Endpoints removed | 1 |", page)
        self.assertIn("| Endpoints added | 1 |", page)
        self.assertIn("| Other changes | 1 |", page)

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

    def test_endpoints_are_labels_not_headings(self):
        page = render([change("response-property-became-nullable", 3)])
        self.assertNotIn("####", page)

    def test_angle_brackets_are_escaped(self):
        page = render([change("x", 3, text="pattern `^<a>$` was set")])
        self.assertIn("`^&lt;a>$`", page)

    def test_full_diff_link_is_optional(self):
        self.assertIn("[full schema diff](full/x-diff-full.md)", render([]))
        self.assertNotIn("full schema diff", render([], full_diff=None))

    def test_no_changes(self):
        page = render([])
        self.assertIn("The API did not change in this release.", page)
        self.assertNotIn("## ", page)


class LoadChangesTest(unittest.TestCase):
    def test_head_operations_are_dropped(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "changelog.json"
            path.write_text(
                json.dumps([change("x", 3, "HEAD"), change("x", 3, "GET")])
            )
            changes = rac.load_changes(path)
        self.assertEqual([c["operation"] for c in changes], ["GET"])

    def test_empty_changelog_means_no_changes(self):
        # oasdiff prints `[]` when the two schemas do not differ.
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "changelog.json"
            for content in ("[]", "null", ""):
                path.write_text(content)
                self.assertEqual(rac.load_changes(path), [])


class RenderIndexTest(unittest.TestCase):
    def test_lists_release_pages_newest_first(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            for name in (
                "waldur-openapi-schema-8.1.3-diff.md",
                "waldur-openapi-schema-8.1.10-diff.md",
                "waldur-openapi-schema-7.9.0-diff.md",
                "index.md",
                ".pages",
            ):
                (directory / name).write_text("")
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


if __name__ == "__main__":
    unittest.main()
