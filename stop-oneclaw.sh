#!/bin/bash
# OneClaw Stop Script - Stop everything with one command

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🛑 Stopping OneClaw..."
echo ""

# Stop the container
echo "1️⃣  Stopping OneClaw container..."
cd oneclaw-container
docker compose down
cd ..

# Stop the web server
if lsof -ti:18791 > /dev/null 2>&1; then
    echo "2️⃣  Stopping web interface..."
    kill $(lsof -ti:18791) 2>/dev/null || true
    sleep 1
fi

# Stop Tailscale serve (if running)
if tailscale serve status 2>/dev/null | grep -q ":443"; then
    echo "3️⃣  Stopping Tailscale serve..."
    tailscale serve --https=443 off 2>/dev/null || true
fi

echo ""
echo "✅ OneClaw stopped"
echo ""
echo "To start again:"
echo "  ./start-oneclaw.sh"
echo ""
