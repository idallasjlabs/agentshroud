#!/usr/bin/env bash
# Helper script to call MCP GitHub tools

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE="ghcr.io/github/github-mcp-server:latest"

TOOL_NAME=$1
shift
ARGS_JSON=${1:-"{}"}

if [ -z "$TOOL_NAME" ]; then
  echo "Usage: ./call-tool.sh <tool_name> [json_args]"
  echo ""
  echo "Available tools:"
  echo "  list_repositories      - List your repos"
  echo "  get_repository         - Get repo details"
  echo "  list_issues            - List issues in a repo"
  echo "  create_issue           - Create a new issue"
  echo "  get_file_contents      - Read a file from repo"
  echo "  create_or_update_file  - Write/update a file"
  echo "  list_pull_requests     - List PRs"
  echo "  search_code            - Search across repos"
  echo ""
  echo "Examples:"
  echo '  ./call-tool.sh list_repositories '"'"'{"perPage":5}'"'"
  echo '  ./call-tool.sh get_repository '"'"'{"owner":"username","repo":"reponame"}'"'"
  exit 1
fi

echo "Calling $TOOL_NAME..."

# Send properly paced MCP protocol sequence
{
  printf '%s\n' '{"jsonrpc":"2.0","id":0,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"cli-test","version":"1.0.0"}}}'
  sleep 0.2
  printf '%s\n' '{"jsonrpc":"2.0","method":"notifications/initialized","params":{}}'
  sleep 0.2
  printf '%s\n' "{\"jsonrpc\":\"2.0\",\"id\":1,\"method\":\"tools/call\",\"params\":{\"name\":\"$TOOL_NAME\",\"arguments\":$ARGS_JSON}}"
  sleep 0.5
} | docker run -i --rm --env-file "$SCRIPT_DIR/.env" "$IMAGE" 2>/dev/null \
  | grep '{"jsonrpc"' \
  | jq -r 'select(.id==1) | .result.content[0].text' 2>/dev/null \
  | jq . 2>/dev/null
