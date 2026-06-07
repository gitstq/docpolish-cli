"""
README Generator - Multi-language README template generator.
"""

from typing import Optional, List, Dict
from .ai_enhance import AIEnhancer


class ReadmeGenerator:
    """Generate professional multi-language README files."""

    def __init__(self, enhancer: Optional[AIEnhancer] = None):
        self.enhancer = enhancer

    def generate(self, project_info: dict, language: str = "en") -> str:
        """Generate a README in the specified language."""
        generators = {
            "zh-cn": self._generate_zh_cn,
            "zh-tw": self._generate_zh_tw,
            "en": self._generate_en,
            "ja": self._generate_ja,
            "ko": self._generate_ko,
            "es": self._generate_es,
        }

        generator = generators.get(language, self._generate_en)
        return generator(project_info)

    def generate_main_readme(self, project_info: dict, languages: List[str]) -> str:
        """Generate main README with language switcher."""
        name = project_info.get("name", "Project")
        desc = project_info.get("description", "")

        lang_links = []
        lang_names = {
            "zh-cn": "简体中文",
            "zh-tw": "繁體中文",
            "en": "English",
            "ja": "日本語",
            "ko": "한국어",
            "es": "Español",
        }

        for lang in languages:
            label = lang_names.get(lang, lang)
            if lang == "en":
                lang_links.append(f"[{label}](README.{lang}.md)")
            else:
                lang_links.append(f"[{label}](README.{lang}.md)")

        return f"""# {name}

{desc}

## 🌐 Language / 语言 / 言語

{' | '.join(lang_links)}

---

> 📖 Please select your preferred language above.
> 📖 请选择您的首选语言。
> 📖 お好みの言語を選択してください。
"""

    def _generate_zh_cn(self, info: dict) -> str:
        name = info.get("name", "项目")
        desc = info.get("description", "一个优秀的开源项目")
        features = info.get("features", ["简单易用", "轻量级", "跨平台"])
        feature_lines = "\n".join(f"- ✨ {f}" for f in features)

        return f"""# 🎉 {name}

{desc}

## ✨ 核心特性

{feature_lines}
- 🚀 **零依赖** - 纯Python实现，无需额外依赖
- 🎨 **智能格式化** - 自动修复Markdown格式问题
- 🤖 **AI增强** - 集成GLM-5.1进行内容润色与翻译
- 🌍 **多语言支持** - 一键生成多语言README
- 📊 **文档分析** - 深度分析文档结构与质量

## 🚀 快速开始

### 环境要求

- Python 3.8+
- pip

### 安装

```bash
pip install docpolish
```

### 基本用法

```bash
# 格式化Markdown文档
docpolish format README.md

# 分析文档结构
docpolish analyze document.md

# AI润色内容
docpolish polish README.md --style professional

# 生成多语言README
docpolish readme --project-name "MyProject" --lang zh-cn,en
```

## 📖 详细使用指南

### 格式化命令

```bash
# 格式化并覆盖原文件
docpolish format README.md

# 格式化并输出到新文件
docpolish format README.md -o README_formatted.md

# 仅检查不修改
docpolish format README.md --check

# 显示修改差异
docpolish format README.md --diff
```

### 分析命令

```bash
# 文本格式分析
docpolish analyze document.md

# JSON格式输出
docpolish analyze document.md --json
```

### AI润色

```bash
# 专业风格润色
docpolish polish README.md --style professional

# 简洁风格润色
docpolish polish README.md --style simple

# 指定API密钥
docpolish polish README.md --api-key YOUR_API_KEY
```

### 翻译功能

```bash
# 翻译为简体中文
docpolish translate README.md --target zh-cn

# 翻译为英文
docpolish translate README.md --target en
```

### README生成器

```bash
# 生成多语言README
docpolish readme --project-name "MyApp" \\
  --description "一个强大的工具" \\
  --lang zh-cn,zh-tw,en \\
  --features "快速,易用,安全"
```

## 💡 设计思路与迭代规划

### 设计理念

DocPolish 旨在解决开发者在编写和维护Markdown文档时遇到的格式不一致、排版混乱、多语言维护困难等问题。通过智能化的格式修复和AI增强功能，让文档编写变得轻松高效。

### 技术选型

- **纯Python实现**：零依赖核心，确保跨平台兼容性
- **正则表达式引擎**：高效的文本解析与格式化
- **GLM-5.1集成**：强大的中文理解与生成能力
- **模块化架构**：易于扩展和维护

### 迭代计划

- [ ] v1.1.0 - 支持更多Markdown扩展语法（GFM、CommonMark）
- [ ] v1.2.0 - 添加实时预览功能
- [ ] v1.3.0 - 支持自定义格式化规则
- [ ] v2.0.0 - Web UI界面

## 📦 打包与部署指南

### 从源码安装

```bash
git clone https://github.com/gitstq/docpolish-cli.git
cd docpolish-cli
pip install -e .
```

### 构建发布包

```bash
python -m build
```

### 安装本地包

```bash
pip install dist/docpolish-1.0.0-py3-none-any.whl
```

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

### 提交规范

- `feat:` 新增功能
- `fix:` 修复问题
- `docs:` 文档更新
- `refactor:` 代码重构

### 开发流程

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feat/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送分支 (`git push origin feat/amazing-feature`)
5. 创建 Pull Request

## 📄 开源协议

本项目采用 [MIT](LICENSE) 开源协议。

---

<p align="center">Made with ❤️ by Lobster AI</p>
"""

    def _generate_zh_tw(self, info: dict) -> str:
        name = info.get("name", "專案")
        desc = info.get("description", "一個優秀的開源專案")
        features = info.get("features", ["簡單易用", "輕量級", "跨平台"])
        feature_lines = "\n".join(f"- ✨ {f}" for f in features)

        return f"""# 🎉 {name}

{desc}

## ✨ 核心特性

{feature_lines}
- 🚀 **零依賴** - 純Python實現，無需額外依賴
- 🎨 **智慧格式化** - 自動修復Markdown格式問題
- 🤖 **AI增強** - 整合GLM-5.1進行內容潤飾與翻譯
- 🌍 **多語言支援** - 一鍵生成多語言README
- 📊 **文件分析** - 深度分析文件結構與品質

## 🚀 快速開始

### 環境要求

- Python 3.8+
- pip

### 安裝

```bash
pip install docpolish
```

### 基本用法

```bash
# 格式化Markdown文件
docpolish format README.md

# 分析文件結構
docpolish analyze document.md

# AI潤飾內容
docpolish polish README.md --style professional

# 生成多語言README
docpolish readme --project-name "MyProject" --lang zh-tw,en
```

## 📖 詳細使用指南

### 格式化命令

```bash
# 格式化並覆蓋原文件
docpolish format README.md

# 格式化並輸出到新文件
docpolish format README.md -o README_formatted.md

# 僅檢查不修改
docpolish format README.md --check

# 顯示修改差異
docpolish format README.md --diff
```

### 分析命令

```bash
# 文字格式分析
docpolish analyze document.md

# JSON格式輸出
docpolish analyze document.md --json
```

### AI潤飾

```bash
# 專業風格潤飾
docpolish polish README.md --style professional

# 簡潔風格潤飾
docpolish polish README.md --style simple

# 指定API密鑰
docpolish polish README.md --api-key YOUR_API_KEY
```

### 翻譯功能

```bash
# 翻譯為繁體中文
docpolish translate README.md --target zh-tw

# 翻譯為英文
docpolish translate README.md --target en
```

### README生成器

```bash
# 生成多語言README
docpolish readme --project-name "MyApp" \\
  --description "一個強大的工具" \\
  --lang zh-tw,zh-cn,en \\
  --features "快速,易用,安全"
```

## 💡 設計思路與迭代規劃

### 設計理念

DocPolish 旨在解決開發者在編寫和維護Markdown文件時遇到的格式不一致、排版混亂、多語言維護困難等問題。通過智慧化的格式修復和AI增強功能，讓文件編寫變得輕鬆高效。

### 技術選型

- **純Python實現**：零依賴核心，確保跨平台相容性
- **正規表示式引擎**：高效的文字解析與格式化
- **GLM-5.1整合**：強大的中文理解與生成能力
- **模組化架構**：易於擴展和維護

### 迭代計劃

- [ ] v1.1.0 - 支援更多Markdown擴展語法（GFM、CommonMark）
- [ ] v1.2.0 - 添加即時預覽功能
- [ ] v1.3.0 - 支援自定義格式化規則
- [ ] v2.0.0 - Web UI介面

## 📦 打包與部署指南

### 從原始碼安裝

```bash
git clone https://github.com/gitstq/docpolish-cli.git
cd docpolish-cli
pip install -e .
```

### 構建發布包

```bash
python -m build
```

### 安裝本地包

```bash
pip install dist/docpolish-1.0.0-py3-none-any.whl
```

## 🤝 貢獻指南

歡迎提交Issue和Pull Request！

### 提交規範

- `feat:` 新增功能
- `fix:` 修復問題
- `docs:` 文件更新
- `refactor:` 代碼重構

### 開發流程

1. Fork 本倉庫
2. 建立功能分支 (`git checkout -b feat/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送分支 (`git push origin feat/amazing-feature`)
5. 建立 Pull Request

## 📄 開源協議

本專案採用 [MIT](LICENSE) 開源協議。

---

<p align="center">Made with ❤️ by Lobster AI</p>
"""

    def _generate_en(self, info: dict) -> str:
        name = info.get("name", "Project")
        desc = info.get("description", "An awesome open-source project")
        features = info.get("features", ["Easy to use", "Lightweight", "Cross-platform"])
        feature_lines = "\n".join(f"- ✨ {f}" for f in features)

        return f"""# 🎉 {name}

{desc}

## ✨ Core Features

{feature_lines}
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
docpolish readme --project-name "MyApp" \\
  --description "A powerful tool" \\
  --lang en,zh-cn,zh-tw \\
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
"""

    def _generate_ja(self, info: dict) -> str:
        name = info.get("name", "プロジェクト")
        desc = info.get("description", "素晴らしいオープンソースプロジェクト")
        features = info.get("features", ["使いやすい", "軽量", "クロスプラットフォーム"])
        feature_lines = "\n".join(f"- ✨ {f}" for f in features)

        return f"""# 🎉 {name}

{desc}

## ✨ 主な機能

{feature_lines}
- 🚀 **ゼロ依存** - 純粋なPython実装、追加の依存関係不要
- 🎨 **スマートフォーマット** - Markdownの書式問題を自動修正
- 🤖 **AI強化** - GLM-5.1統合によるコンテンツの磨き上げと翻訳
- 🌍 **多言語サポート** - ワンクリックで多言語READMEを生成
- 📊 **ドキュメント分析** - ドキュメント構造と品質の深層分析

## 🚀 クイックスタート

### 必要条件

- Python 3.8+
- pip

### インストール

```bash
pip install docpolish
```

### 基本的な使い方

```bash
# Markdownドキュメントをフォーマット
docpolish format README.md

# ドキュメント構造を分析
docpolish analyze document.md

# AIによるコンテンツ磨き上げ
docpolish polish README.md --style professional

# 多言語READMEを生成
docpolish readme --project-name "MyProject" --lang ja,en
```

## 📖 詳細な使用ガイド

### フォーマットコマンド

```bash
# フォーマットして元のファイルを上書き
docpolish format README.md

# 新しいファイルに出力
docpolish format README.md -o README_formatted.md

# 確認のみ、変更しない
docpolish format README.md --check

# 変更の差分を表示
docpolish format README.md --diff
```

### 分析コマンド

```bash
# テキスト形式の分析
docpolish analyze document.md

# JSON形式で出力
docpolish analyze document.md --json
```

### AI磨き上げ

```bash
# プロフェッショナルスタイル
docpolish polish README.md --style professional

# シンプルスタイル
docpolish polish README.md --style simple

# APIキーを指定
docpolish polish README.md --api-key YOUR_API_KEY
```

### 翻訳機能

```bash
# 日本語に翻訳
docpolish translate README.md --target ja

# 英語に翻訳
docpolish translate README.md --target en
```

## 💡 設計思想とロードマップ

### 設計思想

DocPolishは、開発者がMarkdownドキュメントの作成と保守において直面する書式の不整合、レイアウトの混乱、多言語保守の困難さを解決するために設計されました。インテリジェントな書式修正とAI強化機能により、ドキュメント作成が効率的になります。

### 技術選定

- **純粋なPython実装**: ゼロ依存のコアでクロスプラットフォーム互換性を確保
- **正規表現エンジン**: 効率的なテキスト解析とフォーマット
- **GLM-5.1統合**: 強力な中国語理解と生成能力
- **モジュール化アーキテクチャ**: 拡張と保守が容易

### ロードマップ

- [ ] v1.1.0 - より多くのMarkdown拡張構文のサポート（GFM、CommonMark）
- [ ] v1.2.0 - リアルタイムプレビュー機能の追加
- [ ] v1.3.0 - カスタムフォーマットルールのサポート
- [ ] v2.0.0 - Web UIインターフェース

## 📦 パッケージングとデプロイガイド

### ソースからインストール

```bash
git clone https://github.com/gitstq/docpolish-cli.git
cd docpolish-cli
pip install -e .
```

### リリースパッケージのビルド

```bash
python -m build
```

### ローカルパッケージのインストール

```bash
pip install dist/docpolish-1.0.0-py3-none-any.whl
```

## 🤝 貢献ガイド

IssueとPull Requestを歓迎します！

### コミット規約

- `feat:` 新機能
- `fix:` バグ修正
- `docs:` ドキュメント更新
- `refactor:` コードリファクタリング

### 開発フロー

1. このリポジトリをFork
2. 機能ブランチを作成 (`git checkout -b feat/amazing-feature`)
3. 変更をコミット (`git commit -m 'feat: add amazing feature'`)
4. ブランチをプッシュ (`git push origin feat/amazing-feature`)
5. Pull Requestを作成

## 📄 ライセンス

このプロジェクトは [MIT](LICENSE) ライセンスの下で公開されています。

---

<p align="center">Made with ❤️ by Lobster AI</p>
"""

    def _generate_ko(self, info: dict) -> str:
        name = info.get("name", "프로젝트")
        desc = info.get("description", "멋진 오픈소스 프로젝트")
        features = info.get("features", ["사용하기 쉬운", "경량", "크로스 플랫폼"])
        feature_lines = "\n".join(f"- ✨ {f}" for f in features)

        return f"""# 🎉 {name}

{desc}

## ✨ 핵심 기능

{feature_lines}
- 🚀 **제로 의존성** - 순수 Python 구현, 추가 의존성 불필요
- 🎨 **스마트 포맷팅** - Markdown 형식 문제 자동 수정
- 🤖 **AI 강화** - GLM-5.1 통합으로 콘텐츠 다듬기 및 번역
- 🌍 **다국어 지원** - 원클릭 다국어 README 생성
- 📊 **문서 분석** - 문서 구조 및 품질 심층 분석

## 🚀 빠른 시작

### 요구사항

- Python 3.8+
- pip

### 설치

```bash
pip install docpolish
```

### 기본 사용법

```bash
# Markdown 문서 포맷팅
docpolish format README.md

# 문서 구조 분석
docpolish analyze document.md

# AI 콘텐츠 다듬기
docpolish polish README.md --style professional

# 다국어 README 생성
docpolish readme --project-name "MyProject" --lang ko,en
```

## 📖 상세 사용 가이드

### 포맷 명령

```bash
# 포맷하고 원본 파일 덮어쓰기
docpolish format README.md

# 새 파일에 출력
docpolish format README.md -o README_formatted.md

# 확인만 하고 수정하지 않음
docpolish format README.md --check

# 변경 사항 차이 표시
docpolish format README.md --diff
```

### 분석 명령

```bash
# 텍스트 형식 분석
docpolish analyze document.md

# JSON 형식 출력
docpolish analyze document.md --json
```

### AI 다듬기

```bash
# 전문가 스타일 다듬기
docpolish polish README.md --style professional

# 간단한 스타일 다듬기
docpolish polish README.md --style simple

# API 키 지정
docpolish polish README.md --api-key YOUR_API_KEY
```

### 번역 기능

```bash
# 한국어로 번역
docpolish translate README.md --target ko

# 영어로 번역
docpolish translate README.md --target en
```

## 💡 설계 철학 및 로드맵

### 설계 철학

DocPolish는 개발자가 Markdown 문서를 작성하고 유지 관리할 때 직면하는 형식 불일치, 레이아웃 혼란, 다국어 유지 관리의 어려움을 해결하기 위해 설계되었습니다. 지능형 형식 수정 및 AI 강화 기능을 통해 문서 작성이 효율적이 됩니다.

### 기술 선택

- **순수 Python 구현**: 제로 의존성 코어로 크로스 플랫폼 호환성 보장
- **정규 표현식 엔진**: 효율적인 텍스트 구문 분석 및 포맷팅
- **GLM-5.1 통합**: 강력한 중국어 이해 및 생성 기능
- **모듈화 아키텍처**: 확장 및 유지 관리가 용이

### 로드맵

- [ ] v1.1.0 - 더 많은 Markdown 확장 구문 지원 (GFM, CommonMark)
- [ ] v1.2.0 - 실시간 미리보기 기능 추가
- [ ] v1.3.0 - 사용자 정의 포맷팅 규칙 지원
- [ ] v2.0.0 - Web UI 인터페이스

## 📦 패키징 및 배포 가이드

### 소스에서 설치

```bash
git clone https://github.com/gitstq/docpolish-cli.git
cd docpolish-cli
pip install -e .
```

### 릴리스 패키지 빌드

```bash
python -m build
```

### 로컬 패키지 설치

```bash
pip install dist/docpolish-1.0.0-py3-none-any.whl
```

## 🤝 기여 가이드

Issue와 Pull Request를 환영합니다!

### 커밋 규약

- `feat:` 새 기능
- `fix:` 버그 수정
- `docs:` 문서 업데이트
- `refactor:` 코드 리팩토링

### 개발 워크플로우

1. 이 저장소를 Fork
2. 기능 브랜치 생성 (`git checkout -b feat/amazing-feature`)
3. 변경사항 커밋 (`git commit -m 'feat: add amazing feature'`)
4. 브랜치 푸시 (`git push origin feat/amazing-feature`)
5. Pull Request 생성

## 📄 라이선스

이 프로젝트는 [MIT](LICENSE) 라이선스 하에 공개되어 있습니다.

---

<p align="center">Made with ❤️ by Lobster AI</p>
"""

    def _generate_es(self, info: dict) -> str:
        name = info.get("name", "Proyecto")
        desc = info.get("description", "Un proyecto open-source increíble")
        features = info.get("features", ["Fácil de usar", "Ligero", "Multiplataforma"])
        feature_lines = "\n".join(f"- ✨ {f}" for f in features)

        return f"""# 🎉 {name}

{desc}

## ✨ Características Principales

{feature_lines}
- 🚀 **Cero Dependencias** - Implementación pura en Python, sin dependencias adicionales
- 🎨 **Formateo Inteligente** - Corrige automáticamente problemas de formato Markdown
- 🤖 **Mejora con IA** - Integrado con GLM-5.1 para pulir contenido y traducir
- 🌍 **Soporte Multiidioma** - Generación de README en múltiples idiomas con un clic
- 📊 **Análisis de Documentos** - Análisis profundo de estructura y calidad del documento

## 🚀 Inicio Rápido

### Requisitos

- Python 3.8+
- pip

### Instalación

```bash
pip install docpolish
```

### Uso Básico

```bash
# Formatear un documento Markdown
docpolish format README.md

# Analizar estructura del documento
docpolish analyze document.md

# Pulir contenido con IA
docpolish polish README.md --style professional

# Generar README multiidioma
docpolish readme --project-name "MyProject" --lang es,en
```

## 📖 Guía de Uso Detallada

### Comando de Formateo

```bash
# Formatear y sobrescribir archivo original
docpolish format README.md

# Formatear y guardar en nuevo archivo
docpolish format README.md -o README_formatted.md

# Solo verificar, no modificar
docpolish format README.md --check

# Mostrar diferencias de cambios
docpolish format README.md --diff
```

### Comando de Análisis

```bash
# Análisis en formato texto
docpolish analyze document.md

# Salida en formato JSON
docpolish analyze document.md --json
```

### Pulido con IA

```bash
# Estilo profesional
docpolish polish README.md --style professional

# Estilo simple
docpolish polish README.md --style simple

# Especificar clave API
docpolish polish README.md --api-key YOUR_API_KEY
```

### Traducción

```bash
# Traducir al español
docpolish translate README.md --target es

# Traducir al inglés
docpolish translate README.md --target en
```

## 💡 Filosofía de Diseño y Hoja de Ruta

### Filosofía de Diseño

DocPolish está diseñado para resolver las inconsistencias de formato, el desorden de diseño y las dificultades de mantenimiento multilingüe que enfrentan los desarrolladores al escribir y mantener documentos Markdown. A través de la corrección inteligente de formato y las funciones de mejora con IA, la escritura de documentos se vuelve eficiente.

### Elecciones Técnicas

- **Implementación Pura en Python**: Núcleo sin dependencias garantiza compatibilidad multiplataforma
- **Motor de Expresiones Regulares**: Análisis y formateo de texto eficiente
- **Integración GLM-5.1**: Potentes capacidades de comprensión y generación en chino
- **Arquitectura Modular**: Fácil de extender y mantener

### Hoja de Ruta

- [ ] v1.1.0 - Soporte para más sintaxis de extensión Markdown (GFM, CommonMark)
- [ ] v1.2.0 - Agregar función de vista previa en tiempo real
- [ ] v1.3.0 - Soporte para reglas de formato personalizadas
- [ ] v2.0.0 - Interfaz Web UI

## 📦 Guía de Empaquetado y Despliegue

### Instalar desde el Código Fuente

```bash
git clone https://github.com/gitstq/docpolish-cli.git
cd docpolish-cli
pip install -e .
```

### Construir Paquete de Lanzamiento

```bash
python -m build
```

### Instalar Paquete Local

```bash
pip install dist/docpolish-1.0.0-py3-none-any.whl
```

## 🤝 Guía de Contribución

¡Issues y Pull Requests son bienvenidos!

### Convención de Commits

- `feat:` Nueva característica
- `fix:` Corrección de errores
- `docs:` Actualización de documentación
- `refactor:` Refactorización de código

### Flujo de Desarrollo

1. Hacer Fork de este repositorio
2. Crear una rama de características (`git checkout -b feat/amazing-feature`)
3. Confirmar tus cambios (`git commit -m 'feat: add amazing feature'`)
4. Subir a la rama (`git push origin feat/amazing-feature`)
5. Crear un Pull Request

## 📄 Licencia

Este proyecto está licenciado bajo la [MIT](LICENSE).

---

<p align="center">Made with ❤️ by Lobster AI</p>
"""
