#!/bin/bash
# ============================================================
# AgentShroud Deploy Script
# ============================================================
# Deploys AgentShroud on any server (Marvin/Pi/Trillian).
# Auto-detects Docker or Podman. Finds available ports.
# 
# Usage: ./scripts/deploy.sh [--port PORT] [--name NAME]
# Example: ./scripts/deploy.sh --port 9000 --name test-v2
# Default: port 8080, name from hostname
# ============================================================

set -euo pipefail

# --- Parse args ---
GATEWAY_PORT=8080
INSTANCE_NAME="agentshroud-$(hostname -s)"

while [[ $# -gt 0 ]]; do
    case $1 in
        --port) GATEWAY_PORT="$2"; shift 2 ;;
        --name) INSTANCE_NAME="$2"; shift 2 ;;
        --find-port) FIND_PORT=true; shift ;;
        -h|--help)
            echo "Usage: $0 [--port PORT] [--name NAME] [--find-port]"
            echo "  --port PORT    Gateway port (default: 8080)"
            echo "  --name NAME    Instance name (default: agentshroud-<hostname>)"
            echo "  --find-port    Auto-find available port starting from 9000"
            exit 0 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

# --- Auto-find port if requested ---
if [ "${FIND_PORT:-false}" = "true" ]; then
    PORT=9000
    while [ $PORT -lt 65000 ]; do
        if ! netstat -an 2>/dev/null | grep -q "[:.]${PORT} .*LISTEN" && \
           ! lsof -nP -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1 && \
           ! ss -tlnp 2>/dev/null | grep -q ":${PORT} "; then
            GATEWAY_PORT=$PORT
            break
        fi
        PORT=$((PORT + 1))
    done
    echo "🔍 Auto-selected port: $GATEWAY_PORT"
fi

# --- Detect container runtime ---
RUNTIME=""
COMPOSE_CMD=""

if command -v docker >/dev/null 2>&1; then
    # Check if docker compose plugin exists
    if docker compose version >/dev/null 2>&1; then
        RUNTIME="docker"
        COMPOSE_CMD="docker compose"
    fi
fi

if [ -z "$RUNTIME" ] && command -v podman >/dev/null 2>&1; then
    RUNTIME="podman"
    if command -v podman-compose >/dev/null 2>&1; then
        COMPOSE_CMD="podman-compose"
    elif podman compose version >/dev/null 2>&1; then
        COMPOSE_CMD="podman compose"
    else
        echo "❌ Podman found but no compose plugin. Install: pip3 install podman-compose"
        exit 1
    fi
fi

if [ -z "$RUNTIME" ]; then
    echo "❌ No container runtime found. Install Docker or Podman."
    echo ""
    echo "  macOS:   brew install --cask docker   (or)  brew install podman"
    echo "  Debian:  sudo apt-get install podman"
    echo "  Pi:      sudo apt-get install podman"
    exit 1
fi

echo "🚀 AgentShroud Deploy"
echo "====================="
echo "  Host:      $(hostname -s)"
echo "  Runtime:   $RUNTIME ($COMPOSE_CMD)"
echo "  Instance:  $INSTANCE_NAME"
echo "  Port:      $GATEWAY_PORT"
echo ""

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
COMPOSE_DIR="$PROJECT_DIR/docker"

cd "$COMPOSE_DIR"

# --- Stop existing instance if running ---
echo "🛑 Stopping existing instance (if any)..."
COMPOSE_PROJECT_NAME="$INSTANCE_NAME" $COMPOSE_CMD \
    -f docker-compose.yml down 2>/dev/null || true

# --- Create port override if not default ---
OVERRIDE_ARGS=""
if [ "$GATEWAY_PORT" != "8080" ]; then
    OVERRIDE_FILE="docker-compose.${INSTANCE_NAME}.yml"
    cat > "$OVERRIDE_FILE" << EOF
services:
  gateway:
    container_name: ${INSTANCE_NAME}-gateway
    ports: !override
      - "127.0.0.1:${GATEWAY_PORT}:8080"
  agentshroud:
    container_name: ${INSTANCE_NAME}-bot
EOF
    OVERRIDE_ARGS="-f $OVERRIDE_FILE"
    echo "📄 Port override: $OVERRIDE_FILE"
fi

# --- Build ---
echo ""
echo "🔨 Building..."
COMPOSE_PROJECT_NAME="$INSTANCE_NAME" $COMPOSE_CMD \
    -f docker-compose.yml $OVERRIDE_ARGS \
    build 2>&1 | tail -10

# --- Start ---
echo ""
echo "🚀 Starting..."
COMPOSE_PROJECT_NAME="$INSTANCE_NAME" $COMPOSE_CMD \
    -f docker-compose.yml $OVERRIDE_ARGS \
    up -d 2>&1

echo ""
echo "⏳ Waiting 20 seconds for startup..."
sleep 20

# --- Health check ---
echo ""
echo "🏥 Health check..."
COMPOSE_PROJECT_NAME="$INSTANCE_NAME" $COMPOSE_CMD \
    -f docker-compose.yml $OVERRIDE_ARGS \
    ps 2>&1

# Check gateway
echo ""
echo -n "Gateway API (port $GATEWAY_PORT)... "
if curl -sf --max-time 5 "http://127.0.0.1:${GATEWAY_PORT}/status" >/dev/null 2>&1; then
    echo "✅ UP"
else
    echo "⚠️  Not responding yet (may still be starting)"
fi

# --- Tailscale serve (if available) ---
if command -v tailscale >/dev/null 2>&1; then
    echo ""
    echo "🌐 Setting up Tailscale serve..."
    tailscale serve --bg --https=$GATEWAY_PORT http://127.0.0.1:$GATEWAY_PORT 2>&1 || true
    TS_NAME=$(tailscale status --self --json 2>/dev/null | python3 -c 'import sys,json; print(json.load(sys.stdin)["Self"]["DNSName"].rstrip("."))' 2>/dev/null || echo "unknown")
    echo "   Tailscale URL: https://${TS_NAME}:${GATEWAY_PORT}"
fi

# --- Summary ---
echo ""
echo "============================================"
echo "✅ $INSTANCE_NAME deployed on $(hostname -s)"
echo "============================================"
echo ""
echo "  Gateway:  http://127.0.0.1:${GATEWAY_PORT}"
echo "  Runtime:  $RUNTIME"
echo ""
echo "  Commands:"
echo "    Logs:   cd $COMPOSE_DIR && COMPOSE_PROJECT_NAME=$INSTANCE_NAME $COMPOSE_CMD -f docker-compose.yml $OVERRIDE_ARGS logs -f"
echo "    Stop:   cd $COMPOSE_DIR && COMPOSE_PROJECT_NAME=$INSTANCE_NAME $COMPOSE_CMD -f docker-compose.yml $OVERRIDE_ARGS down"
echo "    Status: cd $COMPOSE_DIR && COMPOSE_PROJECT_NAME=$INSTANCE_NAME $COMPOSE_CMD -f docker-compose.yml $OVERRIDE_ARGS ps"
