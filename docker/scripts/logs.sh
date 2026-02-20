#!/bin/bash
# View AgentShroud and Gateway logs

# Auto-detect project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

SERVICE=${1:-all}
LINES=${2:-50}

case $SERVICE in
    agentshroud|oc)
        echo "=== AgentShroud Logs (last $LINES lines) ==="
        docker logs agentshroud-bot --tail $LINES
        ;;
    gateway|gw)
        echo "=== Gateway Logs (last $LINES lines) ==="
        docker logs agentshroud-gateway --tail $LINES
        ;;
    all|*)
        echo "=== Gateway Logs (last $LINES lines) ==="
        docker logs agentshroud-gateway --tail $LINES
        echo -e "\n=== AgentShroud Logs (last $LINES lines) ==="
        docker logs agentshroud-bot --tail $LINES
        ;;
esac

echo -e "\n📋 Usage: ./logs.sh [agentshroud|gateway|all] [lines]"
