# SuperClaude Agents Plugin

15 specialized AI agents for architecture, quality, analysis, and development workflows.

## What's Included

### 15 Specialized Agents

#### Architecture Agents (3)
- **system-architect** - Design scalable system architecture with long-term maintainability focus
- **backend-architect** - Design reliable backend systems with data integrity and fault tolerance
- **frontend-architect** - Create accessible, performant user interfaces with modern frameworks

#### Quality Agents (3)
- **refactoring-expert** - Improve code quality through systematic refactoring and clean code principles
- **quality-engineer** - Comprehensive testing strategies and systematic edge case detection
- **python-expert** - Production-ready Python code following SOLID principles and best practices

#### Analysis Agents (3)
- **performance-engineer** - Optimize system performance through measurement-driven analysis
- **security-engineer** - Identify vulnerabilities and ensure compliance with security standards
- **root-cause-analyst** - Systematically investigate complex problems through evidence-based analysis

#### Workflow Agents (3)
- **devops-architect** - Automate infrastructure and deployment with reliability and observability
- **requirements-analyst** - Transform ambiguous ideas into concrete specifications
- **technical-writer** - Create clear, comprehensive technical documentation

#### Strategy & Learning Agents (3)
- **learning-guide** - Teach programming concepts with progressive learning and practical examples
- **socratic-mentor** - Educational guide using Socratic method for discovery learning
- **business-panel-experts** - Multi-expert business strategy panel (Christensen, Porter, Drucker, etc.)

#### Research Agent (1)
- **deep-research-agent** - Autonomous web research with adaptive planning and multi-hop reasoning

## Installation

```bash
# Add SuperClaude marketplace
/plugin marketplace add Utakata/SuperClaude_Plugin

# Install agents plugin
/plugin install superclaude-agents@superclaude-official
```

## Usage

Agents are automatically available through Claude Code's Task tool:

```bash
# Use an agent via Claude Code
@agent-system-architect
"Design a microservices architecture for our e-commerce platform"

# Invoke multiple agents
@agent-backend-architect, @agent-security-engineer
"Review our API design for security and scalability"
```

### With SuperClaude Commands

```bash
# Combine with /sc: commands
/sc:design "User authentication system" @agent-security-engineer

/sc:improve "Optimize database queries" @agent-performance-engineer

/sc:troubleshoot "Debug production error" @agent-root-cause-analyst
```

## Agent Capabilities

Each agent has specialized capabilities:

- **system-architect**: architecture-design, scalability-planning, system-modeling
- **backend-architect**: backend-design, api-design, database-design, security, fault-tolerance
- **security-engineer**: security-analysis, vulnerability-detection, compliance, threat-modeling
- **refactoring-expert**: refactoring, code-quality, clean-code, design-patterns
- **quality-engineer**: testing, quality-assurance, edge-cases, test-automation
- **performance-engineer**: performance-optimization, profiling, bottleneck-analysis

## Component Structure

```
superclaude-agents/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── SuperClaude/
│   └── Agents/                  # 15 specialized agents
│       ├── system-architect.md
│       ├── backend-architect.md
│       ├── frontend-architect.md
│       └── [12 more agents]
└── README.md                    # This file
```

## Requirements

- Claude Code (latest version recommended)
- Optional: SuperClaude Core plugin (for enhanced integration)

## License

MIT License - See [LICENSE](https://github.com/Utakata/SuperClaude_Plugin/blob/main/LICENSE)

## Version

**v4.3.0** - Plugin system migration release
