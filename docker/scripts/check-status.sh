#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# Check AgentShroud and Gateway status

# Auto-detect project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "=== Container Status ==="
docker compose -f docker/docker-compose.yml ps

echo -e "\n=== Telegram Channel ==="
docker compose -f docker/docker-compose.yml exec agentshroud agentshroud channels list

echo -e "\n=== Model Configuration ==="
docker compose -f docker/docker-compose.yml exec agentshroud bash -c '
export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)
export ANTHROPIC_API_KEY=$(cat /run/secrets/anthropic_api_key)
agentshroud models status
'

echo -e "\n=== Gateway Health ==="
curl -s http://localhost:8080/status | jq '.' 2>/dev/null || curl -s http://localhost:8080/status

echo -e "\n=== AgentShroud UI ==="
echo "Control UI: http://localhost:18790"
