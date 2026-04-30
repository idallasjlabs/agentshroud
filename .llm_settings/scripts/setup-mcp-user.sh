#!/usr/bin/env bash
# setup-mcp-user.sh - Configure MCP servers at user level
# Run once to make MCP servers available in all projects via `claude mcp list`
#
# This configures ~/.claude/settings.json with MCP servers that work globally

set -e

echo "🔌 Configuring MCP servers at user level..."
echo "   Config file: ~/.claude/settings.json"
echo ""

# Get absolute path to LLM_Settings directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LLM_SETTINGS_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# GitHub MCP (stdio via wrapper script - requires absolute path)
GITHUB_WRAPPER="$LLM_SETTINGS_ROOT/.llm_settings/mcp-servers/github/github-mcp-wrapper.sh"
echo "1️⃣  Adding GitHub MCP (stdio)..."
if [[ -f "$GITHUB_WRAPPER" ]]; then
  claude mcp add --transport stdio github "$GITHUB_WRAPPER" --scope user 2>/dev/null \
    && echo "   ✅ GitHub MCP added" \
    || echo "   ⚠️  GitHub MCP already exists or failed"
else
  echo "   ❌ Wrapper not found: $GITHUB_WRAPPER"
fi

# Atlassian MCP (HTTP transport - uses OAuth)
echo "2️⃣  Adding Atlassian MCP (http)..."
claude mcp add --transport http atlassian https://mcp.atlassian.com/v1/mcp --scope user 2>/dev/null \
  && echo "   ✅ Atlassian MCP added" \
  || echo "   ⚠️  Atlassian MCP already exists or failed"

# AWS MCP (stdio via uvx)
echo "3️⃣  Adding AWS API MCP (stdio)..."
UVX_PATH="$(command -v uvx 2>/dev/null \
    || ([ -f "$HOME/.cargo/bin/uvx" ]  && echo "$HOME/.cargo/bin/uvx") \
    || ([ -f "$HOME/.local/bin/uvx" ]  && echo "$HOME/.local/bin/uvx") \
    || echo '/opt/homebrew/bin/uvx')"
claude mcp add --transport stdio awslabs.aws-api-mcp-server "$UVX_PATH" \
  --args "awslabs.aws-api-mcp-server@latest" \
  --args "--readonly" \
  --scope user 2>/dev/null \
  && echo "   ✅ AWS MCP added" \
  || echo "   ⚠️  AWS MCP already exists or failed"

echo ""
echo "✅ Done! Your MCP servers are now configured globally."
echo ""
echo "Verify with:"
echo "  claude mcp list"
echo ""
echo "These servers will now work in any directory, not just in LLM_Settings."
