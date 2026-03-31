#!/usr/bin/env bash
set -euo pipefail

# Suppress Node deprecation warnings (punycode, etc.)
export NODE_OPTIONS="--no-deprecation ${NODE_OPTIONS:-}"

# Source nvm if npx is not in PATH (common on Linux with nvm-managed Node)
if ! command -v npx &>/dev/null; then
    [ -s "$HOME/.nvm/nvm.sh" ]         && . "$HOME/.nvm/nvm.sh" --no-use
    [ -s "/usr/local/nvm/nvm.sh" ]     && . "/usr/local/nvm/nvm.sh" --no-use
    [ -s "/usr/share/nvm/init-nvm.sh" ] && . "/usr/share/nvm/init-nvm.sh"
fi

# Run Atlassian mcp-remote as an MCP stdio server
exec npx -y mcp-remote https://mcp.atlassian.com/v1/mcp
