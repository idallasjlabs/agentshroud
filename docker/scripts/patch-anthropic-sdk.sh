#!/bin/sh
# Patch Anthropic SDK to always respect ANTHROPIC_BASE_URL env var
# This routes ALL LLM API calls through the AgentShroud gateway
SDK_PATH="$(npm root -g)/openclaw/node_modules/@anthropic-ai/sdk/client.js"
if [ -f "$SDK_PATH" ]; then
    node -e "
const fs = require('fs');
const p = '$SDK_PATH';
let c = fs.readFileSync(p, 'utf8');
const old = 'baseURL: baseURL || \`https://api.anthropic.com\`';
const rep = 'baseURL: process.env.ANTHROPIC_BASE_URL || baseURL || \`https://api.anthropic.com\`';
if (c.includes(old)) {
    c = c.replace(old, rep);
    fs.writeFileSync(p, c);
    console.log('Patched Anthropic SDK to respect ANTHROPIC_BASE_URL');
} else {
    console.log('WARNING: Pattern not found in SDK, may already be patched');
}
"
else
    echo "WARNING: Anthropic SDK not found at $SDK_PATH"
fi
