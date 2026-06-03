#!/usr/bin/env bash
# Smoke test: Hermes agentshroud-secrets.sh chown coverage.
# Verifies that the chown block covers auth.json, mcp.json, .local, .cache,
# and cron — preventing EACCES on token refresh and MCP config reads.
# Run as part of scripts/smoke.sh.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
fail=0

check() {
    local label="$1" file="$2" pattern="$3"
    if /usr/bin/grep -q "$pattern" "$REPO/$file" 2>/dev/null; then
        echo "  OK : $label"
    else
        echo "  FAIL: $label — pattern '$pattern' not found in $file" >&2
        fail=1
    fi
}

echo ""
echo "── Hermes secrets chown assertions ────────────────────"

check "agentshroud-secrets.sh: chown covers auth.json" \
    "docker/bots/hermes/agentshroud-secrets.sh" "auth\.json"

check "agentshroud-secrets.sh: chown covers mcp.json" \
    "docker/bots/hermes/agentshroud-secrets.sh" "mcp\.json"

check "agentshroud-secrets.sh: chown covers .local" \
    "docker/bots/hermes/agentshroud-secrets.sh" "\.local"

check "agentshroud-secrets.sh: chown covers .cache" \
    "docker/bots/hermes/agentshroud-secrets.sh" "\.cache"

check "agentshroud-secrets.sh: chown covers cron" \
    "docker/bots/hermes/agentshroud-secrets.sh" "cron"

check "agentshroud-secrets.sh: chown target uid is 10000" \
    "docker/bots/hermes/agentshroud-secrets.sh" "10000:10000"

echo ""
if [[ "$fail" -eq 0 ]]; then
    echo "  ALL CHECKS PASSED"
    exit 0
else
    echo "  ONE OR MORE CHECKS FAILED" >&2
    exit 1
fi
