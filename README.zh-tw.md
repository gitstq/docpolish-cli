# 🎉 DocPolish-CLI

🦞 Lightweight Markdown Document Intelligent Beautification Engine | 轻量级Markdown文档智能美化引擎

## ✨ 核心特性

- ✨ Smart Markdown formatting
- ✨ Document structure analysis
- ✨ AI content polishing
- ✨ Multi-language README generation
- ✨ Zero-dependency core
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
docpolish readme --project-name "MyApp" \
  --description "一個強大的工具" \
  --lang zh-tw,zh-cn,en \
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
