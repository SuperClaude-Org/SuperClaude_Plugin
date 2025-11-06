---
description: Verify MCP server installation and configuration status
---

# MCP Server Verification

You are now in **MCP Verification Mode**. Your goal is to check the status of MCP servers and guide the user through any necessary setup.

## Verification Steps

### 1. Check Prerequisites

```bash
# Check if uvx is available
uvx --version

# Check if the plugin's MCP server configuration exists
cat ~/.claude/settings.local.json | grep -A 5 "airis-mcp-gateway" || echo "Not found in user settings"
```

### 2. Check MCP Server Status

Use the Bash tool to check:
```bash
# List configured MCP servers
claude mcp list

# Test AIRIS MCP Gateway connection (if available)
claude mcp get airis-mcp-gateway
```

### 3. Report Status

Provide a clear status report:

**✅ Working**:
- List MCP servers that are properly configured and responding
- Confirm which tools are available

**⚠️ Needs Attention**:
- Missing prerequisites (e.g., uvx not installed)
- MCP servers configured but not responding
- Missing optional API keys

**❌ Not Configured**:
- MCP servers that should be available but aren't configured

### 4. Provide Guidance

For any issues found, provide specific commands to fix them:

**Missing uvx**:
```bash
# Install uv (includes uvx)
pip install uv
# or
brew install uv
```

**Plugin MCP Not Starting**:
```bash
# Check plugin is installed
/plugin list

# Reinstall plugin if needed
/plugin update sc@superclaude-official
```

**Missing API Keys** (optional):
```bash
# Add to your shell profile (~/.zshrc, ~/.bashrc, etc.)
export TAVILY_API_KEY="your-key-here"
export TWENTYFIRST_API_KEY="your-key-here"
```

### 5. Troubleshooting

If AIRIS MCP Gateway is not working:

1. **Check logs**: Look for error messages in Claude Code output
2. **Test uvx directly**:
   ```bash
   uvx --from git+https://github.com/agiletec-inc/airis-mcp-gateway airis-mcp-gateway --help
   ```
3. **Verify network access**: Ensure you can access GitHub
4. **Check Claude Code version**: MCP server support requires recent version

## Summary Format

Present findings in a clear table:

| MCP Server | Status | Tools Available | Action Needed |
|------------|--------|-----------------|---------------|
| AIRIS MCP Gateway | ✅ Working | 10 tools | None |
| AIRIS MCP Gateway | ⚠️ Partial | Limited | Install uvx |
| AIRIS MCP Gateway | ❌ Not Found | None | Check plugin |

## Exit

After providing the status report and any necessary guidance, exit verification mode.
