#!/bin/bash
set -e

###############################################################################
# One Claw Tied Behind Your Back - Local Deployment
# Self-contained secure OpenClaw deployment
#
# Author: Isaiah Jefferson (via Claude Code)
# Security: Maximum - container-only, no host dependencies
###############################################################################

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTAINER_DIR="$SCRIPT_DIR/oneclaw-container"

# Colors
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  One Claw Tied Behind Your Back                           ║"
echo "║  Self-Contained Secure Deployment                          ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check prerequisites
echo "Checking prerequisites..."

if [[ $(uname) != "Darwin" ]]; then
    echo -e "${RED}ERROR:${NC} This deployment is designed for macOS"
    exit 1
fi

if ! docker ps &> /dev/null; then
    echo -e "${RED}ERROR:${NC} Docker is not running. Please start Docker and try again."
    exit 1
fi

if ! command -v docker &> /dev/null; then
    echo -e "${RED}ERROR:${NC} Docker not found. Install Docker Desktop or OrbStack."
    exit 1
fi

echo -e "${GREEN}✓${NC} Prerequisites met"
echo ""

# Check if already deployed
if [[ -f "$CONTAINER_DIR/.deployed" ]]; then
    echo -e "${YELLOW}⚠️${NC}  Deployment already exists at: $CONTAINER_DIR"
    read -p "Redeploy? This will rebuild the container. (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Deployment cancelled."
        exit 0
    fi
fi

echo "Deployment directory: $CONTAINER_DIR"
echo ""

# Build the image
echo -e "${BLUE}[1/3]${NC} Building OpenClaw image..."
echo "This builds OpenClaw entirely in a container - source code never touches your Mac."
echo "Build time: 10-20 minutes on first run..."
echo ""

cd "$SCRIPT_DIR"

if docker build -t oneclaw-secure:latest -f Dockerfile.secure . ; then
    echo -e "${GREEN}✓${NC} Image built successfully"
else
    echo -e "${RED}ERROR:${NC} Build failed"
    exit 1
fi

echo ""

# Verify personality files
echo -e "${BLUE}[2/3]${NC} Verifying Isaiah's personality files..."

for file in IDENTITY SOUL.md USER.md; do
    if [[ -f "$CONTAINER_DIR/workspace/$file" ]]; then
        echo -e "${GREEN}✓${NC} $file present"
    else
        echo -e "${YELLOW}⚠️${NC}  $file missing - bot will have generic personality"
    fi
done

echo ""

# Check secrets
echo -e "${BLUE}[3/3]${NC} Checking configuration..."

if grep -q "^ANTHROPIC_API_KEY=.\+$" "$CONTAINER_DIR/secrets/.env" 2>/dev/null || \
   grep -q "^OPENAI_API_KEY=.\+$" "$CONTAINER_DIR/secrets/.env" 2>/dev/null; then
    echo -e "${GREEN}✓${NC} API key configured"
else
    echo -e "${YELLOW}⚠️${NC}  No API key found in $CONTAINER_DIR/secrets/.env"
    echo "You'll need to add one before starting:"
    echo "  nano $CONTAINER_DIR/secrets/.env"
    echo "  Add: ANTHROPIC_API_KEY=sk-ant-..."
fi

# Mark as deployed
touch "$CONTAINER_DIR/.deployed"

echo ""
echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  Deployment Complete!                                      ║${NC}"
echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

echo "📂 Deployment Location:"
echo "   $CONTAINER_DIR"
echo ""

echo "🔐 Security Status:"
echo "   ✓ All data in current directory (self-contained)"
echo "   ✓ No host dependencies (except Docker)"
echo "   ✓ Container isolated (internet-only access)"
echo "   ✓ Isaiah's personality loaded from workspace files"
echo ""

echo "📋 Next Steps:"
echo ""
echo "1. Add your API key (if not done):"
echo "   nano $CONTAINER_DIR/secrets/.env"
echo ""
echo "2. Start OpenClaw:"
echo "   cd $CONTAINER_DIR"
echo "   docker-compose up -d"
echo ""
echo "3. Access WebChat:"
echo "   open http://localhost:18790"
echo ""
echo "4. View logs:"
echo "   cd $CONTAINER_DIR"
echo "   docker-compose logs -f"
echo ""

echo "📖 Management:"
echo "   Start:  cd $CONTAINER_DIR && docker-compose up -d"
echo "   Stop:   cd $CONTAINER_DIR && docker-compose down"
echo "   Logs:   cd $CONTAINER_DIR && docker-compose logs -f"
echo "   Status: docker ps | grep openclaw"
echo ""

echo "🔍 Verify Network Isolation:"
echo "   # Should work (internet):"
echo "   docker exec oneclaw_isaiah curl -I https://google.com"
echo ""
echo "   # Should fail (LAN blocked - use your router IP):"
echo "   docker exec oneclaw_isaiah curl --connect-timeout 5 http://192.168.1.1"
echo ""

echo "🆘 Troubleshooting:"
echo "   See: $SCRIPT_DIR/SECURITY.md"
echo "   See: $SCRIPT_DIR/QUICK-REFERENCE.md"
echo ""
