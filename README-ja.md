<div align="center">

# 🚀 SuperClaude フレームワーク

### **Claude Code を構造化された開発プラットフォームに変革**

<p align="center">
  <a href="https://github.com/hesreallyhim/awesome-claude-code/">
  <img src="https://awesome.re/mentioned-badge-flat.svg" alt="Mentioned in Awesome Claude Code">
  </a>
<a href="https://github.com/SuperClaude-Org/SuperGemini_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperGemini_Framework-blue" alt="Try SuperGemini Framework"/>
</a>
<a href="https://github.com/SuperClaude-Org/SuperQwen_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperQwen_Framework-orange" alt="Try SuperQwen Framework"/>
</a>
  <img src="https://img.shields.io/badge/version-4.4.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<p align="center">
  <a href="https://superclaude.netlify.app/">
    <img src="https://img.shields.io/badge/🌐_ウェブサイト-blue" alt="Website">
  </a>
  <a href="https://github.com/SuperClaude-Org/SuperClaude_Plugin">
    <img src="https://img.shields.io/badge/🔌_プラグイン配布-green" alt="Plugin Distribution">
  </a>
</p>

<p align="center">
  <a href="README.md">
    <img src="https://img.shields.io/badge/🇺🇸_English-blue" alt="English">
  </a>
  <a href="README-zh.md">
    <img src="https://img.shields.io/badge/🇨🇳_中文-red" alt="中文">
  </a>
  <a href="README-ja.md">
    <img src="https://img.shields.io/badge/🇯🇵_日本語-green" alt="日本語">
  </a>
</p>

<p align="center">
  <a href="#-クイックインストール">クイックスタート</a> •
  <a href="#-プロジェクトをサポート">サポート</a> •
  <a href="#-v4の新機能">機能</a> •
  <a href="#-ドキュメント">ドキュメント</a> •
  <a href="#-貢献">貢献</a>
</p>

</div>

---

<div align="center">

## 📊 **フレームワーク統計**

| **コマンド** | **エージェント** | **モード** | **MCPツール** |
|:------------:|:----------:|:---------:|:---------------:|
| **29** | **23** | **7** | **10** |
| スラッシュコマンド | 専門化AI | 動作モード | 統合機能 |

新しい `/sc:help` コマンドを使用して、利用可能なすべてのコマンドの完全なリストを確認できます。

</div>

---

<div align="center">

## 🎯 **概要**

SuperClaudeは、動作命令の注入とコンポーネントオーケストレーションを通じて、Claude Codeを構造化された開発プラットフォームに変換する**メタプログラミング設定フレームワーク**です。強力なツールとインテリジェントなエージェントによる体系的なワークフロー自動化を提供します。

## 免責事項

