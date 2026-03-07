#!/bin/sh
# Patch Anthropic SDK to ALWAYS route through ANTHROPIC_BASE_URL
SDK_PATH="$(npm root -g)/openclaw/node_modules/@anthropic-ai/sdk/client.js"
if [ -f "$SDK_PATH" ]; then
    node -e "
const fs = require('fs');
const p = process.argv[1];
let c = fs.readFileSync(p, 'utf8');

// Patch 1: Force env var to always override in constructor default
const old1 = 'baseURL: baseURL || \`https://api.anthropic.com\`';
const new1 = 'baseURL: process.env.ANTHROPIC_BASE_URL || baseURL || \`https://api.anthropic.com\`';
if (c.includes(old1)) {
    c = c.replace(old1, new1);
    console.log('Patch 1 applied: constructor default');
}

// Patch 2: Override in the actual URL builder method (belt and suspenders)
// Find: const baseURL = (!...baseURLOverridden... && defaultBaseURL) || this.baseURL;
// Replace with forced env check
const old2 = 'const baseURL = (!tslib_1.__classPrivateFieldGet(this, _BaseAnthropic_instances, \"m\", _BaseAnthropic_baseURLOverridden).call(this) && defaultBaseURL) || this.baseURL;';
const new2 = 'const baseURL = process.env.ANTHROPIC_BASE_URL || ((!tslib_1.__classPrivateFieldGet(this, _BaseAnthropic_instances, \"m\", _BaseAnthropic_baseURLOverridden).call(this) && defaultBaseURL) || this.baseURL);';
if (c.includes(old2)) {
    c = c.replace(old2, new2);
    console.log('Patch 2 applied: URL builder override');
}

fs.writeFileSync(p, c);
console.log('Anthropic SDK patched successfully');
" "$SDK_PATH"
else
    echo "WARNING: Anthropic SDK not found at $SDK_PATH"
fi
