#!/bin/bash
# Complete system test

# Auto-detect project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║         AgentShroud + AgentShroud Complete System Test          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

echo "1️⃣  Container Health"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
docker compose -f docker/docker-compose.yml ps
echo ""

echo "2️⃣  API Keys Status"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
docker compose -f docker/docker-compose.yml exec agentshroud bash -c '
export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key)
export ANTHROPIC_API_KEY=$(cat /run/secrets/anthropic_api_key)
agentshroud models status | grep -A 5 "Auth overview"
'
echo ""

echo "3️⃣  Telegram Status"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
docker compose -f docker/docker-compose.yml exec agentshroud agentshroud channels list | grep -A 2 "Telegram"
echo ""

echo "4️⃣  Gmail Status"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
docker compose -f docker/docker-compose.yml exec agentshroud agentshroud channels list | grep -i gmail || echo "Gmail not configured yet"
echo ""

echo "5️⃣  Gateway Health"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
curl -s http://localhost:8080/status | jq '.' 2>/dev/null || curl -s http://localhost:8080/status
echo ""

echo "6️⃣  Control UI"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "URL: http://localhost:18790"
echo "Status: $(curl -s -o /dev/null -w '%{http_code}' http://localhost:18790)"
echo ""

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                      Test Complete!                          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "✅ Next Steps:"
echo "  1. Message @therealidallasj_bot on Telegram to test"
echo "  2. Set up Gmail (see TELEGRAM_GMAIL_SETUP.md Part 2)"
echo "  3. Ask bot to send a test email"
echo ""
