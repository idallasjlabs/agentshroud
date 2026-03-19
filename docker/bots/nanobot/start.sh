#!/usr/bin/env bash
# NanoBot startup script — adapt entrypoint once integrated.
set -euo pipefail

export AGENTSHROUD_BOT_ID="${AGENTSHROUD_BOT_ID:-nanobot}"
export AGENTSHROUD_WORKSPACE="${AGENTSHROUD_WORKSPACE:-/app/workspace}"

echo "[nanobot] Starting NanoBot on port 8000"
echo "[nanobot] Gateway: ${ANTHROPIC_BASE_URL:-not set}"
echo "[nanobot] Proxy: ${HTTP_PROXY:-not set}"

# Replace with actual NanoBot entry point:
exec python -m nanobot --host 0.0.0.0 --port 8000
