#!/bin/bash
# Backup AgentShroud bot memory from running container
# Runs every 4 hours via launchd, keeps last 6 snapshots
set -euo pipefail

CONTAINER="agentshroud-bot"
BACKUP_DIR="/Users/ijefferson.admin/Development/agentshroud/memory-backups"
MAX_BACKUPS=6
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE="$BACKUP_DIR/memory-$TIMESTAMP.tar.gz"
TMP_DIR="/tmp/agentshroud-memory-$$"

mkdir -p "$BACKUP_DIR"

# Check container is running
if ! docker inspect "$CONTAINER" --format '{{.State.Running}}' 2>/dev/null | grep -q true; then
  echo "[$(date)] SKIP: $CONTAINER not running" >&2
  exit 0
fi

mkdir -p "$TMP_DIR"

# Snapshot workspace (MEMORY.md, USER.md, TOOLS.md, HEARTBEAT.md, memory/ daily logs)
docker cp "$CONTAINER:/home/node/.openclaw/workspace/." "$TMP_DIR/"

# Also grab workspace-collaborator if it exists
docker cp "$CONTAINER:/home/node/.openclaw/workspace-collaborator" "$TMP_DIR/workspace-collaborator" 2>/dev/null || true

# Compress
tar czf "$BACKUP_FILE" -C "$TMP_DIR" .

# Cleanup temp
rm -rf "$TMP_DIR"

# Rotate: keep only newest MAX_BACKUPS
cd "$BACKUP_DIR"
ls -1t memory-*.tar.gz 2>/dev/null | tail -n +$((MAX_BACKUPS + 1)) | xargs rm -f 2>/dev/null || true

echo "[$(date)] Backup OK: $BACKUP_FILE ($(du -h "$BACKUP_FILE" | cut -f1))"
