#!/bin/sh
# Patch @slack/socket-mode SDK to demote transient-disconnect noise to debug level.
# These messages are harmless (VPN reconnects / DNS hiccups) and flood bot logs,
# making it hard to spot actionable messages.
#
# OpenClaw ≥2026.6.9 no longer ships @slack/socket-mode as a separate npm package;
# the pong-timeout noise was eliminated upstream. This script checks both the legacy
# npm path and any dist-bundled copy so it works across versions without warnings.

_PONG_PATCH='
const fs = require("fs");
const p = process.argv[1];
let c = fs.readFileSync(p, "utf8");
let changed = false;

// Patch 1: Demote pong timeout warning to debug.
if (c.includes("this.logger.debug(`A pong wasn'\''t received")) {
    console.log("patch-slack-sdk: pong timeout already patched (" + p + ")");
} else if (c.includes("this.logger.warn(`A pong wasn'\''t received")) {
    c = c.replace(
        /this\.logger\.warn\(`A pong wasn'\''t received/g,
        "this.logger.debug(`A pong wasn'\''t received"
    );
    changed = true;
    console.log("patch-slack-sdk: pong timeout warn -> debug (" + p + ")");
} else {
    console.log("patch-slack-sdk: pattern not found — skipped, continuing (" + p + ")");
}

// Patch 2: Demote reconnect retry warn/error to debug.
const before = c;
c = c.replace(
    /this\.logger\.(warn|error)\(([^;]*?[Rr]etr[yi][^;]*?)\);/g,
    "this.logger.debug($2);"
);
if (c !== before) { changed = true; }

if (changed) fs.writeFileSync(p, c);
'

_patched=0

# --- Path 1: legacy separate npm package (OpenClaw < 2026.6.9) ---
_SDK_PATH="$(npm root -g)/openclaw/node_modules/@slack/socket-mode/dist/src/SlackWebSocket.js"
if [ -f "$_SDK_PATH" ]; then
    node -e "$_PONG_PATCH" "$_SDK_PATH"
    _patched=1
fi

# --- Path 2: bundled in dist (future versions that inline socket-mode) ---
_DIST_DIR="$(npm root -g)/openclaw/dist"
if [ -d "$_DIST_DIR" ]; then
    _dist_hit=$(grep -rl "A pong wasn't received" "$_DIST_DIR" 2>/dev/null || true)
    if [ -n "$_dist_hit" ]; then
        for _f in $_dist_hit; do
            node -e "$_PONG_PATCH" "$_f"
        done
        _patched=1
    fi
fi

if [ "$_patched" -eq 0 ]; then
    echo "patch-slack-sdk: pong noise patch not applicable in this OpenClaw version (already fixed upstream)"
fi
