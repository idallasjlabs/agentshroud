#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE="ghcr.io/github/github-mcp-server:latest"
ENVFILE="$SCRIPT_DIR/.env"

# Your server drops messages without pauses when driven via pipes.
SLEEP_INIT="${SLEEP_INIT:-0.25}"
SLEEP_AFTER_INIT="${SLEEP_AFTER_INIT:-0.25}"
SLEEP_AFTER_CALL="${SLEEP_AFTER_CALL:-1.00}"

need() { command -v "$1" >/dev/null 2>&1 || { echo "ERROR: missing: $1" >&2; exit 1; }; }
need docker
need jq
need sed

if [[ ! -f "$ENVFILE" ]]; then
  echo "ERROR: $ENVFILE not found in $(pwd)" >&2
  exit 1
fi

# Optional overrides:
#   REPO_QUERY='org:fluenceenergy archived:false' ./test-github.sh
#   REPO_QUERY='llm_settings in:name' ./test-github.sh
REPO_QUERY="${REPO_QUERY:-}"

say() { printf '%s\n' "$*" >&2; }

run_mcp() {
  docker run -i --rm --env-file "$ENVFILE" "$IMAGE" stdio 2>&1 \
    | tee /tmp/github-mcp-run.log \
    | sed -n '/^[[:space:]]*{/p'
}

mcp_call_tool() {
  # args: <id> <tool_name> <json_arguments_object>
  local id="$1"
  local tool="$2"
  local args_json="$3"

  (
    printf '%s\n' '{"jsonrpc":"2.0","id":0,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{"tools":{}},"clientInfo":{"name":"test-github","version":"1.0"}}}'
    sleep "$SLEEP_INIT"
    printf '%s\n' '{"jsonrpc":"2.0","method":"notifications/initialized","params":{}}'
    sleep "$SLEEP_AFTER_INIT"
    # Important: arguments must be a JSON object, not a string.
    printf '%s\n' "{\"jsonrpc\":\"2.0\",\"id\":${id},\"method\":\"tools/call\",\"params\":{\"name\":\"${tool}\",\"arguments\":${args_json}}}"
    sleep "$SLEEP_AFTER_CALL"
  ) | run_mcp
}

extract_tool_text() {
  # reads a single JSON-RPC response object from stdin
  jq -r '
    if .error then
      "ERROR: \(.error.message) (\(.error.code))"
    else
      (.result.content // [])
      | map(select(.type=="text") | .text)
      | .[0] // ""
    end
  '
}

try_get_login() {
  local resp text
  resp="$(mcp_call_tool 10 get_me '{}' \
    | tee /tmp/github-mcp-getme.log \
    | jq -c 'select(.id==10)' || true)"

  if [[ -z "${resp:-}" ]]; then
    return 1
  fi

  text="$(printf '%s\n' "$resp" | extract_tool_text)"
  if [[ "$text" == ERROR:* || -z "$text" ]]; then
    return 1
  fi

  # expect JSON in text
  printf '%s\n' "$text" | jq -r '.login // .user.login // empty' 2>/dev/null | grep -E '^[A-Za-z0-9_-]+$' || true
}

search_repos() {
  local query="$1"
  local args
  args="$(jq -nc --arg q "$query" '{
    query: $q,
    perPage: 5,
    page: 1,
    minimal_output: false,
    sort: "updated",
    order: "desc"
  }')"

  local resp text
  resp="$(mcp_call_tool 2 search_repositories "$args" \
    | tee /tmp/github-mcp-searchrepos.log \
    | jq -c 'select(.id==2)' || true)"

  if [[ -z "${resp:-}" ]]; then
    echo "ERROR: no response for search_repositories (id=2). See /tmp/github-mcp-searchrepos.log" >&2
    exit 2
  fi

  text="$(printf '%s\n' "$resp" | extract_tool_text)"
  if [[ "$text" == ERROR:* ]]; then
    echo "$text" >&2
    echo "Raw response:" >&2
    printf '%s\n' "$resp" | jq . >&2
    exit 3
  fi

  if ! printf '%s' "$text" | jq -e . >/dev/null 2>&1; then
    echo "Tool output was not JSON. Raw text:" >&2
    printf '%s\n' "$text"
    exit 0
  fi

  # Pretty-print and also show a formatted table (handles {items:[...]} or [...]
  printf '%s' "$text" | jq . | tee /tmp/github-mcp-searchrepos.json >/dev/null

  echo ""
  echo "=== First 5 repos (formatted) ==="
  printf '%s' "$text" | jq -r '
    (if type=="object" and has("items") then .items else . end)
    | (if type=="array" then . else [] end)
    | .[:5]
    | map({
        name: (.full_name // .name // "unknown"),
        private: (.private // false),
        stars: (.stargazers_count // 0),
        updated: (.updated_at // .pushed_at // ""),
        url: (.html_url // "")
      })
    | (["name","private","stars","updated","url"] | @tsv),
      (.[] | [.name, (.private|tostring), (.stars|tostring), .updated, .url] | @tsv)
  ' | column -t -s $'\t'
}

main() {
  echo "Testing GitHub MCP Server..."
  echo ""

  local query="$REPO_QUERY"

  if [[ -z "$query" ]]; then
    say "=== Discovering authenticated user (get_me) ==="
    local login
    login="$(try_get_login || true)"
    if [[ -n "${login:-}" ]]; then
      say "Authenticated as: $login"
      query="user:${login}"
    else
      say "get_me did not return; falling back to a generic query."
      # Generic fallback that still returns something useful:
      # Search for your likely repos by local folder name; change as you like.
      query="llm_settings in:name"
    fi
  else
    say "Using REPO_QUERY override: $query"
  fi

  say ""
  say "=== search_repositories (first 5) ==="
  say "Query: $query"

  search_repos "$query"

  echo ""
  echo "Logs:"
  echo "  get_me:      /tmp/github-mcp-getme.log"
  echo "  search repos:/tmp/github-mcp-searchrepos.log"
  echo "  run log:     /tmp/github-mcp-run.log"
  echo "  json output: /tmp/github-mcp-searchrepos.json"
}

main "$@"
