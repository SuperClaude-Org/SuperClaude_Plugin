# 🛡️ SuperClaude Plugin - Complete Backup & Safety Guide

> **Your data safety is our priority.** This guide ensures you can safely install, test, and rollback the SuperClaude plugin without any risk to your existing Claude Code configuration.

---

## 📋 Quick Start Checklist

Before installing the SuperClaude plugin, complete this checklist:

- [ ] **Read this guide** (5 minutes)
- [ ] **Run backup script** (30 seconds)
- [ ] **Verify backup** (1 minute)
- [ ] **Install plugin** (2 minutes)
- [ ] **Test configuration** (5 minutes)
- [ ] **Keep backup for 1 week**

**Total time: ~15 minutes for complete safety**

---

## 🎯 Who Needs to Backup?

### ✅ You MUST backup if you have:
- ✅ Existing MCP servers configured (Context7, Sequential, Tavily, etc.)
- ✅ Custom Claude Code settings or configurations
- ✅ API keys configured in environment variables
- ✅ Project-specific `.mcp.json` files
- ✅ Custom slash commands or agents
- ✅ Modified `.claude/CLAUDE.md` file

### 🆕 You can skip backup if:
- 🆕 Fresh Claude Code installation
- 🆕 Never configured MCP servers
- 🆕 No custom settings in `~/.claude/`

**When in doubt, backup anyway. It takes 30 seconds.**

---

## 🚀 Method 1: Automated Backup (Recommended)

We provide a safe, automated backup script.

### Step 1: Download the Backup Script

```bash
# Download backup script from repository
curl -o /tmp/backup-claude-config.sh \
  https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Plugin/main/scripts/backup-claude-config.sh

chmod +x /tmp/backup-claude-config.sh
```

### Step 2: Run the Backup

```bash
# Run with automatic timestamp
/tmp/backup-claude-config.sh

# Or specify custom backup directory
/tmp/backup-claude-config.sh ~/my-backups/
```

### What Gets Backed Up?

The script automatically backs up:
- ✅ `~/.claude/settings.local.json` → Global MCP settings
- ✅ `~/.claude/CLAUDE.md` → Your custom instructions
- ✅ `~/.claude/.credentials.json` → API credentials (if exists)
- ✅ `.mcp.json` → Project MCP config (current directory)
- ✅ `.claude/` → Project-specific config (current directory)

### Output Format

```
📦 Backup created at:
~/claude-backups/backup-2025-01-07-14-30-25/

Contents:
  ✅ settings.local.json (12 KB)
  ✅ CLAUDE.md (45 KB)
  ✅ .credentials.json (2 KB)
  ✅ .mcp.json (3 KB)

💾 Total backup size: 62 KB
🔒 Backup location: ~/claude-backups/backup-2025-01-07-14-30-25/
```

---

## 📝 Method 2: Manual Backup (Alternative)

Prefer to backup manually? Follow these steps:

### Step 1: Create Backup Directory

```bash
# Create dated backup directory
BACKUP_DIR=~/claude-backups/backup-$(date +%Y-%m-%d-%H-%M-%S)
mkdir -p "$BACKUP_DIR"
echo "📦 Backup directory: $BACKUP_DIR"
```

### Step 2: Backup Global Settings

```bash
# Backup Claude Code global settings
if [ -f ~/.claude/settings.local.json ]; then
    cp ~/.claude/settings.local.json "$BACKUP_DIR/"
    echo "✅ Backed up: settings.local.json"
fi

# Backup custom instructions
if [ -f ~/.claude/CLAUDE.md ]; then
    cp ~/.claude/CLAUDE.md "$BACKUP_DIR/"
    echo "✅ Backed up: CLAUDE.md"
fi

# Backup credentials (if exists)
if [ -f ~/.claude/.credentials.json ]; then
    cp ~/.claude/.credentials.json "$BACKUP_DIR/"
    echo "✅ Backed up: .credentials.json"
fi
```

### Step 3: Backup Project Settings

```bash
# Backup project-specific MCP config
if [ -f .mcp.json ]; then
    cp .mcp.json "$BACKUP_DIR/"
    echo "✅ Backed up: .mcp.json"
fi

# Backup project-specific Claude config
if [ -d .claude ]; then
    cp -r .claude "$BACKUP_DIR/"
    echo "✅ Backed up: .claude/"
fi
```

