#!/usr/bin/env bash
# Smoke test: OpenClaw + Hermes startup photo — static assertions only.
# Verifies that both bots have the _telegram_send_photo helper wired and
# that the logo COPY exists in each Dockerfile. Run as part of scripts/smoke.sh.
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
echo "── OpenClaw startup photo assertions ──────────────────"

check "openclaw start.sh: _telegram_send_photo helper defined" \
    "docker/bots/openclaw/start.sh" "_telegram_send_photo()"

check "openclaw start.sh: _telegram_send_photo called with AgentShroud™ caption" \
    "docker/bots/openclaw/start.sh" "_telegram_send_photo.*AgentShroud"

check "openclaw Dockerfile: logo.png COPY" \
    "docker/bots/openclaw/Dockerfile" "COPY branding/logos/png/logo.png"

echo ""
echo "── Hermes startup photo assertions ────────────────────"

check "hermes start.sh: _telegram_send_photo helper defined" \
    "docker/bots/hermes/start.sh" "_telegram_send_photo()"

check "hermes start.sh: _telegram_send_photo called at startup" \
    "docker/bots/hermes/start.sh" "_telegram_send_photo"

check "hermes Dockerfile: logo.png COPY" \
    "docker/bots/hermes/Dockerfile" "logo.png"

echo ""
echo "── Collaborator greeter assertions ────────────────────"

check "branding/taglines.json exists and has content" \
    "branding/taglines.json" "agent"

check "gateway Dockerfile: taglines.json COPY" \
    "gateway/Dockerfile" "taglines.json"

check "collaborator_greeter.py: CollaboratorGreeter class" \
    "gateway/proxy/collaborator_greeter.py" "class CollaboratorGreeter"

check "telegram_proxy.py: greeter hook wired" \
    "gateway/proxy/telegram_proxy.py" "_collab_greeter"

echo ""
if [[ "$fail" -eq 0 ]]; then
    echo "  ALL CHECKS PASSED"
    exit 0
else
    echo "  ONE OR MORE CHECKS FAILED" >&2
    exit 1
fi
