#!/bin/bash
# SecureClaw System Health Check
# Verifies all components are operational

set -e

cd "$(dirname "$0")/../.."

echo "================================================================"
echo "SecureClaw + OpenClaw Health Check"
echo "================================================================"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check 1: Docker Compose
echo -n "1. Checking containers... "
if docker compose -f docker/docker-compose.yml ps --format json | jq -r '.Health' | grep -q "healthy"; then
    echo -e "${GREEN}✅ PASS${NC}"
else
    echo -e "${RED}❌ FAIL${NC}"
    echo "   Run: docker compose -f docker/docker-compose.yml ps"
    exit 1
fi

# Check 2: Gateway Health
echo -n "2. Gateway API health... "
if curl -s -f http://localhost:8080/status > /dev/null 2>&1; then
    echo -e "${GREEN}✅ PASS${NC}"
else
    echo -e "${RED}❌ FAIL${NC}"
    exit 1
fi

# Check 3: OpenClaw UI accessible
echo -n "3. OpenClaw UI accessible... "
if curl -s http://localhost:18790 | grep -q "OpenClaw Control"; then
    echo -e "${GREEN}✅ PASS${NC}"
else
    echo -e "${RED}❌ FAIL${NC}"
    exit 1
fi

# Check 4: OpenClaw internet access
echo -n "4. OpenClaw internet access... "
if docker exec openclaw-bot curl -s -m 3 https://api.openai.com | grep -q "Welcome to the OpenAI API"; then
    echo -e "${GREEN}✅ PASS${NC}"
else
    echo -e "${RED}❌ FAIL${NC}"
    exit 1
fi

# Check 5: Security token configured
echo -n "5. Security token configured... "
if docker compose -f docker/docker-compose.yml exec openclaw printenv OPENCLAW_GATEWAY_TOKEN | grep -q "[a-f0-9]\{64\}"; then
    echo -e "${GREEN}✅ PASS${NC}"
else
    echo -e "${RED}❌ FAIL${NC}"
    exit 1
fi

# Check 6: Network isolation (Gateway can reach OpenClaw)
echo -n "6. Internal networking... "
if docker exec secureclaw-gateway python -c "import urllib.request; urllib.request.urlopen('http://openclaw:18789/api/health', timeout=3)" > /dev/null 2>&1; then
    echo -e "${GREEN}✅ PASS${NC}"
else
    echo -e "${RED}❌ FAIL${NC}"
    exit 1
fi

echo ""
echo "================================================================"
echo -e "${GREEN}✅ All health checks PASSED${NC}"
echo "================================================================"
echo ""
echo "🔐 SECURE ACCESS:"
echo "   OpenClaw UI: http://localhost:18790/#token=$(docker compose -f docker/docker-compose.yml exec openclaw printenv OPENCLAW_GATEWAY_TOKEN | tr -d '\r')"
echo ""
echo "📚 Documentation:"
echo "   Quick Access: QUICK_ACCESS.md"
echo "   Full Status:  DEPLOYMENT_STATUS.md"
echo "   Telegram:     TELEGRAM_SETUP.md"
echo ""
echo "🚀 System Status: OPERATIONAL"
echo ""
