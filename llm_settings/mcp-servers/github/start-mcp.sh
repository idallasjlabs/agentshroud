#!/usr/bin/env bash
# Start GitHub MCP Server

# Get script directory for relative paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Starting GitHub MCP Server..."

# Stop existing container if running
docker stop github-mcp-persistent 2>/dev/null
docker rm github-mcp-persistent 2>/dev/null

# Start new container
docker run -d \
  --name github-mcp-persistent \
  --restart unless-stopped \
  -i \
  --env-file "$SCRIPT_DIR/.env" \
  ghcr.io/github/github-mcp-server:latest

if [ $? -eq 0 ]; then
  echo "✓ GitHub MCP Server started successfully"
  docker ps | grep github-mcp-persistent
else
  echo "✗ Failed to start GitHub MCP Server"
  exit 1
fi
