# Changelog

All notable changes to SuperClaude will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [4.3.0-beta] - 2025-10-21

### 🎉 Major Changes

#### Plugin System Migration
SuperClaude is now available as a **native Claude Code plugin**. This represents a fundamental shift in distribution and installation methodology.

**Three modular plugins**:
- `superclaude-core`: 25 commands + 7 behavioral modes + 6 core behaviors
- `superclaude-agents`: 15 specialized AI agents + 6 context engineering agents
- `superclaude-mcp-docs`: 8 MCP server integration guides

### ✨ Added

#### Plugin Distribution System
- `.claude-plugin/marketplace.json` - Official SuperClaude plugin marketplace
- Plugin manifests for all three plugins with proper metadata
- Hooks system (`hooks.json`) for behavioral mode activation
- Modular component architecture with frontmatter metadata
- GitHub-based distribution via SuperClaude-Org/SuperClaude_Plugin

#### Documentation
- `docs/MIGRATION_GUIDE.md` - Comprehensive migration guide from installer to plugin
- `MIGRATION_COMPATIBILITY.md` - Technical analysis of installer vs plugin conflicts
- Plugin-specific README.md for each plugin
- Updated main README with plugin-first installation approach

#### Migration Tools
- `cleanup_superclaude.py` - Official cleanup utility for safe migration
  - Automatic detection of pip, pipx, uv, npm installations
  - Automatic backup creation before cleanup
  - Protection for Claude Code configuration files
  - Safe removal of conflicting installations

### 📦 Plugin Structure

#### superclaude-core (v4.3.0)
**Commands** (25 total):
- `/sc:analyze`, `/sc:brainstorm`, `/sc:build`, `/sc:business-panel`, `/sc:cleanup`
- `/sc:design`, `/sc:document`, `/sc:estimate`, `/sc:explain`, `/sc:git`
- `/sc:help`, `/sc:implement`, `/sc:improve`, `/sc:index`, `/sc:load`
- `/sc:reflect`, `/sc:research`, `/sc:save`, `/sc:select-tool`, `/sc:spawn`
- `/sc:spec-panel`, `/sc:task`, `/sc:test`, `/sc:troubleshoot`, `/sc:workflow`

**Kiro Commands** (10 total):
- `/kiro:spec-design`, `/kiro:spec-impl`, `/kiro:spec-init`, `/kiro:spec-requirements`
- `/kiro:spec-status`, `/kiro:spec-tasks`, `/kiro:steering`, `/kiro:steering-custom`
- `/kiro:validate-design`, `/kiro:validate-gap`

**Core Behaviors** (6 files):
- `BUSINESS_PANEL_EXAMPLES.md` - Business panel usage patterns
- `BUSINESS_SYMBOLS.md` - Business analysis symbol system
- `FLAGS.md` - Mode activation and control flags
- `PRINCIPLES.md` - Software engineering philosophy
- `RESEARCH_CONFIG.md` - Deep research configuration
- `RULES.md` - Behavioral rules and decision trees

**Behavioral Modes** (7 files):
- `MODE_Brainstorming.md`, `MODE_Business_Panel.md`, `MODE_DeepResearch.md`
- `MODE_Introspection.md`, `MODE_Orchestration.md`, `MODE_Task_Management.md`
- `MODE_Token_Efficiency.md`

#### superclaude-agents (v4.3.0)
**Specialized Agents** (15 total):
- `backend-architect`, `business-panel-experts`, `devops-architect`, `frontend-architect`
- `learning-guide`, `performance-engineer`, `python-expert`, `quality-engineer`
- `refactoring-expert`, `requirements-analyst`, `root-cause-analyst`, `security-engineer`
- `socratic-mentor`, `system-architect`, `technical-writer`

**Context Engineering Agents** (6 total):
- `context-orchestrator`, `documentation-specialist`, `metrics-analyst`
- `output-architect`, `query-optimizer`, `token-budget-manager`

#### superclaude-mcp-docs (v4.3.0)
**MCP Server Guides** (8 servers):
- Context7, Sequential Thinking, Magic, Playwright, Morphllm, Serena, Tavily, Chrome DevTools

