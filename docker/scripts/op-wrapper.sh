#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# Wrapper script for 1Password CLI that handles authentication
# Usage: op-wrapper.sh <op command arguments>
#
# P2 — Credential isolation:
#   If GATEWAY_OP_PROXY_URL and GATEWAY_AUTH_TOKEN are set, routes
#   "op read" calls through the gateway /credentials/op-proxy endpoint
#   instead of calling 1Password directly. This moves credential
#   ownership to the gateway (activated in the FINAL PR).
#
#   Until FINAL, GATEWAY_OP_PROXY_URL is unset and the script falls
#   through to the original direct 1Password authentication below.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# P2: Route through gateway op-proxy if configured
if [ -n "${GATEWAY_OP_PROXY_URL:-}" ] && [ -n "${GATEWAY_AUTH_TOKEN:-}" ]; then
    if [ "${1:-}" = "read" ] && [ -n "${2:-}" ]; then
        reference="$2"
        # Escape reference for JSON (basic — reference should be alphanumeric/slash)
        json_ref=$(printf '%s' "$reference" | sed 's/\\/\\\\/g; s/"/\\"/g')
        response=$(curl -sf \
            -H "Authorization: Bearer ${GATEWAY_AUTH_TOKEN}" \
            -H "Content-Type: application/json" \
            -X POST "${GATEWAY_OP_PROXY_URL}/credentials/op-proxy" \
            -d "{\"reference\":\"${json_ref}\"}" 2>/dev/null) || true
        if [ -n "$response" ]; then
            # Extract .value from JSON response (use node since python3 may not be present)
            printf '%s' "$response" | node -e \
                "let d=''; process.stdin.on('data',c=>d+=c); process.stdin.on('end',()=>process.stdout.write(JSON.parse(d).value))"
            exit 0
        fi
        echo "[op-wrapper] ERROR: Gateway op-proxy request failed" >&2
        exit 1
    fi
fi

# Fall through: direct 1Password authentication (original behavior)
# shellcheck source=op-auth-common.sh
source "$SCRIPT_DIR/op-auth-common.sh"

if op_authenticate; then
    op --session "$OP_SESSION" "$@"
else
    echo "[ERROR] Failed to sign in to 1Password" >&2
    exit 1
fi
