#!/bin/bash
# AgentShroud Preflight Check — validates a running instance
# Usage: ./preflight-check.sh [gateway_url] [gateway_password]
set -euo pipefail

GW_URL="${1:-http://127.0.0.1:8080}"
GW_PASS="${2:-$(cat /run/secrets/gateway_password 2>/dev/null || echo '')}"
AUTH="Authorization: Bearer ${GW_PASS}"

pass=0 fail=0 warn=0

check() {
    local name="$1" result="$2" expected="${3:-}"
    if [ -n "$expected" ] && [ "$result" != "$expected" ]; then
        echo "❌ $name: got $result (expected $expected)"
        fail=$((fail + 1))
    elif [ -z "$result" ] || [ "$result" = "null" ]; then
        echo "⚠️  $name: empty/null"
        warn=$((warn + 1))
    else
        echo "✅ $name: $result"
        pass=$((pass + 1))
    fi
}

echo "═══════════════════════════════════════════════════════════"
echo "  AgentShroud Preflight Check"
echo "  Gateway: $GW_URL"
echo "  Time: $(date -u '+%Y-%m-%d %H:%M UTC')"
echo "═══════════════════════════════════════════════════════════"
echo ""

# 1. Gateway health
echo "── Gateway Health ──"
status=$(curl -sf "$GW_URL/status" 2>/dev/null)
check "Status" "$(echo "$status" | grep -o '"status":"[^"]*"' | cut -d'"' -f4)" "healthy"
check "Version" "$(echo "$status" | grep -o '"version":"[^"]*"' | cut -d'"' -f4)"
check "PII Engine" "$(echo "$status" | grep -o '"pii_engine":"[^"]*"' | cut -d'"' -f4)"
check "Config" "$(echo "$status" | grep -o '"config_loaded":[a-z]*' | cut -d: -f2)" "true"
echo ""

# 2. Security modules
echo "── Security Modules ──"
modules=$(curl -sf -H "$AUTH" "$GW_URL/manage/modules" 2>/dev/null)
total=$(echo "$modules" | grep -o '"total":[0-9]*' | cut -d: -f2)
active=$(echo "$modules" | grep -o '"active":[0-9]*' | cut -d: -f2)
loaded=$(echo "$modules" | grep -o '"loaded":[0-9]*' | cut -d: -f2)
unavailable=$(echo "$modules" | grep -o '"unavailable":[0-9]*' | cut -d: -f2)
check "Total modules" "$total"
check "Active" "$active"
check "Loaded" "$loaded"
check "Unavailable" "$unavailable" "0"
echo ""

# 3. Auth enforcement
echo "── Auth Enforcement ──"
noauth=$(curl -sf -o /dev/null -w '%{http_code}' "$GW_URL/agents" 2>/dev/null)
check "Unauth /agents" "$noauth" "401"
echo ""

# 4. Op-proxy (credential isolation)
echo "── Credential Isolation ──"
blocked=$(curl -sf -o /dev/null -w '%{http_code}' -X POST -H "$AUTH" -H "Content-Type: application/json" \
    -d '{"reference":"op://Personal/secret/pw"}' "$GW_URL/credentials/op-proxy" 2>/dev/null)
check "Blocked vault" "$blocked" "403"

traversal=$(curl -sf -o /dev/null -w '%{http_code}' -X POST -H "$AUTH" -H "Content-Type: application/json" \
    -d '{"reference":"op://Agent Shroud Bot Credentials/../../../etc/passwd"}' "$GW_URL/credentials/op-proxy" 2>/dev/null)
check "Path traversal" "$traversal" "403"
echo ""

# 5. Dashboard
echo "── Dashboard ──"
stats_code=$(curl -sf -o /dev/null -w '%{http_code}' -H "$AUTH" "$GW_URL/dashboard/stats" 2>/dev/null)
check "Dashboard stats" "$stats_code" "200"
echo ""

# 6. SSH proxy
echo "── SSH Proxy ──"
hosts=$(curl -sf -H "$AUTH" "$GW_URL/ssh/hosts" 2>/dev/null)
check "SSH hosts" "$(echo "$hosts" | grep -o '"hosts"' | head -1)" '"hosts"'
echo ""

# Summary
echo "═══════════════════════════════════════════════════════════"
echo "  Results: ✅ $pass passed / ❌ $fail failed / ⚠️  $warn warnings"
echo "═══════════════════════════════════════════════════════════"

[ "$fail" -eq 0 ] && exit 0 || exit 1
