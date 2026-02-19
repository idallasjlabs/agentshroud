#!/bin/bash
# AgentShroud Security Verification Script
# Validates all security controls are properly configured

set -e

COMPOSE_FILE="$DOCKER_DIR/docker-compose.yml"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCKER_DIR="$(dirname "$SCRIPT_DIR")"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASSED=0
FAILED=0
WARNINGS=0

echo "======================================"
echo "AgentShroud Security Verification"
echo "======================================"
echo ""

check_pass() {
    echo -e "${GREEN}✓${NC} $1"
    PASSED=$((PASSED + 1))
}

check_fail() {
    echo -e "${RED}✗${NC} $1"
    FAILED=$((FAILED + 1))
}

check_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
    WARNINGS=$((WARNINGS + 1))
}

# Check 1: Both containers running as non-root
echo "[1/13] Checking non-root users..."
GATEWAY_USER=$(docker inspect --format '{{.Config.User}}' agentshroud-gateway 2>/dev/null || echo "")
OPENCLAW_USER=$(docker inspect --format '{{.Config.User}}' openclaw-bot 2>/dev/null || echo "")

if [ "$GATEWAY_USER" != "" ] && [ "$GATEWAY_USER" != "0" ] && [ "$GATEWAY_USER" != "root" ]; then
    check_pass "Gateway running as non-root user: $GATEWAY_USER"
else
    check_fail "Gateway running as root or user not set"
fi

if [ "$OPENCLAW_USER" != "" ] && [ "$OPENCLAW_USER" != "0" ] && [ "$OPENCLAW_USER" != "root" ]; then
    check_pass "OpenClaw running as non-root user: $OPENCLAW_USER"
else
    check_fail "OpenClaw running as root or user not set"
fi

# Check 2: Read-only root filesystem
echo ""
echo "[2/13] Checking read-only root filesystem..."
GATEWAY_READONLY=$(docker inspect --format '{{.HostConfig.ReadonlyRootfs}}' agentshroud-gateway 2>/dev/null || echo "false")
OPENCLAW_READONLY=$(docker inspect --format '{{.HostConfig.ReadonlyRootfs}}' openclaw-bot 2>/dev/null || echo "false")

if [ "$GATEWAY_READONLY" == "true" ]; then
    check_pass "Gateway has read-only root filesystem"
else
    check_fail "Gateway does not have read-only root filesystem"
fi

if [ "$OPENCLAW_READONLY" == "true" ]; then
    check_pass "OpenClaw has read-only root filesystem"
else
    check_warn "OpenClaw does not have read-only root filesystem (expected during development)"
fi

# Check 3: All capabilities dropped
echo ""
echo "[3/13] Checking capabilities..."
GATEWAY_CAPDROP=$(docker inspect --format '{{.HostConfig.CapDrop}}' agentshroud-gateway 2>/dev/null || echo "")
OPENCLAW_CAPDROP=$(docker inspect --format '{{.HostConfig.CapDrop}}' openclaw-bot 2>/dev/null || echo "")

if echo "$GATEWAY_CAPDROP" | grep -q "ALL"; then
    check_pass "Gateway has dropped all capabilities"
else
    check_fail "Gateway has not dropped all capabilities: $GATEWAY_CAPDROP"
fi

if echo "$OPENCLAW_CAPDROP" | grep -q "ALL"; then
    check_pass "OpenClaw has dropped all capabilities"
else
    check_fail "OpenClaw has not dropped all capabilities: $OPENCLAW_CAPDROP"
fi

# Check 4: NET_RAW capability not added
echo ""
echo "[4/13] Checking NET_RAW capability..."
OPENCLAW_CAPADD=$(docker inspect --format '{{.HostConfig.CapAdd}}' openclaw-bot 2>/dev/null || echo "")

if ! echo "$OPENCLAW_CAPADD" | grep -q "NET_RAW"; then
    check_pass "OpenClaw does not have NET_RAW capability"
else
    check_fail "OpenClaw has NET_RAW capability (should be removed)"
fi

