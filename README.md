<div align="center">

# 🚀 SuperClaude Framework

### **Transform Claude Code into a Structured Development Platform**

<p align="center">
  <a href="https://github.com/hesreallyhim/awesome-claude-code/">
  <img src="https://awesome.re/mentioned-badge-flat.svg" alt="Mentioned in Awesome Claude Code">
  </a>
<a href="https://github.com/SuperClaude-Org/SuperGemini_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperGemini_Framework-blue" alt="Try SuperGemini Framework"/>
</a>
<a href="https://github.com/SuperClaude-Org/SuperQwen_Framework" target="_blank">
  <img src="https://img.shields.io/badge/Try-SuperQwen_Framework-orange" alt="Try SuperQwen Framework"/>
</a>
  <img src="https://img.shields.io/badge/version-4.3.2-blue" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

<p align="center">
  <a href="https://superclaude.netlify.app/">
    <img src="https://img.shields.io/badge/🌐_Visit_Website-blue" alt="Website">
  </a>
  <a href="https://github.com/SuperClaude-Org/SuperClaude_Plugin">
    <img src="https://img.shields.io/badge/🔌_Plugin-Distribution-green" alt="Plugin Distribution">
  </a>
</p>

<p align="center">
  <a href="README.md">
    <img src="https://img.shields.io/badge/🇺🇸_English-blue" alt="English">
  </a>
  <a href="README-zh.md">
    <img src="https://img.shields.io/badge/🇨🇳_中文-red" alt="中文">
  </a>
  <a href="README-ja.md">
    <img src="https://img.shields.io/badge/🇯🇵_日本語-green" alt="日本語">
  </a>
</p>

<p align="center">
  <a href="#-quick-installation">Quick Start</a> •
  <a href="#-support-the-project">Support</a> •
  <a href="#-whats-new-in-v4">Features</a> •
  <a href="#-documentation">Docs</a> •
  <a href="#-contributing">Contributing</a>
</p>

</div>

---

<div align="center">

## 📊 **Framework Statistics**

| **Commands** | **Agents** | **Modes** | **MCP Servers** |
|:------------:|:----------:|:---------:|:---------------:|
| **25** | **15** | **7** | **8** |
| Slash Commands | Specialized AI | Behavioral | Integrations |

Use the new `/sc:help` command to see a full list of all available commands.

</div>

---

<div align="center">

## 🎯 **Overview**

SuperClaude is a **meta-programming configuration framework** that transforms Claude Code into a structured development platform through behavioral instruction injection and component orchestration. It provides systematic workflow automation with powerful tools and intelligent agents.


## Disclaimer

