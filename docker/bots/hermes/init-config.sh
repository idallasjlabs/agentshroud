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
# Upgrade path: if present but missing telegram.extra.base_url (added in v1.1.0
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

# ── Native cron jobs — seed on first boot ──────────────────────────────────
# Uses `hermes cron create` (writes to Hermes's internal db) rather than
# the YAML file, which is not read natively by hermes-agent.
# Idempotent: stamp file prevents re-seeding on every restart.
_CRON_STAMP="${DATA_DIR}/.hermes-cron-seeded"
if [ ! -f "${_CRON_STAMP}" ]; then
    echo "[hermes-init] Seeding native cron jobs..."
    hermes cron create \
        --name "AgentShroud Daily Check-in" \
        --deliver telegram \
        "0 14 * * *" \
        "Daily AgentShroud check-in from Hermes. Report current date/time, brief status of active tasks, and anything noteworthy from today. Under 150 words, send via Telegram to Isaiah." \
        2>/dev/null && echo "[hermes-init] Created Daily Check-in job" || echo "[hermes-init] WARN: Daily Check-in job failed"

    hermes cron create \
        --name "AgentShroud Weekly Summary" \
        --deliver telegram \
        "0 18 * * 5" \
        "Weekly summary from Hermes: key topics this week, skills learned or created, and what to focus on next week. Format concisely, deliver via Telegram." \
        2>/dev/null && echo "[hermes-init] Created Weekly Summary job" || echo "[hermes-init] WARN: Weekly Summary job failed"

    hermes cron create \
        --name "Weekly Kaizen Review" \
        --deliver telegram \
        "0 17 * * 5" \
        "Friday 5 PM weekly kaizen review (Hermes). What shipped this week? What caused friction? What process improvements would most help AgentShroud development? Format: SHIPPED / FRICTION / IMPROVE. Be specific and actionable." \
        2>/dev/null && echo "[hermes-init] Created Weekly Kaizen job" || echo "[hermes-init] WARN: Weekly Kaizen job failed"

    hermes cron create \
        --name "Monthly Chaos Engineering Drill" \
        --deliver telegram \
        "0 9 1 * *" \
        "First of month chaos engineering drill (Hermes). Simulate one failure scenario for AgentShroud involving Hermes: gateway crash, volume corruption, bot disconnect, or dependency outage. Describe failure mode, detection method, blast radius, and recovery procedure." \
        2>/dev/null && echo "[hermes-init] Created Monthly Chaos Drill job" || echo "[hermes-init] WARN: Monthly Chaos Drill job failed"

    hermes cron create \
        --name "Daily Memory Journal" \
        --deliver local \
        "55 23 * * *" \
        "Nightly memory consolidation. Summarize today's active projects, pending tasks, decisions made, and key facts for continuity. Store in memory. Silent operation." \
        2>/dev/null && echo "[hermes-init] Created Daily Memory Journal job" || echo "[hermes-init] WARN: Daily Memory Journal job failed"

    touch "${_CRON_STAMP}"
    echo "[hermes-init] Cron jobs seeded"
else
    echo "[hermes-init] Cron jobs already seeded — skipping"
fi

# ── GitHub MCP server — wire on first boot if PAT is available ─────────────
# Requires github_pat Docker secret (stored in 1Password "Agent Shroud Bot Credentials").
# If the secret is absent or empty, this step is skipped silently.
_MCP_STAMP="${DATA_DIR}/.hermes-mcp-github-added"
if [ ! -f "${_MCP_STAMP}" ]; then
    if [ -f "/run/secrets/github_pat" ] && [ -s "/run/secrets/github_pat" ]; then
        _github_pat="$(cat /run/secrets/github_pat)"
        if hermes mcp list 2>/dev/null | grep -q "github"; then
            echo "[hermes-init] GitHub MCP server already configured — skipping"
            touch "${_MCP_STAMP}"
        else
            echo "[hermes-init] Adding GitHub MCP server..."
            HOME="${DATA_DIR}" hermes mcp add github \
                --command npx \
                --args -y @modelcontextprotocol/server-github \
                --env "GITHUB_PERSONAL_ACCESS_TOKEN=${_github_pat}" \
                2>/dev/null \
                && touch "${_MCP_STAMP}" \
                && echo "[hermes-init] GitHub MCP server added" \
                || echo "[hermes-init] WARN: GitHub MCP add failed (will retry on next boot)"
        fi
    else
        echo "[hermes-init] github_pat secret absent — skipping GitHub MCP setup"
        echo "[hermes-init]   To enable: store github_pat in 1Password 'Agent Shroud Bot Credentials' vault"
        echo "[hermes-init]   and run: asb rebuild full"
    fi
else
    echo "[hermes-init] GitHub MCP already configured — skipping"
fi

echo "[hermes-init] Config init complete"
