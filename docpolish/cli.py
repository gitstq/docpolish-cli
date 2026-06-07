#!/usr/bin/env python3
"""
DocPolish CLI - Command-line interface for Markdown document beautification.
"""

import argparse
import os
import sys
import json
from pathlib import Path

from .core import MarkdownFormatter, ContentAnalyzer
from .ai_enhance import AIEnhancer
from .readme_generator import ReadmeGenerator


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog="docpolish",
        description="🦞 DocPolish - Lightweight Markdown Document Intelligent Beautification Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  docpolish format README.md -o README_polished.md
  docpolish analyze document.md
  docpolish readme --project-name "MyApp" --lang zh-cn,en
  docpolish polish README.md --style professional
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Format command
    fmt_parser = subparsers.add_parser("format", help="Format and beautify Markdown files")
    fmt_parser.add_argument("input", help="Input Markdown file")
    fmt_parser.add_argument("-o", "--output", help="Output file (default: overwrite input)")
    fmt_parser.add_argument("--check", action="store_true", help="Check only, don't modify")
    fmt_parser.add_argument("--diff", action="store_true", help="Show diff of changes")

    # Analyze command
    ana_parser = subparsers.add_parser("analyze", help="Analyze Markdown document structure")
    ana_parser.add_argument("input", help="Input Markdown file")
    ana_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Polish command (AI)
    pol_parser = subparsers.add_parser("polish", help="AI-powered content polishing")
    pol_parser.add_argument("input", help="Input Markdown file")
    pol_parser.add_argument("-o", "--output", help="Output file")
    pol_parser.add_argument("--style", default="professional", choices=["professional", "casual", "technical", "simple"])
    pol_parser.add_argument("--api-key", help="GLM-5.1 API key")

    # Translate command (AI)
    trans_parser = subparsers.add_parser("translate", help="Translate Markdown content")
    trans_parser.add_argument("input", help="Input Markdown file")
    trans_parser.add_argument("-o", "--output", help="Output file")
    trans_parser.add_argument("--target", required=True, help="Target language (zh-cn, zh-tw, en, ja, ko, es)")
    trans_parser.add_argument("--api-key", help="GLM-5.1 API key")

    # README generator command
    readme_parser = subparsers.add_parser("readme", help="Generate multi-language README")
    readme_parser.add_argument("--project-name", required=True, help="Project name")
    readme_parser.add_argument("--description", default="", help="Project description")
    readme_parser.add_argument("--lang", default="zh-cn,zh-tw,en", help="Languages to generate (comma-separated)")
    readme_parser.add_argument("--output-dir", default=".", help="Output directory")
    readme_parser.add_argument("--features", default="", help="Comma-separated feature list")
    readme_parser.add_argument("--api-key", help="GLM-5.1 API key for AI enhancement")

    # Version
    parser.add_argument("--version", action="version", version="%(prog)s 1.0.0")

    return parser


def show_diff(original: str, formatted: str) -> None:
    """Show unified diff between original and formatted content."""
    import difflib

    original_lines = original.splitlines(keepends=True)
    formatted_lines = formatted.splitlines(keepends=True)

    diff = difflib.unified_diff(
        original_lines,
        formatted_lines,
        fromfile="original",
        tofile="formatted",
        lineterm="",
    )

    for line in diff:
        if line.startswith("+"):
            print(f"\033[92m{line}\033[0m")
        elif line.startswith("-"):
            print(f"\033[91m{line}\033[0m")
        elif line.startswith("@@"):
            print(f"\033[36m{line}\033[0m")
        else:
            print(line)


def cmd_format(args) -> int:
    """Execute format command."""
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"❌ Error: File not found: {args.input}", file=sys.stderr)
        return 1

    with open(input_path, "r", encoding="utf-8") as f:
        original = f.read()

    formatter = MarkdownFormatter()
    formatted = formatter.format(original)

    if args.check:
        if original == formatted:
            print("✅ Document is already properly formatted!")
            return 0
        else:
            print("⚠️  Document needs formatting. Run without --check to apply.")
            return 1

    if args.diff:
        show_diff(original, formatted)
        return 0

    output_path = Path(args.output) if args.output else input_path
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted)

    changes = sum(1 for a, b in zip(original.split("\n"), formatted.split("\n")) if a != b)
    print(f"✅ Formatted: {output_path}")
    print(f"📊 Lines changed: ~{changes}")

    return 0


