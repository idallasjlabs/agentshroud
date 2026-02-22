#!/bin/bash
# Restore AgentShroud from backup
# Usage: restore-backup.sh <backup-directory>

set -euo pipefail

BACKUP_DIR="${1:-}"

if [ -z "$BACKUP_DIR" ] || [ ! -d "$BACKUP_DIR" ]; then
  echo "Usage: restore-backup.sh <backup-directory>"
  echo
  echo "Available backups:"
  ls -dt backup-* 2>/dev/null || echo "  (none found)"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "=== AgentShroud Backup Restore ==="
echo "Restoring from: $BACKUP_DIR"
echo

# Stop containers
echo "1. Stopping containers..."
docker compose -f "$REPO_ROOT/docker/docker-compose.yml" down
echo "✓ Containers stopped"
echo

# Restore volumes
echo "2. Restoring volumes..."

if [ -f "$BACKUP_DIR/openclaw-config.tar.gz" ]; then
  docker run --rm \
    -v docker_agentshroud-config:/data \
    -v "$BACKUP_DIR":/backup \
    alpine sh -c "rm -rf /data/* && tar xzf /backup/openclaw-config.tar.gz -C /data"
  echo "  ✓ openclaw-config"
fi

if [ -f "$BACKUP_DIR/gateway-data.tar.gz" ]; then
  docker run --rm \
    -v docker_gateway-data:/data \
    -v "$BACKUP_DIR":/backup \
    alpine sh -c "rm -rf /data/* && tar xzf /backup/gateway-data.tar.gz -C /data"
  echo "  ✓ gateway-data"
fi

if [ -f "$BACKUP_DIR/openclaw-workspace.tar.gz" ]; then
  docker run --rm \
    -v docker_agentshroud-workspace:/data \
    -v "$BACKUP_DIR":/backup \
    alpine sh -c "rm -rf /data/* && tar xzf /backup/openclaw-workspace.tar.gz -C /data"
  echo "  ✓ openclaw-workspace"
fi

if [ -f "$BACKUP_DIR/openclaw-ssh.tar.gz" ]; then
  docker run --rm \
    -v docker_agentshroud-ssh:/data \
    -v "$BACKUP_DIR":/backup \
    alpine sh -c "rm -rf /data/* && tar xzf /backup/openclaw-ssh.tar.gz -C /data"
  echo "  ✓ openclaw-ssh"
fi

echo "✓ Volumes restored"
echo

# Start containers
echo "3. Starting containers..."
docker compose -f "$REPO_ROOT/docker/docker-compose.yml" up -d
echo "✓ Containers started"
echo

echo "4. Waiting for services to become healthy (60s)..."
sleep 60
echo

echo "5. Container status:"
docker compose -f "$REPO_ROOT/docker/docker-compose.yml" ps
echo

echo "=== Restore Complete ==="