# Check 5: no-new-privileges set
echo ""
echo "[5/13] Checking no-new-privileges..."
GATEWAY_SECOPT=$(docker inspect --format '{{.HostConfig.SecurityOpt}}' agentshroud-gateway 2>/dev/null || echo "")
OPENCLAW_SECOPT=$(docker inspect --format '{{.HostConfig.SecurityOpt}}' openclaw-bot 2>/dev/null || echo "")

if echo "$GATEWAY_SECOPT" | grep -q "no-new-privileges:true"; then
    check_pass "Gateway has no-new-privileges enabled"
else
    check_fail "Gateway does not have no-new-privileges enabled"
fi

if echo "$OPENCLAW_SECOPT" | grep -q "no-new-privileges:true"; then
    check_pass "OpenClaw has no-new-privileges enabled"
else
    check_fail "OpenClaw does not have no-new-privileges enabled"
fi

# Check 6: Seccomp profiles active
echo ""
echo "[6/13] Checking seccomp profiles..."
if echo "$GATEWAY_SECOPT" | grep -q "seccomp"; then
    check_pass "Gateway has seccomp profile active"
else
    check_warn "Gateway does not have seccomp profile active (check if disabled for debugging)"
fi

if echo "$OPENCLAW_SECOPT" | grep -q "seccomp"; then
    check_pass "OpenClaw has seccomp profile active"
else
    check_warn "OpenClaw does not have seccomp profile active (check if disabled for debugging)"
fi

# Check 7: Localhost-only binding
echo ""
echo "[7/13] Checking localhost-only port binding..."
GATEWAY_PORTS=$(docker port agentshroud-gateway 2>/dev/null || echo "")
OPENCLAW_PORTS=$(docker port openclaw-bot 2>/dev/null || echo "")

if echo "$GATEWAY_PORTS" | grep -q "127.0.0.1"; then
    check_pass "Gateway bound to localhost only"
else
    check_fail "Gateway not bound to localhost (exposed to network)"
fi

if echo "$OPENCLAW_PORTS" | grep -q "127.0.0.1"; then
    check_pass "OpenClaw UI bound to localhost only"
else
    check_fail "OpenClaw UI not bound to localhost (exposed to network)"
fi

# Check 8: Resource limits set
echo ""
echo "[8/13] Checking resource limits..."
GATEWAY_MEM=$(docker inspect --format '{{.HostConfig.Memory}}' agentshroud-gateway 2>/dev/null || echo "0")
OPENCLAW_MEM=$(docker inspect --format '{{.HostConfig.Memory}}' openclaw-bot 2>/dev/null || echo "0")

if [ "$GATEWAY_MEM" -gt 0 ]; then
    check_pass "Gateway has memory limit: $((GATEWAY_MEM / 1024 / 1024))MB"
else
    check_fail "Gateway does not have memory limit"
fi

if [ "$OPENCLAW_MEM" -gt 0 ]; then
    check_pass "OpenClaw has memory limit: $((OPENCLAW_MEM / 1024 / 1024))MB"
else
    check_fail "OpenClaw does not have memory limit"
fi

# Check 9: Docker secrets mounted
echo ""
echo "[9/13] Checking Docker secrets..."

# Gateway doesn't need secrets currently
check_pass "Gateway secrets check (not required)"

# Check if OpenClaw has secret files mounted
if docker exec openclaw-bot test -f /run/secrets/openai_api_key 2>/dev/null; then
    check_pass "OpenClaw has OpenAI API key secret mounted"
else
    check_fail "OpenClaw missing OpenAI API key secret"
fi

if docker exec openclaw-bot test -f /run/secrets/gateway_password 2>/dev/null; then
    check_pass "OpenClaw has Gateway password secret mounted"
else
    check_fail "OpenClaw missing Gateway password secret"
fi

# Check 10: Network isolation
echo ""
echo "[10/13] Checking network isolation..."
GATEWAY_NETWORKS=$(docker inspect --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}} {{end}}' agentshroud-gateway 2>/dev/null || echo "")
OPENCLAW_NETWORKS=$(docker inspect --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}} {{end}}' openclaw-bot 2>/dev/null || echo "")

