#!/usr/bin/env bash
# promote-firmware.sh — Deliberate gate between "firmware builds" and "firmware
# ships to the live ESP32 over OTA."
#
# Incident (2026-07-27): the voice-gateway container bind-mounted
# firmware/voice-terminal/build/ directly and served whatever was in it as the
# OTA payload. That meant a single `idf.py build` on a dev machine became what
# the one physical production device downloaded on its next OTA check — no
# review, no staging, no verification step. A one-line sdkconfig change (never
# boot-tested on real hardware) went straight to OTA, crashed on boot, and the
# device could not self-heal because its own OTA-check endpoint was the thing
# that broke.
#
# This script is the fix: it is the ONLY way a build becomes OTA-servable.
# docker-compose.yml now mounts ota-release/, not build/, into the container.
#
# Usage:
#   scripts/promote-firmware.sh
#
# Requires interactive confirmation that the candidate binary has been
# boot-tested over a real USB serial connection on real hardware. There is no
# --yes / non-interactive bypass for this gate — that is intentional.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FW_DIR="$REPO_DIR/firmware/voice-terminal"
BUILD_BIN="$FW_DIR/build/voice_terminal.bin"
RELEASE_DIR="$FW_DIR/ota-release"
RELEASE_BIN="$RELEASE_DIR/voice_terminal.bin"
RELEASE_META="$RELEASE_DIR/voice_terminal.bin.meta"

if [ ! -f "$BUILD_BIN" ]; then
    echo "ERROR: $BUILD_BIN not found. Run 'idf.py build' first." >&2
    exit 1
fi

echo "==> Candidate firmware: $BUILD_BIN"
echo "    Size: $(stat -f%z "$BUILD_BIN" 2>/dev/null || stat -c%s "$BUILD_BIN") bytes"
echo "    sdkconfig CONFIG_VT_VG_WS_URL: $(grep '^CONFIG_VT_VG_WS_URL=' "$FW_DIR/sdkconfig" || echo '(not set)')"
echo ""
echo "This binary will become what the live ESP32 downloads on its next OTA"
echo "check. Before promoting, confirm ALL of the following on real hardware"
echo "over a physical USB serial connection (idf.py -p PORT flash monitor, or"
echo "python -m serial.tools.miniterm PORT 115200):"
echo ""
echo "  1. Device boots cleanly — no crash, no boot loop, no watchdog reset."
echo "  2. WiFi connects successfully."
echo "  3. It reaches 'esp_ota_mark_app_valid_cancel_rollback' (logged) —"
echo "     i.e. it did NOT get stuck before this point."
echo "  4. The voice WebSocket actually connects end-to-end (not just boots)."
echo "  5. A real voice interaction round-trips successfully."
echo ""
echo "If ANY of these were not verified on real hardware, abort now and do not"
echo "promote — an OTA push is not a substitute for this. There is currently"
echo "only one physical device; a bad promotion strands it, exactly as"
echo "happened on 2026-07-27."
echo ""
read -r -p "Type 'VERIFIED' to confirm all five checks passed on real hardware: " CONFIRM
if [ "$CONFIRM" != "VERIFIED" ]; then
    echo "Aborted. Nothing was promoted."
    exit 1
fi

mkdir -p "$RELEASE_DIR"
cp "$BUILD_BIN" "$RELEASE_BIN"

{
    echo "promoted_at_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "promoted_by=$(whoami)"
    echo "git_commit=$(git -C "$REPO_DIR" rev-parse HEAD 2>/dev/null || echo 'unknown')"
    echo "git_dirty=$(git -C "$REPO_DIR" status --porcelain firmware/voice-terminal 2>/dev/null | wc -l | tr -d ' ')"
    echo "ws_url=$(grep '^CONFIG_VT_VG_WS_URL=' "$FW_DIR/sdkconfig" || echo 'unknown')"
    echo "sha256=$(shasum -a 256 "$RELEASE_BIN" | awk '{print $1}')"
} > "$RELEASE_META"

echo ""
echo "==> Promoted. $RELEASE_BIN is now the OTA payload the voice-gateway"
echo "    container serves at /firmware/bin. Metadata: $RELEASE_META"
echo ""
echo "If the voice-gateway container is already running, no restart is"
echo "needed — it re-hashes the file lazily on the next /firmware/bin request."
