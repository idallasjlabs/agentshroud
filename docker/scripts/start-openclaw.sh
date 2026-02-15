#!/bin/bash
# OpenClaw startup wrapper - exports API keys from Docker secrets

set -e

# Export OpenAI API key from secret file
if [ -f "/run/secrets/openai_api_key" ]; then
    export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)
    echo "[startup] Loaded OpenAI API key"
else
    echo "[startup] Warning: OpenAI API key file not found"
fi

# Export Anthropic API key from secret file
if [ -f "/run/secrets/anthropic_api_key" ]; then
    export ANTHROPIC_API_KEY=$(cat /run/secrets/anthropic_api_key)
    echo "[startup] Loaded Anthropic API key"
else
    echo "[startup] Warning: Anthropic API key file not found"
fi

# Start OpenClaw gateway
echo "[startup] Starting OpenClaw gateway..."
exec openclaw gateway --allow-unconfigured --bind lan
