#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# Manage Telegram bot configuration

# Auto-detect project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

COMMAND=$1

case $COMMAND in
    status)
        echo "=== Telegram Channel Status ==="
        docker compose -f docker/docker-compose.yml exec agentshroud openclaw channels list
        echo -e "\n=== Telegram Pairing Status ==="
        docker compose -f docker/docker-compose.yml exec agentshroud openclaw pairing list telegram
        ;;
    add)
        if [ -z "$2" ]; then
            echo "Usage: ./telegram.sh add <BOT_TOKEN>"
            echo "Example: ./telegram.sh add 1234567890:ABCdef..."
            exit 1
        fi
        echo "Adding Telegram channel..."
        docker compose -f docker/docker-compose.yml exec agentshroud \
            openclaw channels add --channel telegram --token "$2"
        echo -e "\n✅ Channel added. Check pairing with: ./telegram.sh status"
        ;;
    remove)
        echo "Removing Telegram channel..."
        docker compose -f docker/docker-compose.yml exec agentshroud \
            openclaw channels remove telegram
        echo -e "\n✅ Channel removed"
        ;;
    approve)
        if [ -z "$2" ]; then
            echo "First, list pending pairings:"
            docker compose -f docker/docker-compose.yml exec agentshroud openclaw pairing list telegram
            echo -e "\nUsage: ./telegram.sh approve <PAIRING_CODE>"
            exit 1
        fi
        echo "Approving pairing: $2"
        docker compose -f docker/docker-compose.yml exec agentshroud \
            openclaw pairing approve telegram "$2"
        echo -e "\n✅ Pairing approved"
        ;;
    *)
        echo "Telegram Bot Management"
        echo ""
        echo "Usage: ./telegram.sh <command> [args]"
        echo ""
        echo "Commands:"
        echo "  status              Show channel and pairing status"
        echo "  add <token>         Add Telegram bot with token"
        echo "  remove              Remove Telegram channel"
        echo "  approve <id>        Approve a pending pairing"
        echo ""
        echo "Example:"
        echo "  ./telegram.sh add 1234567890:ABCdef..."
        echo "  ./telegram.sh approve telegram:123456"
        ;;
esac
