#!/bin/sh
# Patch @slack/socket-mode SDK to demote pong timeout warnings to debug level.
# These warnings are harmless (network hiccups / VPN reconnects) and flood bot
# logs, making it hard to spot actionable messages. Only the pong timeout line
# is demoted — all other Slack SDK warnings remain at warn level.
SDK_PATH="$(npm root -g)/openclaw/node_modules/@slack/socket-mode/dist/src/SlackWebSocket.js"
if [ -f "$SDK_PATH" ]; then
    node -e "
const fs = require('fs');
const p = process.argv[1];
let c = fs.readFileSync(p, 'utf8');
// Match: this.logger.warn(\`A pong wasn't received from the server before...
if (c.includes(\"this.logger.warn(\\\`A pong wasn't received\")) {
    c = c.replace(
        /this\.logger\.warn\(\`A pong wasn't received/g,
        \"this.logger.debug(\\\`A pong wasn't received\"
    );
    fs.writeFileSync(p, c);
    console.log('patch-slack-sdk: pong timeout warn -> debug (applied)');
} else {
    console.log('patch-slack-sdk: pong warning pattern not found — skipped (SDK may have changed)');
}
" "$SDK_PATH"
else
    echo "patch-slack-sdk: WARNING: @slack/socket-mode SDK not found at $SDK_PATH — skipped"
fi
