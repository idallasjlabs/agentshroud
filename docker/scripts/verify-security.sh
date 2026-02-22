#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
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
AGENTSHROUD_USER=$(docker inspect --format '{{.Config.User}}' agentshroud-bot 2>/dev/null || echo "")

if [ "$GATEWAY_USER" != "" ] && [ "$GATEWAY_USER" != "0" ] && [ "$GATEWAY_USER" != "root" ]; then
    check_pass "Gateway running as non-root user: $GATEWAY_USER"
else
    check_fail "Gateway running as root or user not set"
fi

if [ "$AGENTSHROUD_USER" != "" ] && [ "$AGENTSHROUD_USER" != "0" ] && [ "$AGENTSHROUD_USER" != "root" ]; then
    check_pass "AgentShroud running as non-root user: $AGENTSHROUD_USER"
else
    check_fail "AgentShroud running as root or user not set"
fi

# Check 2: Read-only root filesystem
echo ""
echo "[2/13] Checking read-only root filesystem..."
GATEWAY_READONLY=$(docker inspect --format '{{.HostConfig.ReadonlyRootfs}}' agentshroud-gateway 2>/dev/null || echo "false")
AGENTSHROUD_READONLY=$(docker inspect --format '{{.HostConfig.ReadonlyRootfs}}' agentshroud-bot 2>/dev/null || echo "false")

if [ "$GATEWAY_READONLY" == "true" ]; then
    check_pass "Gateway has read-only root filesystem"
else
    check_fail "Gateway does not have read-only root filesystem"
fi

if [ "$AGENTSHROUD_READONLY" == "true" ]; then
    check_pass "AgentShroud has read-only root filesystem"
else
    check_warn "AgentShroud does not have read-only root filesystem (expected during development)"
fi

# Check 3: All capabilities dropped
echo ""
echo "[3/13] Checking capabilities..."
GATEWAY_CAPDROP=$(docker inspect --format '{{.HostConfig.CapDrop}}' agentshroud-gateway 2>/dev/null || echo "")
AGENTSHROUD_CAPDROP=$(docker inspect --format '{{.HostConfig.CapDrop}}' agentshroud-bot 2>/dev/null || echo "")

if echo "$GATEWAY_CAPDROP" | grep -q "ALL"; then
    check_pass "Gateway has dropped all capabilities"
else
    check_fail "Gateway has not dropped all capabilities: $GATEWAY_CAPDROP"
fi

if echo "$AGENTSHROUD_CAPDROP" | grep -q "ALL"; then
    check_pass "AgentShroud has dropped all capabilities"
else
    check_fail "AgentShroud has not dropped all capabilities: $AGENTSHROUD_CAPDROP"
fi

# Check 4: NET_RAW capability not added
echo ""
echo "[4/13] Checking NET_RAW capability..."
AGENTSHROUD_CAPADD=$(docker inspect --format '{{.HostConfig.CapAdd}}' agentshroud-bot 2>/dev/null || echo "")

if ! echo "$AGENTSHROUD_CAPADD" | grep -q "NET_RAW"; then
    check_pass "AgentShroud does not have NET_RAW capability"
else
    check_fail "AgentShroud has NET_RAW capability (should be removed)"
fi

# Check 5: no-new-privileges set
echo ""
echo "[5/13] Checking no-new-privileges..."
GATEWAY_SECOPT=$(docker inspect --format '{{.HostConfig.SecurityOpt}}' agentshroud-gateway 2>/dev/null || echo "")
AGENTSHROUD_SECOPT=$(docker inspect --format '{{.HostConfig.SecurityOpt}}' agentshroud-bot 2>/dev/null || echo "")

if echo "$GATEWAY_SECOPT" | grep -q "no-new-privileges:true"; then
    check_pass "Gateway has no-new-privileges enabled"
else
    check_fail "Gateway does not have no-new-privileges enabled"
fi

if echo "$AGENTSHROUD_SECOPT" | grep -q "no-new-privileges:true"; then
    check_pass "AgentShroud has no-new-privileges enabled"
else
    check_fail "AgentShroud does not have no-new-privileges enabled"
fi

# Check 6: Seccomp profiles active
echo ""
echo "[6/13] Checking seccomp profiles..."
if echo "$GATEWAY_SECOPT" | grep -q "seccomp"; then
    check_pass "Gateway has seccomp profile active"
else
    check_warn "Gateway does not have seccomp profile active (check if disabled for debugging)"
fi

if echo "$AGENTSHROUD_SECOPT" | grep -q "seccomp"; then
    check_pass "AgentShroud has seccomp profile active"
else
    check_warn "AgentShroud does not have seccomp profile active (check if disabled for debugging)"
fi

# Check 7: Localhost-only binding
echo ""
echo "[7/13] Checking localhost-only port binding..."
GATEWAY_PORTS=$(docker port agentshroud-gateway 2>/dev/null || echo "")
AGENTSHROUD_PORTS=$(docker port agentshroud-bot 2>/dev/null || echo "")

if echo "$GATEWAY_PORTS" | grep -q "127.0.0.1"; then
    check_pass "Gateway bound to localhost only"
else
    check_fail "Gateway not bound to localhost (exposed to network)"
