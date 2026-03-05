#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# init-openclaw-config.sh — Bootstrap OpenClaw config from image defaults.
#
# Called by entrypoint-agentshroud.sh before OpenClaw starts.
# Safe to run on every container startup (all operations are idempotent).
#
# What this does:
#   1. Bootstraps cron/jobs.json from image defaults (only on fresh volume)
#   2. Patches openclaw.json for required agent routing (always, idempotent)
#   3. Manages workspace brand/identity files
#   4. Refreshes SSH config (approved host allowlist) from image defaults

set -euo pipefail

DEFAULTS_DIR="/app/config-defaults/openclaw"
OPENCLAW_DIR="/home/node/.openclaw"

# ── 1. cron/jobs.json — bootstrap only if missing ────────────────────────────
# We only copy on first run (missing file) so that live CLI changes via
# `openclaw cron edit` are not overwritten on restart.
# If you want to forcibly reset cron jobs, delete the volume file and restart.

CRON_DIR="${OPENCLAW_DIR}/cron"
CRON_JOBS="${CRON_DIR}/jobs.json"

mkdir -p "${CRON_DIR}"

if [ ! -f "${CRON_JOBS}" ]; then
  cp "${DEFAULTS_DIR}/cron/jobs.json" "${CRON_JOBS}"
  echo "[init] ✓ Bootstrapped cron/jobs.json from image defaults (first run)"
else
  echo "[init] ✓ cron/jobs.json already present — skipping (use CLI to modify)"
fi

# ── 2. openclaw.json — patch required fields (idempotent) ────────────────────
# Applies agents.list and bindings patches every startup.
# All other fields (Telegram token, channel config, etc.) are preserved.

node "${DEFAULTS_DIR}/apply-patches.js" "${OPENCLAW_DIR}/openclaw.json"

# Security: harden config and state dir permissions
chmod 700 "${OPENCLAW_DIR}" 2>/dev/null || true
chmod 600 "${OPENCLAW_DIR}/openclaw.json" 2>/dev/null || true

# ── 3. Workspace brand/identity files ────────────────────────────────────────
# BRAND.md    — always refreshed from image (authoritative trademark & brand rules)
# IDENTITY.md — seeded on first run only (bot evolves this over time)
# AGENTS.md   — append "read BRAND.md" instruction if not already present

WORKSPACE_DIR="${OPENCLAW_DIR}/workspace"
mkdir -p "${WORKSPACE_DIR}"

# BRAND.md: always overwrite — it's the authoritative source from the repo.
cp "${DEFAULTS_DIR}/workspace/BRAND.md" "${WORKSPACE_DIR}/BRAND.md"
echo "[init] ✓ Refreshed BRAND.md (trademark & brand rules)"

# IDENTITY.md: seed only if missing or still the unfilled OpenClaw default.
IDENTITY_FILE="${WORKSPACE_DIR}/IDENTITY.md"
if [ ! -f "${IDENTITY_FILE}" ] || grep -q "_Fill this in during your first conversation_" "${IDENTITY_FILE}" 2>/dev/null; then
  cp "${DEFAULTS_DIR}/workspace/IDENTITY.md" "${IDENTITY_FILE}"
  echo "[init] ✓ Seeded IDENTITY.md with AgentShroud identity"
else
  echo "[init] ✓ IDENTITY.md already set — skipping"
fi

# AGENTS.md: add "read BRAND.md" to the session startup checklist if absent.
AGENTS_FILE="${WORKSPACE_DIR}/AGENTS.md"
if [ -f "${AGENTS_FILE}" ] && ! grep -q "BRAND.md" "${AGENTS_FILE}" 2>/dev/null; then
  # Insert after the last numbered item in the "Every Session" section
  sed -i 's/4\. \*\*If in MAIN SESSION\*\*/5. Read `BRAND.md` — AgentShroud trademark \& communication standards\n4. **If in MAIN SESSION**/' "${AGENTS_FILE}"
  echo "[init] ✓ Added BRAND.md to AGENTS.md session startup checklist"
else
  echo "[init] ✓ AGENTS.md already references BRAND.md — skipping"
fi

# ── 4. Memory persistence — backup/restore across fresh installs ─────────────
# Memory files (MEMORY.md, memory/*.md) are the bot's continuity.
# They live on the workspace volume, which survives rebuilds but not volume
# deletion. A host-mounted backup directory provides durability across
# fresh installs, volume resets, and machine migrations.

MEMORY_BACKUP_DIR="/app/memory-backup"
MEMORY_DIR="${WORKSPACE_DIR}/memory"
MEMORY_FILE="${WORKSPACE_DIR}/MEMORY.md"

# Restore: if workspace has no memory but backup exists, restore it
if [ -d "${MEMORY_BACKUP_DIR}" ] && [ "$(ls -A ${MEMORY_BACKUP_DIR} 2>/dev/null)" ]; then
  if [ ! -f "${MEMORY_FILE}" ] && [ ! -d "${MEMORY_DIR}" ]; then
    echo "[init] Fresh workspace detected — restoring memory from backup"
    # Restore MEMORY.md
    if [ -f "${MEMORY_BACKUP_DIR}/MEMORY.md" ]; then
      cp "${MEMORY_BACKUP_DIR}/MEMORY.md" "${MEMORY_FILE}"
      echo "[init] ✓ Restored MEMORY.md"
    fi
    # Restore memory/ directory
    if [ -d "${MEMORY_BACKUP_DIR}/memory" ]; then
      mkdir -p "${MEMORY_DIR}"
      cp -r "${MEMORY_BACKUP_DIR}/memory/"* "${MEMORY_DIR}/" 2>/dev/null || true
      echo "[init] ✓ Restored memory/ directory ($(ls ${MEMORY_DIR} | wc -l) files)"
    fi
    # Restore USER.md, TOOLS.md if they exist in backup
    for f in USER.md TOOLS.md HEARTBEAT.md; do
      if [ -f "${MEMORY_BACKUP_DIR}/${f}" ]; then
        cp "${MEMORY_BACKUP_DIR}/${f}" "${WORKSPACE_DIR}/${f}"
        echo "[init] ✓ Restored ${f}"
      fi
    done
  else
    echo "[init] ✓ Memory already present — no restore needed"
  fi
