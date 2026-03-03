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
