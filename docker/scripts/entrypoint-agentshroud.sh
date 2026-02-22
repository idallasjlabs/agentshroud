#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# AgentShroud entrypoint - setup browsers on first run, then start AgentShroud

set -euo pipefail

echo "[entrypoint] Checking Playwright browsers..."

# Copy browsers from root cache to volume if not already there (first run only)
if [ ! -d "/home/node/.cache/ms-playwright/chromium-1208" ] && [ -d "/root/.cache/ms-playwright" ]; then
    echo "[entrypoint] First run detected - copying Playwright browsers from /root to volume..."
    cp -r /root/.cache/ms-playwright/* /home/node/.cache/ms-playwright/
    chown -R node:node /home/node/.cache/ms-playwright
    echo "[entrypoint] ✓ Browsers installed ($(du -sh /home/node/.cache/ms-playwright 2>/dev/null | cut -f1))"
elif [ -d "/home/node/.cache/ms-playwright/chromium-1208" ]; then
    echo "[entrypoint] ✓ Browsers already installed ($(du -sh /home/node/.cache/ms-playwright 2>/dev/null | cut -f1))"
else
    echo "[entrypoint] Warning: No Playwright browsers found in /root/.cache/ms-playwright"
fi

# Apply required OpenClaw config (agents, bindings, cron jobs)
echo "[entrypoint] Applying OpenClaw config..."
/usr/local/bin/init-openclaw-config.sh

# Run startup script as node user (no privilege drop needed - already set USER in Dockerfile)
echo "[entrypoint] Starting AgentShroud..."
exec /usr/local/bin/start-agentshroud.sh