### Step 4: Verify Backup

```bash
# List backed up files
echo ""
echo "📂 Backup contents:"
ls -lh "$BACKUP_DIR"
```

---

## ✅ Verify Your Backup

**Critical: Always verify your backup worked!**

```bash
# Check backup exists and has files
BACKUP_DIR=~/claude-backups/backup-2025-01-07-14-30-25  # Use your actual path

# Should show your backed up files
ls -lh "$BACKUP_DIR"

# Check settings.local.json has content
if [ -f "$BACKUP_DIR/settings.local.json" ]; then
    echo "✅ settings.local.json size: $(wc -c < "$BACKUP_DIR/settings.local.json") bytes"
    echo "✅ Preview:"
    head -5 "$BACKUP_DIR/settings.local.json"
else
    echo "⚠️  No settings.local.json found in backup"
fi
```

### What to Look For:
- ✅ Files exist in backup directory
- ✅ File sizes are > 0 bytes
- ✅ settings.local.json contains your MCP configuration
- ✅ CLAUDE.md contains your custom instructions

---

## 🔄 Safe Installation Process

Now that you have a backup, follow this safe installation process:

### Step 1: Record Current State

```bash
# Document what MCP servers you currently have
claude mcp list > ~/claude-backups/mcp-before.txt

# Document installed plugins
/plugin list > ~/claude-backups/plugins-before.txt
```

### Step 2: Install SuperClaude Plugin

```bash
# Add marketplace
/plugin marketplace add SuperClaude-Org/SuperClaude_Plugin

# Install plugin
/plugin install sc@superclaude-official
```

### Step 3: Restart Claude Code

**Important**: Restart Claude Code completely before testing.

```bash
# macOS/Linux
pkill -9 claude-code
# Then relaunch Claude Code
```

### Step 4: Verify Installation

```bash
# Check plugin is loaded
/plugin list | grep sc

# Run setup wizard
/sc:setup-mcp

# Check MCP status
/sc:verify-mcp
```

---

## 🚨 If Something Goes Wrong

### Quick Rollback (1 minute)

If the plugin doesn't work or conflicts with your setup:

```bash
# 1. Uninstall the plugin
/plugin uninstall sc@superclaude-official

# 2. Restore your backup
BACKUP_DIR=~/claude-backups/backup-2025-01-07-14-30-25  # Your backup path

cp "$BACKUP_DIR/settings.local.json" ~/.claude/
cp "$BACKUP_DIR/CLAUDE.md" ~/.claude/ 2>/dev/null
cp "$BACKUP_DIR/.credentials.json" ~/.claude/ 2>/dev/null
cp "$BACKUP_DIR/.mcp.json" . 2>/dev/null

# 3. Restart Claude Code
pkill -9 claude-code
# Then relaunch
```

### Verify Rollback

```bash
# Check MCP servers are back
claude mcp list

# Should match your recorded state
diff ~/claude-backups/mcp-before.txt <(claude mcp list)
```

---

## 🔧 Common Issues & Solutions

### Issue 1: MCP Servers Not Working After Install

**Symptoms:**
- Commands fail with "MCP server not found"
- `/sc:verify-mcp` shows errors

**Solution:**
```bash
# 1. Check uvx is installed
uvx --version

# If not installed:
pip install uv

# 2. Restart Claude Code
# 3. Run setup wizard
/sc:setup-mcp
```

### Issue 2: Existing MCP Servers Disappeared

**Symptoms:**
- Your manual MCP servers (Context7, Sequential) are gone
- Only AIRIS MCP Gateway appears

**Explanation:**
This is expected! AIRIS MCP Gateway **replaces** individual servers with a unified gateway that includes all 10 tools.

**Verification:**
```bash
# Check AIRIS Gateway provides your tools
claude mcp get airis-mcp-gateway

# Should show: sequential-thinking, context7, tavily, etc.
```

### Issue 3: Conflicts with Existing Settings

**Symptoms:**
- Error messages about duplicate MCP servers
- Settings file corruption warnings

