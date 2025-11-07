---
description: Interactive MCP server setup wizard
---

# MCP Server Setup Wizard

You are now in **MCP Setup Wizard Mode**. Guide the user through checking prerequisites, verifying the automatic MCP configuration, and setting up optional features.

## Setup Process

### Step 1: Welcome & Overview

Explain the MCP server architecture:

```
🚀 SuperClaude MCP Setup Wizard

SuperClaude plugin automatically configures AIRIS MCP Gateway, which provides
unified access to 10 powerful tools:

Essential (Free):
  • sequential-thinking - Multi-step problem solving
  • context7 - Official documentation search
  • git - Repository operations
  • puppeteer - Browser automation
  • playwright - Cross-browser testing
  • chrome-devtools - Browser debugging

Optional (API Key Required):
  • tavily - Web search ($)
  • magic - UI component generation ($)
  • serena - Context-aware intelligence
  • morphllm - Multi-model orchestration

Let's verify your setup...
```

### Step 2: Backup Existing MCP Configuration (Safety First!)

**IMPORTANT**: Before proceeding, check if the user has existing MCP servers configured.

```bash
# Check for existing MCP configuration
if [ -f ~/.claude/settings.local.json ]; then
    echo "⚠️  Found existing Claude Code settings"
    echo ""
    echo "RECOMMENDED: Backup your settings before enabling the plugin:"
    echo "  cp ~/.claude/settings.local.json ~/.claude/settings.local.json.backup"
    echo ""
    read -p "Have you backed up your settings? (y/n): " backup_done

    if [ "$backup_done" != "y" ]; then
        echo ""
        echo "Creating backup now..."
        cp ~/.claude/settings.local.json ~/.claude/settings.local.json.backup
        echo "✅ Backup created: ~/.claude/settings.local.json.backup"
    fi
else
    echo "✅ No existing settings found (fresh installation)"
fi

# Check for project-specific MCP config
if [ -f .mcp.json ]; then
    echo ""
    echo "⚠️  Found project-specific MCP configuration (.mcp.json)"
    echo "RECOMMENDED: Backup before proceeding:"
    echo "  cp .mcp.json .mcp.json.backup"
fi
```

### Step 3: Check Prerequisites

```bash
# Check uvx installation
if command -v uvx &> /dev/null; then
    echo "✅ uvx is installed ($(uvx --version))"
else
    echo "❌ uvx is not installed"
    echo ""
    echo "Install with:"
    echo "  pip install uv"
    echo "  # or"
    echo "  brew install uv"
fi
```

### Step 4: Verify Plugin MCP Configuration

```bash
# Check if plugin is installed
/plugin list | grep "sc" || echo "⚠️ SuperClaude plugin not found"

# Test MCP server availability
claude mcp list 2>/dev/null || echo "⚠️ MCP CLI not available (check Claude Code version)"
```

### Step 5: Interactive Configuration (Optional Features)

Present an interactive menu for optional API keys:

```
📝 Optional API Key Configuration

Some MCP tools require API keys for full functionality.
Would you like to configure them now?

Available services:
  1. Tavily (Web Search) - Get key: https://tavily.com
  2. 21st.dev (Magic UI) - Get key: https://21st.dev

Select options (comma-separated, or 'skip'): _
```

If user wants to configure:

```bash
# Guide them through setting environment variables
echo "Add these to your shell profile (~/.zshrc or ~/.bashrc):"
echo ""
echo "export TAVILY_API_KEY='your-tavily-key'"
echo "export TWENTYFIRST_API_KEY='your-21st-key'"
echo ""
echo "Then restart your terminal or run: source ~/.zshrc"
```

### Step 6: Test MCP Connection

```bash
# Try to invoke AIRIS MCP Gateway
echo "Testing MCP server connection..."

# This would test if the MCP server responds
claude mcp get airis-mcp-gateway 2>&1 | head -20

# Check if tools are available
echo ""
echo "Available MCP tools:"
# List available tools from the server
```

### Step 7: Troubleshooting Guide

If any issues are detected, provide specific solutions:

**Issue: uvx not found**
```bash
# Solution 1: Install via pip
pip install uv

# Solution 2: Install via Homebrew (macOS)
brew install uv

# Verify installation
uvx --version
```

**Issue: MCP server not responding**
```bash
# Check Claude Code version (needs v1.5+)
claude --version

# Test direct uvx execution
uvx --from git+https://github.com/agiletec-inc/airis-mcp-gateway airis-mcp-gateway --help

# Check plugin installation
/plugin list

# Reinstall plugin if needed
/plugin update sc@superclaude-official
```

**Issue: Plugin MCP not in settings**
```
The plugin's MCP configuration should be automatic.
If it's not working:

1. Restart Claude Code completely
2. Check plugin is enabled: /plugin list
3. Look for errors in Claude Code console
4. Report issue: https://github.com/SuperClaude-Org/SuperClaude_Plugin/issues
```

### Step 8: Final Summary

Provide a setup summary:

```
✅ MCP Setup Complete!

Status:
  • Prerequisites: ✅ All installed
  • AIRIS MCP Gateway: ✅ Connected
  • Available Tools: 10 tools ready
  • API Keys: 2 configured, 8 free tools ready

Quick Test:
  Try: /sc:research "test query"
  Or: /sc:implement "test feature"

Documentation:
  https://superclaude.netlify.app/mcp-servers

Need help? Run: /sc:verify-mcp
```

## Best Practices

- Always check prerequisites before attempting configuration
- Provide copy-paste ready commands
- Explain what each tool does and why it's useful
- Make API key setup optional and clear about costs
- Offer a quick verification test at the end

## Exit

After completing the setup wizard and providing the summary, exit setup mode.

The user can re-run this wizard anytime by using `/sc:setup-mcp`.
