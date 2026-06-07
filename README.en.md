# 🎉 DocPolish-CLI

🦞 Lightweight Markdown Document Intelligent Beautification Engine | 轻量级Markdown文档智能美化引擎

## ✨ Core Features

- ✨ Smart Markdown formatting
- ✨ Document structure analysis
- ✨ AI content polishing
- ✨ Multi-language README generation
- ✨ Zero-dependency core
- 🚀 **Zero Dependencies** - Pure Python implementation, no extra dependencies needed
- 🎨 **Smart Formatting** - Automatically fix Markdown formatting issues
- 🤖 **AI Enhancement** - Integrated with GLM-5.1 for content polishing and translation
- 🌍 **Multi-language Support** - One-click multi-language README generation
- 📊 **Document Analysis** - Deep analysis of document structure and quality

## 🚀 Quick Start

### Requirements

- Python 3.8+
- pip

### Installation

```bash
pip install docpolish
```

### Basic Usage

```bash
# Format a Markdown document
docpolish format README.md

# Analyze document structure
docpolish analyze document.md

# AI-powered content polishing
docpolish polish README.md --style professional

# Generate multi-language README
docpolish readme --project-name "MyProject" --lang en,zh-cn
```

## 📖 Detailed Usage Guide

### Format Command

```bash
# Format and overwrite original file
docpolish format README.md

# Format and output to new file
docpolish format README.md -o README_formatted.md

# Check only, don't modify
docpolish format README.md --check

# Show diff of changes
docpolish format README.md --diff
```

### Analyze Command

```bash
# Text format analysis
docpolish analyze document.md

# JSON output
docpolish analyze document.md --json
```

### AI Polishing

```bash
# Professional style polishing
docpolish polish README.md --style professional

# Simple style polishing
docpolish polish README.md --style simple

# Specify API key
docpolish polish README.md --api-key YOUR_API_KEY
```

### Translation

```bash
# Translate to English
docpolish translate README.md --target en

# Translate to Simplified Chinese
docpolish translate README.md --target zh-cn
```

### README Generator

```bash
# Generate multi-language README
docpolish readme --project-name "MyApp" \
  --description "A powerful tool" \
  --lang en,zh-cn,zh-tw \
  --features "Fast,Easy,Secure"
```

## 💡 Design Philosophy & Roadmap

### Design Philosophy

DocPolish is designed to solve the formatting inconsistencies, layout chaos, and multi-language maintenance difficulties that developers face when writing and maintaining Markdown documents. Through intelligent format fixing and AI enhancement features, document writing becomes effortless and efficient.

### Technical Choices

- **Pure Python Implementation**: Zero-dependency core ensures cross-platform compatibility
- **Regex Engine**: Efficient text parsing and formatting
- **GLM-5.1 Integration**: Powerful Chinese understanding and generation capabilities
- **Modular Architecture**: Easy to extend and maintain

### Roadmap

- [ ] v1.1.0 - Support more Markdown extension syntaxes (GFM, CommonMark)
- [ ] v1.2.0 - Add real-time preview feature
- [ ] v1.3.0 - Support custom formatting rules
- [ ] v2.0.0 - Web UI interface

## 📦 Packaging & Deployment Guide

### Install from Source

```bash
git clone https://github.com/gitstq/docpolish-cli.git
cd docpolish-cli
pip install -e .
```

### Build Release Package

```bash
python -m build
```

### Install Local Package

```bash
pip install dist/docpolish-1.0.0-py3-none-any.whl
```

## 🤝 Contributing Guide

Issues and Pull Requests are welcome!

### Commit Convention

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation update
- `refactor:` Code refactoring

### Development Workflow

1. Fork this repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the [MIT](LICENSE) License.

---

<p align="center">Made with ❤️ by Lobster AI</p>
