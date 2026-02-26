#!/bin/sh
# Patch Anthropic SDK to always respect ANTHROPIC_BASE_URL env var
# This routes ALL LLM API calls through the AgentShroud gateway
SDK_PATH="$(npm root -g)/openclaw/node_modules/@anthropic-ai/sdk/client.js"
if [ -f "$SDK_PATH" ]; then
    sed -i "s|baseURL: baseURL || \`https://api.anthropic.com\`|baseURL: process.env.ANTHROPIC_BASE_URL || baseURL || \`https://api.anthropic.com\`|" "$SDK_PATH"
    echo "Patched Anthropic SDK to respect ANTHROPIC_BASE_URL"
else
    echo "WARNING: Anthropic SDK not found at $SDK_PATH"
fi
