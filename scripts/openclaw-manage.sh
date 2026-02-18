#!/usr/bin/env zsh
# OneClaw Version Manager CLI
# Usage: openclaw-manage.sh <command> [options]

set -euo pipefail

GATEWAY_URL="${GATEWAY_URL:-http://localhost:8080}"
AUTH_TOKEN="${GATEWAY_AUTH_TOKEN:-}"

usage() {
    cat <<EOF
OneClaw Version Manager

Usage: $(basename "$0") <command> [options]

Commands:
  check                     Show current installed version
  list                      List version history
  available                 List available versions
  review <version>          Run security review for a version
  upgrade <version>         Upgrade to target version (requires approval)
  downgrade <version>       Downgrade to target version (requires approval)
  rollback                  Rollback to previous version (requires approval)

Options:
  --dry-run                 Preview without executing
  --approval-id <id>        Approval queue ID (required for mutations)
  --gateway-url <url>       Gateway URL (default: http://localhost:8080)

Environment:
  GATEWAY_URL               Gateway base URL
  GATEWAY_AUTH_TOKEN        Authentication token

EOF
    exit 1
}

api_call() {
    local method="$1"
    local path="$2"
    local data="${3:-}"

    local args=(-s -w "\n%{http_code}" -H "Content-Type: application/json")
    if [[ -n "$AUTH_TOKEN" ]]; then
        args+=(-H "Authorization: Bearer $AUTH_TOKEN")
    fi

    if [[ "$method" == "POST" && -n "$data" ]]; then
        args+=(-X POST -d "$data")
    fi

    local response
    response=$(curl "${args[@]}" "${GATEWAY_URL}${path}")

    local http_code
    http_code=$(echo "$response" | tail -1)
    local body
    body=$(echo "$response" | sed '$d')

    if [[ "$http_code" -ge 400 ]]; then
        echo "Error ($http_code): $body" >&2
        exit 1
    fi

    echo "$body" | python3 -m json.tool 2>/dev/null || echo "$body"
}

# Parse global options
DRY_RUN=false
APPROVAL_ID=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=true; shift ;;
        --approval-id) APPROVAL_ID="$2"; shift 2 ;;
        --gateway-url) GATEWAY_URL="$2"; shift 2 ;;
        check|list|available|review|upgrade|downgrade|rollback)
            COMMAND="$1"; shift; break ;;
        -h|--help) usage ;;
        *) echo "Unknown option: $1" >&2; usage ;;
    esac
done

# Handle remaining args (version for some commands)
VERSION="${1:-}"

case "${COMMAND:-}" in
    check)
        api_call GET "/api/v1/versions/current"
        ;;
    list)
        api_call GET "/api/v1/versions/history"
        ;;
    available)
        api_call GET "/api/v1/versions/available"
        ;;
    review)
        [[ -z "$VERSION" ]] && { echo "Usage: $(basename "$0") review <version>" >&2; exit 1; }
        api_call POST "/api/v1/versions/review" "{\"target_version\": \"$VERSION\"}"
        ;;
    upgrade)
        [[ -z "$VERSION" ]] && { echo "Usage: $(basename "$0") upgrade <version>" >&2; exit 1; }
        api_call POST "/api/v1/versions/upgrade" \
            "{\"target_version\": \"$VERSION\", \"dry_run\": $DRY_RUN, \"approval_id\": $([ -n "$APPROVAL_ID" ] && echo "\"$APPROVAL_ID\"" || echo null)}"
        ;;
    downgrade)
        [[ -z "$VERSION" ]] && { echo "Usage: $(basename "$0") downgrade <version>" >&2; exit 1; }
        api_call POST "/api/v1/versions/downgrade" \
            "{\"target_version\": \"$VERSION\", \"dry_run\": $DRY_RUN, \"approval_id\": $([ -n "$APPROVAL_ID" ] && echo "\"$APPROVAL_ID\"" || echo null)}"
        ;;
    rollback)
        [[ -z "$APPROVAL_ID" ]] && { echo "Error: --approval-id required for rollback" >&2; exit 1; }
        api_call POST "/api/v1/versions/rollback" "{\"approval_id\": \"$APPROVAL_ID\"}"
        ;;
    *)
        usage
        ;;
esac
