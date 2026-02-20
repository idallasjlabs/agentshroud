#!/bin/bash
# Manage AgentShroud trusted devices

cd /Users/ijefferson.admin/Development/agentshroud

COMMAND=$1

case $COMMAND in
    list)
        echo "=== AgentShroud Trusted Devices ==="
        docker compose -f docker/docker-compose.yml exec agentshroud agentshroud devices list
        ;;
    approve)
        if [ -z "$2" ]; then
            echo "First, list pending devices:"
            docker compose -f docker/docker-compose.yml exec agentshroud agentshroud devices list
            echo ""
            echo "Usage: ./devices.sh approve <REQUEST_ID>"
            echo "Example: ./devices.sh approve 6c16f64f-c3df-4544-aa6b-a89182228d4c"
            exit 1
        fi
        echo "Approving device: $2"
        docker compose -f docker/docker-compose.yml exec agentshroud agentshroud devices approve "$2"
        echo ""
        echo "✅ Device approved. Refresh the browser to connect."
        ;;
    approve-all)
        echo "⚠️  WARNING: This will approve ALL pending device requests."
        echo ""
        docker compose -f docker/docker-compose.yml exec agentshroud agentshroud devices list
        echo ""
        read -p "Are you sure you want to approve all? (yes/no): " confirm
        if [ "$confirm" = "yes" ]; then
            docker compose -f docker/docker-compose.yml exec agentshroud agentshroud devices approve-all
            echo "✅ All devices approved"
        else
            echo "Cancelled"
        fi
        ;;
    remove|unpair)
        if [ -z "$2" ]; then
            echo "First, list paired devices:"
            docker compose -f docker/docker-compose.yml exec agentshroud agentshroud devices list
            echo ""
            echo "Usage: ./devices.sh remove <DEVICE_ID>"
            echo "Example: ./devices.sh remove 542982a6190c3b6e9c7383fa484df6ec..."
            exit 1
        fi
        echo "Removing device: $2"
        docker compose -f docker/docker-compose.yml exec agentshroud agentshroud devices unpair "$2"
        echo "✅ Device removed"
        ;;
    *)
        echo "AgentShroud Device Management"
        echo ""
        echo "Usage: ./devices.sh <command> [args]"
        echo ""
        echo "Commands:"
        echo "  list              Show all devices (pending and paired)"
        echo "  approve <id>      Approve a pending device request"
        echo "  approve-all       Approve all pending devices (use with caution)"
        echo "  remove <id>       Remove/unpair a trusted device"
        echo ""
        echo "Examples:"
        echo "  ./devices.sh list"
        echo "  ./devices.sh approve 6c16f64f-c3df-4544-aa6b-a89182228d4c"
        echo "  ./devices.sh remove 542982a6190c3b6e9c7383fa484df6ec18a07b0745b24696a6ea6137f38550cd"
        echo ""
        echo "Common Workflow:"
        echo "  1. Browser shows 'pairing required'"
        echo "  2. Run: ./devices.sh list"
        echo "  3. Copy the Request ID from 'Pending' section"
        echo "  4. Run: ./devices.sh approve REQUEST_ID"
        echo "  5. Refresh browser - now connected!"
        ;;
esac
