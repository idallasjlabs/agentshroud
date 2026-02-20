#!/bin/bash
# Set default model for AgentShroud

# Auto-detect project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

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
    docker compose -f docker/docker-compose.yml exec agentshroud bash -c '
    export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)
    export ANTHROPIC_API_KEY=$(cat /run/secrets/anthropic_api_key)
    agentshroud models status | head -n 3
    '
    exit 1
fi

echo "Setting default model to: $1"
docker compose -f docker/docker-compose.yml exec agentshroud bash -c "
export OPENAI_API_KEY=\$(cat /run/secrets/openai_api_key)
export ANTHROPIC_API_KEY=\$(cat /run/secrets/anthropic_api_key)
agentshroud models set $1
"

echo -e "\n✅ Model set successfully"