This project is not affiliated with or endorsed by Anthropic.
Claude Code is a product built and maintained by [Anthropic](https://www.anthropic.com/).

---

## 🛡️ **CRITICAL: Backup Your Configuration First!**

> **⚠️ DO NOT SKIP THIS STEP ⚠️**
>
> The SuperClaude plugin modifies your Claude Code MCP configuration.
> **Always backup before installing** to ensure you can safely rollback if needed.

<div align="center">

### **⏱️ Quick Backup (30 seconds)**

```bash
# Download and run automated backup script
curl -o /tmp/backup-claude.sh https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Plugin/main/scripts/backup-claude-config.sh
chmod +x /tmp/backup-claude.sh
/tmp/backup-claude.sh
```

**✅ Backup complete!** Now you can safely install the plugin.

</div>

<details>
<summary><b>📋 What Gets Backed Up?</b></summary>

The automated backup script saves:
- ✅ `~/.claude/settings.local.json` - Your MCP server configurations
- ✅ `~/.claude/CLAUDE.md` - Your custom instructions
- ✅ `~/.claude/.credentials.json` - Your API credentials (if exists)
- ✅ `.mcp.json` - Project-specific MCP config (if exists)
- ✅ `.claude/` - Project-specific settings (if exists)

**Backup location:** `~/claude-backups/backup-YYYY-MM-DD-HH-MM-SS/`

</details>

<details>
<summary><b>🔧 Manual Backup Alternative</b></summary>

Prefer to backup manually?

```bash
# Create backup directory
BACKUP_DIR=~/claude-backups/backup-$(date +%Y-%m-%d-%H-%M-%S)
mkdir -p "$BACKUP_DIR"

# Backup global settings
cp ~/.claude/settings.local.json "$BACKUP_DIR/" 2>/dev/null
cp ~/.claude/CLAUDE.md "$BACKUP_DIR/" 2>/dev/null
cp ~/.claude/.credentials.json "$BACKUP_DIR/" 2>/dev/null

# Backup project settings (if in a project directory)
cp .mcp.json "$BACKUP_DIR/" 2>/dev/null
cp -r .claude "$BACKUP_DIR/" 2>/dev/null

echo "✅ Backup created at: $BACKUP_DIR"
```

</details>

<details>
<summary><b>🚨 Emergency Rollback</b></summary>

If something goes wrong after installation:

```bash
# 1. Uninstall plugin
/plugin uninstall sc@superclaude

# 2. Restore your backup (use your actual backup path)
BACKUP_DIR=~/claude-backups/backup-2025-01-07-14-30-25

cp "$BACKUP_DIR/settings.local.json" ~/.claude/
cp "$BACKUP_DIR/CLAUDE.md" ~/.claude/ 2>/dev/null
cp "$BACKUP_DIR/.credentials.json" ~/.claude/ 2>/dev/null

# 3. Restart Claude Code
pkill -9 claude-code
# Then relaunch Claude Code
```

**Rollback time: ~1 minute**

</details>

<div align="center">

**📖 Full Guide:** [Complete Backup & Safety Guide](BACKUP_GUIDE.md)

</div>

---

## ⚠️ **IMPORTANT: Beta Version Notice**

> **This plugin version is currently in BETA.**

### **Critical Compatibility Information:**

**NOT COMPATIBLE** with previous SuperClaude installations:
- pip version (`pip install SuperClaude`)
- pipx version (`pipx install SuperClaude`)
- npm version (`npm install -g @bifrost_inc/superclaude`)
- uv version (`uv tool install SuperClaude`)

### **Required Steps Before Installation:**

1. **✅ BACKUP** your configuration (see section above)
2. **UNINSTALL** previous versions:
   ```bash
   # For pip users
   pip uninstall SuperClaude

   # For pipx users
   pipx uninstall SuperClaude

   # For npm users
   npm uninstall -g @bifrost_inc/superclaude

   # For uv users
   uv tool uninstall SuperClaude
   ```
3. **THEN** proceed with plugin installation

⚠️ **Beta Limitations:**
- May contain bugs or incomplete features
- Configuration format may change
- Not recommended for production-critical work yet
- Feedback and issue reports are highly appreciated!

---

## ⚡ **Quick Installation**

SuperClaude is available as a native Claude Code plugin for easy installation and automatic updates.

```shell
# Add the SuperClaude marketplace
/plugin marketplace add SuperClaude-Org/SuperClaude_Plugin

# Install the plugin
/plugin install sc@superclaude

# Restart Claude Code to activate
```

**Plugin Benefits:**
- ✅ **Simple Installation**: One command, no Python/Node.js required
- ✅ **Automatic Updates**: Managed by Claude Code
- ✅ **No Conflicts**: Isolated from system packages
- ✅ **Team Sharing**: Easy distribution via marketplace
- ✅ **Native Integration**: Seamless Claude Code experience
- ✅ **Auto MCP Setup**: AIRIS MCP Gateway configured automatically

### **MCP Server Setup**

The plugin automatically configures **AIRIS MCP Gateway** with 10 integrated tools.

> ⚠️ **IMPORTANT: Backup Existing MCP Configuration**
>
> If you have existing MCP servers configured, **backup your settings first**:
> ```bash
> # Backup Claude Code MCP settings
> cp ~/.claude/settings.local.json ~/.claude/settings.local.json.backup
>
> # Or backup project-specific MCP config
> cp .mcp.json .mcp.json.backup  # If you have project MCP config
> ```
>
> The plugin adds AIRIS MCP Gateway to your configuration. Review for conflicts with existing MCP servers before enabling.

**Setup Options:**

**Option 1: AIRIS MCP Gateway (Recommended - One-Step Setup)**

Unified endpoint for 25+ MCP servers with 90% token reduction:

```bash
# 1. Start the Gateway
git clone https://github.com/agiletec-inc/airis-mcp-gateway.git
cd airis-mcp-gateway
just up

# 2. Connect to Claude Code
claude mcp add --transport http airis-mcp-gateway http://api.gateway.localhost:9400/api/v1/mcp
```

**Benefits:**
- ✅ 25+ servers in one endpoint
- ✅ 90% token reduction via schema partitioning
- ✅ Native HTTP transport (no Docker bridge)
- ✅ Hot-reload server management

**Option 2: Individual Server Setup (Advanced)**

For users who prefer individual server control:

```bash
# Install uvx (required for individual MCP servers)
pip install uv
# or
brew install uv
```

**Verify Setup**:
```shell
/sc:setup-mcp   # Interactive setup wizard
/sc:verify-mcp  # Check MCP status
```

**Optional API Keys** (for premium features):
```bash
# Tavily (web search) - Get key at https://tavily.com
export TAVILY_API_KEY="your-key"

# Magic (UI generation) - Get key at https://21st.dev
export TWENTYFIRST_API_KEY="your-key"
```

### **Quick Start**

After installation, restart Claude Code and try:

```shell
# See all commands
/sc:help

# Start brainstorming
/sc:brainstorm "your project idea"

# Analyze codebase
/sc:analyze

# Deep research
/sc:research "your topic"
```

</div>

<details>
<summary><b>📦 Alternative: pip/npm Installation</b></summary>

> ⚠️ **WARNING:** The pip/npm versions are NOT compatible with this plugin version.
>
> If you choose to use pip/npm installation instead:
> 1. Do NOT install both plugin and pip/npm versions simultaneously
> 2. Uninstall this plugin first if already installed
> 3. They use different configuration formats and cannot coexist

SuperClaude V4 is also available via package managers. See the main [SuperClaude Framework repository](https://github.com/SuperClaude-Org/SuperClaude_Framework) for pip/npm installation instructions.

</details>

---

<div align="center">

## 💖 **Support the Project**

> Hey, let's be real - maintaining SuperClaude takes time and resources.
> 
> *The Claude Max subscription alone runs $100/month for testing, and that's before counting the hours spent on documentation, bug fixes, and feature development.*
> *If you're finding value in SuperClaude for your daily work, consider supporting the project.*
> *Even a few dollars helps cover the basics and keeps development active.*
> 
> Every contributor matters, whether through code, feedback, or support. Thanks for being part of this community! 🙏

<table>
<tr>
<td align="center" width="33%">
  
### ☕ **Ko-fi**
[![Ko-fi](https://img.shields.io/badge/Support_on-Ko--fi-ff5e5b?logo=ko-fi)](https://ko-fi.com/superclaude)

*One-time contributions*

</td>
<td align="center" width="33%">

### 🎯 **Patreon**
[![Patreon](https://img.shields.io/badge/Become_a-Patron-f96854?logo=patreon)](https://patreon.com/superclaude)

*Monthly support*

</td>
<td align="center" width="33%">

### 💜 **GitHub**
[![GitHub Sponsors](https://img.shields.io/badge/GitHub-Sponsor-30363D?logo=github-sponsors)](https://github.com/sponsors/SuperClaude-Org)

*Flexible tiers*

</td>
</tr>
</table>

### **Your Support Enables:**

| Item | Cost/Impact |
|------|-------------|
| 🔬 **Claude Max Testing** | $100/month for validation & testing |
| ⚡ **Feature Development** | New capabilities & improvements |
| 📚 **Documentation** | Comprehensive guides & examples |
| 🤝 **Community Support** | Quick issue responses & help |
| 🔧 **MCP Integration** | Testing new server connections |
| 🌐 **Infrastructure** | Hosting & deployment costs |

> **Note:** No pressure though - the framework stays open source regardless. Just knowing people use and appreciate it is motivating. Contributing code, documentation, or spreading the word helps too! 🙏

</div>

---

<div align="center">

## 🎉 **What's New in V4**

> *Version 4 brings significant improvements based on community feedback and real-world usage patterns.*

<table>
<tr>
<td width="50%">

### 🤖 **Smarter Agent System**
**15 specialized agents** with domain expertise:
- Deep Research agent for autonomous web research
- Security engineer catches real vulnerabilities
- Frontend architect understands UI patterns
- Automatic coordination based on context
- Domain-specific expertise on demand

</td>
<td width="50%">

### 📝 **Improved Namespace**
**`/sc:` prefix** for all commands:
- No conflicts with custom commands
- 25 commands covering full lifecycle
- From brainstorming to deployment
- Clean, organized command structure

</td>
</tr>
<tr>
<td width="50%">

### 🔧 **MCP Server Integration**
**Powered by [AIRIS MCP Gateway](https://github.com/agiletec-inc/airis-mcp-gateway)**

A unified MCP proxy that reduces IDE startup token overhead through schema partitioning:
- **How it works**: Intercepts `tools/list` responses and returns only top-level schemas (1,250 tokens instead of 12,500)
- **25+ MCP servers** accessible through one endpoint
- **On-demand expansion**: Full schemas loaded only when needed via `expandSchema` tool

**Quick Setup:**
```bash
git clone https://github.com/agiletec-inc/airis-mcp-gateway.git
cd airis-mcp-gateway && just up
claude mcp add --transport http airis-mcp-gateway http://api.gateway.localhost:9400/api/v1/mcp
```

**🚀 Boost Further with [AIRIS Agent](https://github.com/agiletec-inc/airis-agent)**

Add the AIRIS Agent plugin for additional workflow optimization:
- ✅ **Repository Indexing**: 94% token reduction (58K → 3K) via `/index-repo`
- ✅ **Confidence Check**: Pre-implementation validation (≥90% required)
- ✅ **Deep Research**: Parallel web search with evidence synthesis
- ✅ **Self Review**: Post-implementation reflexion and validation

```bash
/plugin marketplace add agiletec-inc/airis-agent
/plugin install airis-agent
```

</td>
<td width="50%">

### 🎯 **Behavioral Modes**
**7 adaptive modes** for different contexts:
- **Brainstorming** → Asks right questions
- **Business Panel** → Multi-expert strategic analysis
- **Deep Research** → Autonomous web research
- **Orchestration** → Efficient tool coordination
- **Token-Efficiency** → 30-50% context savings
- **Task Management** → Systematic organization
- **Introspection** → Meta-cognitive analysis

</td>
</tr>
<tr>
<td width="50%">

### ⚡ **Optimized Performance**
**Smaller framework, bigger projects:**
- Reduced framework footprint
- More context for your code
- Longer conversations possible
- Complex operations enabled

</td>
<td width="50%">

### 📚 **Documentation Overhaul**
**Complete rewrite** for developers:
- Real examples & use cases
- Common pitfalls documented
- Practical workflows included
- Better navigation structure

</td>
</tr>
</table>

</div>

---

<div align="center">

## 🔬 **Deep Research Capabilities**

### **Autonomous Web Research Aligned with DR Agent Architecture**

SuperClaude v4.2 introduces comprehensive Deep Research capabilities, enabling autonomous, adaptive, and intelligent web research.

<table>
<tr>
<td width="50%">

### 🎯 **Adaptive Planning**
**Three intelligent strategies:**
- **Planning-Only**: Direct execution for clear queries
- **Intent-Planning**: Clarification for ambiguous requests
- **Unified**: Collaborative plan refinement (default)

</td>
<td width="50%">

### 🔄 **Multi-Hop Reasoning**
**Up to 5 iterative searches:**
- Entity expansion (Paper → Authors → Works)
- Concept deepening (Topic → Details → Examples)
- Temporal progression (Current → Historical)
- Causal chains (Effect → Cause → Prevention)

</td>
</tr>
<tr>
<td width="50%">

### 📊 **Quality Scoring**
**Confidence-based validation:**
- Source credibility assessment (0.0-1.0)
- Coverage completeness tracking
- Synthesis coherence evaluation
- Minimum threshold: 0.6, Target: 0.8

</td>
<td width="50%">

### 🧠 **Case-Based Learning**
**Cross-session intelligence:**
- Pattern recognition and reuse
- Strategy optimization over time
- Successful query formulations saved
- Performance improvement tracking

</td>
</tr>
</table>

### **Research Command Usage**

```bash
# Basic research with automatic depth
/sc:research "latest AI developments 2024"

# Controlled research depth
/sc:research "quantum computing breakthroughs" --depth exhaustive

# Specific strategy selection
/sc:research "market analysis" --strategy planning-only

# Domain-filtered research
/sc:research "React patterns" --domains "reactjs.org,github.com"
```

### **Research Depth Levels**

| Depth | Sources | Hops | Time | Best For |
|:-----:|:-------:|:----:|:----:|----------|
| **Quick** | 5-10 | 1 | ~2min | Quick facts, simple queries |
| **Standard** | 10-20 | 3 | ~5min | General research (default) |
| **Deep** | 20-40 | 4 | ~8min | Comprehensive analysis |
| **Exhaustive** | 40+ | 5 | ~10min | Academic-level research |

### **Integrated Tool Orchestration**

The Deep Research system intelligently coordinates multiple tools:
- **Tavily MCP**: Primary web search and discovery
- **Playwright MCP**: Complex content extraction
- **Sequential MCP**: Multi-step reasoning and synthesis
- **Serena MCP**: Memory and learning persistence
- **Context7 MCP**: Technical documentation lookup

</div>

---

<div align="center">

## 📚 **Documentation**

### **Complete Guide to SuperClaude**

<table>
<tr>
<th align="center">🚀 Getting Started</th>
<th align="center">📖 User Guides</th>
<th align="center">🛠️ Developer Resources</th>
<th align="center">📋 Reference</th>
</tr>
<tr>
<td valign="top">

- 📝 [**Quick Start Guide**](Docs/Getting-Started/quick-start.md)  
  *Get up and running fast*

- 💾 [**Installation Guide**](Docs/Getting-Started/installation.md)  
  *Detailed setup instructions*

</td>
<td valign="top">

- 🎯 [**Commands Reference**](Docs/User-Guide/commands.md)  
  *All 25 slash commands*

- 🤖 [**Agents Guide**](Docs/User-Guide/agents.md)  
  *15 specialized agents*

- 🎨 [**Behavioral Modes**](Docs/User-Guide/modes.md)  
  *7 adaptive modes*

- 🚩 [**Flags Guide**](Docs/User-Guide/flags.md)  
  *Control behaviors*

- 🔧 [**MCP Servers**](Docs/User-Guide/mcp-servers.md)  
  *7 server integrations*

- 💼 [**Session Management**](Docs/User-Guide/session-management.md)  
  *Save & restore state*

</td>
<td valign="top">

- 🏗️ [**Technical Architecture**](Docs/Developer-Guide/technical-architecture.md)  
  *System design details*

- 💻 [**Contributing Code**](Docs/Developer-Guide/contributing-code.md)  
  *Development workflow*

- 🧪 [**Testing & Debugging**](Docs/Developer-Guide/testing-debugging.md)  
  *Quality assurance*

</td>
<td valign="top">
- 📓 [**Examples Cookbook**](Docs/Reference/examples-cookbook.md)  
  *Real-world recipes*

- 🔍 [**Troubleshooting**](Docs/Reference/troubleshooting.md)  
  *Common issues & fixes*

</td>
</tr>
</table>

</div>

---

<div align="center">

## 🤝 **Contributing**

### **Join the SuperClaude Community**

We welcome contributions of all kinds! Here's how you can help:

| Priority | Area | Description |
|:--------:|------|-------------|
| 📝 **High** | Documentation | Improve guides, add examples, fix typos |
| 🔧 **High** | MCP Integration | Add server configs, test integrations |
| 🎯 **Medium** | Workflows | Create command patterns & recipes |
| 🧪 **Medium** | Testing | Add tests, validate features |
| 🌐 **Low** | i18n | Translate docs to other languages |

<p align="center">
  <a href="CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/📖_Read-Contributing_Guide-blue" alt="Contributing Guide">
  </a>
  <a href="https://github.com/SuperClaude-Org/SuperClaude_Framework/graphs/contributors">
    <img src="https://img.shields.io/badge/👥_View-All_Contributors-green" alt="Contributors">
  </a>
</p>

</div>

---

<div align="center">

## ⚖️ **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?" alt="MIT License">
</p>

</div>

---

<div align="center">

## ⭐ **Star History**

<a href="https://www.star-history.com/#SuperClaude-Org/SuperClaude_Framework&Timeline">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=SuperClaude-Org/SuperClaude_Framework&type=Timeline" />
 </picture>
</a>


</div>

---

<div align="center">

### **🚀 Built with passion by the SuperClaude community**

<p align="center">
  <sub>Made with ❤️ for developers who push boundaries</sub>
</p>

<p align="center">
  <a href="#-superclaude-framework">Back to Top ↑</a>
</p>

</div>
