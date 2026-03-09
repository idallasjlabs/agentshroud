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

# Patch OpenClaw dist: file download URL must also route through gateway
# OpenClaw's downloadAndSaveTelegramFile() has a hardcoded api.telegram.org URL
# that is separate from grammY's apiRoot. Node.js native fetch() does not
# respect HTTPS_PROXY, so on the isolated network this causes a timeout.
OPENCLAW_DIST="$(npm root -g)/openclaw/dist"
if [ -d "$OPENCLAW_DIST" ]; then
    node -e "
const fs = require('fs');
const path = require('path');
const dir = process.argv[1];
const old = 'https://api.telegram.org/file/bot\${params.token}/\${params.filePath}';
const rep = '\${process.env.TELEGRAM_API_BASE_URL || \"https://api.telegram.org\"}/file/bot\${params.token}/\${params.filePath}';
let count = 0;
for (const f of fs.readdirSync(dir)) {
    if (!f.endsWith('.js')) continue;
    const fp = path.join(dir, f);
    const c = fs.readFileSync(fp, 'utf8');
    if (c.includes(old)) {
        fs.writeFileSync(fp, c.replaceAll(old, rep));
        count++;
        console.log('Patched file download URL in', f);
    }
}
console.log('OpenClaw dist: patched ' + count + ' file(s)');
" "$OPENCLAW_DIST"
else
    echo "WARNING: OpenClaw dist not found at $OPENCLAW_DIST"
fi
