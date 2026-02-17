#!/bin/bash
# OpenClaw entrypoint - setup browsers on first run, then start OpenClaw

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

# Run startup script as node user (no privilege drop needed - already set USER in Dockerfile)
echo "[entrypoint] Starting OpenClaw..."
exec /usr/local/bin/start-openclaw.sh
