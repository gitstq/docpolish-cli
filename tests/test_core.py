"""Tests for DocPolish core module."""

import unittest
from docpolish.core import MarkdownFormatter, ContentAnalyzer


class TestMarkdownFormatter(unittest.TestCase):
    """Test MarkdownFormatter class."""

    def setUp(self):
        self.formatter = MarkdownFormatter()

    def test_fix_heading_levels(self):
        """Test heading level fixing."""
        content = "# Title\n### Skip\n## Normal"
        result = self.formatter._fix_heading_levels(content)
        self.assertIn("## Skip", result)

    def test_fix_list_indentation(self):
        """Test list indentation fixing."""
        content = "- Item 1\n   - Item 2"
        result = self.formatter._fix_list_indentation(content)
        self.assertIn("  - Item 2", result)

    def test_fix_horizontal_rules(self):
        """Test horizontal rule standardization."""
        content = "Text\n***\nMore text\n---\nEnd"
        result = self.formatter._fix_horizontal_rules(content)
        self.assertEqual(result.count("---"), 2)

    def test_full_format(self):
        """Test full document formatting."""
        content = "# Title  \n\n\n\n- item\n\n***\n"
        result = self.formatter.format(content)
        self.assertIn("# Title", result)
        self.assertNotIn("  \n", result)


class TestContentAnalyzer(unittest.TestCase):
    """Test ContentAnalyzer class."""

    def setUp(self):
        self.analyzer = ContentAnalyzer()

    def test_analyze(self):
        """Test document analysis."""
        content = "# Title\n\n- Item 1\n- Item 2\n\n```python\nprint('hello')\n```\n\n[Link](http://example.com)\n\n| A | B |\n|---|---|\n| 1 | 2 |\n"
        report = self.analyzer.analyze(content)

        self.assertEqual(report["headings"]["h1"], 1)
        self.assertEqual(report["lists"]["unordered"], 2)
        self.assertEqual(report["code_blocks"], 2)  # Opening ```python and closing ```
        self.assertEqual(report["tables"], 1)
        self.assertEqual(report["links"], 1)
        self.assertEqual(report["images"], 0)
        self.assertEqual(len(report["issues"]), 0)

    def test_detect_issues(self):
        """Test issue detection."""
        content = "# \n\n[Empty]()\n\n```\ncode\n"
        issues = self.analyzer._detect_issues(content)
        self.assertTrue(len(issues) > 0)


if __name__ == "__main__":
    unittest.main()
