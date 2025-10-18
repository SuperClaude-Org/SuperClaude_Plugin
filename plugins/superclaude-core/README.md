# SuperClaude Core Plugin

Core SuperClaude framework with 25 slash commands and 7 behavioral modes for systematic software development.

## What's Included

### 25 Slash Commands (`/sc:*`)
- **Analysis**: `/sc:analyze` - Multi-domain code analysis
- **Implementation**: `/sc:implement` - Feature implementation with MCP integration
- **Design**: `/sc:design` - System architecture and API design
- **Quality**: `/sc:improve`, `/sc:test`, `/sc:cleanup` - Code quality tools
- **Workflow**: `/sc:brainstorm`, `/sc:workflow`, `/sc:task`, `/sc:spawn` - Development workflows
- **Documentation**: `/sc:document`, `/sc:index`, `/sc:explain` - Documentation generation
- **Troubleshooting**: `/sc:troubleshoot` - Problem diagnosis and resolution
- **Strategy**: `/sc:business-panel`, `/sc:spec-panel` - Strategic analysis
- **Research**: `/sc:research` - Autonomous web research
- **Utilities**: `/sc:git`, `/sc:build`, `/sc:estimate`, `/sc:help` - Development utilities
- **Session Management**: `/sc:save`, `/sc:load`, `/sc:reflect` - Session persistence
- **Tool Selection**: `/sc:select-tool` - Intelligent MCP tool selection

### 7 Behavioral Modes
- **Orchestration Mode** (`--orchestrate`): Intelligent tool coordination
- **Task Management Mode** (`--task-manage`): Systematic organization with persistent memory
- **Token Efficiency Mode** (`--uc`, `--ultracompressed`): Symbol-enhanced communication (30-50% reduction)
- **Brainstorming Mode** (`--brainstorm`): Collaborative discovery for vague requirements
- **Business Panel Mode** (`--business-panel`): Multi-expert strategic analysis
- **Deep Research Mode**: Autonomous web research with multi-hop reasoning
- **Introspection Mode** (`--introspect`): Meta-cognitive analysis

### Core Behaviors
- **FLAGS.md**: Behavioral activation flags and mode triggers
- **PRINCIPLES.md**: Software engineering principles (SOLID, DRY, YAGNI)
- **RULES.md**: Actionable behavioral rules and decision trees
- **BUSINESS_SYMBOLS.md**: Business analysis symbol system
- **BUSINESS_PANEL_EXAMPLES.md**: Business strategy analysis examples
- **RESEARCH_CONFIG.md**: Deep research configuration

## Installation

### Via Claude Code Plugin System

```bash
# Add SuperClaude marketplace
/plugin marketplace add Utakata/SuperClaude_Plugin

# Install core plugin
/plugin install superclaude-core@superclaude-official

# Restart Claude Code
```

### Verify Installation

```bash
# List available /sc: commands
/help

# Test a command
/sc:help
```

## Usage

### Basic Commands

```bash
# Analyze code quality
/sc:analyze src/

# Implement a feature
/sc:implement "Add authentication to API"

# Design system architecture
/sc:design "Microservices architecture for e-commerce platform"
```

### With Behavioral Modes

```bash
# Use orchestration for multi-tool tasks
/sc:implement "Add user dashboard" --orchestrate

# Use token efficiency for large codebases
/sc:analyze --uc

# Use brainstorming for unclear requirements
/sc:brainstorm "Maybe build something with blockchain?" --brainstorm
```

### Advanced Workflows

```bash
# Full development workflow
/sc:brainstorm "New feature idea"
/sc:design "Feature architecture"
/sc:implement "Feature code"
/sc:test "Run tests"
/sc:document "Generate docs"
```

## Component Structure

```
superclaude-core/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── SuperClaude/
│   ├── Commands/                # 25 slash commands
│   ├── Core/                    # Core behaviors (FLAGS, PRINCIPLES, RULES)
│   └── Modes/                   # 7 behavioral modes
├── hooks/
│   └── hooks.json               # Mode activation hooks
└── README.md                    # This file
```

## Requirements

- Claude Code (latest version recommended)
- No additional dependencies

## License

MIT License - See [LICENSE](https://github.com/Utakata/SuperClaude_Plugin/blob/main/LICENSE)

## Support

- **GitHub**: https://github.com/Utakata/SuperClaude_Plugin
- **Issues**: https://github.com/Utakata/SuperClaude_Plugin/issues
- **Documentation**: https://github.com/Utakata/SuperClaude_Plugin/blob/main/README.md

## Version

**v4.3.0** - Plugin system migration release
