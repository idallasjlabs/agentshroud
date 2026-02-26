#!/bin/bash
# AgentShroud Upgrade Script
# Usage: ./docker/upgrade.sh <host-profile>
# Examples:
#   ./docker/upgrade.sh marvin-prod
#   ./docker/upgrade.sh marvin-test
#   ./docker/upgrade.sh trillian
#   ./docker/upgrade.sh pi

set -euo pipefail

PROFILE="${1:-}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

if [ -z "$PROFILE" ]; then
  echo "Usage: $0 <host-profile>"
  echo "Available profiles:"
  ls "$SCRIPT_DIR"/docker-compose.*.yml 2>/dev/null | sed 's/.*docker-compose\.\(.*\)\.yml/  \1/'
  exit 1
fi

OVERRIDE="$SCRIPT_DIR/docker-compose.${PROFILE}.yml"
BASE="$SCRIPT_DIR/docker-compose.yml"

if [ ! -f "$OVERRIDE" ]; then
  echo "Error: $OVERRIDE not found"
  exit 1
fi

# Derive project name from profile
PROJECT="agentshroud"
if [ "$PROFILE" != "marvin-prod" ]; then
  PROJECT="agentshroud-${PROFILE}"
fi

echo "=== AgentShroud Upgrade: $PROFILE ==="
echo "Project: $PROJECT"
echo "Base:    $BASE"
echo "Override: $OVERRIDE"
echo ""

# Step 1: Pull latest code
echo "[1/5] Pulling latest code..."
cd "$REPO_DIR"
git pull origin main

# Step 2: Backup (optional — volumes persist)
echo "[2/5] Volumes will persist. Skipping backup (run manually if needed)."

# Step 3: Stop existing containers
echo "[3/5] Stopping existing containers..."
docker compose -f "$BASE" -f "$OVERRIDE" -p "$PROJECT" down || true

# Step 4: Rebuild
echo "[4/5] Rebuilding images (no cache)..."
docker compose -f "$BASE" -f "$OVERRIDE" -p "$PROJECT" build --no-cache

# Step 5: Start
echo "[5/5] Starting containers..."
docker compose -f "$BASE" -f "$OVERRIDE" -p "$PROJECT" up -d

echo ""
echo "=== Upgrade complete ==="
docker compose -f "$BASE" -f "$OVERRIDE" -p "$PROJECT" ps
echo ""
echo "Logs: docker compose -f $BASE -f $OVERRIDE -p $PROJECT logs -f"
