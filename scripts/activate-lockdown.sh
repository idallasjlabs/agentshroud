#!/bin/bash
# ============================================================
# AgentShroud Network Lockdown Activation
# ============================================================
# Enables internal:true network + proxy routing.
# Backs up docker-compose.yml first so emergency-rollback.sh works.
#
# Usage: ./scripts/activate-lockdown.sh
# ============================================================

set -euo pipefail

COMPOSE_FILE="$(dirname "$0")/../docker/docker-compose.yml"
BACKUP_FILE="${COMPOSE_FILE}.pre-lockdown"

echo "🔒 AgentShroud Network Lockdown Activation"
echo "==========================================="

# Backup current compose file
echo "📦 Backing up docker-compose.yml → docker-compose.yml.pre-lockdown"
cp "$COMPOSE_FILE" "$BACKUP_FILE"

# Apply lockdown changes
echo "🔧 Applying network lockdown..."

# Set internal: true on the isolated network
sed -i "s/internal: false/internal: true/g" "$COMPOSE_FILE"

# Uncomment proxy env vars (if previously commented by rollback)
sed -i "s/^\\([[:space:]]*\\)# HTTP_PROXY:/\\1HTTP_PROXY:/g" "$COMPOSE_FILE"
sed -i "s/^\\([[:space:]]*\\)# HTTPS_PROXY:/\\1HTTPS_PROXY:/g" "$COMPOSE_FILE"
sed -i "s/^\\([[:space:]]*\\)# NO_PROXY:/\\1NO_PROXY:/g" "$COMPOSE_FILE"

echo ""
echo "Restarting containers..."
cd "$(dirname "$0")/../docker"
docker compose down
docker compose up -d

echo ""
echo "⏳ Waiting 15 seconds for containers to start..."
sleep 15

echo ""
echo "Container status:"
docker compose ps

echo ""
echo "🔒 Lockdown active."
echo "   Network: ISOLATED (bot cannot reach internet directly)"
echo "   Proxy: ENABLED (all traffic routes through gateway)"
echo ""
echo "To rollback if something breaks:"
echo "   ./scripts/emergency-rollback.sh"
