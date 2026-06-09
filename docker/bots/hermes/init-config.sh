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

# ── Workspace seeding — competitive-intel files ────────────────────────────
# Seeds competitive-analysis.md and reports/ dir into /opt/data/workspace/
# on first boot. Idempotent via separate stamp.
_WS_STAMP="${DATA_DIR}/.hermes-workspace-seeded"
if [ ! -f "${_WS_STAMP}" ]; then
    mkdir -p "${DATA_DIR}/workspace/reports"
    if [ ! -f "${DATA_DIR}/workspace/competitive-analysis.md" ]; then
        cp "${DEFAULTS_DIR}/workspace/competitive-analysis.md" \
           "${DATA_DIR}/workspace/competitive-analysis.md"
        echo "[hermes-init] Seeded workspace/competitive-analysis.md"
    fi
    touch "${_WS_STAMP}"
    echo "[hermes-init] Workspace seeded"
else
    echo "[hermes-init] Workspace already seeded — skipping"
fi

# ── Native cron jobs — idempotent seed on every boot ───────────────────────
# Uses `hermes cron create` (writes to Hermes's internal db) rather than
# the YAML file, which is not read natively by hermes-agent.
# Idempotent: _seed_cron deletes any existing job with the same name before
# creating, so re-seeds on upgrade never accumulate duplicates.
# (Prior stamp-file gating v1/v2/v3 caused triplication on each version bump
# because hermes cron create has no dedup — removed in favour of this approach.)

_seed_cron() {
    local _name="$1" _deliver="$2" _schedule="$3" _prompt="$4"
    # Remove all pre-existing jobs with this exact name, then create one canonical copy.
    hermes cron list 2>/dev/null \
      | awk -v name="$_name" '
            /^  [a-f0-9]{12} \[/ { id = $1; next }
            index($0, "Name:") && index($0, name) { print id }
          ' \
      | xargs -r -n1 hermes cron delete >/dev/null 2>&1 || true
    hermes cron create --name "$_name" --deliver "$_deliver" "$_schedule" "$_prompt" \
      2>/dev/null \
      && echo "[hermes-init] Seeded: $_name" \
      || echo "[hermes-init] WARN: seed failed: $_name"
}

echo "[hermes-init] Seeding native cron jobs (idempotent)..."

_seed_cron "AgentShroud Daily Check-in" "telegram" "0 14 * * *" \
    "Daily AgentShroud check-in from Hermes. Report current date/time, brief status of active tasks, and anything noteworthy from today. Under 150 words, send via Telegram to Isaiah."

_seed_cron "AgentShroud Weekly Summary" "telegram" "0 18 * * 5" \
    "Weekly summary from Hermes: key topics this week, skills learned or created, and what to focus on next week. Format concisely, deliver via Telegram."

_seed_cron "Weekly Kaizen Review" "telegram" "0 17 * * 5" \
    "Friday 5 PM weekly kaizen review (Hermes). What shipped this week? What caused friction? What process improvements would most help AgentShroud development? Format: SHIPPED / FRICTION / IMPROVE. Be specific and actionable."

_seed_cron "Monthly Chaos Engineering Drill" "telegram" "0 9 1 * *" \
    "First of month chaos engineering drill (Hermes). Simulate one failure scenario for AgentShroud involving Hermes: gateway crash, volume corruption, bot disconnect, or dependency outage. Describe failure mode, detection method, blast radius, and recovery procedure."

# SC2016: $(date) intentionally not expanded — agent evaluates at run time
# shellcheck disable=SC2016
_memory_journal_prompt='Nightly memory consolidation. Summarize today'"'"'s active projects, pending tasks, decisions made, and key facts for continuity. Append your summary to /opt/data/memories/journal-$(date +%Y-%m).md as a new dated section (use today'"'"'s date in YYYY-MM-DD format as the section heading). Create the file if it does not exist. Silent operation — no Telegram delivery.'
_seed_cron "Daily Memory Journal" "local" "55 23 * * *" "$_memory_journal_prompt"

_seed_cron "Weekly Hermes Stability Report" "telegram" "0 9 * * 1" \
    "Read /opt/data/logs/gateway-exit-diag.log (last 7 days entries) and /opt/data/.start-history (one epoch per line). Compute: total restarts this week, crashes per day as a sparkline (e.g. 0 0 2 0 1 0 3), longest stable window in hours, top 3 exit codes by frequency, any backoff pauses triggered (5-minute sleeps). Format as 'Hermes Weekly Stability — <date range>' in under 200 words. Send via Telegram. If log files do not exist, report that Hermes has been stable with no recorded exits this week."

# SC2016: $(date) intentionally not expanded — agent evaluates at run time
# shellcheck disable=SC2016
_competitive_landscape_prompt='Read /opt/data/workspace/competitive-analysis.md for research instructions. Execute the full 4-section competitive intelligence report. CRITICAL RULES: zero hallucinations — every company, product, and statistic must be verified against a live primary source. Exclude anything unverified. Every claim requires a working URL. Research competitors of AgentShroud (autonomous agent security tools — NOT the agents themselves). Verify GitHub star counts from live pages. Save report as /opt/data/workspace/reports/competitive-report-$(date +%Y-%m-%d).md (use today'"'"'s date in YYYY-MM-DD format). Append one-line summary to /opt/data/workspace/reports/trend-log.md. Silence is correct if nothing new is found; hallucination is a critical failure.'
_seed_cron "Hermes Competitive Landscape Update (AM/PM)" "local" "0 6,15 * * *" "$_competitive_landscape_prompt"

# SC2016: $(cat ...) in prompt is instructions to the agent, not a shell expansion
# shellcheck disable=SC2016
_competitive_email_prompt='Read the most recent competitive-report-*.md from /opt/data/workspace/reports/ (prefer today'"'"'s date in YYYY-MM-DD format). If no report exists, use body '"'"'No significant changes detected today.'"'"' Render as a clean HTML email with inline CSS only (white bg #ffffff, text #111111, links #1a73e8, code bg #f6f8fa). Write the rendered HTML to /tmp/competitive-email.html. Then run EXACTLY: /usr/local/bin/agentshroud-email-send.sh --html --subject '"'"'AgentShroud Hermes Competitive Intelligence'"'"' --body "$(cat /tmp/competitive-email.html)". The --html flag is mandatory — omitting it delivers raw markdown as plain text. Expect HTTP 200. On failure, report the full error via Telegram.'
_seed_cron "Hermes Competitive Intelligence Email (AM/PM)" "local" "0 7,16 * * *" "$_competitive_email_prompt"

# Ensure memory journal write directory exists on the persistent volume
mkdir -p "${DATA_DIR}/memories"

echo "[hermes-init] Cron jobs seeded"

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