**Solution:**
```bash
# 1. Uninstall plugin
/plugin uninstall sc@superclaude-official

# 2. Restore backup
cp ~/claude-backups/backup-XXXX/settings.local.json ~/.claude/

# 3. Edit settings to remove conflicts
# Open ~/.claude/settings.local.json
# Remove or rename conflicting MCP servers

# 4. Reinstall plugin
/plugin install sc@superclaude-official
```

---

## 📖 FAQ

### Q: How long should I keep backups?

**A:** Keep backups for at least **1 week** after installing the plugin. Once you're confident everything works, you can delete old backups.

### Q: Can I use the plugin alongside my existing MCP servers?

**A:** Yes, but **not recommended**. AIRIS MCP Gateway already includes 10 tools. Having both creates:
- Duplicate tools (confusing)
- Increased token usage
- Potential conflicts

**Recommendation:** Let the plugin manage MCP via AIRIS Gateway.

### Q: What if I have custom MCP servers?

**A:** Custom MCP servers are safe! The plugin only adds AIRIS MCP Gateway. Your custom servers remain in your settings.

**Example:**
```json
{
  "mcpServers": {
    "airis-mcp-gateway": { ... },    // Added by plugin
    "my-custom-server": { ... }       // Your custom server (safe!)
  }
}
```

### Q: Can I disable AIRIS MCP Gateway?

**A:** Yes! The plugin commands work without MCP servers (with reduced functionality). To disable:

```bash
# Edit ~/.claude/settings.local.json
# Remove or comment out the airis-mcp-gateway section
```

### Q: What happens to my API keys?

**A:** API keys are **never modified** by the plugin. Your Tavily, Magic, and other API keys in environment variables remain unchanged.

---

## 📊 Before vs After Comparison

### Before Plugin Installation

```
MCP Servers (8 individual):
  ├── sequential-thinking (npm)
  ├── context7 (npm)
  ├── tavily (npm)
  ├── magic (npm)
  ├── playwright (npm)
  ├── serena (npm)
  ├── morphllm (npm)
  └── chrome-devtools (npm)

Settings: ~/.claude/settings.local.json (each server configured separately)
Token usage: ~45,000 tokens
Management: Manual npm install for each
```

### After Plugin Installation

```
MCP Server (1 unified gateway):
  └── airis-mcp-gateway (uvx)
      ├── sequential-thinking
      ├── context7
      ├── tavily
      ├── magic
      ├── playwright
      ├── serena
      ├── morphllm
      ├── chrome-devtools
      ├── git
      └── puppeteer

Settings: Managed by plugin.json
Token usage: ~5,000 tokens (89% reduction)
Management: Automatic via plugin
```

---

## ✅ Post-Installation Checklist

After installing and testing the plugin:

- [ ] Verify all MCP tools work (`/sc:verify-mcp`)
- [ ] Test key commands (`/sc:help`, `/sc:brainstorm`)
- [ ] Confirm API keys still work (if using Tavily/Magic)
- [ ] Check no error messages in Claude Code console
- [ ] Document any issues encountered
- [ ] Keep backup for 1 week
- [ ] Delete old npm MCP packages (optional)

---

## 🆘 Emergency Support

If you encounter issues not covered in this guide:

1. **Check GitHub Issues**: [SuperClaude Plugin Issues](https://github.com/SuperClaude-Org/SuperClaude_Plugin/issues)
2. **Join Discussions**: [GitHub Discussions](https://github.com/SuperClaude-Org/SuperClaude_Plugin/discussions)
3. **Report Bug**: Include:
   - Your backup location
   - Error messages
   - Output of `/sc:verify-mcp`
   - Claude Code version

**Emergency Rollback Script:**
```bash
/plugin uninstall sc@superclaude-official
cp ~/claude-backups/backup-LATEST/* ~/.claude/
pkill -9 claude-code
```

---

## 📝 Summary

**Key Takeaways:**

1. ✅ **Always backup before installing** (30 seconds)
2. ✅ **Verify your backup** (1 minute)
3. ✅ **Use `/sc:setup-mcp`** for guided setup
4. ✅ **Keep backups for 1 week**
5. ✅ **Rollback is easy** if needed (1 minute)

**You're in control.** With proper backups, you can safely test the plugin and rollback anytime.

---

**Last Updated:** 2025-01-07
**Plugin Version:** 4.3.2+
**Guide Version:** 1.0
