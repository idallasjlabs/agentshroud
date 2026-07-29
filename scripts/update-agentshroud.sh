#!/bin/bash
# Update OpenClaw to latest npm version
# This script:
# 1. Backs up current config
# 2. Rebuilds openclaw container with latest npm version
# 3. Restores config
# 4. Tests openclaw startup

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BACKUP_DIR="$REPO_ROOT/backup-openclaw-$(date +%Y%m%d-%H%M%S)"

# Compose project/service names must match scripts/asb's convention (SCRUM-92),
# not Docker Compose's directory-derived default. This script previously used
# no -p flag (defaulting to a "docker_"-prefixed project from the compose
# file's parent dir) and targeted a service named "agentshroud" — neither
# matches the real running stack ("agentshroud"/"agentshroud-bot" project,
# "openclaw" service, container_name agentshroud-openclaw), so every command
# below failed against a real install.
if [ "$USER" = "agentshroud-bot" ]; then
  PROJECT="agentshroud-bot"
else
  PROJECT="agentshroud"
fi
COMPOSE="docker compose -f $REPO_ROOT/docker/docker-compose.yml -p $PROJECT"
CONFIG_VOLUME="${PROJECT}_agentshroud-config"

echo "=== OpenClaw Update Script ==="
echo "Repository: $REPO_ROOT"
echo "Compose project: $PROJECT"
echo "Backup directory: $BACKUP_DIR"
echo

# 1. Create backup directory
echo "1. Creating backup directory..."
mkdir -p "$BACKUP_DIR"
echo "✓ Created: $BACKUP_DIR"
echo

# 2. Export openclaw config volume
echo "2. Backing up OpenClaw config..."
docker run --rm \
  -v "$CONFIG_VOLUME":/data \
  -v "$BACKUP_DIR":/backup \
  alpine tar czf /backup/openclaw-config.tar.gz -C /data .
echo "✓ Config backed up to $BACKUP_DIR"
echo

# 3. Stop openclaw container
echo "3. Stopping openclaw container..."
$COMPOSE stop openclaw
$COMPOSE rm -f openclaw
echo "✓ Container stopped and removed"
echo

# 4. Restore config volume
echo "4. Restoring config..."
docker run --rm \
  -v "$CONFIG_VOLUME":/data \
  -v "$BACKUP_DIR":/backup \
  alpine sh -c "rm -rf /data/* && tar xzf /backup/openclaw-config.tar.gz -C /data"
echo "✓ Config restored"
echo

# 5. Rebuild and start openclaw with latest npm version
echo "5. Rebuilding openclaw container with latest version..."
echo "   (This will pull latest openclaw@latest from npm)"
$COMPOSE up -d --build openclaw
echo "✓ Container rebuilt and started"
echo

# 6. Wait for service to be healthy
echo "6. Waiting for openclaw to become healthy (60s)..."
sleep 60
echo

# 7. Check status and logs
echo "7. Checking openclaw status..."
$COMPOSE ps openclaw
echo

echo "8. Recent logs:"
$COMPOSE logs openclaw --tail=15
echo

echo "=== Update Complete ==="
echo "Backup saved to: $BACKUP_DIR"
echo
echo "If you encounter issues, restore from backup:"
echo "  bash scripts/restore-backup.sh $BACKUP_DIR"
