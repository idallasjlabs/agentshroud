#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
set -euo pipefail

MODE="${1:-}"

if [ "$MODE" = "dev" ]; then
    echo "🔧 Enabling DEVELOPMENT mode (read-write)"
    sed -i.bak 's/read_only: true/read_only: false/g' docker/docker-compose.yml
    echo "✅ Containers will be writable"

elif [ "$MODE" = "prod" ]; then
    echo "🔒 Enabling PRODUCTION mode (read-only)"
    sed -i.bak 's/read_only: false/read_only: true/g' docker/docker-compose.yml
    echo "✅ Containers will be read-only"

elif [ "$MODE" = "test" ]; then
    echo "🧪 Testing read-only mode..."

    # Enable read-only
    sed -i.bak 's/read_only: false/read_only: true/g' docker/docker-compose.yml

    # Rebuild
    docker compose -f docker/docker-compose.yml down
    docker compose -f docker/docker-compose.yml up -d --build

    # Wait for healthy
    echo "Waiting for containers to be healthy..."
    sleep 30

    # Test OS immutability
    echo ""
    echo "Testing OS immutability..."

    if docker exec agentshroud-bot touch /etc/test-file 2>&1 | grep -q "Read-only file system"; then
        echo "✅ AgentShroud OS is read-only"
    else
        echo "❌ AgentShroud OS is WRITABLE (BAD)"
    fi

    if docker exec agentshroud-bot touch /home/node/workspace/test-file 2>&1; then
        echo "✅ AgentShroud workspace is writable"
        docker exec agentshroud-bot rm /home/node/workspace/test-file
    else
        echo "❌ AgentShroud workspace is read-only (BAD)"
    fi

    if docker exec agentshroud-gateway touch /etc/test-file 2>&1 | grep -q "Read-only file system"; then
        echo "✅ Gateway OS is read-only"
    else
        echo "❌ Gateway OS is WRITABLE (BAD)"
    fi

    if docker exec agentshroud-gateway touch /app/data/test-file 2>&1; then
        echo "✅ Gateway data is writable"
        docker exec agentshroud-gateway rm /app/data/test-file
    else
        echo "❌ Gateway data is read-only (BAD)"
    fi

    echo ""
    echo "Read-only test complete!"

else
    echo "Usage: $0 {dev|prod|test}"
    echo ""
    echo "  dev   - Enable development mode (read-write)"
    echo "  prod  - Enable production mode (read-only)"
    echo "  test  - Test read-only mode and verify"
    exit 1
fi

echo ""
echo "Run 'docker compose -f docker/docker-compose.yml up -d' to apply changes"
