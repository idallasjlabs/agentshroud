#!/bin/bash
# Check OpenClaw and Gateway status

# Auto-detect project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "=== Container Status ==="
docker compose -f docker/docker-compose.yml ps

echo -e "\n=== Telegram Channel ==="
docker compose -f docker/docker-compose.yml exec openclaw openclaw channels list

echo -e "\n=== Model Configuration ==="
docker compose -f docker/docker-compose.yml exec openclaw bash -c '
export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)
export ANTHROPIC_API_KEY=$(cat /run/secrets/anthropic_api_key)
openclaw models status
'

echo -e "\n=== Gateway Health ==="
curl -s http://localhost:8080/status | jq '.' 2>/dev/null || curl -s http://localhost:8080/status

echo -e "\n=== OpenClaw UI ==="
echo "Control UI: http://localhost:18790"
