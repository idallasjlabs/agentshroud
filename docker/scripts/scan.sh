#!/bin/bash
# AgentShroud OpenSCAP Compliance Scanner
# Runs SCAP security compliance checks on both containers

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCKER_DIR="$(dirname "$SCRIPT_DIR")"
REPORTS_DIR="$DOCKER_DIR/reports"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "======================================"
echo "AgentShroud OpenSCAP Compliance Scan"
echo "======================================"
echo ""

# Create reports directory if it doesn't exist
mkdir -p "$REPORTS_DIR"

# Check if containers are running
if ! docker ps | grep -q "openclaw-bot"; then
    echo -e "${RED}Error:${NC} OpenClaw container is not running"
    echo "Start containers with: docker compose -f docker/docker-compose.yml up -d"
    exit 1
fi

if ! docker ps | grep -q "agentshroud-gateway"; then
    echo -e "${RED}Error:${NC} Gateway container is not running"
    echo "Start containers with: docker compose -f docker/docker-compose.yml up -d"
    exit 1
fi

echo "Checking for OpenSCAP installation..."
if ! docker exec openclaw-bot which oscap >/dev/null 2>&1; then
    echo -e "${YELLOW}Warning:${NC} OpenSCAP not installed in OpenClaw container"
    echo "OpenSCAP can be added to the Dockerfile for compliance scanning"
    echo "Skipping OpenClaw SCAP scan..."
    OPENCLAW_SCAP=false
else
    OPENCLAW_SCAP=true
    echo -e "${GREEN}✓${NC} OpenSCAP found in OpenClaw container"
fi

if ! docker exec agentshroud-gateway which oscap >/dev/null 2>&1; then
    echo -e "${YELLOW}Warning:${NC} OpenSCAP not installed in Gateway container"
    echo "OpenSCAP can be added to the Dockerfile for compliance scanning"
    echo "Skipping Gateway SCAP scan..."
    GATEWAY_SCAP=false
else
    GATEWAY_SCAP=true
    echo -e "${GREEN}✓${NC} OpenSCAP found in Gateway container"
fi

# Scan OpenClaw container
if [ "$OPENCLAW_SCAP" = true ]; then
    echo ""
    echo "Scanning OpenClaw container..."

    # Check for available SCAP content
    SCAP_CONTENT=$(docker exec openclaw-bot find /usr/share/xml/scap -name "*-ds.xml" 2>/dev/null | head -1 || echo "")

    if [ -n "$SCAP_CONTENT" ]; then
        echo "Using SCAP content: $SCAP_CONTENT"

        # Run SCAP evaluation
        docker exec openclaw-bot oscap xccdf eval \
            --results-arf "/tmp/openclaw-scan-$TIMESTAMP.xml" \
            --report "/tmp/openclaw-scan-$TIMESTAMP.html" \
            "$SCAP_CONTENT" 2>&1 | tee "$REPORTS_DIR/openclaw-scan-$TIMESTAMP.log" || true

        # Copy reports out of container
        docker cp "openclaw-bot:/tmp/openclaw-scan-$TIMESTAMP.xml" "$REPORTS_DIR/" 2>/dev/null || true
        docker cp "openclaw-bot:/tmp/openclaw-scan-$TIMESTAMP.html" "$REPORTS_DIR/" 2>/dev/null || true

        echo -e "${GREEN}✓${NC} OpenClaw scan complete"
        echo "   Report: $REPORTS_DIR/openclaw-scan-$TIMESTAMP.html"
    else
        echo -e "${YELLOW}Warning:${NC} No SCAP content found in OpenClaw container"
        echo "Install SCAP Security Guide: apt-get install -y ssg-base ssg-debderived"
    fi
fi

# Scan Gateway container
if [ "$GATEWAY_SCAP" = true ]; then
    echo ""
    echo "Scanning Gateway container..."

    # Check for available SCAP content
    SCAP_CONTENT=$(docker exec agentshroud-gateway find /usr/share/xml/scap -name "*-ds.xml" 2>/dev/null | head -1 || echo "")

    if [ -n "$SCAP_CONTENT" ]; then
        echo "Using SCAP content: $SCAP_CONTENT"

        # Run SCAP evaluation
        docker exec agentshroud-gateway oscap xccdf eval \
            --results-arf "/tmp/gateway-scan-$TIMESTAMP.xml" \
            --report "/tmp/gateway-scan-$TIMESTAMP.html" \
            "$SCAP_CONTENT" 2>&1 | tee "$REPORTS_DIR/gateway-scan-$TIMESTAMP.log" || true

        # Copy reports out of container
        docker cp "agentshroud-gateway:/tmp/gateway-scan-$TIMESTAMP.xml" "$REPORTS_DIR/" 2>/dev/null || true
        docker cp "agentshroud-gateway:/tmp/gateway-scan-$TIMESTAMP.html" "$REPORTS_DIR/" 2>/dev/null || true

        echo -e "${GREEN}✓${NC} Gateway scan complete"
        echo "   Report: $REPORTS_DIR/gateway-scan-$TIMESTAMP.html"
    else
        echo -e "${YELLOW}Warning:${NC} No SCAP content found in Gateway container"
        echo "Install SCAP Security Guide: apt-get install -y ssg-base ssg-debderived"
    fi
