#!/bin/sh
# Patch grammY SDK to route Telegram API through TELEGRAM_API_BASE_URL
SDK_PATH="$(npm root -g)/openclaw/node_modules/grammy/out/core/client.js"
if [ -f "$SDK_PATH" ]; then
    node -e "
const fs = require('fs');
const p = process.argv[1];
let c = fs.readFileSync(p, 'utf8');
const old1 = 'const apiRoot = (_a = options.apiRoot) !== null && _a !== void 0 ? _a : \"https://api.telegram.org\"';
const new1 = 'const apiRoot = process.env.TELEGRAM_API_BASE_URL || ((_a = options.apiRoot) !== null && _a !== void 0 ? _a : \"https://api.telegram.org\")';
if (c.includes(old1)) {
    c = c.replace(old1, new1);
    console.log('Patch applied: grammY apiRoot env override');
}
fs.writeFileSync(p, c);
console.log('grammY SDK patched successfully');
" "$SDK_PATH"
else
    echo "WARNING: grammY SDK not found at $SDK_PATH"
fi

# Patch OpenClaw dist: ALL hardcoded api.telegram.org URLs must route through gateway.
# Node.js native fetch() does not respect HTTPS_PROXY, so any hardcoded
# https://api.telegram.org URL bypasses the Slack bridge intercept and is blocked
# by CONNECT_FORCE_BLOCK_DOMAINS. This patch rewrites every occurrence.
OPENCLAW_DIST="$(npm root -g)/openclaw/dist"
if [ -d "$OPENCLAW_DIST" ]; then
    node -e "
const fs = require('fs');
const path = require('path');
const dir = process.argv[1];
const BASE_ENV = 'process.env.TELEGRAM_API_BASE_URL';
const FALLBACK = '\"https://api.telegram.org\"';

// Pattern replacements: ordered most-specific to least-specific to avoid double-patching
const patterns = [
    // File download URL (separate from apiRoot)
    {
        old: 'https://api.telegram.org/file/bot\${params.token}/\${params.filePath}',
        rep: '\${' + BASE_ENV + ' || ' + FALLBACK + '}/file/bot\${params.token}/\${params.filePath}',
    },
    // getChat / other direct bot API calls with token in path
    {
        old: 'https://api.telegram.org/bot\${params.token}/',
        rep: '\${' + BASE_ENV + ' || ' + FALLBACK + '}/bot\${params.token}/',
    },
    // const TELEGRAM_API_BASE = \"https://api.telegram.org\"
    {
        old: 'const TELEGRAM_API_BASE = \"https://api.telegram.org\"',
        rep: 'const TELEGRAM_API_BASE = (' + BASE_ENV + ' || ' + FALLBACK + ')',
    },
    // Bare literal (catch-all for remaining occurrences not already replaced above)
    {
        old: '\"https://api.telegram.org\"',
        rep: '(' + BASE_ENV + ' || ' + FALLBACK + ')',
    },
];

let totalPatched = 0;
for (const f of fs.readdirSync(dir)) {
    if (!f.endsWith('.js')) continue;
    const fp = path.join(dir, f);
    let c = fs.readFileSync(fp, 'utf8');
    let changed = false;
    for (const { old, rep } of patterns) {
        if (c.includes(old)) {
            c = c.replaceAll(old, rep);
            changed = true;
        }
    }
    if (changed) {
        fs.writeFileSync(fp, c);
        totalPatched++;
        console.log('Patched:', f);
    }
}
console.log('OpenClaw dist: patched ' + totalPatched + ' file(s)');
" "$OPENCLAW_DIST"
else
    echo "WARNING: OpenClaw dist not found at $OPENCLAW_DIST"
fi
