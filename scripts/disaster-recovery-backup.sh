#!/bin/bash
# AgentShroud Disaster Recovery Backup
# Creates an encrypted tarball of ALL non-repo config, secrets, volumes, and state.
#
# Usage:
#   ./scripts/disaster-recovery-backup.sh                    # default: ~/agentshroud-dr/
#   ./scripts/disaster-recovery-backup.sh /Volumes/USB/dr    # custom output dir
#
# Output:
#   <dest>/disaster-recovery-<date>.tar.gz.enc   (AES-256-CBC encrypted)
#   <dest>/disaster-recovery-<date>.manifest      (plaintext file list)
#
# Restore:
#   openssl enc -d -aes-256-cbc -pbkdf2 -in disaster-recovery-*.tar.gz.enc | tar xzf -
#
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
set -euo pipefail

REPO="/Users/ijefferson.admin/Development/agentshroud"
DEST="${1:-$HOME/agentshroud-dr}"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
STAGING="/tmp/agentshroud-dr-$$"
ARCHIVE="disaster-recovery-${TIMESTAMP}"

mkdir -p "$DEST" "$STAGING"
trap 'rm -rf "$STAGING"' EXIT

echo "═══════════════════════════════════════════════════"
echo " AgentShroud™ Disaster Recovery Backup"
echo " $(date)"
echo "═══════════════════════════════════════════════════"
echo ""

# ── 1. Configuration files ────────────────────────────
echo "[1/7] Configuration files..."
mkdir -p "$STAGING/config"
cp "$REPO/agentshroud.yaml"                          "$STAGING/config/" 2>/dev/null || echo "  ⚠ agentshroud.yaml not found"
cp "$REPO/docker/.env"                                "$STAGING/config/docker-env" 2>/dev/null || echo "  ⚠ docker/.env not found"
cp "$REPO/docker/docker-compose.yml"                  "$STAGING/config/" 2>/dev/null || true

