#!/bin/bash
# OneClaw Startup Script - Start everything with one command

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🦞 Starting OneClaw..."
echo ""

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running!"
    echo "   Please start Docker Desktop or OrbStack and try again."
    exit 1
fi

# Start the container
echo "1️⃣  Starting OneClaw container..."
cd oneclaw-container
docker compose up -d
cd ..

# Wait for container to be healthy
echo "2️⃣  Waiting for OneClaw to start (30 seconds)..."
sleep 30

# Check if container is running
if ! docker ps | grep -q oneclaw_isaiah; then
    echo "❌ OneClaw container failed to start!"
    echo "   Check logs with: docker compose -f oneclaw-container/docker-compose.yml logs"
    exit 1
fi

# Kill any existing web server on port 18791
if lsof -ti:18791 > /dev/null 2>&1; then
    echo "3️⃣  Stopping existing web server..."
    kill $(lsof -ti:18791) 2>/dev/null || true
    sleep 2
fi

# Start the web interface
echo "4️⃣  Starting web interface..."
nohup python3 -m http.server 18791 --directory oneclaw-container/control-ui > /tmp/oneclaw-webserver.log 2>&1 &
sleep 2

# Verify web server started
if ! curl -s http://localhost:18791/ > /dev/null; then
    echo "❌ Web interface failed to start!"
    echo "   Check logs at: /tmp/oneclaw-webserver.log"
    exit 1
fi

echo ""
echo "✅ OneClaw is running!"
echo ""
echo "Access the web interface:"
echo "  🌐 Local:  http://localhost:18791"
echo ""
echo "Optional: Enable remote access via Tailscale:"
echo "  tailscale serve --bg http://127.0.0.1:18791"
echo ""
echo "To stop OneClaw:"
echo "  ./stop-oneclaw.sh"
echo ""
echo "To view logs:"
echo "  docker compose -f oneclaw-container/docker-compose.yml logs -f"
echo ""

# Optionally open in browser
read -p "Open in browser now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    open http://localhost:18791
fi
