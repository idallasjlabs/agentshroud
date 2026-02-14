#!/bin/bash

###############################################################################
# Environment Test Script
# Project: One Claw Tied Behind Your Back
#
# Tests environment prerequisites before deployment
###############################################################################

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

PASSED=0
FAILED=0
WARNINGS=0

echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  OpenClaw Environment Test                                 ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Function: Test check
test_check() {
    local name="$1"
    local status="$2"
    local message="$3"

    if [[ "$status" == "pass" ]]; then
        echo -e "${GREEN}✓${NC} $name"
        ((PASSED++))
    elif [[ "$status" == "fail" ]]; then
        echo -e "${RED}✗${NC} $name"
        if [[ -n "$message" ]]; then
            echo -e "  ${RED}→${NC} $message"
        fi
        ((FAILED++))
    elif [[ "$status" == "warn" ]]; then
        echo -e "${YELLOW}⚠${NC}  $name"
        if [[ -n "$message" ]]; then
            echo -e "  ${YELLOW}→${NC} $message"
        fi
        ((WARNINGS++))
    fi
}

# Test: macOS
echo "Testing Operating System..."
if [[ $(uname) == "Darwin" ]]; then
    OS_VERSION=$(sw_vers -productVersion)
    MAJOR_VERSION=$(echo "$OS_VERSION" | cut -d'.' -f1)
    if [[ $MAJOR_VERSION -ge 12 ]]; then
        test_check "macOS Version ($OS_VERSION)" "pass"
    else
        test_check "macOS Version ($OS_VERSION)" "warn" "macOS 12+ recommended"
    fi
else
    test_check "macOS" "fail" "This deployment requires macOS"
fi
echo ""

# Test: Docker/OrbStack
echo "Testing Container Runtime..."
if command -v orb &> /dev/null; then
    ORBSTACK_VERSION=$(orb version 2>/dev/null | head -1 || echo "unknown")
    test_check "OrbStack ($ORBSTACK_VERSION)" "pass"
    DOCKER_CMD="orb"
    DOCKER_RUNTIME="OrbStack"
elif command -v docker &> /dev/null; then
    DOCKER_VERSION=$(docker --version | cut -d' ' -f3 | tr -d ',')
    test_check "Docker Desktop ($DOCKER_VERSION)" "pass"
    DOCKER_CMD="docker"
    DOCKER_RUNTIME="Docker Desktop"
else
    test_check "Docker/OrbStack" "fail" "Install OrbStack or Docker Desktop"
    DOCKER_CMD=""
fi

# Test: Docker running
if [[ -n "$DOCKER_CMD" ]]; then
    if $DOCKER_CMD ps &> /dev/null; then
        test_check "$DOCKER_RUNTIME Running" "pass"
    else
        test_check "$DOCKER_RUNTIME Running" "fail" "Please start $DOCKER_RUNTIME"
    fi
fi
echo ""

# Test: Node.js
echo "Testing Node.js..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
    FULL_NODE_VERSION=$(node -v)
    if [[ $NODE_VERSION -ge 22 ]]; then
        test_check "Node.js ($FULL_NODE_VERSION)" "pass"
    else
        test_check "Node.js ($FULL_NODE_VERSION)" "fail" "Node.js 22+ required"
    fi
else
    test_check "Node.js" "fail" "Install with: brew install node@22"
fi

# Test: npm
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    test_check "npm ($NPM_VERSION)" "pass"
else
    test_check "npm" "fail" "Should be installed with Node.js"
fi
echo ""

# Test: Disk space
echo "Testing Disk Space..."
AVAILABLE_GB=$(df -g "$HOME" | awk 'NR==2 {print $4}')
if [[ $AVAILABLE_GB -ge 20 ]]; then
    test_check "Disk Space (${AVAILABLE_GB}GB free)" "pass"
elif [[ $AVAILABLE_GB -ge 10 ]]; then
    test_check "Disk Space (${AVAILABLE_GB}GB free)" "warn" "20GB+ recommended"
else
    test_check "Disk Space (${AVAILABLE_GB}GB free)" "fail" "10GB minimum required"
fi
echo ""

