#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# Restart AgentShroud and/or Gateway

# Auto-detect project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

SERVICE=${1:-all}

case $SERVICE in
    agentshroud|oc)
        echo "Restarting AgentShroud..."
        docker compose -f docker/docker-compose.yml restart agentshroud
        ;;
    gateway|gw)
        echo "Restarting Gateway..."
        docker compose -f docker/docker-compose.yml restart gateway
        ;;
    rebuild)
        echo "Rebuilding and restarting entire stack..."
        docker compose -f docker/docker-compose.yml down
        docker compose -f docker/docker-compose.yml up -d --build
        ;;
    all|*)
        echo "Restarting all services..."
        docker compose -f docker/docker-compose.yml restart
        ;;
esac

echo -e "\nWaiting for services to become healthy..."
sleep 30

docker compose -f docker/docker-compose.yml ps

echo -e "\n✅ Restart complete"
echo -e "\n📋 Usage: ./restart.sh [agentshroud|gateway|all|rebuild]"