# ── 2. Secrets (Docker secrets dir) ───────────────────
echo "[2/7] Secrets..."
mkdir -p "$STAGING/secrets/prod" "$STAGING/secrets/dev" "$STAGING/secrets/other"
# Production secrets
for f in "$REPO"/docker/secrets/*.txt; do
  [ -f "$f" ] && cp "$f" "$STAGING/secrets/prod/"
done
# Dev secrets
for f in "$REPO"/docker/agentshroud-dev-secrets/*.txt; do
  [ -f "$f" ] && cp "$f" "$STAGING/secrets/dev/"
done
# Other sensitive files
cp "$REPO/secrets/pihole_password.txt"                         "$STAGING/secrets/other/" 2>/dev/null || true
cp "$REPO/.llm_settings/mcp-servers/github/.env"               "$STAGING/secrets/other/github-mcp-env" 2>/dev/null || true
cp "$REPO/security_assessment/.assessment_env"                 "$STAGING/secrets/other/assessment-env" 2>/dev/null || true

# ── 3. SSH keys from Docker volume ────────────────────
echo "[3/7] SSH keys from Docker volume..."
mkdir -p "$STAGING/ssh"
if docker volume inspect agentshroud_agentshroud-ssh >/dev/null 2>&1 || \
   docker volume inspect agentshroud-ssh >/dev/null 2>&1; then
  docker run --rm \
    -v agentshroud_agentshroud-ssh:/ssh:ro \
    -v "$STAGING/ssh":/out \
    alpine sh -c "cp -a /ssh/* /out/ 2>/dev/null || cp -a /ssh/. /out/" 2>/dev/null || \
  docker run --rm \
    -v agentshroud-ssh:/ssh:ro \
    -v "$STAGING/ssh":/out \
    alpine sh -c "cp -a /ssh/* /out/ 2>/dev/null || cp -a /ssh/. /out/" 2>/dev/null || \
    echo "  ⚠ Could not extract SSH keys from volume"
else
  echo "  ⚠ SSH volume not found"
fi

# ── 4. Bot memory / workspace from Docker volume ─────
echo "[4/7] Bot workspace + memory..."
mkdir -p "$STAGING/workspace"
CONTAINER="agentshroud-bot"
if docker inspect "$CONTAINER" --format '{{.State.Running}}' 2>/dev/null | grep -q true; then
  docker cp "$CONTAINER:/home/node/.openclaw/workspace/." "$STAGING/workspace/" 2>/dev/null || true
  docker cp "$CONTAINER:/home/node/.openclaw/workspace-collaborator" "$STAGING/workspace/workspace-collaborator" 2>/dev/null || true
  docker cp "$CONTAINER:/home/node/.agentshroud/openclaw.json" "$STAGING/config/openclaw-runtime.json" 2>/dev/null || true
else
  echo "  ⚠ Bot container not running — using latest memory backup"
  LATEST_BACKUP=$(ls -t "$REPO"/memory-backups/memory-*.tar.gz 2>/dev/null | head -1)
  if [ -n "$LATEST_BACKUP" ]; then
    cp "$LATEST_BACKUP" "$STAGING/workspace/latest-memory-backup.tar.gz"
  else
    echo "  ⚠ No memory backups found"
  fi
fi

# Also grab all existing memory backups
mkdir -p "$STAGING/memory-backups"
cp "$REPO"/memory-backups/memory-*.tar.gz "$STAGING/memory-backups/" 2>/dev/null || true

# ── 5. Gateway data (audit ledger) from Docker volume ─
echo "[5/7] Gateway data (audit ledger)..."
mkdir -p "$STAGING/gateway-data"
GW_CONTAINER="agentshroud-gateway"
if docker inspect "$GW_CONTAINER" --format '{{.State.Running}}' 2>/dev/null | grep -q true; then
  docker cp "$GW_CONTAINER:/app/data/." "$STAGING/gateway-data/" 2>/dev/null || true
else
  echo "  ⚠ Gateway container not running — skipping ledger"
fi

# ── 6. LaunchAgent plist ──────────────────────────────
echo "[6/7] LaunchAgent plist..."
mkdir -p "$STAGING/launchd"
cp "$HOME/Library/LaunchAgents/com.agentshroud.memory-backup.plist" "$STAGING/launchd/" 2>/dev/null || \
  echo "  ⚠ LaunchAgent plist not found"

# ── 7. Create manifest ───────────────────────────────
echo "[7/7] Creating manifest and encrypted archive..."
(cd "$STAGING" && find . -type f | sort) > "$DEST/${ARCHIVE}.manifest"

# Create tarball
tar czf "$STAGING/${ARCHIVE}.tar.gz" -C "$STAGING" \
  config secrets ssh workspace memory-backups gateway-data launchd

# Encrypt with AES-256 (prompts for password)
echo ""
echo "Set an encryption password for the DR archive:"
openssl enc -aes-256-cbc -pbkdf2 -salt \
  -in "$STAGING/${ARCHIVE}.tar.gz" \
  -out "$DEST/${ARCHIVE}.tar.gz.enc"

# Summary
ARCHIVE_SIZE=$(du -sh "$DEST/${ARCHIVE}.tar.gz.enc" | cut -f1)
FILE_COUNT=$(wc -l < "$DEST/${ARCHIVE}.manifest")

echo ""
echo "═══════════════════════════════════════════════════"
echo " ✓ Disaster Recovery Backup Complete"
echo "═══════════════════════════════════════════════════"
echo ""
echo "  Archive:   $DEST/${ARCHIVE}.tar.gz.enc ($ARCHIVE_SIZE)"
echo "  Manifest:  $DEST/${ARCHIVE}.manifest ($FILE_COUNT files)"
echo ""
echo "  Restore:"
echo "    openssl enc -d -aes-256-cbc -pbkdf2 \\"
echo "      -in $DEST/${ARCHIVE}.tar.gz.enc | tar xzf - -C /tmp/restore"
echo ""
echo "  ⚠ Store this archive OFFLINE (USB, NAS, or encrypted cloud)."
echo "  ⚠ macOS Keychain secrets are NOT in this archive — back up via"
echo "    Time Machine or export from 1Password separately."
echo ""
