# SuperClaude Plugin - AI Assistant Development Guide

> **Purpose**: This document provides comprehensive guidance for AI assistants working with the SuperClaude Plugin codebase. It explains architecture, conventions, workflows, and best practices for development.

---

## Table of Contents
1. [Repository Overview](#repository-overview)
2. [Architecture & Design Patterns](#architecture--design-patterns)
3. [Directory Structure](#directory-structure)
4. [File Conventions](#file-conventions)
5. [Development Workflows](#development-workflows)
6. [Core Framework](#core-framework)
7. [Command System](#command-system)
8. [Agent System](#agent-system)
9. [Mode System](#mode-system)
10. [Flag System](#flag-system)
11. [MCP Integration](#mcp-integration)
12. [CI/CD & Automation](#cicd--automation)
13. [Testing & Validation](#testing--validation)
14. [Best Practices](#best-practices)

---

## Repository Overview

**What is SuperClaude Plugin?**
SuperClaude is a meta-programming framework that transforms Claude Code through behavioral instruction injection. It's NOT executable code—it's a collection of markdown files containing behavioral patterns and instructions that modify Claude's behavior when commands are invoked.

**Key Statistics:**
- **Version:** 4.4.0
- **29 Commands** (slash commands for workflow automation)
- **21 Agents** (15 specialized + 6 context engineering)
- **7 Behavioral Modes** (brainstorming, business panel, deep research, etc.)
- **6 Core Framework Files** (principles, rules, flags, examples, symbols, research config)
- **~6,700+ lines** of behavioral instructions
- **License:** MIT

**Repository:** https://github.com/SuperClaude-Org/SuperClaude_Plugin

---

## Architecture & Design Patterns

### Meta-Programming Pattern
SuperClaude uses **behavioral instruction injection** instead of traditional code execution:

```
User types: /sc:brainstorm "my idea"
           ↓
Claude Code loads: commands/brainstorm.md
           ↓
Claude reads behavioral instructions
           ↓
Claude applies the patterns/behaviors defined in the file
           ↓
Claude executes with modified behavior
```

**Key Principle:** Commands are **context triggers**, not executable code. They modify how Claude thinks and operates.

### Frontmatter-Driven Metadata
All commands and agents use YAML frontmatter for classification:

```yaml
---
description: "What this command does"
category: orchestration|analysis|implementation|utility|documentation|mcp
complexity: low|medium|advanced
mcp-servers: [list, of, mcp, servers]
personas: [list, of, agent, personas]
---
```

### Modular Architecture
```
Core Framework (Philosophy & Rules)
        ↓
Behavioral Modes (How to behave)
        ↓
Commands (User-facing actions)
        ↓
Agents (Specialized expertise)
        ↓
MCP Servers (Tool integration)
```

### Context Engineering Principles
Four strategies for context optimization:
1. **Write Context** - External persistence (save important info)
2. **Select Context** - Retrieval optimization (load relevant info)
3. **Compress Context** - Token optimization (use symbols, summaries)
4. **Isolate Context** - Separation of concerns (modular scoping)

---

## Directory Structure

```
/home/user/SuperClaude_Plugin/
├── .claude-plugin/          # Plugin configuration & marketplace metadata
│   ├── plugin.json          # Plugin metadata for Claude Code
│   └── marketplace.json     # Marketplace distribution config
│
├── .github/workflows/       # CI/CD automation
│   ├── cleanup-commands.yml # SSSP-optimized command cleanup
│   └── blank.yml           # Template workflow
│
├── agents/                  # 21 specialized AI agents
│   ├── backend-architect.md
│   ├── frontend-architect.md
│   ├── python-expert.md
│   ├── security-engineer.md
│   ├── ... (11 more specialized agents)
│   └── ContextEngineering/  # 6 advanced context optimization agents
│       ├── context-orchestrator.md
│       ├── documentation-specialist.md
│       ├── metrics-analyst.md
│       ├── output-architect.md
│       ├── IMPLEMENTATION_SUMMARY.md
│       └── README.md
│
├── commands/                # 29 slash commands
│   ├── agent.md            # /sc:agent - Activate specialized agents
│   ├── analyze.md          # /sc:analyze - Codebase analysis
│   ├── brainstorm.md       # /sc:brainstorm - Requirements discovery
│   ├── build.md            # /sc:build - Build project
│   ├── business-panel.md   # /sc:business-panel - Strategic analysis
│   ├── cleanup.md          # /sc:cleanup - Code cleanup
│   ├── design.md           # /sc:design - Architecture design
│   ├── document.md         # /sc:document - Generate documentation
│   ├── estimate.md         # /sc:estimate - Effort estimation
│   ├── explain.md          # /sc:explain - Code explanation
│   ├── git.md              # /sc:git - Git operations
│   ├── help.md             # /sc:help - Show help
│   ├── implement.md        # /sc:implement - Implementation
│   ├── improve.md          # /sc:improve - Code improvement
│   ├── index-repo.md       # /sc:index-repo - Repository indexing
│   ├── index.md            # /sc:index - General indexing
│   ├── load.md             # /sc:load - Load context
│   ├── reflect.md          # /sc:reflect - Self-reflection
│   ├── research.md         # /sc:research - Deep research
│   ├── save.md             # /sc:save - Save context
│   ├── select-tool.md      # /sc:select-tool - Tool selection
│   ├── setup-mcp.md        # /sc:setup-mcp - MCP configuration
│   ├── spawn.md            # /sc:spawn - Spawn sub-agents
│   ├── spec-panel.md       # /sc:spec-panel - Specification panel
│   ├── task.md             # /sc:task - Task management
│   ├── test.md             # /sc:test - Run tests
│   ├── troubleshoot.md     # /sc:troubleshoot - Debugging
│   ├── verify-mcp.md       # /sc:verify-mcp - Verify MCP setup
│   └── workflow.md         # /sc:workflow - Workflow orchestration
│
├── core/                    # 6 core framework files
│   ├── BUSINESS_PANEL_EXAMPLES.md  # Strategic analysis patterns
│   ├── BUSINESS_SYMBOLS.md         # Symbol communication system
│   ├── FLAGS.md                    # Mode activation & control flags
│   ├── PRINCIPLES.md               # Software engineering philosophy
│   ├── RESEARCH_CONFIG.md          # Deep research configuration
│   └── RULES.md                    # Behavioral rules & decision trees
│
├── modes/                   # 7 behavioral mode definitions
│   ├── MODE_Brainstorming.md       # Interactive discovery
│   ├── MODE_Business_Panel.md      # Multi-expert strategic analysis
│   ├── MODE_DeepResearch.md        # Autonomous web research
│   ├── MODE_Introspection.md       # Meta-cognitive analysis
│   ├── MODE_Orchestration.md       # Tool coordination
│   ├── MODE_Task_Management.md     # Systematic organization
│   └── MODE_Token_Efficiency.md    # Symbol-enhanced communication
│
├── scripts/                 # Utility scripts
│   ├── backup-claude-config.sh     # Backup Claude Code config
│   └── clean_command_names.py      # Cleanup command frontmatter
│
├── BACKUP_GUIDE.md         # Configuration backup guide
├── CLAUDE.md               # This file (AI assistant guide)
├── LICENSE                 # MIT License
├── MIGRATION_GUIDE.md      # pip/npm to plugin migration
├── PLUGIN_SUMMARY.md       # Component statistics & overview
├── README.md               # Main project documentation (English)
├── README-ja.md            # Japanese documentation
├── README-zh.md            # Chinese documentation
├── plugin.json             # Root plugin configuration
└── .gitignore              # Git exclusions
```

**Total Files:** ~80+ markdown files, 3 JSON configs, 2 scripts

---

## File Conventions

### Naming Patterns

#### Commands
- **Pattern:** `{command-name}.md`
- **Example:** `brainstorm.md` → `/sc:brainstorm`
- **Location:** `/commands/`
- **Prefix:** Derived from `plugin.json` name field (`"sc"`)
- **Case:** lowercase with hyphens

#### Agents
- **Pattern:** `{domain}-{role}.md`
- **Example:** `backend-architect.md`, `python-expert.md`
- **Location:** `/agents/` (root) or `/agents/ContextEngineering/`
- **Case:** lowercase with hyphens

#### Modes
- **Pattern:** `MODE_{ModeName}.md`
- **Example:** `MODE_Brainstorming.md`, `MODE_Task_Management.md`
- **Location:** `/modes/`
- **Case:** MODE_ prefix (all caps) + PascalCase name

#### Core Files
- **Pattern:** `{PURPOSE}.md`
- **Example:** `PRINCIPLES.md`, `FLAGS.md`, `RULES.md`
- **Location:** `/core/`
- **Case:** ALL CAPS

### Frontmatter Structure

#### Command Frontmatter
```yaml
---
description: "Brief description of what this command does"
category: orchestration|analysis|implementation|utility|documentation|mcp
complexity: low|medium|advanced
mcp-servers: [sequential, context7, magic, playwright, morphllm, serena]
personas: [architect, analyzer, frontend, backend, security, devops, project-manager]
---
```

**IMPORTANT:** Do NOT include a `name:` field in command frontmatter. The name is automatically derived from the filename. Including `name:` causes redundancy and is removed by CI/CD automation.

#### Agent Frontmatter
```yaml
---
name: agent-name
description: "Brief description of agent role"
category: specialized|context-engineering
activation: auto|manual|context
priority: P0|P1|P2
keywords: [list, of, trigger, keywords]
---
```

### File Structure Templates

#### Command File Template
```markdown
---
description: "What this command does"
category: category-name
complexity: low|medium|advanced
mcp-servers: [optional, list]
personas: [optional, list]
---

# /sc:command-name - Title

> **Context Framework Note**: This file provides behavioral instructions for Claude Code when users type `/sc:command-name` patterns. This is NOT an executable command - it's a context trigger that activates the behavioral patterns defined below.

## Triggers
- When this command should activate
- Specific user scenarios
- Keywords or patterns

## Context Trigger Pattern
```
/sc:command-name [args] [--flags]
```
**Usage**: Description of how to use this command

## Behavioral Flow
1. **Step 1**: Description
2. **Step 2**: Description
3. **Step 3**: Description
4. **Step N**: Description

Key behaviors:
- Behavior 1
- Behavior 2
- Behavior 3

## MCP Integration
- **MCP Server 1**: How it's used
- **MCP Server 2**: How it's used

## Tool Coordination
- **Tool 1**: How it's used
- **Tool 2**: How it's used

## Boundaries
**Will do:**
- Action 1
- Action 2

**Won't do:**
- Anti-pattern 1
- Anti-pattern 2

## Examples
[Optional examples of usage]
```

#### Agent File Template
```markdown
---
name: agent-name
description: "Agent role description"
category: specialized|context-engineering
activation: auto|manual|context
priority: P0|P1|P2
keywords: [keyword1, keyword2]
---

# Agent Name

## Triggers
- When this agent activates
- Specific scenarios

## Behavioral Mindset
- How the agent thinks
- Key principles

## Focus Areas
- Area 1
- Area 2
- Area 3

## Key Actions
1. Action 1
2. Action 2
3. Action 3

## Outputs
- Output type 1
- Output type 2

## Boundaries
**Will do:**
- Responsibility 1
- Responsibility 2

**Won't do:**
- Out of scope 1
- Out of scope 2
```

---

## Development Workflows

### Adding a New Command

**Step 1: Create Command File**
```bash
# Create file in /commands/ directory
# Filename becomes the command name
touch commands/my-new-command.md
```

**Step 2: Add Frontmatter**
```yaml
---
description: "Brief description of command"
category: orchestration  # Choose appropriate category
complexity: medium       # low|medium|advanced
mcp-servers: [sequential, context7]  # Optional
personas: [architect, analyzer]      # Optional
---
```

**Step 3: Write Behavioral Instructions**
Follow the command file template above. Include:
- Triggers
- Context trigger pattern
- Behavioral flow
- MCP integration (if applicable)
- Tool coordination
- Boundaries
- Examples

**Step 4: Test the Command**
```bash
# In Claude Code, test the command
/sc:my-new-command
```

**Step 5: Commit Changes**
```bash
git add commands/my-new-command.md
git commit -m "feat: add /sc:my-new-command for [purpose]"
git push -u origin claude/[branch-name]
```

### Adding a New Agent

**Step 1: Create Agent File**
```bash
# Create file in /agents/ directory
# Use {domain}-{role}.md naming pattern
touch agents/database-expert.md
```

**Step 2: Add Frontmatter**
```yaml
---
name: database-expert
description: "Database design and optimization specialist"
category: specialized
activation: auto
priority: P1
keywords: [database, sql, nosql, schema, query]
---
```

**Step 3: Write Agent Definition**
Follow the agent file template above.

**Step 4: Link Agent to Commands**
Update relevant command files to include the agent in `personas:` list.

**Step 5: Test Activation**
```bash
# Test auto-activation via keywords
# Or manual activation
/sc:agent database-expert
```

### Modifying Core Framework Files

**Core Files:**
- `PRINCIPLES.md` - Software engineering philosophy
- `RULES.md` - Behavioral rules and decision trees
- `FLAGS.md` - Mode activation and control flags
- `BUSINESS_PANEL_EXAMPLES.md` - Strategic analysis examples
- `BUSINESS_SYMBOLS.md` - Symbol communication system
- `RESEARCH_CONFIG.md` - Deep research configuration

**When to Modify:**
- **PRINCIPLES.md**: Adding new engineering principles or patterns
- **RULES.md**: Adding new behavioral rules or decision trees
- **FLAGS.md**: Adding new flags for modes or MCP servers
- **BUSINESS_PANEL_EXAMPLES.md**: Adding new strategic analysis examples
- **BUSINESS_SYMBOLS.md**: Adding new symbols for token efficiency
- **RESEARCH_CONFIG.md**: Modifying research depth or strategies

**Best Practice:** Core files affect ALL commands and agents. Test thoroughly before committing.

### Adding a New Behavioral Mode

**Step 1: Create Mode File**
```bash
# Create file in /modes/ directory
# Use MODE_{ModeName}.md naming pattern
touch modes/MODE_Code_Review.md
```

**Step 2: Define Mode**
```markdown
# Code Review Mode

**Purpose**: Systematic code review with quality assurance focus

## Activation Triggers
- User requests code review
- Pull request analysis
- Quality assessment needs

## Behavioral Changes
- Enable critical analysis mindset
- Focus on code quality metrics
- Apply SOLID principles rigorously
- Generate actionable feedback

## Outcomes
- Detailed review comments
- Quality scores
- Improvement recommendations

## Examples
[Examples of when this mode activates]
```

**Step 3: Add Flag to FLAGS.md**
```markdown
**--code-review**
- Trigger: Code review requests, PR analysis, quality assessment
- Behavior: Enable systematic code review with quality metrics
```

**Step 4: Reference in Commands**
Update relevant commands to reference the new mode.

### Updating Plugin Version

**Step 1: Update Version in All Configs**
```bash
# Update version in plugin.json (root)
# Update version in .claude-plugin/plugin.json
# Update version in README.md
# Ensure all three match
```

**Step 2: Update PLUGIN_SUMMARY.md**
Document what changed in the new version.

**Step 3: Tag Release**
```bash
git tag -a v4.5.0 -m "Release version 4.5.0"
git push origin v4.5.0
```

---

## Core Framework

### PRINCIPLES.md
**Purpose:** Defines software engineering philosophy and decision-making frameworks

**Key Sections:**
- **Philosophy**: Task-first approach, evidence-based reasoning, parallel thinking
- **Engineering Mindset**: SOLID, DRY, KISS, YAGNI, systems thinking
- **Decision Framework**: Data-driven choices, trade-off analysis, risk management
- **Quality Philosophy**: Quality quadrants, testing strategies

**When Referenced:**
- All implementation commands
- Architecture decisions
- Code review processes
- Design patterns

### RULES.md
**Purpose:** Behavioral rules and decision trees for Claude's operation

**Key Sections:**
- Behavioral rules for different scenarios
- Decision trees for common situations
- Conflict resolution patterns
- Escalation pathways

**When Referenced:**
- Complex decision-making
- Conflict resolution
- Edge case handling
- Multi-agent coordination

### FLAGS.md
**Purpose:** Comprehensive flag system for mode activation and MCP server selection

**Categories:**
1. **Mode Activation Flags**: --brainstorm, --introspect, --task-manage, --orchestrate, --token-efficient
2. **MCP Server Flags**: --c7, --seq, --magic, --morph, --serena, --play, --chrome, --tavily
3. **Analysis Depth Flags**: --think, --think-hard, --ultrathink
4. **Execution Control Flags**: --delegate, --loop, --validate
5. **Output Optimization Flags**: --uc (ultra-compressed), --scope, --focus

**When Referenced:**
- Command execution
- MCP server selection
- Mode activation
- Performance optimization

### BUSINESS_PANEL_EXAMPLES.md
**Purpose:** Examples of multi-expert strategic analysis patterns

**When Referenced:**
- /sc:business-panel command
- Strategic planning
- Multi-stakeholder analysis
- Investment decisions

### BUSINESS_SYMBOLS.md
**Purpose:** Symbol system for ultra-compressed communication (30-50% token reduction)

**Symbol Categories:**
- Status indicators (✓, ✗, ⚠, ⏸, ⏭)
- Priority markers (🔴, 🟡, 🟢)
- Process flow (→, ↓, ↔, ⇒)
- Thinking markers (🤔, 💡, 🎯)
- Technical symbols (⚙, 🔧, 🐛, ⚡)

**When Referenced:**
- --uc flag enabled
- Token efficiency mode
- Large-scale operations
- Context >75% usage

### RESEARCH_CONFIG.md
**Purpose:** Configuration for deep research mode operations

**Key Settings:**
- Research depth levels (shallow, normal, deep)
- Source credibility thresholds
- Parallel search strategies
- Output formatting

**When Referenced:**
- /sc:research command
- Deep research mode
- Market analysis
- Technology validation

---

## Command System

### Command Prefix System
All commands use the `/sc:` prefix, derived from `plugin.json`:

```json
{
  "name": "sc"  // This becomes the command prefix
}
```

**Invocation Pattern:**
```
/sc:command-name [args] [--flags]
```

### Command Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| **orchestration** | Workflow coordination | brainstorm, task, spawn, workflow |
| **analysis** | Code analysis & debugging | analyze, troubleshoot, explain |
| **implementation** | Development tasks | implement, build, design |
| **documentation** | Docs generation | document, index, index-repo |
| **utility** | Helper commands | help, agent, load, save |
| **mcp** | MCP integration | setup-mcp, verify-mcp, select-tool |

### Complexity Levels

| Level | Description | Characteristics |
|-------|-------------|-----------------|
| **low** | Simple, direct | Single-step, minimal coordination |
| **medium** | Multi-step | Some coordination, moderate scope |
| **advanced** | Complex orchestration | MCP integration, multi-agent, parallel ops |

### Command Lifecycle

```
User types command
        ↓
Claude Code loads .md file
        ↓
Frontmatter parsed (metadata extracted)
        ↓
Behavioral instructions read
        ↓
MCP servers activated (if specified)
        ↓
Agents spawned (if specified in personas)
        ↓
Command behavior executed
        ↓
Output generated
```

### MCP Server Integration in Commands

Commands can declare MCP server dependencies:

```yaml
mcp-servers: [sequential, context7, magic, playwright]
```

**Available MCP Servers:**
- **sequential** - Multi-step reasoning
- **context7** - Documentation lookup
- **magic** - UI generation (21st.dev)
- **playwright** - Browser testing
- **morphllm** - Code transformation
- **serena** - Session persistence
- **chrome** - Chrome DevTools
- **tavily** - Web search

### Persona (Agent) Integration in Commands

Commands can declare agent personas to activate:

```yaml
personas: [architect, analyzer, frontend, backend, security, devops]
```

**Available Personas:**
- architect, analyzer, frontend, backend, security, devops, project-manager
- python-expert, quality-engineer, performance-engineer, refactoring-expert
- technical-writer, requirements-analyst, root-cause-analyst
- learning-guide, socratic-mentor, self-review
- business-panel-experts, deep-research-agent
- context-orchestrator, documentation-specialist, metrics-analyst, output-architect

---

## Agent System

### Agent Types

#### Specialized Agents (15)
Domain expertise agents located in `/agents/` root directory:

1. **backend-architect.md** - Backend system design
2. **business-panel-experts.md** - Strategic business analysis
3. **deep-research-agent.md** - Research coordination
4. **devops-architect.md** - DevOps & infrastructure
5. **frontend-architect.md** - Frontend architecture
6. **learning-guide.md** - Educational guidance
7. **performance-engineer.md** - Performance optimization
8. **python-expert.md** - Python expertise
9. **quality-engineer.md** - Quality assurance
10. **refactoring-expert.md** - Code refactoring
11. **requirements-analyst.md** - Requirements analysis
12. **root-cause-analyst.md** - Problem diagnosis
13. **security-engineer.md** - Security analysis
14. **socratic-mentor.md** - Socratic teaching
15. **technical-writer.md** - Documentation

#### Context Engineering Agents (6)
Advanced optimization agents in `/agents/ContextEngineering/`:

1. **context-orchestrator.md** - Memory management & RAG
2. **documentation-specialist.md** - Auto-documentation
3. **metrics-analyst.md** - Performance tracking
4. **output-architect.md** - Structured output generation

### Agent Activation Methods

#### 1. Auto-Activation
Agents with `activation: auto` activate based on keywords:

```yaml
---
activation: auto
keywords: [database, sql, schema]
---
```

When user mentions "database schema design", the database-expert agent activates automatically.

#### 2. Manual Activation
```bash
/sc:agent agent-name
```

Example:
```bash
/sc:agent python-expert
```

#### 3. Command-Based Activation
Commands declare agents via `personas:` frontmatter:

```yaml
personas: [architect, security, devops]
```

When command runs, these agents activate.

### Agent Priority System

| Priority | Meaning | Usage |
|----------|---------|-------|
| **P0** | Critical | Core functionality agents |
| **P1** | High | Frequently used specialists |
| **P2** | Normal | Contextual specialists |

Higher priority agents activate first in multi-agent scenarios.

### Multi-Agent Coordination

Commands like `/sc:brainstorm` coordinate multiple agents:

```yaml
personas: [architect, analyzer, frontend, backend, security, devops, project-manager]
```

**Coordination Pattern:**
1. Primary agent analyzes task
2. Delegate to specialist agents for domain expertise
3. Synthesize insights from multiple perspectives
4. Generate comprehensive output

---

## Mode System

### Available Modes

| Mode | File | Activation Flag | Purpose |
|------|------|-----------------|---------|
| **Brainstorming** | MODE_Brainstorming.md | --brainstorm | Interactive discovery |
| **Business Panel** | MODE_Business_Panel.md | N/A | Strategic analysis |
| **Deep Research** | MODE_DeepResearch.md | N/A | Autonomous research |
| **Introspection** | MODE_Introspection.md | --introspect | Meta-cognition |
| **Orchestration** | MODE_Orchestration.md | --orchestrate | Tool coordination |
| **Task Management** | MODE_Task_Management.md | --task-manage | Systematic organization |
| **Token Efficiency** | MODE_Token_Efficiency.md | --token-efficient | Symbol communication |

### Mode Activation Triggers

#### Brainstorming Mode
**Triggers:**
- Vague project requests
- Exploration keywords ("maybe", "thinking about", "not sure")
- Requirements discovery needs

**Behavior Changes:**
- Collaborative discovery mindset
- Probing questions
- Requirement elicitation

#### Introspection Mode
**Triggers:**
- Self-analysis requests
- Error recovery
- Complex problem-solving requiring meta-cognition

**Behavior Changes:**
- Expose thinking process
- Transparency markers (🤔, 🎯, ⚡, 📊, 💡)
- Step-by-step reasoning

#### Task Management Mode
**Triggers:**
- Multi-step operations (>3 steps)
- Complex scope (>2 directories OR >3 files)
- Large refactoring

**Behavior Changes:**
- Delegation orchestration
- Progressive enhancement
- Systematic organization

#### Orchestration Mode
**Triggers:**
- Multi-tool operations
- Performance constraints
- Parallel execution opportunities

**Behavior Changes:**
- Tool selection optimization
- Parallel thinking
- Resource constraint adaptation

#### Token Efficiency Mode
**Triggers:**
- Context usage >75%
- Large-scale operations
- --uc flag

**Behavior Changes:**
- Symbol-enhanced communication
- 30-50% token reduction
- Preserved clarity

### Mode Combinations

Modes can activate simultaneously:
```
/sc:brainstorm --introspect --token-efficient
```

This activates:
1. Brainstorming mode (collaborative discovery)
2. Introspection mode (transparent thinking)
3. Token efficiency mode (symbol communication)

---

## Flag System

### Mode Activation Flags

```
--brainstorm          # Collaborative discovery mode
--introspect          # Expose thinking process
--task-manage         # Systematic organization
--orchestrate         # Tool coordination optimization
--token-efficient     # Symbol-enhanced communication
```

### MCP Server Flags

```
--c7 / --context7     # Enable Context7 for documentation
--seq / --sequential  # Enable Sequential for multi-step reasoning
--magic               # Enable Magic for UI generation
--morph / --morphllm  # Enable Morphllm for code transformation
--serena              # Enable Serena for session persistence
--play / --playwright # Enable Playwright for browser testing
--chrome              # Enable Chrome DevTools for debugging
--tavily              # Enable Tavily for web search
```

### Analysis Depth Flags

```
--think               # Standard analysis depth
--think-hard          # Deep analysis with multiple perspectives
--ultrathink          # Exhaustive analysis with all available tools
```

### Execution Control Flags

```
--delegate            # Enable multi-agent delegation
--loop                # Enable iterative refinement
--validate            # Enable validation at each step
```

### Output Optimization Flags

```
--uc                  # Ultra-compressed output (30-50% token reduction)
--scope               # Scope-focused output (relevant context only)
--focus               # Focused output (eliminate verbosity)
```

### Flag Usage Examples

```bash
# Deep research with introspection and token efficiency
/sc:research "AI agents" --introspect --token-efficient --tavily

# Brainstorming with multi-agent delegation
/sc:brainstorm "e-commerce platform" --delegate --seq --c7

# Code analysis with ultra-thinking
/sc:analyze --ultrathink --validate

# Implementation with orchestration
/sc:implement --orchestrate --loop --morph
```

---

## MCP Integration

### MCP Server Configuration

MCP servers are configured in `plugin.json`:

```json
{
  "mcpServers": {
    "airis-mcp-gateway": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/agiletec-inc/airis-mcp-gateway",
        "airis-mcp-gateway"
      ],
      "env": {}
    }
  }
}
```

### Available MCP Servers

| Server | Purpose | Activation Flag |
|--------|---------|-----------------|
| **Context7** | Documentation lookup | --c7, --context7 |
| **Sequential** | Multi-step reasoning | --seq, --sequential |
| **Magic** | UI generation (21st.dev) | --magic |
| **Morphllm** | Code transformation | --morph, --morphllm |
| **Serena** | Session persistence | --serena |
| **Playwright** | Browser testing | --play, --playwright |
| **Chrome DevTools** | Browser debugging | --chrome |
| **Tavily** | Web search | --tavily |

### MCP Server Selection Matrix

Commands can declare MCP dependencies:

```yaml
mcp-servers: [sequential, context7, magic]
```

**Selection Logic:**
1. Check command frontmatter for `mcp-servers:` list
2. Check flags in user command (--c7, --seq, etc.)
3. Auto-select based on task type (if FLAGS.md rules apply)
4. Enable selected servers for command execution

### MCP Integration Patterns

#### Pattern 1: Documentation Lookup
```
User needs framework docs → Context7 activated → Curated docs retrieved
```

#### Pattern 2: Multi-Step Reasoning
```
Complex debugging → Sequential activated → Structured hypothesis testing
```

#### Pattern 3: UI Generation
```
UI component request → Magic activated → 21st.dev patterns applied
```

#### Pattern 4: Code Transformation
```
Bulk refactoring → Morphllm activated → Pattern-based transformation
```

#### Pattern 5: Session Persistence
```
Large codebase → Serena activated → Semantic memory + context retention
```

---

## CI/CD & Automation

### GitHub Actions Workflows

#### cleanup-commands.yml
**Purpose:** SSSP-optimized CI/CD for automatic command frontmatter cleanup

**What It Does:**
1. Triggers on pushes to `commands/*.md` files
2. Runs `clean_command_names.py` script
3. Removes redundant `name:` attributes from frontmatter
4. Auto-commits changes if cleanup occurred

**Why It Exists:**
- Enforces convention: command names derived from filenames
- Prevents redundant `name:` fields
- Maintains consistency across all commands

**SSSP Optimizations:**
- Parallel job execution
- Smart caching (58% faster than sequential)
- Path-based triggers (only runs when commands/ changed)

**Workflow Trigger:**
```yaml
on:
  push:
    paths:
      - 'commands/*.md'
```

**Manual Trigger:**
```bash
# GitHub Actions UI → Run workflow
```

### Utility Scripts

#### clean_command_names.py
**Location:** `/scripts/clean_command_names.py`

**Purpose:** Remove redundant `name:` attributes from command frontmatter

**Usage:**
```bash
# Run locally
python scripts/clean_command_names.py

# Run via GitHub Actions
# (Automatic on push to commands/)
```

**What It Does:**
1. Scans all files in `commands/` directory
2. Parses YAML frontmatter
3. Removes `name:` field if present
4. Preserves all other frontmatter fields
5. Writes cleaned file back (idempotent)

**Example:**
```yaml
# Before
---
name: brainstorm  # ← REMOVED
description: "Interactive requirements discovery"
category: orchestration
---

# After
---
description: "Interactive requirements discovery"
category: orchestration
---
```

#### backup-claude-config.sh
**Location:** `/scripts/backup-claude-config.sh`

**Purpose:** Backup Claude Code configuration before plugin installation

**Usage:**
```bash
# Run before installing plugin
bash scripts/backup-claude-config.sh
```

**What It Backs Up:**
- Claude Code MCP server configurations
- Plugin settings
- User preferences

**Backup Location:** `~/.claude-code-backup-{timestamp}/`

---

## Testing & Validation

### Pre-Commit Checklist

Before committing changes, verify:

#### For New/Modified Commands:
- [ ] Frontmatter includes all required fields
- [ ] NO `name:` field in frontmatter (auto-derived from filename)
- [ ] Description is clear and concise
- [ ] Category is correct (orchestration|analysis|implementation|utility|documentation|mcp)
- [ ] Complexity level is appropriate (low|medium|advanced)
- [ ] MCP servers listed if used
- [ ] Personas listed if agents activated
- [ ] Behavioral flow is clear
- [ ] Boundaries defined (will/won't do)
- [ ] Examples provided (if helpful)

#### For New/Modified Agents:
- [ ] Frontmatter includes name, description, category
- [ ] Activation method specified (auto|manual|context)
- [ ] Priority set (P0|P1|P2)
- [ ] Keywords defined for auto-activation
- [ ] Triggers clearly stated
- [ ] Focus areas defined
- [ ] Key actions enumerated
- [ ] Boundaries defined

#### For New/Modified Modes:
- [ ] MODE_ prefix used in filename
- [ ] Purpose clearly stated
- [ ] Activation triggers defined
- [ ] Behavioral changes documented
- [ ] Outcomes specified
- [ ] Flag added to FLAGS.md

#### For Core Framework Changes:
- [ ] Impact on all commands/agents considered
- [ ] Documentation updated
- [ ] Examples provided
- [ ] Backward compatibility maintained (if possible)

### Manual Testing

#### Test Commands:
```bash
# In Claude Code, test the command
/sc:your-command

# Test with flags
/sc:your-command --introspect --token-efficient

# Test with arguments
/sc:your-command "argument value"
```

#### Test Agents:
```bash
# Manual activation
/sc:agent your-agent

# Auto-activation via keywords
# Type a message containing agent keywords
```

#### Test Modes:
```bash
# Test mode activation via flag
/sc:command --your-mode-flag

# Verify behavioral changes occur
```

### Validation Scripts

#### Validate Frontmatter:
```bash
# Check all commands have valid frontmatter
python scripts/validate_frontmatter.py  # (if exists)
```

#### Validate No Redundant Names:
```bash
# Run cleanup script and check for changes
python scripts/clean_command_names.py
git status  # Should show no changes if already clean
```

---

## Best Practices

### General Principles

1. **Evidence-Based Development**
   - Test all changes before committing
   - Verify behavioral changes match expectations
   - Document unexpected behaviors

2. **Consistency is Key**
   - Follow naming conventions strictly
   - Use established patterns from existing files
   - Maintain frontmatter structure

3. **Clarity Over Cleverness**
   - Write clear behavioral instructions
   - Use explicit trigger descriptions
   - Avoid ambiguous language

4. **Modularity**
   - Keep commands focused on single responsibilities
   - Delegate complex operations to multiple agents
   - Separate concerns (modes, agents, commands)

5. **Documentation**
   - Document all behavioral patterns
   - Provide examples where helpful
   - Keep README files updated

### Command Development Best Practices

1. **Single Responsibility**
   - Each command should do ONE thing well
   - Don't create multi-purpose commands
   - Delegate complex flows to /sc:workflow

2. **Clear Triggers**
   - Define explicit activation conditions
   - Use specific keywords
   - Avoid overlapping triggers with other commands

3. **Explicit Boundaries**
   - Clearly state what command WILL do
   - Clearly state what command WON'T do
   - Handle edge cases gracefully

4. **MCP Integration**
   - Only declare MCP servers actually used
   - Provide fallback behavior if MCP unavailable
   - Document MCP requirements

5. **Agent Coordination**
   - List all relevant personas
   - Define coordination patterns
   - Specify delegation strategy

### Agent Development Best Practices

1. **Focused Expertise**
   - Define clear domain boundaries
   - Don't create generalist agents
   - Specialize deeply in one area

2. **Clear Activation**
   - Choose activation method carefully (auto vs manual)
   - Define specific keywords for auto-activation
   - Document when agent should be used

3. **Priority Setting**
   - P0: Core functionality (context-orchestrator, system-architect)
   - P1: Frequent specialists (python-expert, security-engineer)
   - P2: Contextual helpers (learning-guide, refactoring-expert)

4. **Behavioral Mindset**
   - Define how agent thinks differently
   - Specify unique perspectives
   - Document decision-making patterns

### Mode Development Best Practices

1. **Mode Naming**
   - Use MODE_{PascalCase} pattern
   - Choose descriptive names
   - Avoid generic names

2. **Behavioral Changes**
   - Clearly document behavioral shifts
   - Provide concrete examples
   - Show before/after patterns

3. **Activation Triggers**
   - Define explicit trigger conditions
   - Avoid overlapping triggers
   - Consider flag-based activation

4. **Mode Combinations**
   - Test compatibility with other modes
   - Document intended combinations
   - Handle conflicts gracefully

### Core Framework Best Practices

1. **PRINCIPLES.md**
   - Add principles backed by evidence
   - Provide concrete examples
   - Link to documentation/resources

2. **RULES.md**
   - Write clear, unambiguous rules
   - Provide decision trees for complex scenarios
   - Include fallback behaviors

3. **FLAGS.md**
   - Document ALL flags comprehensively
   - Specify trigger conditions
   - Explain behavioral changes

4. **Symbol Systems**
   - Use symbols consistently
   - Document meaning clearly
   - Test token reduction claims

### Git Workflow Best Practices

1. **Branch Naming**
   - Use `claude/` prefix: `claude/feature-name-sessionid`
   - Include session ID at end
   - Use descriptive feature names

2. **Commit Messages**
   - Use conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`
   - Be specific and descriptive
   - Reference issues when applicable

3. **Pull Requests**
   - Provide clear descriptions
   - List all changes
   - Include testing evidence
   - Link related issues

4. **Push Retry Logic**
   - Retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)
   - Use `git push -u origin branch-name`
   - Only retry on network errors, not auth failures

### Documentation Best Practices

1. **README Updates**
   - Keep component counts accurate
   - Update installation instructions
   - Maintain translation consistency (EN, JA, ZH)

2. **Inline Documentation**
   - Add Context Framework Notes to all commands
   - Explain behavioral patterns clearly
   - Provide usage examples

3. **Version Updates**
   - Update ALL version references simultaneously
   - Document breaking changes
   - Provide migration guides

---

## Common Development Patterns

### Pattern 1: Command with Multi-Agent Coordination

```yaml
---
description: "Complex task requiring multiple perspectives"
category: orchestration
complexity: advanced
personas: [architect, security, performance, quality]
---

# /sc:complex-task

## Behavioral Flow
1. **Architect Agent**: Analyze system design
2. **Security Agent**: Assess security implications
3. **Performance Agent**: Evaluate performance impact
4. **Quality Agent**: Review code quality standards
5. **Synthesis**: Combine insights into comprehensive output
```

### Pattern 2: Command with MCP Integration

```yaml
---
description: "Task requiring external tools"
category: implementation
complexity: advanced
mcp-servers: [sequential, context7, morphllm]
---

# /sc:mcp-task

## MCP Integration
- **Sequential**: Multi-step reasoning for complex logic
- **Context7**: Framework documentation lookup
- **Morphllm**: Code transformation at scale
```

### Pattern 3: Mode-Aware Command

```markdown
## Behavioral Flow
1. Check active modes (--introspect, --token-efficient)
2. If --introspect: Expose thinking with transparency markers
3. If --token-efficient: Use symbol communication
4. Adapt output format to active modes
```

### Pattern 4: Context Engineering Agent

```yaml
---
name: context-optimizer
description: "Optimizes context usage through strategic techniques"
category: context-engineering
activation: auto
keywords: [context, memory, token, optimization]
---

# Context Optimizer Agent

## Focus Areas
1. **Write Context**: External persistence strategies
2. **Select Context**: Retrieval optimization
3. **Compress Context**: Token reduction techniques
4. **Isolate Context**: Separation of concerns
```

### Pattern 5: Hierarchical Agent Delegation

```
Command: /sc:brainstorm
    ↓
Primary Agent: System Architect
    ↓
Delegates to:
    → Frontend Architect (UI/UX analysis)
    → Backend Architect (API design)
    → Security Engineer (threat modeling)
    → DevOps Architect (deployment strategy)
    ↓
Synthesis: Comprehensive project specification
```

### Pattern 6: Flag-Based Behavior Adaptation

```markdown
## Behavioral Flow
1. Parse flags from command
2. If --think-hard:
   - Enable deep analysis mode
   - Activate multiple reasoning paths
   - Generate comprehensive output
3. If --uc (ultra-compressed):
   - Enable symbol communication
   - Reduce token usage 30-50%
   - Maintain information density
4. Execute core command logic with adapted behavior
```

---

## Troubleshooting

### Common Issues

#### Issue: Command Not Recognized
**Symptoms:** `/sc:command` not found

**Solutions:**
1. Check filename matches command name exactly
2. Verify plugin.json `name` field is `"sc"`
3. Restart Claude Code
4. Re-install plugin if necessary

#### Issue: Agent Not Activating
**Symptoms:** Agent doesn't activate on keywords

**Solutions:**
1. Check `activation: auto` in agent frontmatter
2. Verify keywords include the ones used
3. Try manual activation: `/sc:agent agent-name`
4. Check priority level (P0 > P1 > P2)

#### Issue: MCP Server Not Available
**Symptoms:** MCP server declared but not used

**Solutions:**
1. Verify MCP server installed: `/sc:verify-mcp`
2. Check plugin.json mcpServers configuration
3. Install missing server: `/sc:setup-mcp`
4. Check server compatibility with Claude Code version

#### Issue: Frontmatter Parse Error
**Symptoms:** Command loads but behaves incorrectly

**Solutions:**
1. Validate YAML frontmatter syntax
2. Check for tabs vs spaces
3. Verify closing `---`
4. Run cleanup script: `python scripts/clean_command_names.py`

#### Issue: CI/CD Workflow Failing
**Symptoms:** GitHub Actions failing on push

**Solutions:**
1. Check workflow logs for specific error
2. Verify Python script syntax
3. Ensure proper file permissions
4. Check branch naming follows convention

---

## Quick Reference

### File Locations Quick Reference

| Component | Location | Pattern |
|-----------|----------|---------|
| Commands | `/commands/` | `{command-name}.md` |
| Agents (specialized) | `/agents/` | `{domain}-{role}.md` |
| Agents (context eng) | `/agents/ContextEngineering/` | `{purpose}.md` |
| Modes | `/modes/` | `MODE_{ModeName}.md` |
| Core Framework | `/core/` | `{PURPOSE}.md` |
| Scripts | `/scripts/` | `{script-name}.{ext}` |
| Plugin Config | `/` & `/.claude-plugin/` | `plugin.json` |

### Command Invocation Quick Reference

```bash
# Basic command
/sc:command

# Command with argument
/sc:command "argument"

# Command with flags
/sc:command --flag1 --flag2

# Command with argument and flags
/sc:command "argument" --flag1 --flag2

# Agent activation
/sc:agent agent-name

# Help
/sc:help
```

### Flag Quick Reference

| Flag | Category | Purpose |
|------|----------|---------|
| --brainstorm | Mode | Collaborative discovery |
| --introspect | Mode | Expose thinking |
| --task-manage | Mode | Systematic organization |
| --orchestrate | Mode | Tool coordination |
| --token-efficient | Mode | Symbol communication |
| --c7, --context7 | MCP | Documentation lookup |
| --seq, --sequential | MCP | Multi-step reasoning |
| --magic | MCP | UI generation |
| --morph, --morphllm | MCP | Code transformation |
| --serena | MCP | Session persistence |
| --play, --playwright | MCP | Browser testing |
| --chrome | MCP | DevTools debugging |
| --tavily | MCP | Web search |
| --think | Analysis | Standard depth |
| --think-hard | Analysis | Deep analysis |
| --ultrathink | Analysis | Exhaustive analysis |
| --delegate | Execution | Multi-agent delegation |
| --loop | Execution | Iterative refinement |
| --validate | Execution | Validation steps |
| --uc | Output | Ultra-compressed |
| --scope | Output | Scope-focused |
| --focus | Output | Eliminate verbosity |

### Frontmatter Fields Quick Reference

#### Commands
```yaml
description: "Required: Brief description"
category: "Required: orchestration|analysis|implementation|utility|documentation|mcp"
complexity: "Required: low|medium|advanced"
mcp-servers: "Optional: [list, of, servers]"
personas: "Optional: [list, of, agents]"
```

#### Agents
```yaml
name: "Required: agent-name"
description: "Required: Brief description"
category: "Required: specialized|context-engineering"
activation: "Optional: auto|manual|context"
priority: "Optional: P0|P1|P2"
keywords: "Optional: [keyword, list]"
```

### Git Workflow Quick Reference

```bash
# Create feature branch
git checkout -b claude/feature-name-sessionid

# Add changes
git add .

# Commit with conventional commits
git commit -m "feat: add new feature"
git commit -m "fix: resolve bug"
git commit -m "docs: update documentation"
git commit -m "refactor: improve code structure"

# Push with retry logic
git push -u origin claude/feature-name-sessionid

# If push fails due to network, retry with exponential backoff:
# Wait 2s, retry
# Wait 4s, retry
# Wait 8s, retry
# Wait 16s, retry
```

---

## Additional Resources

### Documentation
- **Main Docs:** https://superclaude.netlify.app/
- **GitHub Repo:** https://github.com/SuperClaude-Org/SuperClaude_Plugin
- **Issues:** https://github.com/SuperClaude-Org/SuperClaude_Plugin/issues
- **Discussions:** https://github.com/SuperClaude-Org/SuperClaude_Plugin/discussions

### Related Files
- **README.md** - Main project documentation (English)
- **README-ja.md** - Japanese documentation
- **README-zh.md** - Chinese documentation
- **PLUGIN_SUMMARY.md** - Component statistics
- **MIGRATION_GUIDE.md** - Migration from pip/npm
- **BACKUP_GUIDE.md** - Configuration backup guide

### Community
- Report bugs via GitHub Issues
- Ask questions in GitHub Discussions
- Contribute via Pull Requests

---

## Version History

**Current Version:** 4.4.0

### Key Changes
- Migrated from pip/npm to native plugin distribution
- Removed redundant `name:` fields from command frontmatter
- SSSP-optimized CI/CD workflows
- Enhanced context engineering agents
- Comprehensive flag system

---

## License

MIT License - see LICENSE file for details

---

**Last Updated:** 2025-11-14

**Maintainer:** SuperClaude Team (support@superclaude.dev)