if echo "$GATEWAY_NETWORKS" | grep -q "agentshroud-internal"; then
    check_pass "Gateway on agentshroud-internal network"
else
    check_fail "Gateway not on agentshroud-internal network"
fi

if echo "$OPENCLAW_NETWORKS" | grep -q "agentshroud-isolated"; then
    check_pass "OpenClaw on agentshroud-isolated network"
else
    check_fail "OpenClaw not on agentshroud-isolated network"
fi

if ! echo "$OPENCLAW_NETWORKS" | grep -q "agentshroud-internal"; then
    check_pass "OpenClaw NOT on external network (properly isolated)"
else
    check_fail "OpenClaw on external network (should be isolated)"
fi

# Check 11: Both containers healthy
echo ""
echo "[11/13] Checking container health..."
GATEWAY_HEALTH=$(docker inspect --format '{{.State.Health.Status}}' agentshroud-gateway 2>/dev/null || echo "unknown")
OPENCLAW_HEALTH=$(docker inspect --format '{{.State.Health.Status}}' openclaw-bot 2>/dev/null || echo "unknown")

if [ "$GATEWAY_HEALTH" == "healthy" ]; then
    check_pass "Gateway is healthy"
else
    check_fail "Gateway health: $GATEWAY_HEALTH"
fi

if [ "$OPENCLAW_HEALTH" == "healthy" ]; then
    check_pass "OpenClaw is healthy"
else
    check_fail "OpenClaw health: $OPENCLAW_HEALTH"
fi

# Check 12: Environment variables properly set
echo ""
echo "[12/13] Checking security environment variables..."
OPENCLAW_ENV=$(docker inspect --format '{{range .Config.Env}}{{println .}}{{end}}' openclaw-bot 2>/dev/null || echo "")

if echo "$OPENCLAW_ENV" | grep -q "OPENCLAW_DISABLE_HOST_FILESYSTEM=true"; then
    check_pass "OpenClaw has host filesystem disabled"
else
    check_fail "OpenClaw does not have host filesystem disabled"
fi

if echo "$OPENCLAW_ENV" | grep -q "OPENCLAW_SANDBOX_MODE=strict"; then
    check_pass "OpenClaw in strict sandbox mode"
else
    check_fail "OpenClaw not in strict sandbox mode"
fi

if echo "$OPENCLAW_ENV" | grep -q "OPENCLAW_DISABLE_BONJOUR=1"; then
    check_pass "OpenClaw has Bonjour/mDNS disabled"
else
    check_fail "OpenClaw does not have Bonjour/mDNS disabled"
fi

# Check 13: No hardcoded secrets in docker-compose.yml
echo ""
echo "[13/13] Checking for hardcoded secrets..."
if grep -q "OPENCLAW_GATEWAY_PASSWORD=" "$COMPOSE_FILE" | grep -v "OPENCLAW_GATEWAY_PASSWORD_FILE"; then
    check_fail "Hardcoded gateway password found in docker-compose.yml"
else
    check_pass "No hardcoded gateway password in docker-compose.yml"
fi

# Summary
echo ""
echo "======================================"
echo "Security Verification Summary"
echo "======================================"
echo -e "${GREEN}Passed:${NC} $PASSED"
echo -e "${YELLOW}Warnings:${NC} $WARNINGS"
echo -e "${RED}Failed:${NC} $FAILED"
echo ""

if [ $FAILED -gt 0 ]; then
    echo -e "${RED}SECURITY VERIFICATION FAILED${NC}"
    echo "Please address the failed checks before deploying to production."
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo -e "${YELLOW}SECURITY VERIFICATION PASSED WITH WARNINGS${NC}"
    echo "Some security features are disabled (expected during development)."
    exit 0
else
    echo -e "${GREEN}SECURITY VERIFICATION PASSED${NC}"
    echo "All security controls are properly configured."
    exit 0
fi
