#!/usr/bin/env bash
# Quick GitHub MCP commands

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# JSON escape helper - escapes quotes, backslashes, and newlines
json_escape() {
  printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g; s/$/\\n/g' | tr -d '\n' | sed 's/\\n$//'
}

case "$1" in
  repos)
    "$SCRIPT_DIR/call-tool.sh" list_repositories '{"perPage":20}'
    ;;

  issues)
    if [ -z "$2" ] || [ -z "$3" ]; then
      echo "Usage: ./quick-commands.sh issues <owner> <repo>"
      exit 1
    fi
    owner_escaped=$(json_escape "$2")
    repo_escaped=$(json_escape "$3")
    "$SCRIPT_DIR/call-tool.sh" list_issues "{\"owner\":\"$owner_escaped\",\"repo\":\"$repo_escaped\",\"state\":\"open\"}"
    ;;

  prs)
    if [ -z "$2" ] || [ -z "$3" ]; then
      echo "Usage: ./quick-commands.sh prs <owner> <repo>"
      exit 1
    fi
    owner_escaped=$(json_escape "$2")
    repo_escaped=$(json_escape "$3")
    "$SCRIPT_DIR/call-tool.sh" list_pull_requests "{\"owner\":\"$owner_escaped\",\"repo\":\"$repo_escaped\"}"
    ;;

  search)
    if [ -z "$2" ]; then
      echo "Usage: ./quick-commands.sh search <query>"
      exit 1
    fi
    query_escaped=$(json_escape "$2")
    "$SCRIPT_DIR/call-tool.sh" search_code "{\"query\":\"$query_escaped\",\"perPage\":10}"
    ;;

  file)
    if [ -z "$2" ] || [ -z "$3" ] || [ -z "$4" ]; then
      echo "Usage: ./quick-commands.sh file <owner> <repo> <path>"
      exit 1
    fi
    owner_escaped=$(json_escape "$2")
    repo_escaped=$(json_escape "$3")
    path_escaped=$(json_escape "$4")
    "$SCRIPT_DIR/call-tool.sh" get_file_contents "{\"owner\":\"$owner_escaped\",\"repo\":\"$repo_escaped\",\"path\":\"$path_escaped\"}"
    ;;

  *)
    echo "GitHub MCP Quick Commands"
    echo ""
    echo "Usage: ./quick-commands.sh <command> [args]"
    echo ""
    echo "Commands:"
    echo "  repos                    - List your repositories"
    echo "  issues <owner> <repo>    - List open issues"
    echo "  prs <owner> <repo>       - List pull requests"
    echo "  search <query>           - Search code"
    echo "  file <owner> <repo> <path> - Get file contents"
    echo ""
    echo "Examples:"
    echo "  ./quick-commands.sh repos"
    echo "  ./quick-commands.sh issues FluenceEnergy my-repo"
    echo "  ./quick-commands.sh search 'language:python user:myusername'"
    echo "  ./quick-commands.sh file owner repo README.md"
    ;;
esac