else
  echo "[init] ✓ No memory backup found (first-ever install or backup not mounted)"
fi

# Backup: save current memory to backup directory (runs every startup)
if [ -d "${MEMORY_BACKUP_DIR}" ]; then
  if [ -f "${MEMORY_FILE}" ] || [ -d "${MEMORY_DIR}" ]; then
    [ -f "${MEMORY_FILE}" ] && cp "${MEMORY_FILE}" "${MEMORY_BACKUP_DIR}/MEMORY.md"
    if [ -d "${MEMORY_DIR}" ]; then
      mkdir -p "${MEMORY_BACKUP_DIR}/memory"
      cp -r "${MEMORY_DIR}/"* "${MEMORY_BACKUP_DIR}/memory/" 2>/dev/null || true
    fi
    for f in USER.md TOOLS.md HEARTBEAT.md; do
      [ -f "${WORKSPACE_DIR}/${f}" ] && cp "${WORKSPACE_DIR}/${f}" "${MEMORY_BACKUP_DIR}/${f}"
    done
    echo "[init] ✓ Memory backed up to ${MEMORY_BACKUP_DIR}"
  fi
fi

# ── 4. SSH config — always refresh from image (approved host allowlist) ──────
# Authoritative allowlist of approved SSH hosts.
# Overwrites on every startup so repo changes take effect on next restart.
# To add a new host: update docker/config/ssh/config in the repo, rebuild image.

SSH_CONFIG_SRC="/app/config-defaults/ssh/config"
SSH_CONFIG_DST="/home/node/.ssh/config"

if [ -f "${SSH_CONFIG_SRC}" ]; then
  mkdir -p "/home/node/.ssh"
  cp "${SSH_CONFIG_SRC}" "${SSH_CONFIG_DST}"
  chmod 600 "${SSH_CONFIG_DST}"
  echo "[init] ✓ Refreshed SSH config (approved host allowlist)"
else
  echo "[init] ⚠ SSH config defaults not found — skipping"
fi

# ── 5. Memory persistence — backup & restore ─────────────────────────────────
# Memory files (MEMORY.md, memory/*.md) are the bot continuity across sessions.
# They live on the workspace volume, but must survive:
#   - docker compose down -v  (volume deletion)
#   - Fresh installs on new machines
#   - Container image rebuilds
#
# Strategy: host-mounted /app/memory-backup is a bind mount to the repo
# memory-backup/ directory. On every startup, we:
#   1. Restore from backup if workspace memory is empty (fresh volume)
#   2. Backup current memory to the host mount (on every startup)

MEMORY_BACKUP_DIR="/app/memory-backup"
WORKSPACE_MEMORY="${WORKSPACE_DIR}/memory"
WORKSPACE_MEMORY_FILE="${WORKSPACE_DIR}/MEMORY.md"

if [ -d "${MEMORY_BACKUP_DIR}" ]; then
  # Restore: if workspace has no memory but backup does, restore it
  if [ ! -f "${WORKSPACE_MEMORY_FILE}" ] && [ -f "${MEMORY_BACKUP_DIR}/MEMORY.md" ]; then
    echo "[init] Fresh volume detected — restoring memory from backup"
    cp "${MEMORY_BACKUP_DIR}/MEMORY.md" "${WORKSPACE_MEMORY_FILE}"
    echo "[init]   Restored MEMORY.md"
  fi

  if [ ! -d "${WORKSPACE_MEMORY}" ] || [ -z "$(ls -A "${WORKSPACE_MEMORY}" 2>/dev/null)" ]; then
    if [ -d "${MEMORY_BACKUP_DIR}/memory" ] && [ -n "$(ls -A "${MEMORY_BACKUP_DIR}/memory" 2>/dev/null)" ]; then
      mkdir -p "${WORKSPACE_MEMORY}"
      cp -r "${MEMORY_BACKUP_DIR}/memory/"* "${WORKSPACE_MEMORY}/" 2>/dev/null || true
      echo "[init]   Restored memory/ directory"
    fi
  fi

  # Backup: snapshot current memory to host mount (runs every startup)
  if [ -f "${WORKSPACE_MEMORY_FILE}" ]; then
    mkdir -p "${MEMORY_BACKUP_DIR}/memory"
    cp "${WORKSPACE_MEMORY_FILE}" "${MEMORY_BACKUP_DIR}/MEMORY.md"
    if [ -d "${WORKSPACE_MEMORY}" ]; then
      cp -r "${WORKSPACE_MEMORY}/"* "${MEMORY_BACKUP_DIR}/memory/" 2>/dev/null || true
    fi
    echo "[init] Memory backed up to host mount (survives volume resets)"
  fi
else
  echo "[init] Memory backup mount not available — memory NOT persisted to host"
fi
