#!/usr/bin/env bash
# Functional regression test: docker/bots/hermes/init-config.sh's MCP servers.json ->
# config.yaml reconciliation logic.
#
# Root cause this guards against (found 2026-08-01, live incident): the reconciliation
# was purely additive -- it only ever added/refreshed entries that servers.json marked
# enabled: true. It had NO code path to disable an entry already sitting in config.yaml
# from before servers.json was updated to disable it. docker/config/hermes/mcp/
# servers.json disabled "agentshroud-gateway" on 2026-07-18 (its url,
# http://gateway:8080/mcp, returns a genuine 404 -- the gateway has never served that
# endpoint), but the stale enabled:true copy already in the live config.yaml survived
# every boot since, causing ~213 failed MCP connection attempts/day indefinitely.
#
# This test extracts the actual embedded Python reconciliation logic from
# init-config.sh (not a reimplementation -- the real code under test) and runs it
# against fixture data, asserting: a stale enabled:true entry gets disabled when the
# source marks it enabled:false; re-running is idempotent; a fresh install with no
# mcp_servers key never picks up a disabled entry.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INIT_SCRIPT="$REPO/docker/bots/hermes/init-config.sh"
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

fail=0
check() {
    local label="$1" condition="$2"
    if [[ "$condition" == "true" ]]; then
        echo "  OK : $label"
    else
        echo "  FAIL: $label" >&2
        fail=1
    fi
}

# Extract the embedded Python heredoc verbatim -- testing the REAL code, not a copy.
awk '/^import json, os, re, sys$/,/^PYEOF$/' "$INIT_SCRIPT" | sed '$d' > "$WORKDIR/reconcile.py"

if [[ ! -s "$WORKDIR/reconcile.py" ]]; then
    echo "  FAIL: could not extract reconciliation Python from $INIT_SCRIPT (heredoc markers changed?)" >&2
    exit 1
fi

cat > "$WORKDIR/servers.json" <<'EOF'
{
  "servers": {
    "agentshroud-gateway": {
      "description": "disabled - gateway never served this endpoint",
      "type": "http",
      "url": "http://gateway:8080/mcp",
      "enabled": false
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp",
      "enabled": true
    }
  }
}
EOF

echo ""
echo "── Hermes MCP reconciliation: stale-disable regression ────────────────"

# Scenario 1: config.yaml has a STALE enabled:true copy of a now-disabled server
# (exactly the real incident state). Reconciliation must flip it to false.
cat > "$WORKDIR/config-stale.yaml" <<'EOF'
model:
  default: claude-opus-4-6
mcp_servers:
  agentshroud-gateway:
    url: http://gateway:8080/mcp
    enabled: true
  github:
    url: https://api.githubcopilot.com/mcp
    enabled: true
EOF

out="$(HERMES_MCP_SRC="$WORKDIR/servers.json" HERMES_MCP_CONFIG="$WORKDIR/config-stale.yaml" python3 "$WORKDIR/reconcile.py")"
check "reports the stale entry as changed/disabled" "$([[ "$out" == *"agentshroud-gateway"*"disabled"* ]] && echo true || echo false)"
check "agentshroud-gateway is enabled: false after reconciliation" \
    "$(grep -A2 '^  agentshroud-gateway:' "$WORKDIR/config-stale.yaml" | grep -q 'enabled: [Ff]alse' && echo true || echo false)"
check "github (still enabled upstream) is untouched and still enabled" \
    "$(grep -A2 '^  github:' "$WORKDIR/config-stale.yaml" | grep -q 'enabled: [Tt]rue' && echo true || echo false)"

# Scenario 2: idempotency -- re-running against the now-fixed config must be a no-op.
out2="$(HERMES_MCP_SRC="$WORKDIR/servers.json" HERMES_MCP_CONFIG="$WORKDIR/config-stale.yaml" python3 "$WORKDIR/reconcile.py")"
check "re-run is idempotent (UNCHANGED)" "$([[ "$out2" == "UNCHANGED" ]] && echo true || echo false)"

# Scenario 3: fresh install (no mcp_servers key at all) must never add the disabled
# entry in the first place.
cat > "$WORKDIR/config-fresh.yaml" <<'EOF'
model:
  default: claude-opus-4-6
EOF
HERMES_MCP_SRC="$WORKDIR/servers.json" HERMES_MCP_CONFIG="$WORKDIR/config-fresh.yaml" python3 "$WORKDIR/reconcile.py" >/dev/null
check "fresh install adds github" \
    "$(grep -q 'github:' "$WORKDIR/config-fresh.yaml" && echo true || echo false)"
check "fresh install never adds the disabled agentshroud-gateway entry" \
    "$(! grep -q 'agentshroud-gateway' "$WORKDIR/config-fresh.yaml" && echo true || echo false)"

echo ""
if [[ "$fail" -eq 0 ]]; then
    echo "  ALL CHECKS PASSED"
    exit 0
else
    echo "  ONE OR MORE CHECKS FAILED" >&2
    exit 1
fi
