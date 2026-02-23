#!/bin/bash
# ============================================================
# AgentShroud Emergency Rollback
# ============================================================
# Run this if the bot goes dark after network lockdown.
# It disables internal:true and removes proxy env vars
# so the bot gets direct internet access again.
#
# Usage: ./scripts/emergency-rollback.sh
# ============================================================

set -euo pipefail

COMPOSE_FILE="$(dirname "$0")/../docker/docker-compose.yml"
BACKUP_FILE="${COMPOSE_FILE}.pre-lockdown"

echo "🚨 AgentShroud Emergency Rollback"
echo "================================="

# If we have a pre-lockdown backup, restore it
if [ -f "$BACKUP_FILE" ]; then
    echo "✅ Found pre-lockdown backup: $BACKUP_FILE"
    echo "   Restoring original docker-compose.yml..."
    cp "$BACKUP_FILE" "$COMPOSE_FILE"
else
    echo "⚠️  No backup found. Patching docker-compose.yml directly..."

    # Remove internal: true from the network
    sed -i.bak 's/internal: true/internal: false/g' "$COMPOSE_FILE"

    # Comment out proxy env vars
    sed -i 's/^\([[:space:]]*\)HTTP_PROXY:/\1# HTTP_PROXY:/g' "$COMPOSE_FILE"
    sed -i 's/^\([[:space:]]*\)HTTPS_PROXY:/\1# HTTPS_PROXY:/g' "$COMPOSE_FILE"
    sed -i 's/^\([[:space:]]*\)NO_PROXY:/\1# NO_PROXY:/g' "$COMPOSE_FILE"

    echo "   Patched docker-compose.yml (backup at ${COMPOSE_FILE}.bak)"
fi

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
echo "✅ Rollback complete."
echo "   Network: OPEN (bot has direct internet access)"
echo "   Proxy: DISABLED"
echo "   The bot should be reachable again in ~30 seconds."
echo ""
echo "To re-enable lockdown after fixing issues:"
echo "   ./scripts/activate-lockdown.sh"
