#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE="ghcr.io/github/github-mcp-server:latest"

echo "Testing MCP GitHub Server..."
echo

# Use a paced writer so the server sees messages before stdin closes.
{
  printf '%s\n' '{"jsonrpc":"2.0","id":0,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test-client","version":"1.0.0"}}}'
  sleep 0.2
  printf '%s\n' '{"jsonrpc":"2.0","method":"notifications/initialized","params":{}}'
  sleep 0.2
  printf '%s\n' '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
  sleep 0.2
  printf '%s\n' '{"jsonrpc":"2.0","id":2,"method":"shutdown","params":{}}'
  sleep 0.2
  printf '%s\n' '{"jsonrpc":"2.0","method":"exit","params":{}}'
  # Keep stdin open just a moment so responses can flush before EOF.
  sleep 0.5
} | docker run -i --rm --env-file "$SCRIPT_DIR/.env" "$IMAGE" stdio \
  | jq -r '
      if .error then
        "ERROR id=\(.id // "null"): \(.error.message) (\(.error.code))"
      elif .id == 1 then
        .result.tools[]? | "\(.name)\t\(.description)"
      else empty end
    '

echo
echo "✓ MCP tools/list succeeded"
