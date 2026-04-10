#!/usr/bin/env bash
# tests/startup_smoke/test_bot_boot_static.sh
#
# Static (no Docker required) assertions on the key assembly files.
# Each assertion catches a specific bug from the 2026-04-10 session.
# Runs in seconds; safe for all CI runners.
#
# Assertions:
#   S1. start-agentshroud.sh uses --stack-size=65536 (ARM64 V8 stack fix)
#   S2. apply-patches.js sets channels.telegram.apiRoot (photo download fix)
#   S3. apply-patches.js validates xoxb-/xapp- prefixes (Slack crash-loop fix)
#   S4. apply-patches.js primary file is the one COPY'd by Dockerfile
#   S5. docker-compose.yml does NOT bind to 0.0.0.0 on sensitive ports
#   S6. setup-secrets.sh routes display output to /dev/tty (garbled secret fix)
#
# Run: bash tests/startup_smoke/test_bot_boot_static.sh
# Exit 0 = pass. Exit 1 = fail.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/../.." && pwd)"

pass=0
fail=0

check() {
    local name="$1" condition="$2" detail="${3:-}"
    if [[ "$condition" == "true" ]]; then
        echo "  PASS: $name"
        (( pass++ )) || true
    else
        echo "  FAIL: $name${detail:+ ($detail)}"
        (( fail++ )) || true
    fi
}

echo ""
echo "=== test_bot_boot_static.sh ==="
echo ""

# S1: --stack-size=65536 is in the openclaw launch command
start_sh="$REPO/docker/scripts/start-agentshroud.sh"
check "S1: start-agentshroud.sh: --stack-size=65536 present" \
    "$(grep -q -- '--stack-size=65536' "$start_sh" && echo true || echo false)" \
    "ARM64 V8 stack overflow fix missing"

# S2: apply-patches.js sets channels.telegram.apiRoot
apply_js="$REPO/docker/config/openclaw/apply-patches.js"
check "S2: apply-patches.js: channels.telegram.apiRoot assignment present" \
    "$(grep -q 'channels\.telegram\.apiRoot' "$apply_js" && echo true || echo false)" \
    "Telegram photo download via proxy requires apiRoot to be set"

# S3: apply-patches.js validates xoxb-/xapp- prefix before activating Slack
check "S3: apply-patches.js: Slack token format validation (startsWith) present" \
    "$(grep -q "startsWith('xoxb-')" "$apply_js" && grep -q "startsWith('xapp-')" "$apply_js" && echo true || echo false)" \
    "Missing token format guard — empty/invalid tokens cause invalid_auth crash loop"

# S4: The Dockerfile COPYs from docker/config/openclaw/, not docker/bots/openclaw/config/
dockerfile="$REPO/docker/bots/openclaw/Dockerfile"
if [[ ! -f "$dockerfile" ]]; then
    dockerfile="$REPO/docker/Dockerfile.openclaw"
fi
if [[ -f "$dockerfile" ]]; then
    # Should COPY from docker/config/openclaw/ (the primary file)
    check "S4: Dockerfile does not COPY from stale docker/bots/openclaw/config/ path" \
        "$(grep -v '^#' "$dockerfile" | grep -q 'COPY.*docker/config/openclaw' && echo true || echo false)" \
        "Dockerfile should COPY from docker/config/openclaw/"
else
    echo "  SKIP: S4 — Dockerfile not found at expected paths"
fi

# S5: docker-compose.yml does not expose gateway on 0.0.0.0
compose="$REPO/docker/docker-compose.yml"
check "S5: docker-compose.yml: no 0.0.0.0 binding on port 8080" \
    "$(! grep -qE '"0\.0\.0\.0:8080|^[[:space:]]*- 0\.0\.0\.0:8080' "$compose" && echo true || echo false)" \
    "Gateway must only bind to 127.0.0.1:8080, not 0.0.0.0"

# S6: setup-secrets.sh routes display output to /dev/tty in read_secret_masked
secrets_sh="$REPO/docker/setup-secrets.sh"
check "S6: setup-secrets.sh: read_secret_masked routes display to /dev/tty" \
    "$(grep -q '> /dev/tty' "$secrets_sh" && echo true || echo false)" \
    "Display output on stdout corrupts captured secret value (garbled token bug)"

# S7: apply-patches.js removes stale channels.slack block when tokens are absent
# Prevents invalid_auth crash loop when config volume has Slack block from a previous run.
check "S7: apply-patches.js: stale channels.slack block removed when no tokens" \
    "$(grep -q 'delete config.channels.slack' "$apply_js" && echo true || echo false)" \
    "Stale Slack block not removed — causes invalid_auth crash loop on restart"

# ── Summary ────────────────────────────────────────────────────────────────
echo ""
total=$(( pass + fail ))
echo "${total} assertions: ${pass} passed, ${fail} failed"
echo ""

[[ "$fail" -eq 0 ]]