# Test: Memory
echo "Testing Memory..."
TOTAL_MEM_GB=$(sysctl hw.memsize | awk '{print int($2/1024/1024/1024)}')
if [[ $TOTAL_MEM_GB -ge 16 ]]; then
    test_check "RAM (${TOTAL_MEM_GB}GB)" "pass"
elif [[ $TOTAL_MEM_GB -ge 8 ]]; then
    test_check "RAM (${TOTAL_MEM_GB}GB)" "warn" "16GB recommended"
else
    test_check "RAM (${TOTAL_MEM_GB}GB)" "fail" "8GB minimum required"
fi
echo ""

# Test: Optional tools
echo "Testing Optional Tools..."
if command -v jq &> /dev/null; then
    test_check "jq (JSON processor)" "pass"
else
    test_check "jq (JSON processor)" "warn" "Install with: brew install jq"
fi

if command -v curl &> /dev/null; then
    test_check "curl" "pass"
else
    test_check "curl" "warn" "Should be pre-installed on macOS"
fi

if command -v wget &> /dev/null; then
    test_check "wget" "pass"
else
    test_check "wget" "warn" "Install with: brew install wget (optional)"
fi
echo ""

# Test: Firewall
echo "Testing Firewall..."
if [[ -f "/Applications/Little Snitch.app/Contents/MacOS/Little Snitch" ]]; then
    test_check "Little Snitch" "pass"
elif [[ -f "/Applications/LuLu.app/Contents/MacOS/LuLu" ]]; then
    test_check "Lulu" "pass"
else
    test_check "Application Firewall" "warn" "Install Little Snitch or Lulu for better security"
fi
echo ""

# Test: Network connectivity
echo "Testing Network..."
if ping -c 1 -W 3 8.8.8.8 &> /dev/null; then
    test_check "Internet Connectivity" "pass"
else
    test_check "Internet Connectivity" "fail" "No internet connection"
fi

if ping -c 1 -W 3 hub.docker.com &> /dev/null; then
    test_check "Docker Hub Reachable" "pass"
else
    test_check "Docker Hub Reachable" "warn" "Cannot reach hub.docker.com"
fi

if ping -c 1 -W 3 github.com &> /dev/null; then
    test_check "GitHub Reachable" "pass"
else
    test_check "GitHub Reachable" "warn" "Cannot reach github.com"
fi
echo ""

# Test: Ports availability
echo "Testing Port Availability..."
if lsof -i :18789 &> /dev/null; then
    test_check "Port 18789 (Gateway)" "warn" "Port already in use"
else
    test_check "Port 18789 (Gateway)" "pass"
fi

if lsof -i :18790 &> /dev/null; then
    test_check "Port 18790 (WebChat)" "warn" "Port already in use"
else
    test_check "Port 18790 (WebChat)" "pass"
fi

if lsof -i :8765 &> /dev/null; then
    test_check "Port 8765 (Bridge)" "warn" "Port already in use"
else
    test_check "Port 8765 (Bridge)" "pass"
fi
echo ""

# Summary
echo "════════════════════════════════════════════════════════════"
echo "Test Summary:"
echo ""
echo -e "${GREEN}Passed:${NC}   $PASSED"
echo -e "${YELLOW}Warnings:${NC} $WARNINGS"
echo -e "${RED}Failed:${NC}   $FAILED"
echo ""

if [[ $FAILED -eq 0 ]]; then
    if [[ $WARNINGS -eq 0 ]]; then
        echo -e "${GREEN}✓ Your environment is ready for OpenClaw deployment!${NC}"
        echo ""
        echo "Next steps:"
        echo "  ./deploy-openclaw.sh"
        exit 0
    else
        echo -e "${YELLOW}⚠ Your environment is ready, but some recommendations were not met.${NC}"
        echo "You can proceed with deployment, but consider addressing the warnings."
        echo ""
        echo "Next steps:"
        echo "  ./deploy-openclaw.sh"
        exit 0
    fi
else
    echo -e "${RED}✗ Your environment has failed tests. Please resolve them before deploying.${NC}"
    echo ""
    exit 1
fi
