#!/bin/bash
# View OpenClaw and Gateway logs

cd /Users/ijefferson.admin/Development/oneclaw

SERVICE=${1:-all}
LINES=${2:-50}

case $SERVICE in
    openclaw|oc)
        echo "=== OpenClaw Logs (last $LINES lines) ==="
        docker logs openclaw-bot --tail $LINES
        ;;
    gateway|gw)
        echo "=== Gateway Logs (last $LINES lines) ==="
        docker logs secureclaw-gateway --tail $LINES
        ;;
    all|*)
        echo "=== Gateway Logs (last $LINES lines) ==="
        docker logs secureclaw-gateway --tail $LINES
        echo -e "\n=== OpenClaw Logs (last $LINES lines) ==="
        docker logs openclaw-bot --tail $LINES
        ;;
esac

echo -e "\n📋 Usage: ./logs.sh [openclaw|gateway|all] [lines]"
