# SuperClaude Migration Compatibility Guide

## インストーラー版とプラグイン版の共存

### 🔍 潜在的な問題

既存のインストーラー版SuperClaudeがインストールされている環境にプラグイン版をインストールした場合、以下の問題が発生する可能性があります:

#### 1. コマンド名の重複 (HIGH RISK)

**問題**:
- インストーラー版: `~/.claude/commands/sc/*.md` にコマンドが配置
- プラグイン版: Claude Code プラグインシステムで `/sc:*` コマンドを提供

**結果**: 同じ `/sc:analyze` などのコマンドが2つ存在し、どちらが実行されるか不明確

**影響度**: 🔴 高 - ユーザー混乱の原因

#### 2. CLAUDE.md への注入の重複 (MEDIUM RISK)

**問題**:
- インストーラー版: `~/.claude/CLAUDE.md` に SuperClaude コンポーネントへの参照を注入
- プラグイン版: プラグインシステム経由で同じ内容を提供

**結果**: 同じ動作定義が二重に読み込まれ、トークン使用量が増加

**影響度**: 🟡 中 - パフォーマンス低下

#### 3. エージェントの重複 (LOW RISK)

**問題**:
- インストーラー版: エージェントファイルが存在（ただし直接使用されない）
- プラグイン版: プラグインシステム経由でエージェント提供

**結果**: 同じエージェントが2回表示される可能性

**影響度**: 🟢 低 - 機能的には問題なし

---

## 推奨される移行パス

### Option A: クリーン移行 (推奨)

既存のインストーラー版をアンインストールしてからプラグイン版をインストール

**手順**:
```bash
# Step 1: インストーラー版をアンインストール
SuperClaude uninstall

# または
pipx uninstall SuperClaude
# または
npm uninstall -g @bifrost_inc/superclaude

# Step 2: ~/.claude/ の SuperClaude 関連ファイルを確認
ls ~/.claude/commands/sc/        # コマンドが削除されていることを確認
cat ~/.claude/CLAUDE.md          # SuperClaude の @参照が削除されていることを確認

# Step 3: プラグイン版をインストール
/plugin marketplace add Utakata/SuperClaude_Plugin
/plugin install superclaude-core@superclaude-official
/plugin install superclaude-agents@superclaude-official

# Step 4: Claude Code を再起動
```

**メリット**:
- ✅ 競合が発生しない
- ✅ 動作が明確
- ✅ トークン使用量が最適

**デメリット**:
- ❌ 既存環境のバックアップが必要
- ❌ 一時的に SuperClaude が使えなくなる

---

### Option B: 並行テスト (非推奨だが可能)

両方をインストールして動作を確認

**前提条件**:
- プラグイン版のコマンド名を変更する必要がある
- 例: `/sc:*` → `/scp:*` (plugin版の意味)

**問題点**:
- インストーラー版とプラグイン版でコマンド名が異なるため、混乱を招く
- 一時的なテスト目的以外では推奨されない

---

### Option C: 段階的移行 (現実的)

まずプラグイン版をテストし、問題がなければインストーラー版を削除

**手順**:
```bash
# Phase 1: 現在の環境をバックアップ
SuperClaude backup

# Phase 2: プラグイン版を別のテスト環境でテスト
# (別のClaude Codeインスタンスまたは別のユーザープロファイル)

# Phase 3: 動作確認後、本番環境で移行
SuperClaude uninstall
/plugin install superclaude-core@superclaude-official
```

---

## 互換性チェックリスト

### インストーラー版がインストールされているか確認

```bash
# Python パッケージ確認
pip list | grep SuperClaude
pipx list | grep SuperClaude

# npm パッケージ確認
npm list -g | grep superclaude

# インストールディレクトリ確認
ls ~/.claude/commands/sc/
ls ~/.claude/core/
ls ~/.claude/modes/

# CLAUDE.md の SuperClaude 参照確認
grep -i "superclaude" ~/.claude/CLAUDE.md
```

### プラグイン版との競合を確認

```bash
# インストール後、コマンドリストを確認
/help | grep "/sc:"

# 重複がある場合、以下のような出力になる:
# /sc:analyze - [インストーラー版の説明]
# /sc:analyze - [プラグイン版の説明]
```

---

## 自動検出スクリプト (提案)

プラグインインストール時に既存のインストーラー版を検出し、警告を表示する機能を追加すべきです。

**plugins/superclaude-core/README.md に追加する警告**:

```markdown
## ⚠️ 既存インストールについて

### SuperClaudeが既にインストールされている場合

既存のインストーラー版（`pip install SuperClaude` または `npm install @bifrost_inc/superclaude`）がインストールされている場合、
プラグイン版と競合する可能性があります。

**確認方法**:
\`\`\`bash
# インストーラー版が存在するか確認
ls ~/.claude/commands/sc/
\`\`\`

**推奨アクション**:
\`\`\`bash
# インストーラー版をアンインストール
SuperClaude uninstall
# または
pipx uninstall SuperClaude
# または
npm uninstall -g @bifrost_inc/superclaude
\`\`\`

その後、プラグイン版をインストールしてください。
```

---

## 今後の対応 (Phase 4で実施)

### 1. README に警告を追加

**ファイル**: `plugins/superclaude-core/README.md`

以下のセクションを追加:
- "既存インストールについて" (警告)
- "移行手順" (ステップバイステップ)
- "トラブルシューティング" (競合時の対処法)

### 2. インストールスクリプトの改善 (将来)

プラグインに `hooks.json` で `PostInstall` フックを追加し、既存のインストーラー版を検出:

```json
{
  "hooks": {
    "PostInstall": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "[ -d ~/.claude/commands/sc ] && echo '⚠️  Warning: Existing SuperClaude installer detected. Consider running: SuperClaude uninstall' || true"
          }
        ]
      }
    ]
  }
}
```

### 3. マイグレーションガイドの作成

**新規ファイル**: `docs/MIGRATION_GUIDE.md`

内容:
- インストーラー版からプラグイン版への移行手順
- バックアップとロールバック方法
- よくある質問と回答

---

## まとめ

### 現状

✅ プラグイン版は正常にインストール・動作している
⚠️ インストーラー版との共存については**明示的なテストが未実施**

### 推奨アクション

1. **ユーザーに確認**: 既存のインストーラー版がインストールされているか
   ```bash
   ls ~/.claude/commands/sc/
   ```

2. **クリーン移行を推奨**: アンインストール → プラグインインストール

3. **ドキュメント作成**: 移行ガイドと警告を README に追加

### 次のステップ

Phase 4 で以下を実施:
- [ ] `plugins/superclaude-core/README.md` に警告セクション追加
- [ ] `MIGRATION_GUIDE.md` 作成
- [ ] インストーラー版との競合テスト実施
- [ ] トラブルシューティングガイド作成
