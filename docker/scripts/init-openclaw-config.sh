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
