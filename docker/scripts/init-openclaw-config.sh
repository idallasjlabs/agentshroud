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
