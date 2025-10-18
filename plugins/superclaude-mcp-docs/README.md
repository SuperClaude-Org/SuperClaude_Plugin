# SuperClaude MCP Documentation Plugin

MCP server integration documentation for 8 powerful external tools.

## What's Included

### 8 MCP Server Integrations

1. **Context7** (`MCP_Context7.md`)
   - Curated documentation lookup and pattern guidance
   - Official framework documentation access
   - Best practices and pattern recognition

2. **Sequential Thinking** (`MCP_Sequential.md`)
   - Structured multi-step reasoning
   - Complex debugging and analysis
   - Hypothesis testing and systematic problem-solving

3. **Magic** (`MCP_Magic.md`)
   - Modern UI generation from 21st.dev patterns
   - Component library integration
   - Design system alignment

4. **Playwright** (`MCP_Playwright.md`)
   - Real browser automation and testing
   - E2E testing scenarios
   - Visual validation and accessibility testing

5. **Morphllm** (`MCP_Morphllm.md`)
   - Bulk code transformations
   - Pattern-based multi-file edits
   - Style enforcement and refactoring

6. **Serena** (`MCP_Serena.md`)
   - Semantic code understanding
   - Session persistence and project memory
   - Large codebase navigation

7. **Tavily** (`MCP_Tavily.md`)
   - Advanced web search capabilities
   - Research and information gathering
   - Source validation

8. **Chrome DevTools** (`MCP_Chrome-DevTools.md`)
   - Browser performance analysis
   - Network and rendering diagnostics
   - Real-time debugging

## Installation

```bash
# Add SuperClaude marketplace
/plugin marketplace add Utakata/SuperClaude_Plugin

# Install MCP docs plugin
/plugin install superclaude-mcp-docs@superclaude-official
```

## Usage

Each MCP documentation file provides:
- Setup instructions
- Configuration examples
- Usage patterns
- Integration with SuperClaude commands
- Troubleshooting guides

### Example: Setting up Context7

1. Read the documentation:
   ```bash
   # Open MCP_Context7.md from the plugin
   ```

2. Configure in `.claude/.claude.json`:
   ```json
   {
     "mcpServers": {
       "context7": {
         "command": "npx",
         "args": ["-y", "@context7/mcp"]
       }
     }
   }
   ```

3. Use with SuperClaude:
   ```bash
   /sc:implement "Add React hooks" --c7
   ```

## MCP Server Categories

### Documentation & Learning
- **Context7**: Official documentation and patterns
- **Tavily**: Web research and information gathering

### Code Analysis & Transformation
- **Sequential**: Multi-step reasoning and analysis
- **Morphllm**: Bulk code transformations
- **Serena**: Semantic understanding and navigation

### UI & Testing
- **Magic**: Modern UI generation
- **Playwright**: Browser automation and E2E testing
- **Chrome DevTools**: Performance and debugging

## Component Structure

```
superclaude-mcp-docs/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── SuperClaude/
│   └── MCP/                     # MCP documentation
│       ├── MCP_Context7.md
│       ├── MCP_Sequential.md
│       ├── MCP_Magic.md
│       ├── MCP_Playwright.md
│       ├── MCP_Morphllm.md
│       ├── MCP_Serena.md
│       ├── MCP_Tavily.md
│       └── MCP_Chrome-DevTools.md
├── templates/
│   └── mcp-config-template.json # Configuration examples
└── README.md                    # This file
```

## Requirements

- Claude Code (latest version recommended)
- MCP servers must be installed separately (see individual documentation)

## License

MIT License - See [LICENSE](https://github.com/Utakata/SuperClaude_Plugin/blob/main/LICENSE)

## Version

**v4.3.0** - Plugin system migration release
