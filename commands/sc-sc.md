---
name: sc
description: SuperClaude command dispatcher - Use /sc:sc [command] to access all SuperClaude features
---

# SuperClaude Command Dispatcher

🚀 **SuperClaude Framework** - Main command dispatcher

## Usage

All SuperClaude commands use the `/sc:sc:` prefix:

```
/sc:sc:command [args...]
```

## Available Commands

### Research & Analysis
```
/sc:sc:research [query]         - Deep web research with parallel search
```

### Repository Management
```
/sc:sc:index-repo              - Index repository for context optimization
```

### AI Agents
```
/sc:sc:agent [type]            - Launch specialized AI agents
```

### Recommendations
```
/sc:sc:recommend [context]     - Get command recommendations
```

### Help
```
/sc:sc                         - Show this help (all available commands)
```

## Command Namespace

All commands are namespaced under `sc:` to keep them organized:
- ✅ `/sc:sc:research query`
- ✅ `/sc:sc:index-repo`
- ✅ `/sc:sc:agent type`
- ✅ `/sc:sc:recommend`
- ✅ `/sc:sc` (help)

## Examples

### Research
```
/sc:sc:research React 18 new features
/sc:sc:research LLM agent architectures 2024
/sc:sc:research Python async best practices
```

### Index Repository
```
/sc:sc:index-repo
```

### Agent
```
/sc:sc:agent deep-research
/sc:sc:agent self-review
/sc:sc:agent repo-index
```

### Recommendations
```
/sc:sc:recommend
```

## Quick Reference

| Command | Description | Example |
|---------|-------------|---------|
| `/sc:sc:research` | Deep web research | `/sc:sc:research topic` |
| `/sc:sc:index-repo` | Repository indexing | `/sc:sc:index-repo` |
| `/sc:sc:agent` | Specialized AI agents | `/sc:sc:agent type` |
| `/sc:sc:recommend` | Command suggestions | `/sc:sc:recommend` |
| `/sc:sc` | Show help | `/sc:sc` |

## Features

- **Parallel Execution**: Research runs multiple searches in parallel
- **Evidence-Based**: All findings backed by sources
- **Context-Aware**: Uses repository context when available
- **Token Efficient**: Optimized for minimal token usage

## Help

For help on specific commands:
```
/sc:sc:research --help
/sc:sc:agent --help
```

Or use the main help command:
```
/sc:sc
```

Check the documentation:
- PLANNING.md - Architecture and design
- TASK.md - Current tasks and priorities
- KNOWLEDGE.md - Tips and best practices

## Version

SuperClaude v4.1.7
- Python package: 0.4.0
- Pytest plugin included
- PM Agent patterns enabled

---

💡 **Tip**: All commands use the `/sc:sc:` prefix - e.g., `/sc:sc:research`, `/sc:sc:agent`

🔧 **Installation**: Run `superclaude install` to install/update commands

📚 **Documentation**: https://github.com/SuperClaude-Org/SuperClaude_Framework

⚠️ **Important**: Restart Claude Code after installing commands to use them!
