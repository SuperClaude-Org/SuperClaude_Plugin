# SuperClaude Plugin

This plugin provides the complete SuperClaude framework as a native Claude Code plugin.

> ⚠️ **Generated Artefact**  
> Do not edit this repository directly. Source-of-truth lives in `SuperClaude_Framework/plugins/superclaude`.  
> Regenerate via `make build-plugin && make sync-plugin-repo` from the framework repo.

## Components Included

### Commands (3 total)
- **3 /sc: commands**: Orchestration, repository indexing, deep research

### Agents (3 total)
- **Deep Research**, **Repo Index**, **Self Review**

### Behavioral Modes (7 modes)
- Brainstorming, Business Panel, Deep Research, Orchestration
- Token Efficiency, Task Management, Introspection

### Core Framework
- **PRINCIPLES.md**: Software engineering philosophy
- **RULES.md**: Behavioral rules and decision trees
- **FLAGS.md**: Mode activation and control flags
- **BUSINESS_PANEL_EXAMPLES.md**: Strategic analysis examples
- **BUSINESS_SYMBOLS.md**: Symbol communication system

## Installation

This plugin is designed to replace the pip/npm installation method with native Claude Code plugin distribution.

### Prerequisites
- Claude Code installed and running

### Install from Marketplace

```shell
/plugin marketplace add SuperClaude-Org/SuperClaude_Plugin
/plugin install superclaude@SuperClaude-Org
```

## Quick Start

After installation, restart Claude Code and try:

```shell
# See all available commands
/sc:help

# Start a new project
/sc:brainstorm "your project idea"

# Analyze codebase
/sc:analyze

# Deep research
/sc:research "your topic"
```

## Documentation

For complete documentation, visit [SuperClaude Documentation](https://superclaude.netlify.app/)

## Migration from pip/npm

If you previously installed SuperClaude via pip or npm, you can safely uninstall those versions:

```bash
# Uninstall pip version
pip uninstall SuperClaude

# Uninstall npm version
npm uninstall -g @bifrost_inc/superclaude
```

The plugin version provides the same functionality with easier installation and updates.

## Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/SuperClaude-Org/SuperClaude_Plugin/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/SuperClaude-Org/SuperClaude_Plugin/discussions)
- 📖 **Documentation**: [SuperClaude Docs](https://superclaude.netlify.app/)

## License

MIT License - see LICENSE file for details