### 🔄 Changed

#### Installation Methods
- **Plugin installation** is now the recommended method
- Traditional installer (pip/npm) remains available for backward compatibility
- Updated installation priority in all documentation

#### Repository Structure
- Added `plugins/` directory with three plugin packages
- Added `.claude-plugin/` for marketplace configuration
- Reorganized components with plugin-specific manifests

#### Documentation
- Main README prioritizes plugin installation
- Added migration path documentation
- Updated all component references for plugin structure

### ⚠️ Migration Required

**If you have existing installer-based installation**:

1. **Recommended**: Use official cleanup script
   ```bash
   curl -o cleanup_superclaude.py https://raw.githubusercontent.com/SuperClaude-Org/SuperClaude_Plugin/master/cleanup_superclaude.py
   python3 cleanup_superclaude.py
   ```

2. **Manual**: Uninstall before installing plugin version
   ```bash
   # Check for conflicts
   ls ~/.claude/commands/sc/

   # Remove if found
   pip uninstall superclaude
   # or
   npm uninstall -g @bifrost_inc/superclaude
   ```

**Why migration is necessary**:
- ❌ Command name conflicts (/sc:* commands duplicated)
- ❌ CLAUDE.md injection conflicts (increased token usage)
- ❌ Agent duplication (redundant system instructions)

See [MIGRATION_GUIDE.md](docs/MIGRATION_GUIDE.md) for detailed migration instructions.

### 🛠️ Technical Details

#### Plugin Manifest Schema
```json
{
  "name": "superclaude-core",
  "version": "4.3.0",
  "description": "Core framework with commands and modes",
  "commands": "./SuperClaude/Commands/",
  "hooks": "./hooks/hooks.json"
}
```

#### Hooks Configuration
Behavioral modes now activate via hooks system:
- `--brainstorm` → Brainstorming Mode
- `--orchestrate` → Orchestration Mode
- `--introspect` → Introspection Mode
- `--task-manage` → Task Management Mode
- `--token-efficient` → Token Efficiency Mode

#### Component Frontmatter
All commands and agents include metadata:
```yaml
name: analyze
description: Comprehensive code analysis
tags: [analysis, quality, security]
version: 4.3.0
```

### 📊 Statistics

- **Total plugins**: 3
- **Total commands**: 35 (25 /sc: + 10 /kiro:)
- **Total agents**: 21 (15 specialized + 6 context engineering)
- **Total modes**: 7
- **Total core behaviors**: 6
- **Total MCP docs**: 8
- **Total files migrated**: 93
- **Total lines of documentation**: 11,864

### 🔗 Links

- **Plugin Repository**: https://github.com/SuperClaude-Org/SuperClaude_Plugin
- **Migration Guide**: [docs/MIGRATION_GUIDE.md](docs/MIGRATION_GUIDE.md)
- **Plugin Documentation**: [plugins/superclaude-core/README.md](plugins/superclaude-core/README.md)

### 🙏 Acknowledgments

Special thanks to:
- Claude Code team for the plugin system architecture
- SuperClaude community for feedback and testing
- Contributors to the cleanup script enhancement

---

## [4.2.0] - 2025-09-18
### Added
- **Deep Research System** - Complete implementation of autonomous web research capabilities
  - New `/sc:research` command for intelligent web research with DR Agent architecture
  - `deep-research-agent` - 15th specialized agent for research orchestration
  - `MODE_DeepResearch` - 7th behavioral mode for research workflows
  - Tavily MCP integration (7th MCP server) for real-time web search
  - Research configuration system (`RESEARCH_CONFIG.md`)
  - Comprehensive workflow examples (`deep_research_workflows.md`)
  - Three planning strategies: Planning-Only, Intent-to-Planning, Unified Intent-Planning
  - Multi-hop reasoning with genealogy tracking for complex queries
  - Case-based reasoning for learning from past research patterns

### Changed
- Updated agent count from 14 to 15 (added deep-research-agent)
- Updated mode count from 6 to 7 (added MODE_DeepResearch)
- Updated MCP server count from 6 to 7 (added Tavily)
- Updated command count from 24 to 25 (added /sc:research)
- Enhanced MCP component with remote server support for Tavily
- Added `_install_remote_mcp_server` method to handle remote MCP configurations

