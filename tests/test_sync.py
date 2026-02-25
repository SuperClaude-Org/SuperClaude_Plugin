"""
Test suite for sync_from_framework.py

Run tests with:
    python -m pytest tests/test_sync.py -v
    or
    python tests/test_sync.py
"""

import unittest
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'scripts'))

from sync_from_framework import ContentTransformer, McpMerger


class TestContentTransformer(unittest.TestCase):
    """Test content transformation logic."""

    def test_command_header_transformation(self):
        """Test command header gets sc: prefix."""
        input_content = """---
description: Test command
---

# /brainstorm - Brainstorming Mode

Use /analyze for analysis.
"""

        expected = """---
description: Test command
---

# /sc:brainstorm - Brainstorming Mode

Use /sc:analyze for analysis.
"""

        result = ContentTransformer.transform_command(input_content, "brainstorm.md")
        self.assertEqual(result, expected)

    def test_command_cross_references(self):
        """Test cross-references to other commands get transformed."""
        input_content = "See /task and /implement for more details."
        expected = "See /sc:task and /sc:implement for more details."

        result = ContentTransformer.transform_command(input_content, "test.md")
        self.assertEqual(result, expected)

    def test_command_link_references(self):
        """Test markdown link references get transformed."""
        input_content = "Use [/analyze] or [/test] commands."
        expected = "Use [/sc:analyze] or [/sc:test] commands."

        result = ContentTransformer.transform_command(input_content, "test.md")
        self.assertEqual(result, expected)

    def test_command_mixed_references(self):
        """Test mixed command references in complex markdown."""
        input_content = """
# /workflow - Workflow Management

Workflow management uses /task internally.

See [/analyze] for code analysis or use /implement.

Example: /workflow "build feature" --use-tasks
"""

        expected = """
# /sc:workflow - Workflow Management

Workflow management uses /sc:task internally.

See [/sc:analyze] for code analysis or use /sc:implement.

Example: /sc:workflow "build feature" --use-tasks
"""

        result = ContentTransformer.transform_command(input_content, "workflow.md")
        self.assertEqual(result, expected)

    def test_agent_name_transformation(self):
        """Test agent frontmatter name gets sc- prefix."""
        input_content = """---
name: backend-architect
description: Backend expert
category: engineering
---

# Backend Architect
"""

        result = ContentTransformer.transform_agent(input_content, "backend-architect.md")
        self.assertIn("name: sc-backend-architect", result)
        self.assertIn("# Backend Architect", result)

    def test_agent_without_name(self):
        """Test agent without name field remains unchanged."""
        input_content = """---
description: Test agent
category: test
---

# Test Agent
"""

        result = ContentTransformer.transform_agent(input_content, "test-agent.md")
        self.assertEqual(result, input_content)

    def test_agent_name_already_prefixed(self):
        """Test agent with sc- prefix already doesn't get double-prefixed."""
        input_content = """---
name: sc-backend-architect
description: Backend expert
---

# Backend Architect
"""

        result = ContentTransformer.transform_agent(input_content, "backend-architect.md")
        self.assertIn("name: sc-backend-architect", result)
        # Should not become sc-sc-backend-architect
        self.assertNotIn("sc-sc-", result)


