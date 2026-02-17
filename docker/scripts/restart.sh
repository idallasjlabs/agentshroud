#!/bin/bash
# Restart OpenClaw and/or Gateway

# Auto-detect project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

SERVICE=${1:-all}

case $SERVICE in
    openclaw|oc)
        echo "Restarting OpenClaw..."
        docker compose -f docker/docker-compose.yml restart openclaw
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
echo -e "\n📋 Usage: ./restart.sh [openclaw|gateway|all|rebuild]"
