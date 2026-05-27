#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# AgentShroud startup wrapper for Hermes Agent.
# Exports secrets from Docker secret files, then execs hermes gateway run.

set -euo pipefail

# Telegram bot token (Hermes-specific — separate bot from OpenClaw)
if [ -f "/run/secrets/hermes_telegram_bot_token" ]; then
    export TELEGRAM_BOT_TOKEN="$(cat /run/secrets/hermes_telegram_bot_token)"
    echo "[hermes-startup] Loaded Telegram bot token"
elif [ -n "${TELEGRAM_BOT_TOKEN:-}" ]; then
    echo "[hermes-startup] Using TELEGRAM_BOT_TOKEN from environment"
else
    echo "[hermes-startup] WARNING: No Telegram bot token configured — Telegram channel disabled"
fi

# Slack tokens (socket mode — matches OpenClaw's Slack integration pattern)
if [ -f "/run/secrets/slack_bot_token_hermes" ] && [ -s "/run/secrets/slack_bot_token_hermes" ]; then
    export SLACK_BOT_TOKEN="$(cat /run/secrets/slack_bot_token_hermes)"
    echo "[hermes-startup] Loaded Slack bot token"
fi
if [ -f "/run/secrets/slack_app_token_hermes" ] && [ -s "/run/secrets/slack_app_token_hermes" ]; then
    export SLACK_APP_TOKEN="$(cat /run/secrets/slack_app_token_hermes)"
    echo "[hermes-startup] Loaded Slack app token"
fi

# Brave Search API key (shared with gateway, same key)
if [ -f "/run/secrets/brave_api_key" ] && [ -s "/run/secrets/brave_api_key" ]; then
    export BRAVE_API_KEY="$(cat /run/secrets/brave_api_key)"
    echo "[hermes-startup] Loaded Brave Search API key"
fi

# Anthropic OAuth token (cloud model — routed through gateway:8080)
if [ -f "/run/secrets/anthropic_oauth_token" ] && [ -s "/run/secrets/anthropic_oauth_token" ]; then
    export ANTHROPIC_API_KEY="$(cat /run/secrets/anthropic_oauth_token)"
    echo "[hermes-startup] Loaded Anthropic token"
fi

# Init config on first boot (idempotent)
/usr/local/bin/init-hermes-config.sh

echo "[hermes-startup] Starting Hermes Agent gateway..."
exec hermes gateway run