class TestMcpMerger(unittest.TestCase):
    """Test MCP configuration merging."""

    def setUp(self):
        """Set up test fixtures."""
        from tempfile import mkdtemp
        self.temp_dir = Path(mkdtemp())

    def test_framework_precedence(self):
        """Test Framework servers take precedence."""
        framework_mcp = {
            "sequential": {"command": "uvx", "args": ["sequential-thinking"]}
        }
        plugin_mcp = {
            "sequential": {"command": "npx", "args": ["sequential"]}  # Conflict
        }

        merger = McpMerger(self.temp_dir)
        merged, warnings = merger.merge(framework_mcp, plugin_mcp)

        # Framework version should win
        self.assertEqual(merged["sequential"], framework_mcp["sequential"])

        # Should have conflict warning
        self.assertTrue(any("conflict" in w.lower() for w in warnings))

    def test_preserve_plugin_specific(self):
        """Test Plugin-specific servers are preserved."""
        framework_mcp = {
            "sequential": {"command": "uvx", "args": ["sequential"]}
        }
        plugin_mcp = {
            "sequential": {"command": "uvx", "args": ["sequential"]},
            "airis-mcp-gateway": {"command": "uvx", "args": ["airis"]}  # Plugin-only
        }

        merger = McpMerger(self.temp_dir)
        merged, warnings = merger.merge(framework_mcp, plugin_mcp)

        # Should have both servers
        self.assertIn("sequential", merged)
        self.assertIn("airis-mcp-gateway", merged)

        # Should warn about preservation
        self.assertTrue(any("preserved" in w.lower() for w in warnings))

    def test_identical_servers_no_warning(self):
        """Test identical servers don't generate warnings."""
        framework_mcp = {
            "sequential": {"command": "uvx", "args": ["sequential"]}
        }
        plugin_mcp = {
            "sequential": {"command": "uvx", "args": ["sequential"]}
        }

        merger = McpMerger(self.temp_dir)
        merged, warnings = merger.merge(framework_mcp, plugin_mcp)

        # Should have server
        self.assertIn("sequential", merged)

        # No conflicts, so no warnings about this server
        conflict_warnings = [w for w in warnings if "conflict" in w.lower()]
        self.assertEqual(len(conflict_warnings), 0)

    def test_empty_framework_mcp(self):
        """Test merge with empty Framework MCP."""
        framework_mcp = {}
        plugin_mcp = {
            "airis-mcp-gateway": {"command": "uvx", "args": ["airis"]}
        }

        merger = McpMerger(self.temp_dir)
        merged, warnings = merger.merge(framework_mcp, plugin_mcp)

        # Plugin servers should be preserved
        self.assertEqual(merged, plugin_mcp)
        self.assertTrue(any("preserved" in w.lower() for w in warnings))

    def test_empty_plugin_mcp(self):
        """Test merge with empty Plugin MCP."""
        framework_mcp = {
            "sequential": {"command": "uvx", "args": ["sequential"]}
        }
        plugin_mcp = {}

        merger = McpMerger(self.temp_dir)
        merged, warnings = merger.merge(framework_mcp, plugin_mcp)

        # Framework servers should be in merged
        self.assertEqual(merged, framework_mcp)
        # No plugin servers to preserve
        self.assertEqual(len(warnings), 0)


class TestPatterns(unittest.TestCase):
    """Test regex patterns used in transformations."""

    def test_command_header_pattern(self):
        """Test command header pattern matches various formats."""
        import re
        pattern = ContentTransformer.COMMAND_HEADER_PATTERN

        test_cases = [
            ("# /brainstorm", True),
            ("## /analyze", True),
            ("### /task", True),
            ("#/nospace", True),
            ("# not-a-command", False),
            ("  # /indented", False),  # Must be at line start
        ]

        for text, should_match in test_cases:
            match = pattern.search(text)
            if should_match:
                self.assertIsNotNone(match, f"Pattern should match: {text}")
            else:
                self.assertIsNone(match, f"Pattern should not match: {text}")

    def test_command_ref_pattern_boundaries(self):
        """Test command reference pattern respects word boundaries."""
        pattern = ContentTransformer.COMMAND_REF_PATTERN

        # Should match
        self.assertTrue(pattern.search("/analyze the code"))
        self.assertTrue(pattern.search("Use /task for"))
        self.assertTrue(pattern.search("See [/implement]"))

        # Should NOT match
        self.assertFalse(pattern.search("https://example.com/path"))  # URL
        self.assertFalse(pattern.search("file/path/to/file"))  # File path
        self.assertFalse(pattern.search("prefix/command"))  # Part of path


def run_tests():
    """Run all tests."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
