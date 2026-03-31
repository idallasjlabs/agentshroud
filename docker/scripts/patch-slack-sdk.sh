#!/bin/sh
# Patch @slack/socket-mode SDK to demote transient-disconnect noise to debug level.
# These messages are harmless (VPN reconnects / DNS hiccups) and flood bot logs,
# making it hard to spot actionable messages.
SDK_PATH="$(npm root -g)/openclaw/node_modules/@slack/socket-mode/dist/src/SlackWebSocket.js"
if [ -f "$SDK_PATH" ]; then
    node -e "
const fs = require('fs');
const p = process.argv[1];
let c = fs.readFileSync(p, 'utf8');
let changed = false;

// Patch 1: Demote pong timeout warning to debug.
// 'A pong wasn't received from the server before...' floods logs on VPN reconnects.
if (c.includes(\"this.logger.warn(\\\`A pong wasn't received\")) {
    c = c.replace(
        /this\.logger\.warn\(\`A pong wasn't received/g,
        \"this.logger.debug(\\\`A pong wasn't received\"
    );
    changed = true;
    console.log('patch-slack-sdk: pong timeout warn -> debug (applied)');
} else {
    console.log('patch-slack-sdk: pong warning pattern not found — skipped (SDK may have changed)');
}

// Patch 2: Demote reconnect retry warn/error to debug.
// Transient disconnects produce WARN + ERROR + INFO triplets; demote all retry lines.
c = c.replace(
    /this\.logger\.(warn|error)\(([^;]*?[Rr]etr[yi][^;]*?)\);/g,
    'this.logger.debug(\$2);'
);
if (c !== fs.readFileSync(p, 'utf8')) { changed = true; }
console.log('patch-slack-sdk: retry warn/error -> debug (applied)');

if (changed) fs.writeFileSync(p, c);
" "$SDK_PATH"
else
    echo "patch-slack-sdk: WARNING: @slack/socket-mode SDK not found at $SDK_PATH — skipped"
fi