def cmd_analyze(args) -> int:
    """Execute analyze command."""
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"❌ Error: File not found: {args.input}", file=sys.stderr)
        return 1

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    analyzer = ContentAnalyzer()
    report = analyzer.analyze(content)

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0

    print("📊 Document Analysis Report")
    print("=" * 40)
    print(f"📄 Total Lines: {report['total_lines']}")
    print(f"🔤 Total Characters: {report['total_chars']}")
    print(f"\n📌 Headings:")
    for level, count in report["headings"].items():
        if count > 0:
            print(f"   {level.upper()}: {count}")
    print(f"\n📝 Lists:")
    print(f"   Unordered: {report['lists']['unordered']}")
    print(f"   Ordered: {report['lists']['ordered']}")
    print(f"\n💻 Code Blocks: {report['code_blocks']}")
    print(f"📋 Tables: {report['tables']}")
    print(f"🔗 Links: {report['links']}")
    print(f"🖼️  Images: {report['images']}")

    if report["issues"]:
        print(f"\n⚠️  Issues Found:")
        for issue in report["issues"]:
            print(f"   - {issue}")
    else:
        print("\n✅ No issues detected!")

    return 0


def cmd_polish(args) -> int:
    """Execute polish command."""
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"❌ Error: File not found: {args.input}", file=sys.stderr)
        return 1

    api_key = args.api_key or os.environ.get("GLM_API_KEY")
    enhancer = AIEnhancer(api_key=api_key)

    if not enhancer.is_available():
        print("❌ Error: GLM API key not provided. Set GLM_API_KEY environment variable or use --api-key.", file=sys.stderr)
        return 1

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    print("🤖 Polishing content with GLM-5.1...")
    polished = enhancer.polish_text(content, style=args.style)

    if polished is None:
        print("❌ Error: Failed to polish content. Check your API key and network connection.", file=sys.stderr)
        return 1

    output_path = Path(args.output) if args.output else input_path
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(polished)

    print(f"✅ Polished: {output_path}")
    return 0


def cmd_translate(args) -> int:
    """Execute translate command."""
    input_path = Path(args.input)

    if not input_path.exists():
        print(f"❌ Error: File not found: {args.input}", file=sys.stderr)
        return 1

    api_key = args.api_key or os.environ.get("GLM_API_KEY")
    enhancer = AIEnhancer(api_key=api_key)

    if not enhancer.is_available():
        print("❌ Error: GLM API key not provided.", file=sys.stderr)
        return 1

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"🌐 Translating to {args.target} with GLM-5.1...")
    translated = enhancer.translate_text(content, target_lang=args.target)

    if translated is None:
        print("❌ Error: Failed to translate content.", file=sys.stderr)
        return 1

    output_path = Path(args.output) if args.output else input_path.with_suffix(f".{args.target}.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(translated)

    print(f"✅ Translated: {output_path}")
    return 0


def cmd_readme(args) -> int:
    """Execute readme generator command."""
    api_key = args.api_key or os.environ.get("GLM_API_KEY")
    enhancer = AIEnhancer(api_key=api_key) if api_key else None

    features = [f.strip() for f in args.features.split(",") if f.strip()]

    project_info = {
        "name": args.project_name,
        "description": args.description,
        "language": "Python",
        "features": features or ["Easy to use", "Lightweight", "Cross-platform"],
    }

    languages = [lang.strip() for lang in args.lang.split(",")]
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    generator = ReadmeGenerator(enhancer=enhancer)

    for lang in languages:
        print(f"📝 Generating README for {lang}...")
        readme = generator.generate(project_info, language=lang)

        output_file = output_dir / f"README.{lang}.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(readme)

        print(f"   ✅ Saved: {output_file}")

    # Also create main README.md with language switcher
    main_readme = generator.generate_main_readme(project_info, languages)
    main_file = output_dir / "README.md"
    with open(main_file, "w", encoding="utf-8") as f:
        f.write(main_readme)

    print(f"   ✅ Main README: {main_file}")
    print(f"\n🎉 Generated {len(languages) + 1} README files in {output_dir}")

    return 0


def main() -> int:
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    commands = {
        "format": cmd_format,
        "analyze": cmd_analyze,
        "polish": cmd_polish,
        "translate": cmd_translate,
        "readme": cmd_readme,
    }

    handler = commands.get(args.command)
    if handler:
        return handler(args)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
