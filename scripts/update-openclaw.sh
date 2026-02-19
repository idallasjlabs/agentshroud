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

echo "=== OpenClaw Update Script ==="
echo "Repository: $REPO_ROOT"
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
  -v docker_openclaw-config:/data \
  -v "$BACKUP_DIR":/backup \
  alpine tar czf /backup/openclaw-config.tar.gz -C /data .
echo "✓ Config backed up to $BACKUP_DIR"
echo

# 3. Stop openclaw container
echo "3. Stopping openclaw container..."
docker compose -f "$REPO_ROOT/docker/docker-compose.yml" stop openclaw
docker compose -f "$REPO_ROOT/docker/docker-compose.yml" rm -f openclaw
echo "✓ Container stopped and removed"
echo

# 4. Restore config volume
echo "4. Restoring config..."
docker run --rm \
  -v docker_openclaw-config:/data \
  -v "$BACKUP_DIR":/backup \
  alpine sh -c "rm -rf /data/* && tar xzf /backup/openclaw-config.tar.gz -C /data"
echo "✓ Config restored"
echo

# 5. Rebuild and start openclaw with latest npm version
echo "5. Rebuilding openclaw container with latest version..."
echo "   (This will pull latest openclaw@latest from npm)"
docker compose -f "$REPO_ROOT/docker/docker-compose.yml" up -d --build openclaw
echo "✓ Container rebuilt and started"
echo

# 6. Wait for service to be healthy
echo "6. Waiting for openclaw to become healthy (60s)..."
sleep 60
echo

# 7. Check status and logs
echo "7. Checking openclaw status..."
docker compose -f "$REPO_ROOT/docker/docker-compose.yml" ps openclaw
echo

echo "8. Recent logs:"
docker compose -f "$REPO_ROOT/docker/docker-compose.yml" logs openclaw --tail=15
echo

echo "=== Update Complete ==="
echo "Backup saved to: $BACKUP_DIR"
echo
echo "If you encounter issues, restore from backup:"
echo "  bash scripts/restore-backup.sh $BACKUP_DIR"