### Technical
- Added Tavily to `server_docs_map` in `setup/components/mcp_docs.py`
- Implemented remote MCP server handler in `setup/components/mcp.py`
- Added `check_research_prerequisites()` function in `setup/utils/environment.py`
- Created verification script `scripts/verify_research_integration.sh`

### Requirements
- `TAVILY_API_KEY` environment variable for web search functionality
- Node.js and npm for Tavily MCP execution

## [4.1.5] - 2025-09-26
### Added
- Comprehensive flag documentation integrated into `/sc:help` command
- All 25 SuperClaude framework flags now discoverable from help system
- Practical usage examples and flag priority rules

### Fixed
- MCP incremental installation and auto-detection system
- Auto-detection of existing MCP servers from .claude.json and claude_desktop_config.json
- Smart server merging (existing + selected + previously installed)
- Documentation cleanup: removed non-existent commands (sc:fix, sc:simple-pix, sc:update, sc:develop, sc:modernize, sc:simple-fix)
- CLI logic to allow mcp_docs installation without server selection
### Changed
- MCP component now supports true incremental installation
- mcp_docs component auto-detects and installs documentation for all detected servers
- Improved error handling and graceful fallback for corrupted config files
- Enhanced user experience with single-source reference for all SuperClaude capabilities

## [4.1.0] - 2025-09-13
### Added
- Display author names and emails in the installer UI header.
- `is_reinstallable` flag for components to allow re-running installation.

### Fixed
- Installer now correctly installs only selected MCP servers on subsequent runs.
- Corrected validation logic for `mcp` and `mcp_docs` components to prevent incorrect failures.
- Ensured empty backup archives are created as valid tar files.
- Addressed an issue where only selected MCPs were being installed.
- Added Mithun Gowda B as an author.
- **MCP Installer:** Addressed several critical bugs in the MCP installation and update process to improve reliability.
  - Corrected the npm package name for the `morphllm` server in `setup/components/mcp.py`.
  - Implemented a custom installation method for the `serena` server using `uv`, as it is not an npm package.
  - Resolved a `NameError` in the `update` command within `setup/cli/commands/install.py`.
  - Patched a recurring "Unknown component: core" error by ensuring the component registry is initialized only once.
  - Added the `claude` CLI as a formal prerequisite for MCP server management, which was previously undocumented.

### Changed

### Technical
- Prepared package for PyPI distribution
- Validated package structure and dependencies

## [4.0.7] - 2025-01-23

### Added
- Automatic update checking for PyPI and NPM packages
- `--no-update-check` flag to skip update checks
- `--auto-update` flag for automatic updates without prompting
- Environment variable `SUPERCLAUDE_AUTO_UPDATE` support
- Update notifications with colored banners showing available version
- Rate limiting to check updates once per 24 hours
- Smart installation method detection (pip/pipx/npm/yarn)
- Cache files for update check timestamps (~/.claude/.update_check and .npm_update_check)

### Fixed
- Component validation now correctly uses pipx-installed version instead of source code

### Technical
- Added `setup/utils/updater.py` for PyPI update checking logic
- Added `bin/checkUpdate.js` for NPM update checking logic
- Integrated update checks into main entry points (superclaude/__main__.py and bin/cli.js)
- Non-blocking update checks with 2-second timeout to avoid delays

### Changed
- **BREAKING**: Agent system restructured to 14 specialized agents
- **BREAKING**: Commands now use `/sc:` namespace to avoid conflicts with user custom commands
- Commands are now installed in `~/.claude/commands/sc/` subdirectory
- All 21 commands updated: `/analyze` → `/sc:analyze`, `/build` → `/sc:build`, etc.
- Automatic migration from old command locations to new `sc/` subdirectory
- **BREAKING**: Documentation reorganization - docs/ directory renamed to Guides/

### Added
- **NEW AGENTS**: 14 specialized domain agents with enhanced capabilities
  - backend-architect.md, devops-architect.md, frontend-architect.md
  - learning-guide.md, performance-engineer.md, python-expert.md
  - quality-engineer.md, refactoring-expert.md, requirements-analyst.md
  - root-cause-analyst.md, security-engineer.md, socratic-mentor.md
