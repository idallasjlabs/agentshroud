#!/usr/bin/env bash
set -euo pipefail

# Suppress Node deprecation warnings (punycode, etc.)
export NODE_OPTIONS="--no-deprecation ${NODE_OPTIONS:-}"

# Run Atlassian mcp-remote as an MCP stdio server
exec npx -y mcp-remote https://mcp.atlassian.com/v1/mcp
