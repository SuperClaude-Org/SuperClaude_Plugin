# Automated Sync System Documentation

## Overview

The SuperClaude Plugin uses an automated synchronization system to pull the latest content from the SuperClaude_Framework repository and transform it for distribution as a Claude Code plugin with proper namespace isolation.

## Architecture

### Source Repository: SuperClaude_Framework
- **Location**: `https://github.com/SuperClaude-Org/SuperClaude_Framework`
- **Structure**: `src/superclaude/commands/`, `src/superclaude/agents/`, `src/superclaude/core/`, `src/superclaude/modes/`
- **Role**: Source of truth for all SuperClaude content

### Destination Repository: SuperClaude_Plugin
- **Location**: `https://github.com/SuperClaude-Org/SuperClaude_Plugin`
- **Structure**: `/commands/`, `/agents/`, `/core/`, `/modes/`
- **Role**: Distribution channel for Claude Code plugin

## Namespace Isolation

To prevent conflicts with Claude Code built-in commands and other plugins (e.g., Conductor), we implement comprehensive namespace isolation:

### Commands
- **Filename**: `brainstorm.md` (no prefix — original filename preserved)
- **Header**: `# /sc:brainstorm` (WITH `sc:` prefix)
- **Invocation**: `/sc:brainstorm` (user types this in Claude Code)
- **plugin.json mapping**: `"sc:brainstorm": "commands/brainstorm.md"`

### Agents
- **Filename**: `backend-architect.md` (no prefix — original filename preserved)
- **Name**: `sc-backend-architect` (in frontmatter `name:` field)
- **Reference**: Agents are referenced by name in command persona lists

### Core & Modes
- **No transformation**: Copied as-is from Framework
- **Files**: PRINCIPLES.md, RULES.md, FLAGS.md, behavioral mode definitions

## Sync Workflow

### Automatic Sync (Every 6 Hours)

GitHub Actions runs `.github/workflows/pull-sync-framework.yml` every 6 hours. It first checks if the Framework has new commits using `git ls-remote`, and skips the sync if no changes are detected:

1. **Check for Updates**: Compare Framework HEAD with stored commit hash (fast, no clone)
2. **Clone Framework**: Download latest Framework content to temp directory (only if updates detected)
3. **Transform Commands**: Apply `sc:` prefix to headers, update cross-references
4. **Transform Agents**: Apply `sc-` prefix to frontmatter names
4. **Copy Core Files**: Sync core/ and modes/ directories without transformation
5. **Generate plugin.json**: Create `.claude-plugin/plugin.json` with command mappings
6. **Merge MCP Configs**: Safely merge MCP server configurations
7. **Validate**: Check all transformations completed successfully
8. **Commit & Push**: Auto-commit changes if any detected

### Manual Sync

#### Via GitHub Actions UI

1. Go to **Actions** tab in repository
2. Select **"Sync from SuperClaude Framework"** workflow
3. Click **"Run workflow"**
4. Optional: Enable "Dry run mode" to preview changes

#### Via Local Script

```bash
# Standard sync
python scripts/sync_from_framework.py \
  --framework-repo "https://github.com/SuperClaude-Org/SuperClaude_Framework" \
  --plugin-root "." \
  --output-report sync-report.json

# Dry run (preview only)
python scripts/sync_from_framework.py \
  --framework-repo "https://github.com/SuperClaude-Org/SuperClaude_Framework" \
  --plugin-root "." \
  --dry-run true \
  --verbose

# Custom Framework branch
python scripts/sync_from_framework.py \
  --framework-repo "https://github.com/SuperClaude-Org/SuperClaude_Framework@develop" \
  --plugin-root "."
```

### Dry Run Mode

Preview changes without applying them:

```bash
python scripts/sync_from_framework.py --dry-run true
```

Dry run mode will:
- ✅ Clone Framework
- ✅ Process transformations
- ✅ Generate sync report
- ❌ NOT write files
- ❌ NOT modify git history
- ❌ NOT commit changes

## Transformation Logic

### Command Transformation

**Input** (`Framework: src/superclaude/commands/brainstorm.md`):
```markdown
---
description: Interactive requirements discovery
---

# /brainstorm - Brainstorming

Use /analyze for analysis and [/task] for task management.
```

