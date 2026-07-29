#!/bin/sh
# Patch grammY SDK to route Telegram API through TELEGRAM_API_BASE_URL
#
# SECURITY: this is the only thing keeping Telegram API calls routed through
# the gateway's egress filtering. If either patch target below stops matching
# because the vendor source drifted, this must fail the build loudly rather
# than silently ship an image where Telegram egress bypasses the gateway.
set -e

SDK_PATH="$(npm root -g)/openclaw/node_modules/grammy/out/core/client.js"
if [ ! -f "$SDK_PATH" ]; then
    echo "ERROR: grammY SDK not found at $SDK_PATH — Telegram egress would bypass the gateway." >&2
    echo "Vendor package layout may have changed; update patch-telegram-sdk.sh." >&2
    exit 1
fi

node -e "
const fs = require('fs');
const p = process.argv[1];
let c = fs.readFileSync(p, 'utf8');
const marker = 'process.env.TELEGRAM_API_BASE_URL';
const old1 = 'const apiRoot = (_a = options.apiRoot) !== null && _a !== void 0 ? _a : \"https://api.telegram.org\"';
const new1 = 'const apiRoot = process.env.TELEGRAM_API_BASE_URL || ((_a = options.apiRoot) !== null && _a !== void 0 ? _a : \"https://api.telegram.org\")';
let patched = false;
if (c.includes(old1)) {
    c = c.replace(old1, new1);
    patched = true;
    console.log('Patch applied: grammY apiRoot env override');
}
if (!patched && !c.includes(marker)) {
    console.error('ERROR: grammY apiRoot patch target not found and no existing TELEGRAM_API_BASE_URL marker.');
    console.error('Telegram egress would bypass the gateway. Vendor SDK source likely changed; update patch-telegram-sdk.sh.');
    process.exit(1);
}
fs.writeFileSync(p, c);
console.log('grammY SDK patched successfully');
" "$SDK_PATH"

# Patch OpenClaw dist: ALL hardcoded api.telegram.org URLs must route through gateway.
# Node.js native fetch() does not respect HTTPS_PROXY, so any hardcoded
# https://api.telegram.org URL bypasses the Slack bridge intercept and is blocked
# by CONNECT_FORCE_BLOCK_DOMAINS. This patch rewrites every occurrence.
OPENCLAW_DIST="$(npm root -g)/openclaw/dist"
if [ ! -d "$OPENCLAW_DIST" ]; then
    echo "ERROR: OpenClaw dist not found at $OPENCLAW_DIST — cannot verify Telegram egress routing." >&2
    echo "Vendor package layout may have changed; update patch-telegram-sdk.sh." >&2
    exit 1
fi

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
    // TELEGRAM_MEDIA_SSRF_POLICY: add \"gateway\" to allowedHostnames so that file downloads
    // routed through http://gateway:8080/telegram-api/... pass the SSRF private-IP check.
    // OpenClaw's SSRF guard blocks private IPs unless the hostname is in allowedHostnames.
    {
        old: 'allowedHostnames: [\"api.telegram.org\"],\n\tallowRfc2544BenchmarkRange: true\n};',
        rep: 'allowedHostnames: [\"api.telegram.org\",\"gateway\"],\n\tallowRfc2544BenchmarkRange: true\n};',
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

// Assert no un-guarded literal survives — a bare 'https://api.telegram.org' string
// left in dist after patching is a live, unrouted egress path. The guarded/patched
// form still CONTAINS that same literal as its fallback value (e.g.
// '(process.env.TELEGRAM_API_BASE_URL || \"https://api.telegram.org\")'), so we
// compare total occurrences against guarded occurrences rather than searching for
// the bare literal directly — otherwise every successfully-patched file would
// false-positive against its own fallback.
const bareRe = /\"https:\/\/api\.telegram\.org\"/g;
const guardedRe = /process\.env\.TELEGRAM_API_BASE_URL \|\| \"https:\/\/api\.telegram\.org\"/g;
let leaked = [];
for (const f of fs.readdirSync(dir)) {
    if (!f.endsWith('.js')) continue;
    const fp = path.join(dir, f);
    const c = fs.readFileSync(fp, 'utf8');
    const bareCount = (c.match(bareRe) || []).length;
    const guardedCount = (c.match(guardedRe) || []).length;
    if (bareCount > guardedCount) leaked.push(f);
}
if (leaked.length > 0) {
    console.error('ERROR: un-guarded \"https://api.telegram.org\" literal(s) survived patching in: ' + leaked.join(', '));
    console.error('Telegram egress would partially bypass the gateway. Vendor dist likely changed shape; update patch-telegram-sdk.sh.');
    process.exit(1);
}
" "$OPENCLAW_DIST"
