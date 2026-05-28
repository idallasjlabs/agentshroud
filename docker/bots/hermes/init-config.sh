#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# Hermes Agent first-boot config materialisation.
# Merges AgentShroud-managed defaults from /app/config-defaults/hermes/ into
# /opt/data/ (Hermes' persistent data directory, backed by the hermes-config volume).
# This script is idempotent — it only writes files that do not already exist.

set -euo pipefail

DEFAULTS_DIR="/app/config-defaults/hermes"
DATA_DIR="/opt/data"

echo "[hermes-init] Checking config..."

# config.yaml — Hermes primary config file
# First-boot: seed from template if absent.
# Upgrade path: if present but missing telegram.extra.base_url (added in v1.4.0
# to route Telegram API calls through AgentShroud gateway:8080/telegram-api/),
# replace it so EgressFilter does not block api.telegram.org CONNECT requests.
if [ ! -f "${DATA_DIR}/config.yaml" ]; then
    cp "${DEFAULTS_DIR}/config.yaml.tmpl" "${DATA_DIR}/config.yaml"
    echo "[hermes-init] Seeded config.yaml from defaults"
elif ! grep -q "telegram-api/bot" "${DATA_DIR}/config.yaml" 2>/dev/null; then
    cp "${DEFAULTS_DIR}/config.yaml.tmpl" "${DATA_DIR}/config.yaml"
    echo "[hermes-init] Upgraded config.yaml: added telegram.extra.base_url for AgentShroud gateway routing"
else
    echo "[hermes-init] config.yaml already exists and is current — skipping"
fi

# SOUL.md — bot identity file
if [ ! -f "${DATA_DIR}/SOUL.md" ]; then
    cp "${DEFAULTS_DIR}/SOUL.md" "${DATA_DIR}/SOUL.md"
    echo "[hermes-init] Seeded SOUL.md from defaults"
else
    echo "[hermes-init] SOUL.md already exists — skipping"
fi

# Cron jobs — seed default job set on first boot
if [ ! -f "${DATA_DIR}/cron/jobs.yaml" ]; then
    mkdir -p "${DATA_DIR}/cron"
    cp "${DEFAULTS_DIR}/cron/jobs.yaml" "${DATA_DIR}/cron/jobs.yaml"
    echo "[hermes-init] Seeded cron/jobs.yaml from defaults"
else
    echo "[hermes-init] cron/jobs.yaml already exists — skipping"
fi

echo "[hermes-init] Config init complete"
