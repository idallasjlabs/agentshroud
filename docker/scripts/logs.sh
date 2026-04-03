#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
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