**Output** (`Plugin: commands/brainstorm.md`):
```markdown
---
description: Interactive requirements discovery
---

# /sc:brainstorm - Brainstorming

Use /sc:analyze for analysis and [/sc:task] for task management.
```

**Changes**:
1. ✅ Header: `# /brainstorm` → `# /sc:brainstorm`
2. ✅ Cross-references: `/analyze` → `/sc:analyze`
3. ✅ Link references: `[/task]` → `[/sc:task]`
4. ⏭️ Filename: Preserved as `brainstorm.md` (no rename)

### Agent Transformation

**Input** (`Framework: src/superclaude/agents/backend-architect.md`):
```markdown
---
name: backend-architect
description: Backend expert
category: engineering
---

# Backend Architect
```

**Output** (`Plugin: agents/backend-architect.md`):
```markdown
---
name: sc-backend-architect
description: Backend expert
category: engineering
---

# Backend Architect
```

**Changes**:
1. ✅ Name field: `name: backend-architect` → `name: sc-backend-architect`
2. ⏭️ Filename: Preserved as `backend-architect.md` (no rename)
3. ⏭️ Content: No changes to markdown body

## MCP Configuration Safety

### Merge Strategy

The sync system safely merges MCP server configurations:

1. **Framework servers take precedence**: Latest Framework MCP configs override Plugin versions
2. **Preserve Plugin-specific servers**: Servers only in Plugin (e.g., `airis-mcp-gateway`) are kept
3. **Conflict detection**: Warnings logged for differing configurations
4. **Automatic backup**: `plugin.json` backed up to `backups/` before merge

### Example Merge Scenario

**Framework** (`plugin.json`):
```json
{
  "mcpServers": {
    "sequential": {
      "command": "uvx",
      "args": ["--from", "git+https://...", "sequential-thinking"]
    },
    "context7": {
      "command": "uvx",
      "args": ["context7-mcp"]
    }
  }
}
```

**Plugin** (`plugin.json`):
```json
{
  "mcpServers": {
    "sequential": {
      "command": "npx",
      "args": ["sequential"]
    },
    "airis-mcp-gateway": {
      "command": "uvx",
      "args": ["airis-mcp-gateway"]
    }
  }
}
```

**Merged Result**:
```json
{
  "mcpServers": {
    "sequential": {
      "command": "uvx",
      "args": ["--from", "git+https://...", "sequential-thinking"]
    },
    "context7": {
      "command": "uvx",
      "args": ["context7-mcp"]
    },
    "airis-mcp-gateway": {
      "command": "uvx",
      "args": ["airis-mcp-gateway"]
    }
  }
}
```

**Warnings**:
- ⚠️ MCP server 'sequential' conflict - using Framework version
- ℹ️ Preserved plugin-specific MCP server: airis-mcp-gateway

### Manual Rollback

If sync causes MCP configuration issues:

```bash
# 1. List backups
ls -la backups/

# 2. Identify backup file (format: plugin.json.YYYYMMDD_HHMMSS.backup)
# Example: plugin.json.20260211_160000.backup

# 3. Restore backup
cp backups/plugin.json.20260211_160000.backup plugin.json

# 4. Commit restoration
git add plugin.json
git commit -m "Restore plugin.json from backup (pre-sync 2026-02-11 16:00)"
git push
```

## Validation

After each sync, the system validates:

1. ✅ **Command headers**: All have `# /sc:` prefix
2. ✅ **Agent names**: All have `sc-` prefix in frontmatter
5. ✅ **plugin.json**: Valid JSON with correct command mappings
6. ✅ **MCP configurations**: Valid JSON structure

If validation fails, sync is automatically rolled back to previous state.

## Monitoring

### Sync Reports

Each sync generates a detailed report (`sync-report.json`):

```json
{
  "success": true,
  "timestamp": "2026-02-11T16:00:00.000Z",
  "framework_commit": "abc123def456...",
  "framework_version": "4.5.0",
  "files_synced": 54,
  "files_modified": 29,
  "commands_transformed": 29,
  "agents_transformed": 25,
  "mcp_servers_merged": 8,
  "warnings": [
    "MCP server 'sequential' conflict - using Framework version"
  ],
  "errors": []
}
```