fi

if echo "$AGENTSHROUD_PORTS" | grep -q "127.0.0.1"; then
    check_pass "AgentShroud UI bound to localhost only"
else
    check_fail "AgentShroud UI not bound to localhost (exposed to network)"
fi

# Check 8: Resource limits set
echo ""
echo "[8/13] Checking resource limits..."
GATEWAY_MEM=$(docker inspect --format '{{.HostConfig.Memory}}' agentshroud-gateway 2>/dev/null || echo "0")
AGENTSHROUD_MEM=$(docker inspect --format '{{.HostConfig.Memory}}' agentshroud-bot 2>/dev/null || echo "0")

if [ "$GATEWAY_MEM" -gt 0 ]; then
    check_pass "Gateway has memory limit: $((GATEWAY_MEM / 1024 / 1024))MB"
else
    check_fail "Gateway does not have memory limit"
fi

if [ "$AGENTSHROUD_MEM" -gt 0 ]; then
    check_pass "AgentShroud has memory limit: $((AGENTSHROUD_MEM / 1024 / 1024))MB"
else
    check_fail "AgentShroud does not have memory limit"
fi

# Check 9: Docker secrets mounted
echo ""
echo "[9/13] Checking Docker secrets..."

# Gateway doesn't need secrets currently
check_pass "Gateway secrets check (not required)"

# Check if AgentShroud has secret files mounted
if docker exec agentshroud-bot test -f /run/secrets/openai_api_key 2>/dev/null; then
    check_pass "AgentShroud has OpenAI API key secret mounted"
else
    check_fail "AgentShroud missing OpenAI API key secret"
fi

if docker exec agentshroud-bot test -f /run/secrets/gateway_password 2>/dev/null; then
    check_pass "AgentShroud has Gateway password secret mounted"
else
    check_fail "AgentShroud missing Gateway password secret"
fi

# Check 10: Network isolation
echo ""
echo "[10/13] Checking network isolation..."
GATEWAY_NETWORKS=$(docker inspect --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}} {{end}}' agentshroud-gateway 2>/dev/null || echo "")
AGENTSHROUD_NETWORKS=$(docker inspect --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}} {{end}}' agentshroud-bot 2>/dev/null || echo "")

if echo "$GATEWAY_NETWORKS" | grep -q "agentshroud-internal"; then
    check_pass "Gateway on agentshroud-internal network"
else
    check_fail "Gateway not on agentshroud-internal network"
fi

if echo "$AGENTSHROUD_NETWORKS" | grep -q "agentshroud-isolated"; then
    check_pass "AgentShroud on agentshroud-isolated network"
else
    check_fail "AgentShroud not on agentshroud-isolated network"
fi

if ! echo "$AGENTSHROUD_NETWORKS" | grep -q "agentshroud-internal"; then
    check_pass "AgentShroud NOT on external network (properly isolated)"
else
    check_fail "AgentShroud on external network (should be isolated)"
fi

# Check 11: Both containers healthy
echo ""
echo "[11/13] Checking container health..."
GATEWAY_HEALTH=$(docker inspect --format '{{.State.Health.Status}}' agentshroud-gateway 2>/dev/null || echo "unknown")
AGENTSHROUD_HEALTH=$(docker inspect --format '{{.State.Health.Status}}' agentshroud-bot 2>/dev/null || echo "unknown")

if [ "$GATEWAY_HEALTH" == "healthy" ]; then
    check_pass "Gateway is healthy"
else
    check_fail "Gateway health: $GATEWAY_HEALTH"
fi

if [ "$AGENTSHROUD_HEALTH" == "healthy" ]; then
    check_pass "AgentShroud is healthy"
else
    check_fail "AgentShroud health: $AGENTSHROUD_HEALTH"
fi

# Check 12: Environment variables properly set
echo ""
echo "[12/13] Checking security environment variables..."
AGENTSHROUD_ENV=$(docker inspect --format '{{range .Config.Env}}{{println .}}{{end}}' agentshroud-bot 2>/dev/null || echo "")

if echo "$AGENTSHROUD_ENV" | grep -q "AGENTSHROUD_DISABLE_HOST_FILESYSTEM=true"; then
    check_pass "AgentShroud has host filesystem disabled"
else
    check_fail "AgentShroud does not have host filesystem disabled"
fi

if echo "$AGENTSHROUD_ENV" | grep -q "AGENTSHROUD_SANDBOX_MODE=strict"; then
    check_pass "AgentShroud in strict sandbox mode"
else
    check_fail "AgentShroud not in strict sandbox mode"
fi

if echo "$AGENTSHROUD_ENV" | grep -q "AGENTSHROUD_DISABLE_BONJOUR=1"; then
    check_pass "AgentShroud has Bonjour/mDNS disabled"
else
    check_fail "AgentShroud does not have Bonjour/mDNS disabled"
fi

# Check 13: No hardcoded secrets in docker-compose.yml
echo ""
echo "[13/13] Checking for hardcoded secrets..."
if grep -q "AGENTSHROUD_GATEWAY_PASSWORD=" "$COMPOSE_FILE" | grep -v "AGENTSHROUD_GATEWAY_PASSWORD_FILE"; then
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
