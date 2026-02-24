#!/bin/bash
# ============================================================
# AgentShroud Port Scanner
# Finds N available consecutive port pairs for new instances
# Usage: ./scripts/find-ports.sh [count] [start_port]
# ============================================================

set -euo pipefail

COUNT=${1:-2}          # How many ports to find (gateway + proxy)
START=${2:-9000}       # Start scanning from this port
END=65000

echo "🔍 Scanning for $COUNT available ports starting from $START..."

found=()
port=$START

while [ ${#found[@]} -lt $COUNT ] && [ $port -lt $END ]; do
    # Check if port is in use (netstat or lsof)
    if ! netstat -an 2>/dev/null | grep -q "[:.]${port} .*LISTEN" && \
       ! lsof -nP -iTCP:$port -sTCP:LISTEN >/dev/null 2>&1; then
        found+=($port)
    fi
    port=$((port + 1))
done

if [ ${#found[@]} -lt $COUNT ]; then
    echo "❌ Could not find $COUNT available ports between $START-$END"
    exit 1
fi

echo ""
echo "✅ Available ports:"
for i in "${!found[@]}"; do
    case $i in
        0) echo "   Gateway API:  ${found[$i]}" ;;
        1) echo "   HTTP Proxy:   ${found[$i]}" ;;
        *) echo "   Extra port $i: ${found[$i]}" ;;
    esac
done
echo ""

# Output machine-readable for scripts
echo "GATEWAY_PORT=${found[0]}"
echo "PROXY_PORT=${found[1]:-}"