### GitHub Actions Artifacts

Sync reports are uploaded as artifacts in GitHub Actions:
- **Retention**: 30 days
- **Location**: Actions → Workflow Run → Artifacts
- **Filename**: `sync-report-{run_number}.json`

### Job Summary

Each workflow run generates a summary visible in the Actions UI:

```markdown
## Sync Results

- **Success**: true
- **Framework Version**: 4.5.0
- **Files Synced**: 54
- **Commands Transformed**: 29
- **Agents Transformed**: 25

### ⚠️ Warnings
- MCP server 'sequential' conflict - using Framework version
```

## Troubleshooting

### Sync Fails with "Git Clone Failed"

**Symptom**: Sync fails at Framework clone step

**Causes**:
- Network connectivity issues
- GitHub service disruption
- Invalid repository URL
- Rate limiting

**Solutions**:
1. Check Framework repository is accessible: `https://github.com/SuperClaude-Org/SuperClaude_Framework`
2. Verify network connectivity
3. Check GitHub Status: `https://www.githubstatus.com/`
4. Wait and retry (6-hour cron will retry automatically)

### Sync Fails with "Validation Error"

**Symptom**: Sync completes but validation fails

**Causes**:
- Framework content format changed
- Transformation logic bug
- Missing required files in Framework

**Solutions**:
1. Review sync report for specific validation errors
2. Check Framework repository for recent breaking changes
3. Report issue: `https://github.com/SuperClaude-Org/SuperClaude_Plugin/issues`
4. Sync is automatically rolled back - no manual intervention needed

### MCP Configuration Issues

**Symptom**: MCP servers not working after sync

**Causes**:
- MCP configuration merge conflict
- Invalid MCP server configuration in Framework

**Solutions**:
1. Review MCP merge warnings in sync report
2. Manually inspect `plugin.json` mcpServers section
3. Restore from backup (see "Manual Rollback" section)
4. Test MCP servers: `claude code --verify-mcp`

### Commands Not Appearing in Claude Code

**Symptom**: `/sc:` commands not recognized after sync

**Causes**:
- Plugin not reloaded
- plugin.json mapping incorrect
- Command file format invalid

**Solutions**:
1. Restart Claude Code to reload plugin
2. Check `.claude-plugin/plugin.json` has correct mappings
3. Verify command files exist in `commands/` directory
4. Check command files have valid frontmatter

## Migration from Old System

### What Changed

**Old System** (`clean_command_names.py`):
- Manual cleanup of `name:` attributes via separate script
- Triggered on command file changes
- No Framework synchronization

**New System** (`sync_from_framework.py`):
- Automatic sync from Framework repository
- Namespace transformation with `sc:` prefix
- Name cleanup built-in to sync process
- Automated execution every 6 hours (with change detection)

### Migration Timeline

- **v4.4.0**: New sync system introduced, old system deprecated
- **v5.0.0**: Old system removed entirely

### Deprecation Status

✅ **Deprecated**:
- `scripts/clean_command_names.py` - Use `sync_from_framework.py` instead
- `.github/workflows/cleanup-commands.yml` - Use `pull-sync-framework.yml` instead

⚠️ **Disabled**:
- Automatic triggers for cleanup workflow disabled
- Manual execution still available for emergency use

### No Action Required

Plugin maintainers and users don't need to do anything. The new system:
- ✅ Runs automatically (every 6 hours, skips if no Framework changes)
- ✅ Handles all transformations
- ✅ Includes old cleanup functionality
- ✅ Generates detailed reports
- ✅ Includes validation and rollback

## Advanced Usage

### Custom Framework Branch

Sync from a specific Framework branch:

```bash
# Sync from develop branch
python scripts/sync_from_framework.py \
  --framework-repo "https://github.com/SuperClaude-Org/SuperClaude_Framework@develop" \
  --plugin-root "."

# Sync from specific commit
python scripts/sync_from_framework.py \
  --framework-repo "https://github.com/SuperClaude-Org/SuperClaude_Framework@abc123" \
  --plugin-root "."
```

### Testing Transformations

Test transformations on specific files without full sync:

```python
from scripts.sync_from_framework import ContentTransformer

# Test command transformation
with open('test_command.md', 'r') as f:
    content = f.read()

transformed = ContentTransformer.transform_command(content, 'test.md')
print(transformed)

# Test agent transformation
with open('test_agent.md', 'r') as f:
    content = f.read()

transformed = ContentTransformer.transform_agent(content, 'test-agent.md')
print(transformed)
```

### Debugging Sync Issues

Enable verbose logging:

```bash
python scripts/sync_from_framework.py --verbose
```

This outputs:
- Detailed transformation steps
- File-by-file processing logs
- Git operations
- Validation checks

## Security Considerations

### Git History Preservation

The sync system preserves file history by updating content in-place rather than renaming files. Filenames are kept as-is from the Framework (e.g., `brainstorm.md`), while namespace isolation is applied through header prefixes (`# /sc:brainstorm`) and agent name fields (`name: sc-backend-architect`).

### Backup Before Sync

Every sync creates automatic backups:

```
backups/
├── plugin.json.20260211_160000.backup
├── plugin.json.20260211_170000.backup
└── plugin.json.20260211_180000.backup
```

Backups are retained for manual rollback if needed.

### Validation Gates

Multiple validation gates prevent invalid syncs:

1. **Pre-sync**: Validate Framework repository structure
2. **Transform**: Validate transformation logic output
3. **Post-sync**: Validate Plugin repository structure
4. **MCP**: Validate JSON structure of merged configs

If any gate fails, sync is automatically rolled back.

## Performance

### Sync Duration

Typical sync completes in **2-4 minutes**:

1. **Clone Framework**: ~30-60 seconds
2. **Transform Content**: ~30-60 seconds
3. **Generate plugin.json**: ~5-10 seconds
4. **Merge MCP**: ~5-10 seconds
5. **Validate**: ~10-20 seconds
6. **Commit & Push**: ~30-60 seconds

### Resource Usage

- **Disk**: ~100MB temporary storage (Framework clone)
- **Memory**: ~50MB Python process
- **Network**: ~20MB download (Framework repository)

### Optimization

The sync system is optimized for:
- ✅ Minimal API calls (single clone)
- ✅ Efficient file operations (batch processing)
- ✅ Fast validation (regex patterns)
- ✅ Automatic cleanup (temp directory removal)

## Support

### Reporting Issues

Found a bug or issue with the sync system?

1. **Check sync report**: Review `sync-report.json` for errors
2. **Review logs**: Check GitHub Actions workflow logs
3. **Search issues**: https://github.com/SuperClaude-Org/SuperClaude_Plugin/issues
4. **Report new issue**: Include sync report and relevant logs

### Getting Help

- 📖 **Documentation**: https://superclaude.netlify.app/
- 💬 **Discussions**: https://github.com/SuperClaude-Org/SuperClaude_Plugin/discussions
- 🐛 **Issues**: https://github.com/SuperClaude-Org/SuperClaude_Plugin/issues

## Appendix

### File Structure Reference

```
SuperClaude_Plugin/
├── commands/
│   ├── brainstorm.md
│   ├── analyze.md
│   └── ... (29 commands)
├── agents/
│   ├── backend-architect.md
│   ├── system-architect.md
│   └── ... (23 agents)
├── core/
│   ├── PRINCIPLES.md
│   ├── RULES.md
│   └── ...
├── modes/
│   ├── MODE_Brainstorming.md
│   └── ...
├── .claude-plugin/
│   └── plugin.json (generated)
├── plugin.json (merged MCP configs)
├── scripts/
│   ├── sync_from_framework.py
│   └── clean_command_names.py (deprecated)
├── .github/workflows/
│   ├── pull-sync-framework.yml
│   └── cleanup-commands.yml (deprecated)
├── tests/
│   └── test_sync.py
├── docs/
│   └── SYNC_SYSTEM.md (this file)
└── backups/
    └── plugin.json.*.backup
```

### Related Documentation

- [README.md](../README.md) - Plugin overview and installation
- [CLAUDE.md](../CLAUDE.md) - Quick start guide
- [MIGRATION_GUIDE.md](../MIGRATION_GUIDE.md) - Migration from pip/npm
- [BACKUP_GUIDE.md](../BACKUP_GUIDE.md) - Configuration backup system
