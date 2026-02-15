#!/bin/bash
# Set default model for OpenClaw

cd /Users/ijefferson.admin/Development/oneclaw

if [ -z "$1" ]; then
    echo "Usage: ./set-model.sh <model>"
    echo ""
    echo "Available models:"
    echo "  anthropic/claude-opus-4-6"
    echo "  anthropic/claude-sonnet-4-5"
    echo "  openai/gpt-4o"
    echo "  openai/gpt-4-turbo"
    echo ""
    echo "Current model:"
    docker compose -f docker/docker-compose.yml exec openclaw bash -c '
    export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)
    export ANTHROPIC_API_KEY=$(cat /run/secrets/anthropic_api_key)
    openclaw models status | head -n 3
    '
    exit 1
fi

echo "Setting default model to: $1"
docker compose -f docker/docker-compose.yml exec openclaw bash -c "
export OPENAI_API_KEY=\$(cat /run/secrets/openai_api_key)
export ANTHROPIC_API_KEY=\$(cat /run/secrets/anthropic_api_key)
openclaw models set $1
"

echo -e "\n✅ Model set successfully"
