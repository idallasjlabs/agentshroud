#!/bin/bash
# Comprehensive AgentShroud system test

set -e

echo "=== AgentShroud System Test ==="
echo

echo "1. Testing Gateway Status..."
curl -s http://127.0.0.1:8080/status || echo "❌ Gateway /status failed"
echo
echo

echo "2. Testing OpenClaw Control UI..."
curl -s http://127.0.0.1:18790/ | grep -q "OpenClaw Control" && echo "✓ OpenClaw UI accessible" || echo "❌ OpenClaw UI failed"
echo

echo "3. Testing Container Health..."
docker compose -f docker/docker-compose.yml ps
echo

echo "4. Testing Gateway Endpoints..."
curl -s http://127.0.0.1:8080/agents && echo "✓ /agents endpoint works" || echo "❌ /agents endpoint failed"
echo

echo "5. Checking OpenClaw Logs..."
docker compose -f docker/docker-compose.yml logs openclaw --tail=5
echo

echo "6. Checking Gateway Logs..."
docker compose -f docker/docker-compose.yml logs gateway --tail=5
echo

echo "=== Test Complete ==="
