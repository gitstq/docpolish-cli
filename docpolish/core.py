"""
DocPolish Core Engine - Markdown formatting and beautification logic.
"""

import re
import textwrap
from typing import List, Tuple, Optional


class MarkdownFormatter:
    """Intelligent Markdown document formatter."""

    def __init__(self):
        self.rules = [
            self._fix_heading_levels,
            self._fix_list_indentation,
            self._fix_table_alignment,
            self._fix_code_block_labels,
            self._fix_horizontal_rules,
            self._fix_empty_lines,
            self._fix_link_format,
            self._fix_emphasis_spacing,
            self._normalize_whitespace,
        ]

    def format(self, content: str) -> str:
        """Apply all formatting rules to the content."""
        for rule in self.rules:
            content = rule(content)
        return content.strip() + "\n"

    def _fix_heading_levels(self, content: str) -> str:
        """Ensure heading levels are continuous (no skipping)."""
        lines = content.split("\n")
        result = []
        prev_level = 0

        for line in lines:
            match = re.match(r"^(#{1,6})\s+(.+)$", line)
            if match:
                level = len(match.group(1))
                # Ensure no level skip > 1
                if prev_level > 0 and level > prev_level + 1:
                    level = prev_level + 1
                    line = "#" * level + " " + match.group(2)
                prev_level = level
            result.append(line)

        return "\n".join(result)

    def _fix_list_indentation(self, content: str) -> str:
        """Standardize list item indentation."""
        lines = content.split("\n")
        result = []

        for line in lines:
            # Fix unordered lists
            match = re.match(r"^(\s*)[-*+]\s+(.+)$", line)
            if match:
                indent = len(match.group(1))
                # Standardize to 2-space indentation per level
                level = indent // 2
                line = "  " * level + "- " + match.group(2)

            # Fix ordered lists
            match = re.match(r"^(\s*)\d+\.\s+(.+)$", line)
            if match:
                indent = len(match.group(1))
                level = indent // 2
                line = "  " * level + "1. " + match.group(2)

            result.append(line)

        return "\n".join(result)

    def _fix_table_alignment(self, content: str) -> str:
        """Align table columns properly."""
        lines = content.split("\n")
        result = []
        table_buffer = []

        for line in lines:
            if "|" in line:
                table_buffer.append(line)
            else:
                if table_buffer:
                    result.extend(self._format_table(table_buffer))
                    table_buffer = []
                result.append(line)

        if table_buffer:
            result.extend(self._format_table(table_buffer))

        return "\n".join(result)

    def _format_table(self, lines: List[str]) -> List[str]:
        """Format a table with aligned columns."""
        if len(lines) < 2:
            return lines

        # Parse rows
        rows = []
        for line in lines:
            cells = [cell.strip() for cell in line.split("|")]
            cells = [c for c in cells if c or c == ""]
            if cells:
                rows.append(cells)

        if not rows:
            return lines

        # Calculate column widths
        num_cols = max(len(row) for row in rows)
        col_widths = [0] * num_cols

        for row in rows:
            for i, cell in enumerate(row):
                if i < num_cols:
                    col_widths[i] = max(col_widths[i], len(cell))

        # Format rows
        formatted = []
        for row in rows:
            cells = []
            for i in range(num_cols):
                cell = row[i] if i < len(row) else ""
                # Center alignment for header separator
                if re.match(r"^:?-+:?$", cell):
                    cells.append(" " + cell.center(col_widths[i]) + " ")
                else:
                    cells.append(" " + cell.ljust(col_widths[i]) + " ")
            formatted.append("|" + "|".join(cells) + "|")

        return formatted

    def _fix_code_block_labels(self, content: str) -> str:
        """Standardize code block language labels."""
        content = re.sub(
            r"```\s*(\w+)\s*\n",
            lambda m: f"```{m.group(1).lower()}\n",
            content,
        )
        return content

    def _fix_horizontal_rules(self, content: str) -> str:
        """Standardize horizontal rules."""
        content = re.sub(r"\n-{3,}\s*\n", "\n---\n", content)
        content = re.sub(r"\n\*{3,}\s*\n", "\n---\n", content)
        content = re.sub(r"\n_{3,}\s*\n", "\n---\n", content)
        return content

    def _fix_empty_lines(self, content: str) -> str:
        """Remove excessive empty lines."""
        content = re.sub(r"\n{4,}", "\n\n\n", content)
        return content

    def _fix_link_format(self, content: str) -> str:
        """Fix common link formatting issues."""
        # Fix spaces in links
        content = re.sub(r"\[\s+(.+?)\s+\]\s*\(\s*(.+?)\s*\)", r"[\1](\2)", content)
        return content

    def _fix_emphasis_spacing(self, content: str) -> str:
        """Fix spacing around emphasis markers."""
        # Remove spaces between ** and text
        content = re.sub(r"\*\*\s+(.+?)\s+\*\*", r"**\1**", content)
        content = re.sub(r"_\s+(.+?)\s+_", r"_\1_", content)
        return content

    def _normalize_whitespace(self, content: str) -> str:
        """Normalize whitespace in the document."""
        # Remove trailing whitespace
        lines = [line.rstrip() for line in content.split("\n")]
        return "\n".join(lines)


