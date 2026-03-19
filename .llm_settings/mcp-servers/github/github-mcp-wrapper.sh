#!/usr/bin/env bash
# Wrapper for Claude Code to communicate with GitHub MCP server

# Get script directory for relative paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Run the official GitHub MCP server image with stdio
exec docker run -i --rm --env-file "$SCRIPT_DIR/.env" ghcr.io/github/github-mcp-server:latest
