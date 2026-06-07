"""Tests for DocPolish CLI module."""

import unittest
import tempfile
import os
from pathlib import Path
from docpolish.cli import create_parser


class TestCLIParser(unittest.TestCase):
    """Test CLI argument parser."""

    def setUp(self):
        self.parser = create_parser()

    def test_format_command(self):
        """Test format command parsing."""
        args = self.parser.parse_args(["format", "test.md"])
        self.assertEqual(args.command, "format")
        self.assertEqual(args.input, "test.md")

    def test_analyze_command(self):
        """Test analyze command parsing."""
        args = self.parser.parse_args(["analyze", "test.md", "--json"])
        self.assertEqual(args.command, "analyze")
        self.assertTrue(args.json)

    def test_readme_command(self):
        """Test readme command parsing."""
        args = self.parser.parse_args([
            "readme",
            "--project-name", "TestProject",
            "--lang", "en,zh-cn"
        ])
        self.assertEqual(args.command, "readme")
        self.assertEqual(args.project_name, "TestProject")
        self.assertEqual(args.lang, "en,zh-cn")


class TestCLICommands(unittest.TestCase):
    """Test CLI command execution."""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = Path(self.temp_dir) / "test.md"
        self.test_file.write_text("# Title\n\n- Item 1\n- Item 2\n", encoding="utf-8")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_dir)

    def test_format_existing_file(self):
        """Test formatting an existing file."""
        from docpolish.cli import cmd_format

        class Args:
            input = str(self.test_file)
            output = None
            check = False
            diff = False

        result = cmd_format(Args())
        self.assertEqual(result, 0)

    def test_analyze_existing_file(self):
        """Test analyzing an existing file."""
        from docpolish.cli import cmd_analyze

        class Args:
            input = str(self.test_file)
            json = False

        result = cmd_analyze(Args())
        self.assertEqual(result, 0)

    def test_format_nonexistent_file(self):
        """Test formatting a non-existent file."""
        from docpolish.cli import cmd_format

        class Args:
            input = "nonexistent.md"
            output = None
            check = False
            diff = False

        result = cmd_format(Args())
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
