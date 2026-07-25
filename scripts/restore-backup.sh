#!/bin/bash
# Restore AgentShroud from backup
# Usage: restore-backup.sh [--yes] <backup-directory>
#
#   --yes   Skip the interactive "type RESTORE to confirm" prompt. For use by
#           automated callers only (scripts/update-agentshroud.sh's rollback
#           path) — manual/interactive use should omit this and keep the
#           confirmation gate.

set -euo pipefail

YES=0
BACKUP_DIR=""
for arg in "$@"; do
  case "$arg" in
    --yes) YES=1 ;;
    *) BACKUP_DIR="$arg" ;;
  esac
done

if [ -z "$BACKUP_DIR" ] || [ ! -d "$BACKUP_DIR" ]; then
  echo "Usage: restore-backup.sh [--yes] <backup-directory>"
  echo
  echo "Available backups:"
  ls -dt backup-* 2>/dev/null || echo "  (none found)"
  exit 1
fi

# Make BACKUP_DIR absolute (important for docker volume mounts)
BACKUP_DIR="$(cd "$BACKUP_DIR" && pwd)"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Compose project name must match scripts/asb's / scripts/update-agentshroud.sh's
# convention, not Docker Compose's directory-derived default — otherwise `down`/`up`
# target the wrong project entirely and volume names below resolve to the wrong,
# nonexistent (stale "docker_"-prefixed) volumes. See update-agentshroud.sh for the
# same derivation.
if [ "$USER" = "agentshroud-bot" ]; then
  PROJECT="agentshroud-bot"
else
  PROJECT="agentshroud"
fi
COMPOSE="docker compose -f $REPO_ROOT/docker/docker-compose.yml -p $PROJECT"

echo "=== AgentShroud Backup Restore ==="
echo "Restoring from: $BACKUP_DIR"
echo "Compose project: $PROJECT"
echo

if [ "$YES" -eq 1 ]; then
  echo "⚠️  --yes passed: skipping interactive confirmation (automated caller)."
else
  echo "⚠️  WARNING: This will DESTROY all current data and replace it with the backup."
  echo "   All container volumes will be wiped and restored from: $BACKUP_DIR"
  echo
  read -p "Type 'RESTORE' to confirm (anything else aborts): " CONFIRM
  if [ "$CONFIRM" != "RESTORE" ]; then
    echo "Aborted."
    exit 0
  fi
fi
echo

# Stop containers
echo "1. Stopping containers..."
$COMPOSE down
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

# Volume names are project-prefixed by Docker Compose (${PROJECT}_<volume-key> for
# any volume without an explicit `name:` override in docker-compose.yml) — NOT the
# stale "docker_" prefix this script previously (and incorrectly) hardcoded.
restore_tar_to_volume "openclaw-config.tar.gz"     "${PROJECT}_agentshroud-config"     "openclaw-config"
restore_tar_to_volume "gateway-data.tar.gz"        "${PROJECT}_gateway-data"           "gateway-data"
restore_tar_to_volume "openclaw-workspace.tar.gz"  "${PROJECT}_agentshroud-workspace"  "openclaw-workspace"
restore_tar_to_volume "openclaw-ssh.tar.gz"        "${PROJECT}_agentshroud-ssh"        "openclaw-ssh"

echo "✓ Volume restore step complete"
echo

# Start containers
echo "3. Starting containers..."
$COMPOSE up -d
echo "✓ Containers started"
echo

echo "4. Waiting for services to become healthy (60s)..."
sleep 60
echo

echo "5. Container status:"
$COMPOSE ps
echo

echo "=== Restore Complete ==="
