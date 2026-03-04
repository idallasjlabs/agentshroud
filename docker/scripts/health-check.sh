#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# AgentShroud System Health Check
# Verifies all components are operational

set -e

cd "$(dirname "$0")/../.."

echo "================================================================"
echo "AgentShroud + AgentShroud Health Check"
echo "================================================================"
echo ""

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

check_pass() { echo -e "${GREEN}✅ PASS${NC} — $1"; }
check_fail() { echo -e "${RED}❌ FAIL${NC} — $1"; }

# Check 1: Docker Compose
echo -n "1. Containers... "
if docker compose -f docker/docker-compose.yml ps --format json 2>/dev/null | grep -q "healthy"; then
    check_pass "Both containers healthy"
else
    check_fail "Containers not healthy"
fi

# Check 2: Gateway Health
echo -n "2. Gateway API... "
if curl -sf http://localhost:8080/status > /dev/null 2>&1; then
    check_pass "Gateway responding"
else
    check_fail "Gateway not responding"
fi

# Check 3: AgentShroud UI
echo -n "3. AgentShroud UI... "
HTTP_CODE=$(curl -so /dev/null -w '%{http_code}' http://localhost:18790 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "302" ]; then
    check_pass "UI accessible (HTTP $HTTP_CODE)"
else
    check_fail "UI not accessible (HTTP $HTTP_CODE)"
fi

# Check 4: Internet access (via gateway — bot has no direct internet)
echo -n "4. Internet access (via gateway)... "
if docker exec agentshroud-gateway python -c "import urllib.request; urllib.request.urlopen('https://api.openai.com', timeout=5).read()" > /dev/null 2>&1; then
    check_pass "Gateway outbound internet working"
else
    check_fail "Gateway has no internet access"
fi

# Check 5: Security token
echo -n "5. Security token... "
if docker compose -f docker/docker-compose.yml exec -T agentshroud printenv AGENTSHROUD_GATEWAY_TOKEN 2>/dev/null | grep -q '[a-f0-9]'; then
    check_pass "Gateway token configured"
else
    check_fail "Gateway token missing"
fi

# Check 6: Internal networking
echo -n "6. Internal network... "
if docker exec agentshroud-gateway python -c "import urllib.request; urllib.request.urlopen('http://agentshroud:18789/api/health', timeout=3)" > /dev/null 2>&1; then
    check_pass "Gateway → AgentShroud connected"
else
    check_fail "Gateway → AgentShroud connection failed"
fi

echo ""
echo "================================================================"
echo "AgentShroud UI: http://localhost:18790"
echo "================================================================"