class ContentAnalyzer:
    """Analyze Markdown content structure and quality."""

    def analyze(self, content: str) -> dict:
        """Return analysis report of the document."""
        report = {
            "total_lines": len(content.split("\n")),
            "total_chars": len(content),
            "headings": self._count_headings(content),
            "lists": self._count_lists(content),
            "code_blocks": self._count_code_blocks(content),
            "tables": self._count_tables(content),
            "links": self._count_links(content),
            "images": self._count_images(content),
            "issues": self._detect_issues(content),
        }
        return report

    def _count_headings(self, content: str) -> dict:
        counts = {}
        for level in range(1, 7):
            pattern = f"^#{{{level}}}\\s+"
            counts[f"h{level}"] = len(re.findall(pattern, content, re.MULTILINE))
        return counts

    def _count_lists(self, content: str) -> dict:
        unordered = len(re.findall(r"^\s*[-*+]\s+", content, re.MULTILINE))
        ordered = len(re.findall(r"^\s*\d+\.\s+", content, re.MULTILINE))
        return {"unordered": unordered, "ordered": ordered}

    def _count_code_blocks(self, content: str) -> int:
        return len(re.findall(r"```\w*", content))

    def _count_tables(self, content: str) -> int:
        lines = content.split("\n")
        table_count = 0
        in_table = False

        for line in lines:
            if "|" in line and not in_table:
                in_table = True
            elif "|" not in line and in_table:
                table_count += 1
                in_table = False

        if in_table:
            table_count += 1

        return table_count

    def _count_links(self, content: str) -> int:
        return len(re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content))

    def _count_images(self, content: str) -> int:
        return len(re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", content))

    def _detect_issues(self, content: str) -> List[str]:
        issues = []

        # Check for empty headings
        if re.search(r"^#{1,6}\s*$", content, re.MULTILINE):
            issues.append("Empty headings detected")

        # Check for broken links
        broken = re.findall(r"\[([^\]]+)\]\(\s*\)", content)
        if broken:
            issues.append(f"Empty link targets: {len(broken)}")

        # Check for unclosed code blocks
        open_blocks = content.count("```") % 2
        if open_blocks:
            issues.append("Unclosed code blocks detected")

        # Check for inconsistent heading levels
        headings = re.findall(r"^(#{1,6})\s+", content, re.MULTILINE)
        if headings:
            levels = [len(h) for h in headings]
            for i in range(1, len(levels)):
                if levels[i] > levels[i - 1] + 1:
                    issues.append(f"Heading level skip at position {i}")

        return issues
