# SuperClaude Migration Guide

## Migrating from pip/npm to Plugin Installation

SuperClaude v4.2+ is available as a native Claude Code plugin, providing easier installation, automatic updates, and better integration with Claude Code's plugin ecosystem.

## Why Migrate?

### Benefits of Plugin Installation

| Feature | pip/npm | Plugin |
|---------|---------|--------|
| **Installation** | Multi-step process | Single command |
| **Updates** | Manual reinstall | Automatic via Claude Code |
| **Distribution** | Python/Node environment | Native to Claude Code |
| **Team Sharing** | Repository config | Marketplace sharing |
| **Compatibility** | Version conflicts | Isolated environment |

## Migration Steps

### 1. Backup Custom Content (Optional)

If you have custom commands or configurations:

```bash
# Backup your custom content
cp ~/.claude/CLAUDE.md ~/claude-backup.md
cp -r ~/.claude/commands/custom ~/commands-backup
```

### 2. Uninstall Previous Version

#### For pip installation:
```bash
pip uninstall SuperClaude
# or
pipx uninstall SuperClaude
```

#### For npm installation:
```bash
npm uninstall -g @bifrost_inc/superclaude
```

### 3. Remove Old Files

Remove SuperClaude-installed files from `.claude/` directory:

```bash
cd ~/.claude

# Remove SuperClaude framework files (but keep your custom content)
rm -rf commands/sc commands/kiro
rm -f *.md *.json  # Only if they're SuperClaude files
```

**⚠️ Important**: Keep your personal customizations:
- Custom commands outside `commands/sc/` and `commands/kiro/`
- Your additions to `CLAUDE.md`
- Claude Code settings (`settings.json`, `settings.local.json`)
- Credentials (`.credentials.json`)

### 4. Install Plugin

```shell
# In Claude Code
/plugin marketplace add SuperClaude-Org/SuperClaude_Plugin
/plugin install superclaude@SuperClaude-Org
```

### 5. Restart Claude Code

Restart Claude Code to activate the plugin.

### 6. Verify Installation

```shell
# Check available commands
/sc:help

# Test basic functionality
/sc:analyze --help
```

## What's Changed?

### Same Functionality
- ✅ All 25 `/sc:` commands work identically
- ✅ All 10 `/kiro:` spec-driven development commands
- ✅ 15 specialized agents with same capabilities
- ✅ 7 behavioral modes with same triggers
- ✅ MCP server integrations unchanged

### What's Better
- ✅ Easier installation (one command)
- ✅ Automatic updates via Claude Code
- ✅ Better isolation from system Python/Node
- ✅ Marketplace distribution for teams
- ✅ Native Claude Code integration

### What's Different
- 📁 Files now live in plugin directory (managed by Claude Code)
- 🔧 Updates via `/plugin update` instead of pip/npm
- 🌐 Distribution via marketplace instead of PyPI/npm

## Troubleshooting

### Plugin Not Loading

**Problem**: Plugin installed but commands not available

**Solution**:
1. Restart Claude Code completely
2. Check plugin status: `/plugin`
3. Verify installation: `/plugin marketplace list`
4. Check debug output: `claude --debug`

### Commands Not Found

**Problem**: `/sc:` or `/kiro:` commands not recognized

**Solution**:
1. Verify plugin is enabled: `/plugin`
2. Check installation: `/plugin install superclaude@SuperClaude-Org`
3. Restart Claude Code

### Old Files Conflict

**Problem**: Conflicts between old pip/npm files and plugin

**Solution**:
1. Completely remove old installation files
2. Clean `.claude/` directory of SuperClaude files
3. Reinstall plugin fresh

### Custom Content Lost

**Problem**: Custom commands or configs disappeared

**Solution**:
1. Restore from backup: `cp ~/claude-backup.md ~/.claude/CLAUDE.md`
2. Custom commands should be outside `commands/sc/` and `commands/kiro/`
3. Plugin commands don't overwrite custom content

## Rollback Procedure

If you need to rollback to pip/npm installation:

### 1. Uninstall Plugin
```shell
/plugin uninstall superclaude@SuperClaude-Org
```

### 2. Reinstall via pip/npm
```bash
# pip
pipx install SuperClaude && SuperClaude install

# npm
npm install -g @bifrost_inc/superclaude && superclaude install
```

## FAQ

### Q: Will my custom commands be affected?
**A**: No, custom commands outside `commands/sc/` and `commands/kiro/` are preserved.

### Q: Do I need to reconfigure MCP servers?
**A**: No, MCP server configurations remain in your Claude Code settings.

### Q: Can I use both pip/npm and plugin versions?
**A**: Not recommended. Choose one installation method to avoid conflicts.

### Q: How do I update the plugin?
**A**: Use `/plugin update superclaude@SuperClaude-Org` or enable automatic updates.

### Q: Will my project-specific `.claude/CLAUDE.md` be affected?
**A**: No, project-specific configurations are independent of the plugin.

### Q: Can I install the plugin on multiple machines?
**A**: Yes, install via marketplace on each machine independently.

## Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/SuperClaude-Org/SuperClaude_Plugin/issues)
- 💬 **Questions**: [GitHub Discussions](https://github.com/SuperClaude-Org/SuperClaude_Plugin/discussions)
- 📖 **Documentation**: [SuperClaude Docs](https://superclaude.netlify.app/)

## Next Steps

After migration:

1. ✅ Test core commands: `/sc:help`, `/sc:analyze`
2. ✅ Verify agents: Check `/agents` for SuperClaude agents
3. ✅ Test spec-driven workflow: `/kiro:spec-init "test project"`
4. ✅ Try deep research: `/sc:research "test query"`
5. ✅ Explore documentation: Visit [superclaude.netlify.app](https://superclaude.netlify.app/)

Welcome to the easier way of using SuperClaude! 🚀
