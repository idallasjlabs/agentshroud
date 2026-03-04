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

# Make BACKUP_DIR absolute (important for docker volume mounts)
BACKUP_DIR="$(cd "$BACKUP_DIR" && pwd)"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "=== AgentShroud Backup Restore ==="
echo "Restoring from: $BACKUP_DIR"
echo
echo "⚠️  WARNING: This will DESTROY all current data and replace it with the backup."
echo "   All container volumes will be wiped and restored from: $BACKUP_DIR"
echo
read -p "Type 'RESTORE' to confirm (anything else aborts): " CONFIRM
if [ "$CONFIRM" != "RESTORE" ]; then
  echo "Aborted."
  exit 0
fi
echo

# Stop containers
echo "1. Stopping containers..."
docker compose -f "$REPO_ROOT/docker/docker-compose.yml" down
echo "✓ Containers stopped"
echo

echo "2. Restoring volumes..."

restore_tar_to_volume() {
  local tar_name="$1"
  local volume_name="$2"
  local label="$3"

  if [ -f "$BACKUP_DIR/$tar_name" ]; then
    echo "  - Restoring $label from $tar_name -> $volume_name"

    docker run --rm \
      -v "${volume_name}":/data \
      -v "${BACKUP_DIR}":/backup:ro \
      alpine sh -euc "
        rm -rf /data/* &&
        tar xzf \"/backup/${tar_name}\" -C /data
      "

    echo "    ✓ $label"
  else
    echo "  - (skip) $label: $tar_name not found in backup"
  fi
}

# If none of the known tarballs exist, fail fast with a helpful message
if ! ls "$BACKUP_DIR"/*.tar.gz >/dev/null 2>&1; then
  echo
  echo "ERROR: No .tar.gz files found in:"
  echo "  $BACKUP_DIR"
  echo
  echo "Tip: choose one of the listed backup-* directories, e.g.:"
  echo "  scripts/restore-backup.sh backup-openclaw-20260228-204949"
  exit 1
fi

restore_tar_to_volume "openclaw-config.tar.gz"     "docker_agentshroud-config"     "openclaw-config"
restore_tar_to_volume "gateway-data.tar.gz"        "docker_gateway-data"          "gateway-data"
restore_tar_to_volume "openclaw-workspace.tar.gz"  "docker_agentshroud-workspace" "openclaw-workspace"
restore_tar_to_volume "openclaw-ssh.tar.gz"        "docker_agentshroud-ssh"       "openclaw-ssh"

echo "✓ Volume restore step complete"
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