- **NEW MODE**: MODE_Orchestration.md for intelligent tool selection mindset (5 total behavioral modes)
- **NEW COMMAND**: `/sc:implement` for feature and code implementation (addresses v2 user feedback)
- **NEW FILE**: CLAUDE.md for project-specific Claude Code instructions
- Migration logic to move existing commands to new namespace automatically
- Enhanced uninstaller to handle both old and new command locations
- Improved command conflict prevention
- Better command organization and discoverability
- Comprehensive PyPI publishing infrastructure
- API key management during SuperClaude MCP setup

### Removed
- **BREAKING**: Removed Templates/ directory (legacy templates no longer needed)
- **BREAKING**: Removed legacy agents and replaced with enhanced 14-agent system

### Improved
- Refactored Modes and MCP documentation for concise behavioral guidance
- Enhanced project cleanup and gitignore for PyPI publishing
- Implemented uninstall and update safety enhancements
- Better agent specialization and domain expertise focus

### Technical Details
- Commands now accessible as `/sc:analyze`, `/sc:build`, `/sc:improve`, etc.
- Migration preserves existing functionality while preventing naming conflicts
- Installation process detects and migrates existing commands automatically
- Tab completion support for `/sc:` prefix to discover all SuperClaude commands
- Guides/ directory replaces docs/ for improved organization

## [4.0.6] - 2025-08-23

### Fixed
- Component validation now correctly checks .superclaude-metadata.json instead of settings.json (#291)
- Standardized version numbers across all components to 4.0.6
- Fixed agent validation to check for correct filenames (architect vs specialist/engineer)
- Fixed package.json version inconsistency (was 4.0.5)

### Changed  
- Bumped version from 4.0.4 to 4.0.6 across entire project
- All component versions now synchronized at 4.0.6
- Cleaned up metadata file structure for consistency

## [4.0.4] - 2025-08-22

### Added
- **Agent System**: 13 specialized domain experts replacing personas
- **Behavioral Modes**: 4 intelligent modes for different workflows (Brainstorming, Introspection, Task Management, Token Efficiency)
- **Session Lifecycle**: /sc:load and /sc:save for cross-session persistence with Serena MCP
- **New Commands**: /sc:brainstorm, /sc:reflect, /sc:save, /sc:select-tool (21 total commands)
- **Serena MCP**: Semantic code analysis and memory management
- **Morphllm MCP**: Intelligent file editing with Fast Apply capability
- **Core Components**: Python-based framework integration (completely redesigned and implemented)
- **Templates**: Comprehensive templates for creating new components
- **Python-Ultimate-Expert Agent**: Master Python architect for production-ready code

### Changed
- Commands expanded from 16 to 21 specialized commands
- Personas replaced with 13 specialized Agents
- Enhanced MCP integration (6 servers total)
- Improved token efficiency (30-50% reduction with Token Efficiency Mode)
- Session management now uses Serena integration for persistence
- Framework structure reorganized for better modularity

### Improved
- Task management with multi-layer orchestration (TodoWrite, /task, /spawn, /loop)
- Quality gates with 8-step validation cycle
- Performance monitoring and optimization
- Cross-session context preservation
- Intelligent routing with ORCHESTRATOR.md enhancements

## [3.0.0] - 2025-07-14

### Added
- Initial release of SuperClaude v3.0
- 15 specialized slash commands for development tasks
- Smart persona auto-activation system
- MCP server integration (Context7, Sequential, Magic, Playwright)
- Unified CLI installer with multiple installation profiles
- Comprehensive documentation and user guides
- Token optimization framework
- Task management system

### Features
- **Commands**: analyze, build, cleanup, design, document, estimate, explain, git, improve, index, load, spawn, task, test, troubleshoot
- **Personas**: architect, frontend, backend, analyzer, security, mentor, refactorer, performance, qa, devops, scribe
- **MCP Servers**: Official library documentation, complex analysis, UI components, browser automation
- **Installation**: Quick, minimal, and developer profiles with component selection
