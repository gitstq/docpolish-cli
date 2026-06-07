# 🎉 DocPolish-CLI

🦞 Lightweight Markdown Document Intelligent Beautification Engine | 轻量级Markdown文档智能美化引擎

## ✨ 主な機能

- ✨ Smart Markdown formatting
- ✨ Document structure analysis
- ✨ AI content polishing
- ✨ Multi-language README generation
- ✨ Zero-dependency core
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