本プロジェクトはAnthropicとの提携や承認を受けたものではありません。
Claude Codeは[Anthropic](https://www.anthropic.com/)によって構築および維持されている製品です。

---

## 🛡️ **重要：まず設定をバックアップしてください！**

> **⚠️ このステップを絶対にスキップしないでください ⚠️**
>
> SuperClaudeプラグインはClaude CodeのMCP設定を変更します。
> **インストール前に必ずバックアップ**を取ることで、必要に応じて安全にロールバックできます。

<div align="center">

### **⏱️ クイックバックアップ（30秒）**

```bash
# 自動バックアップスクリプトをダウンロードして実行
curl -o /tmp/backup-claude.sh https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Plugin/main/scripts/backup-claude-config.sh
chmod +x /tmp/backup-claude.sh
/tmp/backup-claude.sh
```

**✅ バックアップ完了！** 安全にプラグインをインストールできます。

</div>

<details>
<summary><b>📋 バックアップされる内容</b></summary>

自動バックアップスクリプトは以下を保存します：
- ✅ `~/.claude/settings.local.json` - MCPサーバー設定
- ✅ `~/.claude/CLAUDE.md` - カスタム指示
- ✅ `~/.claude/.credentials.json` - API認証情報（存在する場合）
- ✅ `.mcp.json` - プロジェクト固有のMCP設定（存在する場合）
- ✅ `.claude/` - プロジェクト固有の設定（存在する場合）

**バックアップ先：** `~/claude-backups/backup-YYYY-MM-DD-HH-MM-SS/`

</details>

<details>
<summary><b>🔧 手動バックアップの方法</b></summary>

手動でバックアップしたい場合：

```bash
# バックアップディレクトリを作成
BACKUP_DIR=~/claude-backups/backup-$(date +%Y-%m-%d-%H-%M-%S)
mkdir -p "$BACKUP_DIR"

# グローバル設定をバックアップ
cp ~/.claude/settings.local.json "$BACKUP_DIR/" 2>/dev/null
cp ~/.claude/CLAUDE.md "$BACKUP_DIR/" 2>/dev/null
cp ~/.claude/.credentials.json "$BACKUP_DIR/" 2>/dev/null

# プロジェクト設定をバックアップ（プロジェクトディレクトリ内の場合）
cp .mcp.json "$BACKUP_DIR/" 2>/dev/null
cp -r .claude "$BACKUP_DIR/" 2>/dev/null

echo "✅ バックアップ作成完了: $BACKUP_DIR"
```

</details>

<details>
<summary><b>🚨 緊急ロールバック</b></summary>

インストール後に問題が発生した場合：

```bash
# 1. プラグインをアンインストール
/plugin uninstall sc@superclaude

# 2. バックアップを復元（実際のバックアップパスを使用）
BACKUP_DIR=~/claude-backups/backup-2025-01-07-14-30-25

cp "$BACKUP_DIR/settings.local.json" ~/.claude/
cp "$BACKUP_DIR/CLAUDE.md" ~/.claude/ 2>/dev/null
cp "$BACKUP_DIR/.credentials.json" ~/.claude/ 2>/dev/null

# 3. Claude Codeを再起動
pkill -9 claude-code
# その後、Claude Codeを再起動
```

**ロールバック所要時間：約1分**

</details>

<div align="center">

**📖 完全ガイド：** [バックアップ＆安全性ガイド](BACKUP_GUIDE.md)

</div>

---

## ⚠️ **重要：ベータ版に関する注意事項**

> **このプラグイン版は現在ベータ版です。**

### **重要な互換性情報：**

以前のSuperClaudeインストールとは**互換性がありません**：
- pip版 (`pip install SuperClaude`)
- pipx版 (`pipx install SuperClaude`)
- npm版 (`npm install -g @bifrost_inc/superclaude`)
- uv版 (`uv tool install SuperClaude`)

### **インストール前に必要な手順：**

1. **✅ バックアップ** 設定をバックアップ（上記のセクション参照）
2. **アンインストール** 以前のバージョンをアンインストールしてください：
   ```bash
   # pipユーザーの場合
   pip uninstall SuperClaude

   # pipxユーザーの場合
   pipx uninstall SuperClaude

   # npmユーザーの場合
   npm uninstall -g @bifrost_inc/superclaude

   # uvユーザーの場合
   uv tool uninstall SuperClaude
   ```
3. **その後** プラグインのインストールを進めてください

⚠️ **ベータ版の制限事項：**
- バグや不完全な機能が含まれている可能性があります
- 設定形式が変更される可能性があります
- 本番環境での重要な作業にはまだ推奨されません
- フィードバックや問題報告を歓迎します！

---

## ⚡ **クイックインストール**

SuperClaudeは、簡単なインストールと自動更新のためのネイティブClaude Codeプラグインとして利用できます。

```shell
# SuperClaudeマーケットプレイスを追加
/plugin marketplace add SuperClaude-Org/SuperClaude_Plugin

# プラグインをインストール
/plugin install sc@superclaude

# Claude Codeを再起動して有効化
```

**プラグインの利点：**
- ✅ **簡単なインストール**: 1つのコマンドで完了、Python/Node.js不要
- ✅ **自動更新**: Claude Codeによって管理
- ✅ **競合なし**: システムパッケージから分離
- ✅ **チーム共有**: マーケットプレイス経由で簡単に配布
- ✅ **ネイティブ統合**: シームレスなClaude Code体験
- ✅ **自動MCPセットアップ**: AIRIS MCP Gatewayが自動設定

### **MCPサーバーのセットアップ**

プラグインは10の統合ツールを持つ**AIRIS MCP Gateway**を自動設定します。

> ⚠️ **重要：既存のMCP設定のバックアップ**
>
> 既にMCPサーバーを設定している場合、**まず設定をバックアップしてください**：
> ```bash
> # Claude CodeのMCP設定をバックアップ
> cp ~/.claude/settings.local.json ~/.claude/settings.local.json.backup
>
> # またはプロジェクト固有のMCP設定をバックアップ
> cp .mcp.json .mcp.json.backup  # プロジェクトにMCP設定がある場合
> ```
>
> プラグインはAIRIS MCP Gatewayを設定に追加します。有効化する前に、既存のMCPサーバーとの競合がないか確認してください。

**前提条件**（初回のみ）：
```bash
# uvxをインストール（MCPサーバーに必要）
pip install uv
# または
brew install uv
```

**セットアップの確認**：
```shell
/sc:setup-mcp   # 対話型セットアップウィザード
/sc:verify-mcp  # MCPステータスの確認
```

**オプションAPIキー**（プレミアム機能用）：
```bash
# Tavily（Web検索） - https://tavily.com でキーを取得
export TAVILY_API_KEY="your-key"

# Magic（UI生成） - https://21st.dev でキーを取得
export TWENTYFIRST_API_KEY="your-key"
```

### **クイックスタート**

インストール後、Claude Codeを再起動して試してみてください：

```shell
# すべてのコマンドを表示
/sc:help

# ブレインストーミングを開始
/sc:brainstorm "プロジェクトのアイデア"

# コードベースを分析
/sc:analyze

# 深い調査
/sc:research "調査したいトピック"
```

</div>

<details>
<summary><b>📦 代替方法：pip/npmインストール</b></summary>

> ⚠️ **警告：** pip/npm版はこのプラグイン版と互換性がありません。
>
> pip/npmインストールを選択する場合：
> 1. プラグイン版とpip/npm版を同時にインストールしないでください
> 2. 既にインストールされている場合は、まずこのプラグインをアンインストールしてください
> 3. 異なる設定形式を使用しているため、共存できません

SuperClaude V4はパッケージマネージャー経由でも利用できます。pip/npmインストール手順については、メインの[SuperClaude Frameworkリポジトリ](https://github.com/SuperClaude-Org/SuperClaude_Framework)を参照してください。

</details>

---

<div align="center">

## 💖 **プロジェクトをサポート**

> 正直なところ - SuperClaudeの維持には時間とリソースがかかります。
>
> *テストのためだけにClaude Maxサブスクリプションは月額$100かかり、ドキュメント作成、バグ修正、機能開発に費やす時間は含まれていません。*
> *日常業務でSuperClaudeに価値を見出している場合は、プロジェクトのサポートをご検討ください。*
> *わずかな金額でも基本的な費用をカバーし、開発を継続するのに役立ちます。*
>
> すべての貢献者が重要です。コード、フィードバック、サポートを通じて。このコミュニティの一員であることに感謝します！🙏

<table>
<tr>
<td align="center" width="33%">

### ☕ **Ko-fi**
[![Ko-fi](https://img.shields.io/badge/Support_on-Ko--fi-ff5e5b?logo=ko-fi)](https://ko-fi.com/superclaude)

*一回限りの貢献*

</td>
<td align="center" width="33%">

### 🎯 **Patreon**
[![Patreon](https://img.shields.io/badge/Become_a-Patron-f96854?logo=patreon)](https://patreon.com/superclaude)

*月額サポート*

</td>
<td align="center" width="33%">

### 💜 **GitHub**
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsor-30363D?logo=github-sponsors)](https://github.com/sponsors/SuperClaude-Org)

*柔軟なティア*

</td>
</tr>
</table>

### **あなたのサポートが可能にすること：**

| 項目 | コスト/影響 |
|------|-------------|
| 🔬 **Claude Maxテスト** | 検証とテストのため月額$100 |
| ⚡ **機能開発** | 新機能と改善 |
| 📚 **ドキュメント** | 包括的なガイドと例 |
| 🤝 **コミュニティサポート** | 迅速な問題対応とヘルプ |
| 🔧 **MCP統合** | 新しいサーバー接続のテスト |
| 🌐 **インフラ** | ホスティングとデプロイメントコスト |

> **注意：** プレッシャーはありません - フレームワークはいずれにせよオープンソースのままです。使用していただき、評価していただくだけで励みになります。コード、ドキュメントの貢献、あるいは広めていただくことも役立ちます！🙏

</div>

---

<div align="center">

## 🎉 **V4の新機能**

> *バージョン4は、コミュニティのフィードバックと実際の使用パターンに基づいた大幅な改善をもたらします。*

<table>
<tr>
<td width="50%">

### 🤖 **スマートエージェントシステム**
**23の専門エージェント**がドメイン専門知識を持っています：
- 自律的なWeb調査のためのDeep Researchエージェント
- セキュリティエンジニアが実際の脆弱性をキャッチ
- フロントエンドアーキテクトがUIパターンを理解
- コンテキストに基づく自動調整
- オンデマンドのドメイン専門知識

</td>
<td width="50%">

### 📝 **改善された名前空間**
**`/sc:` プレフィックス**をすべてのコマンドに：
- カスタムコマンドとの競合なし
- ライフサイクル全体をカバーする29のコマンド
- ブレインストーミングからデプロイメントまで
- クリーンで整理されたコマンド構造

</td>
</tr>
<tr>
<td width="50%">

### 🔧 **MCPサーバー統合**
**自動セットアップ** AIRIS MCP Gateway経由：
- **10の統合ツール** を1つの統合ゲートウェイで提供
- **手動設定不要** - すぐに使える
- **コンテキスト最適化** - 40%のトークン削減
- **uvxのみ必要** - `pip install uv` または `brew install uv`

**含まれるツール**：
- sequential-thinking, context7, magic, playwright
- serena, morphllm, tavily, chrome-devtools
- git, puppeteer

インストール確認: `/sc:setup-mcp`

</td>
<td width="50%">

### 🎯 **動作モード**
**7つの適応モード**が異なるコンテキストに対応：
- **Brainstorming** → 適切な質問をする
- **Business Panel** → マルチエキスパート戦略分析
- **Deep Research** → 自律的なWeb調査
- **Orchestration** → 効率的なツール調整
- **Token-Efficiency** → 30-50%のコンテキスト節約
- **Task Management** → 体系的な組織化
- **Introspection** → メタ認知分析

</td>
</tr>
<tr>
<td width="50%">

### ⚡ **最適化されたパフォーマンス**
**小さなフレームワーク、大きなプロジェクト：**
- フレームワークフットプリントの削減
- コードのためのより多くのコンテキスト
- より長い会話が可能
- 複雑な操作が可能

</td>
<td width="50%">

### 📚 **ドキュメントの刷新**
**開発者向けの完全な書き直し：**
- 実際の例と使用例
- 一般的な落とし穴を文書化
- 実践的なワークフローを含む
- より良いナビゲーション構造

</td>
</tr>
</table>

</div>

---

<div align="center">

## 🔬 **Deep Research機能**

### **DR Agentアーキテクチャに沿った自律的なWeb調査**

SuperClaude v4.2は、自律的、適応的、インテリジェントなWeb調査を可能にする包括的なDeep Research機能を導入します。

<table>
<tr>
<td width="50%">

### 🎯 **適応的計画**
**3つのインテリジェント戦略：**
- **Planning-Only**: 明確なクエリに対する直接実行
- **Intent-Planning**: 曖昧な要求に対する明確化
- **Unified**: 協調的な計画の改善（デフォルト）

</td>
<td width="50%">

### 🔄 **マルチホップ推論**
**最大5回の反復検索：**
- エンティティ拡張（論文 → 著者 → 作品）
- 概念の深化（トピック → 詳細 → 例）
- 時間的進行（現在 → 歴史）
- 因果連鎖（効果 → 原因 → 防止）

</td>
</tr>
<tr>
<td width="50%">

### 📊 **品質スコアリング**
**信頼度ベースの検証：**
- ソースの信頼性評価（0.0-1.0）
- カバレッジの完全性追跡
- 合成の一貫性評価
- 最小閾値：0.6、目標：0.8

</td>
<td width="50%">

### 🧠 **ケースベース学習**
**セッション間のインテリジェンス：**
- パターン認識と再利用
- 時間をかけた戦略の最適化
- 成功したクエリ定式化の保存
- パフォーマンス改善の追跡

</td>
</tr>
</table>

### **調査コマンドの使用法**

```bash
# 自動深度での基本調査
/sc:research "2024年の最新AI開発"

# 制御された調査深度
/sc:research "量子コンピューティングの飛躍的進歩" --depth exhaustive

# 特定の戦略選択
/sc:research "市場分析" --strategy planning-only

# ドメインフィルタリングされた調査
/sc:research "Reactパターン" --domains "reactjs.org,github.com"
```

### **調査深度レベル**

| 深度 | ソース | ホップ | 時間 | 最適な用途 |
|:-----:|:-------:|:----:|:----:|----------|
| **Quick** | 5-10 | 1 | 約2分 | 簡単な事実、シンプルなクエリ |
| **Standard** | 10-20 | 3 | 約5分 | 一般的な調査（デフォルト） |
| **Deep** | 20-40 | 4 | 約8分 | 包括的な分析 |
| **Exhaustive** | 40+ | 5 | 約10分 | 学術レベルの調査 |

### **統合ツールオーケストレーション**

Deep Researchシステムは複数のツールをインテリジェントに調整します：
- **Tavily MCP**: 主要なWeb検索と発見
- **Playwright MCP**: 複雑なコンテンツ抽出
- **Sequential MCP**: マルチステップ推論と合成
- **Serena MCP**: メモリと学習の永続化
- **Context7 MCP**: 技術ドキュメントの検索

</div>

---

<div align="center">

## 📚 **ドキュメント**

### **SuperClaudeの完全ガイド**

<table>
<tr>
<th align="center">🚀 はじめに</th>
<th align="center">📖 ユーザーガイド</th>
<th align="center">🛠️ 開発者リソース</th>
<th align="center">📋 リファレンス</th>
</tr>
<tr>
<td valign="top">

- 📝 [**クイックスタートガイド**](Docs/Getting-Started/quick-start.md)
  *素早く開始*

- 💾 [**インストールガイド**](Docs/Getting-Started/installation.md)
  *詳細なセットアップ手順*

</td>
<td valign="top">

- 🎯 [**コマンドリファレンス**](Docs/User-Guide/commands.md)
  *全29スラッシュコマンド*

- 🤖 [**エージェントガイド**](Docs/User-Guide/agents.md)
  *23の専門エージェント*

- 🎨 [**動作モード**](Docs/User-Guide/modes.md)
  *7つの適応モード*

- 🚩 [**フラグガイド**](Docs/User-Guide/flags.md)
  *動作の制御*

- 🔧 [**MCPサーバー**](Docs/User-Guide/mcp-servers.md)
  *10ツール統合*

- 💼 [**セッション管理**](Docs/User-Guide/session-management.md)
  *状態の保存と復元*

</td>
<td valign="top">

- 🏗️ [**技術アーキテクチャ**](Docs/Developer-Guide/technical-architecture.md)
  *システム設計の詳細*

- 💻 [**コード貢献**](Docs/Developer-Guide/contributing-code.md)
  *開発ワークフロー*

- 🧪 [**テストとデバッグ**](Docs/Developer-Guide/testing-debugging.md)
  *品質保証*

</td>
<td valign="top">
- 📓 [**サンプル集**](Docs/Reference/examples-cookbook.md)
  *実際のレシピ*

- 🔍 [**トラブルシューティング**](Docs/Reference/troubleshooting.md)
  *よくある問題と修正*

</td>
</tr>
</table>

</div>

---

<div align="center">

## 🤝 **貢献**

### **SuperClaudeコミュニティに参加**

あらゆる種類の貢献を歓迎します！協力できる方法は次のとおりです：

| 優先度 | 領域 | 説明 |
|:--------:|------|-------------|
| 📝 **高** | ドキュメント | ガイドの改善、例の追加、タイポの修正 |
| 🔧 **高** | MCP統合 | サーバー設定の追加、統合のテスト |
| 🎯 **中** | ワークフロー | コマンドパターンとレシピの作成 |
| 🧪 **中** | テスト | テストの追加、機能の検証 |
| 🌐 **低** | i18n | ドキュメントを他の言語に翻訳 |

<p align="center">
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/📖_Read-Contributing_Guide-blue" alt="Contributing Guide">
  </a>
  <a href="https://github.com/SuperClaude-Org/SuperClaude_Framework/graphs/contributors">
    <img src="https://img.shields.io/badge/👥_View-All_Contributors-green" alt="Contributors">
  </a>
</p>

</div>

---

<div align="center">

## ⚖️ **ライセンス**

このプロジェクトは**MITライセンス**の下でライセンスされています - 詳細は[LICENSE](LICENSE)ファイルを参照してください。

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?" alt="MIT License">
</p>

</div>

---

<div align="center">

## ⭐ **スター履歴**

<a href="https://www.star-history.com/#SuperClaude-Org/SuperClaude_Framework&Timeline">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
 </picture>
</a>


</div>

---

<div align="center">

### **🚀 SuperClaudeコミュニティによって情熱を持って構築されました**

<p align="center">
  <sub>境界を押し広げる開発者のために❤️を込めて作られました</sub>
</p>

<p align="center">
  <a href="#-superclaude-フレームワーク">トップに戻る ↑</a>
</p>

</div>
