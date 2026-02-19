#!/bin/bash
# Update AgentShroud to latest from main branch
# This script:
# 1. Backs up current volumes
# 2. Pulls latest code
# 3. Rebuilds containers
# 4. Restores config
# 5. Runs system test

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
BACKUP_DIR="$REPO_ROOT/backup-$(date +%Y%m%d-%H%M%S)"

echo "=== AgentShroud Update Script ==="
echo "Repository: $REPO_ROOT"
echo "Backup directory: $BACKUP_DIR"
echo

# 1. Create backup directory
echo "1. Creating backup directory..."
mkdir -p "$BACKUP_DIR"
echo "✓ Created: $BACKUP_DIR"
echo

# 2. Export current volumes
echo "2. Backing up volumes..."
docker run --rm \
  -v docker_openclaw-config:/data \
  -v "$BACKUP_DIR":/backup \
  alpine tar czf /backup/openclaw-config.tar.gz -C /data .
echo "  ✓ openclaw-config"

docker run --rm \
  -v docker_gateway-data:/data \
  -v "$BACKUP_DIR":/backup \
  alpine tar czf /backup/gateway-data.tar.gz -C /data .
echo "  ✓ gateway-data"

docker run --rm \
  -v docker_openclaw-workspace:/data \
  -v "$BACKUP_DIR":/backup \
  alpine tar czf /backup/openclaw-workspace.tar.gz -C /data .
echo "  ✓ openclaw-workspace"

docker run --rm \
  -v docker_openclaw-ssh:/data \
  -v "$BACKUP_DIR":/backup \
  alpine tar czf /backup/openclaw-ssh.tar.gz -C /data .
echo "  ✓ openclaw-ssh"

echo "✓ Volumes backed up to $BACKUP_DIR"
echo

# 3. Pull latest code
echo "3. Pulling latest code from main..."
cd "$REPO_ROOT"
git fetch origin main
git checkout main
git pull origin main
echo "✓ Code updated to latest main"
echo

# 4. Stop containers
echo "4. Stopping containers..."
docker compose -f docker/docker-compose.yml down
echo "✓ Containers stopped"
echo

# 5. Restore volumes
echo "5. Restoring volumes..."
docker run --rm \
  -v docker_openclaw-config:/data \
  -v "$BACKUP_DIR":/backup \
  alpine sh -c "rm -rf /data/* && tar xzf /backup/openclaw-config.tar.gz -C /data"
echo "  ✓ openclaw-config"

docker run --rm \
  -v docker_gateway-data:/data \
  -v "$BACKUP_DIR":/backup \
  alpine sh -c "rm -rf /data/* && tar xzf /backup/gateway-data.tar.gz -C /data"
echo "  ✓ gateway-data"

docker run --rm \
  -v docker_openclaw-workspace:/data \
  -v "$BACKUP_DIR":/backup \
  alpine sh -c "rm -rf /data/* && tar xzf /backup/openclaw-workspace.tar.gz -C /data"
echo "  ✓ openclaw-workspace"

docker run --rm \
  -v docker_openclaw-ssh:/data \
  -v "$BACKUP_DIR":/backup \
  alpine sh -c "rm -rf /data/* && tar xzf /backup/openclaw-ssh.tar.gz -C /data"
echo "  ✓ openclaw-ssh"

echo "✓ Volumes restored"
echo

# 6. Rebuild and start containers
echo "6. Rebuilding and starting containers..."
docker compose -f docker/docker-compose.yml up -d --build
echo "✓ Containers rebuilt and started"
echo

# 7. Wait for services to be healthy
echo "7. Waiting for services to become healthy (60s)..."
sleep 60
echo

# 8. Run system test
echo "8. Running system test..."
if [ -f "$REPO_ROOT/test-system.sh" ]; then
  bash "$REPO_ROOT/test-system.sh"
else
  echo "⚠ test-system.sh not found, skipping system test"
  docker compose -f docker/docker-compose.yml ps
fi
echo

echo "=== Update Complete ==="
echo "Backup saved to: $BACKUP_DIR"
echo
echo "If you encounter issues, restore from backup:"
echo "  bash scripts/restore-backup.sh $BACKUP_DIR"