fi

# Docker Bench Security (if available)
echo ""
echo "Running Docker Bench Security..."
if command -v docker-bench-security >/dev/null 2>&1; then
    docker-bench-security | tee "$REPORTS_DIR/docker-bench-$TIMESTAMP.log"
    echo -e "${GREEN}✓${NC} Docker Bench Security complete"
    echo "   Report: $REPORTS_DIR/docker-bench-$TIMESTAMP.log"
else
    echo -e "${YELLOW}Note:${NC} Docker Bench Security not installed"
    echo "Install with: git clone https://github.com/docker/docker-bench-security.git"
fi

# Manual security checks
echo ""
echo "Running manual security checks..."
{
    echo "======================================"
    echo "AgentShroud Manual Security Checks"
    echo "Date: $(date)"
    echo "======================================"
    echo ""

    echo "Container User (should be non-root):"
    echo "  Gateway: $(docker exec agentshroud-gateway whoami)"
    echo "  OpenClaw: $(docker exec openclaw-bot whoami)"
    echo ""

    echo "Read-only filesystem test:"
    echo -n "  Gateway: "
    docker exec agentshroud-gateway touch /test-file 2>&1 && echo "FAIL" || echo "PASS (read-only)"
    echo -n "  OpenClaw: "
    docker exec openclaw-bot touch /test-file 2>&1 && echo "FAIL (expected during dev)" || echo "PASS (read-only)"
    echo ""

    echo "Network connectivity:"
    echo -n "  Gateway to internet: "
    docker exec agentshroud-gateway ping -c 1 8.8.8.8 >/dev/null 2>&1 && echo "PASS" || echo "FAIL"
    echo -n "  OpenClaw to internet: "
    docker exec openclaw-bot ping -c 1 8.8.8.8 >/dev/null 2>&1 && echo "PASS" || echo "FAIL"
    echo ""

    echo "Port bindings (should be 127.0.0.1 only):"
    docker port agentshroud-gateway
    docker port openclaw-bot
    echo ""

    echo "Security options:"
    echo "  Gateway:"
    docker inspect --format '  {{.HostConfig.SecurityOpt}}' agentshroud-gateway
    echo "  OpenClaw:"
    docker inspect --format '  {{.HostConfig.SecurityOpt}}' openclaw-bot
    echo ""

    echo "Capabilities:"
    echo "  Gateway dropped: {{.HostConfig.CapDrop}}"
    docker inspect --format '  {{.HostConfig.CapDrop}}' agentshroud-gateway
    echo "  Gateway added: {{.HostConfig.CapAdd}}"
    docker inspect --format '  {{.HostConfig.CapAdd}}' agentshroud-gateway
    echo "  OpenClaw dropped: {{.HostConfig.CapDrop}}"
    docker inspect --format '  {{.HostConfig.CapDrop}}' openclaw-bot
    echo "  OpenClaw added: {{.HostConfig.CapAdd}}"
    docker inspect --format '  {{.HostConfig.CapAdd}}' openclaw-bot
    echo ""

} | tee "$REPORTS_DIR/manual-checks-$TIMESTAMP.log"

echo ""
echo "======================================"
echo "Scan Complete"
echo "======================================"
echo "Reports saved to: $REPORTS_DIR/"
echo ""
ls -lh "$REPORTS_DIR/"*"$TIMESTAMP"* 2>/dev/null || echo "No reports generated"
echo ""
echo "View HTML reports:"
if [ -f "$REPORTS_DIR/openclaw-scan-$TIMESTAMP.html" ]; then
    echo "  open $REPORTS_DIR/openclaw-scan-$TIMESTAMP.html"
fi
if [ -f "$REPORTS_DIR/gateway-scan-$TIMESTAMP.html" ]; then
    echo "  open $REPORTS_DIR/gateway-scan-$TIMESTAMP.html"
fi
