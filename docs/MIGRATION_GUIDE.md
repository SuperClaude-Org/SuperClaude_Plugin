# SuperClaude Migration Guide
## From Installer (pip/npm) to Plugin System

This guide helps you migrate from the installer-based SuperClaude to the new plugin system.

---

## Quick Migration (5 minutes)

### Step 1: Check Current Installation

```bash
# Check if installer version is present
ls ~/.claude/commands/sc/

# Check Python package
pip list | grep SuperClaude
# OR
pipx list | grep SuperClaude

# Check npm package
npm list -g | grep superclaude
```

### Step 2: Backup (Optional but Recommended)

```bash
# If using installer version
SuperClaude backup

# Manual backup
cp -r ~/.claude ~/.claude_backup_$(date +%Y%m%d)
```

### Step 3: Uninstall Old Version

```bash
# Python version
SuperClaude uninstall
# OR
pipx uninstall SuperClaude

# npm version
npm uninstall -g @bifrost_inc/superclaude
```

### Step 4: Verify Clean Uninstall

```bash
# These should return "No such file or directory"
ls ~/.claude/commands/sc/
ls ~/.claude/core/
ls ~/.claude/modes/

# Check CLAUDE.md has no SuperClaude references
grep -i "superclaude" ~/.claude/CLAUDE.md
# Should return no results or only user-added custom content
```

### Step 5: Install Plugin Version

```bash
# Open Claude Code
/plugin marketplace add Utakata/SuperClaude_Plugin

# Install desired plugins
/plugin install superclaude-core@superclaude-official
/plugin install superclaude-agents@superclaude-official
/plugin install superclaude-mcp-docs@superclaude-official

# Restart Claude Code
```

### Step 6: Verify Installation

```bash
# Check commands are available
/help | grep "/sc:"

# Test a command
/sc:help

# Check agents (if installed)
/agents | grep -i "SuperClaude\|architect\|quality"
```

---

## Comparison: Installer vs Plugin

| Feature | Installer (pip/npm) | Plugin System |
|---------|---------------------|---------------|
| **Installation** | `pipx install SuperClaude && SuperClaude install` | `/plugin install superclaude-core` |
| **Time to Install** | ~30-60 seconds | ~5-10 seconds |
| **Updates** | Manual (`SuperClaude update`) | Automatic via Claude Code |
| **Modularity** | All-or-nothing | Install only what you need |
| **Team Setup** | Manual installation per member | Auto-install via `.claude/settings.json` |
| **Uninstall** | `SuperClaude uninstall` | `/plugin uninstall superclaude-core` |
| **File Location** | `~/.claude/` | Managed by Claude Code |
| **Conflicts** | May conflict with plugins | None (native integration) |

---

## What if Both Are Installed?

### Symptoms

If both installer and plugin versions are installed, you may experience:

- ❌ `/sc:*` commands appear twice in `/help`
- ❌ Unclear which version is executing
- ❌ Increased token usage (duplicate content in CLAUDE.md)
- ❌ Inconsistent behavior

### Quick Fix

```bash
# Uninstall installer version
SuperClaude uninstall

# Verify plugin version works
/sc:help
```

---

## Rollback Plan

If you need to revert to the installer version:

```bash
# Step 1: Uninstall plugins
/plugin uninstall superclaude-core@superclaude-official
/plugin uninstall superclaude-agents@superclaude-official
/plugin uninstall superclaude-mcp-docs@superclaude-official

# Step 2: Reinstall via installer
pipx install SuperClaude==4.2.0
SuperClaude install

# OR
npm install -g @bifrost_inc/superclaude@4.2.0
SuperClaude install

# Step 3: Restore backup if needed
cp -r ~/.claude_backup_YYYYMMDD/* ~/.claude/
```

---

## Team Migration

### For Project Leads

Add to project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "superclaude-official": {
      "source": {
        "source": "github",
        "repo": "Utakata/SuperClaude_Plugin"
      }
    }
  },
  "enabledPlugins": [
    "superclaude-core@superclaude-official",
    "superclaude-agents@superclaude-official"
  ]
}
```

### For Team Members

1. **Clone project** with `.claude/settings.json`
2. **Open in Claude Code**
3. **Trust repository** when prompted
4. **Plugins auto-install** on first use
5. **Restart Claude Code**

---

## Troubleshooting

### Problem: Commands not showing after plugin install

**Solution**:
```bash
# Restart Claude Code completely
# Then verify
/help | grep "/sc:"
```

### Problem: "Command not found: /sc:analyze"

**Cause**: Plugin not installed or not activated

**Solution**:
```bash
# Check plugin status
/plugin list

# Reinstall if needed
/plugin install superclaude-core@superclaude-official
```

### Problem: Old installer version still active

**Cause**: Incomplete uninstall

**Solution**:
```bash
# Manually remove files
rm -rf ~/.claude/commands/sc/
rm -rf ~/.claude/core/
rm -rf ~/.claude/modes/

# Remove SuperClaude references from CLAUDE.md
# Edit ~/.claude/CLAUDE.md and remove lines like:
# @commands/sc/*.md
# @core/*.md
# @modes/*.md
```

### Problem: Both versions appear in /help

**Cause**: Both installer and plugin are active

**Solution**:
```bash
# Completely uninstall installer version
SuperClaude uninstall

# Verify only plugin version remains
/help | grep "/sc:" | wc -l
# Should show ~25 lines (not 50)
```

---

## FAQ

### Q: Will my custom configurations be lost?

**A**: Plugin version uses the same `/sc:*` command names and behaviors. However:
- Custom MCP configurations in `~/.claude/.claude.json` are preserved
- Custom slash commands in `~/.claude/commands/` are preserved
- User-added content in `~/.claude/CLAUDE.md` should be backed up before migration

### Q: Can I use both installer and plugin versions?

**A**: Not recommended. They will conflict. Choose one method.

### Q: How do I know which version I'm using?

**A**:
```bash
# Check for installer files
ls ~/.claude/commands/sc/
# If exists: installer version

# Check for plugins
/plugin list | grep superclaude
# If shows: plugin version
```

### Q: What happens to my existing workflows?

**A**: No changes. All `/sc:*` commands work identically. Your workflows, scripts, and documentation remain valid.

### Q: Do I need to update my team's documentation?

**A**: Update installation instructions only:
- **Old**: "Run `pipx install SuperClaude && SuperClaude install`"
- **New**: "Add marketplace and install plugins via `/plugin install`"

Command usage documentation stays the same.

---

## Support

If you encounter issues during migration:

1. **Check GitHub Issues**: https://github.com/Utakata/SuperClaude_Plugin/issues
2. **Report New Issues**: Provide migration context and error messages
3. **Community Help**: Ask in discussions or contact maintainers

---

## Version History

- **v4.3.0**: Plugin system introduced, installer maintained
- **v4.2.0**: Last installer-only version
- **Future**: Both methods supported indefinitely

---

**Last Updated**: 2025-10-19
**Plugin Version**: v4.3.0
