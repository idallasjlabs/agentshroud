#!/bin/sh
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# /etc/cont-init.d/00-agentshroud-secrets.sh
#
# s6-overlay cont-init script — runs as root before any supervised service starts.
# Reads Docker secret files from /run/secrets/ and writes their values to
# /run/s6/container_environment/ so all supervised processes (dashboard, CMD) inherit
# them automatically via the with-contenv mechanism.
#
# This runs at priority 00 — before hermes' own 01-hermes-setup — so secrets are
# available from the very start of init.

set -eu

S6_ENV="/run/s6/container_environment"

inject() {
    local var="$1" file="$2"
    if [ -f "$file" ] && [ -s "$file" ]; then
        # Write value without trailing newline (s6 env values must not have trailing \n)
        printf '%s' "$(cat "$file")" > "$S6_ENV/$var"
        echo "[agentshroud-secrets] Injected $var"
    else
        echo "[agentshroud-secrets] Skipped $var (secret file absent or empty)"
    fi
}

# Hermes Telegram bot token (separate from OpenClaw's token)
inject TELEGRAM_BOT_TOKEN   /run/secrets/hermes_telegram_bot_token

# Slack integration (optional — socket mode)
inject SLACK_BOT_TOKEN      /run/secrets/slack_bot_token_hermes
inject SLACK_APP_TOKEN      /run/secrets/slack_app_token_hermes

# Brave Search (optional — shared key)
inject BRAVE_API_KEY        /run/secrets/brave_api_key

# Anthropic API key (routed through gateway:8080 via ANTHROPIC_BASE_URL in compose)
inject ANTHROPIC_API_KEY    /run/secrets/anthropic_oauth_token

# Hermes OpenAI-compatible API server key (gates port 8642)
inject API_SERVER_KEY       /run/secrets/hermes_api_key

# Healthchecks.io dead-man's-switch ping URL (optional — item 2)
inject HERMES_HEALTHCHECKS_URL  /run/secrets/hermes_healthchecks_url

# GitHub Personal Access Token (for GitHub MCP server — optional)
inject GITHUB_TOKEN                 /run/secrets/github_pat
inject GITHUB_PERSONAL_ACCESS_TOKEN /run/secrets/github_pat

# Hermes runs as uid 10000; cron jobs.json can be created root-owned on a prior
# boot, making the scheduler fail EACCES every tick. Reclaim ownership here.
if [ -d /opt/data/cron ]; then
    chown -R 10000:10000 /opt/data/cron 2>/dev/null || true
fi
