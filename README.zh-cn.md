# 🎉 DocPolish-CLI

🦞 Lightweight Markdown Document Intelligent Beautification Engine | 轻量级Markdown文档智能美化引擎

## ✨ 核心特性

- ✨ Smart Markdown formatting
- ✨ Document structure analysis
- ✨ AI content polishing
- ✨ Multi-language README generation
- ✨ Zero-dependency core
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
docpolish readme --project-name "MyApp" \
  --description "一个强大的工具" \
  --lang zh-cn,zh-tw,en \
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
