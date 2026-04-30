#!/usr/bin/env bash
set -euo pipefail

export NODE_OPTIONS="--no-deprecation ${NODE_OPTIONS:-}"

if ! command -v npx &>/dev/null; then
    [ -s "$HOME/.nvm/nvm.sh" ]         && . "$HOME/.nvm/nvm.sh" --no-use
    [ -s "/usr/local/nvm/nvm.sh" ]     && . "/usr/local/nvm/nvm.sh" --no-use
    [ -s "/usr/share/nvm/init-nvm.sh" ] && . "/usr/share/nvm/init-nvm.sh"
fi

# Free the OAuth callback port if a stale process is holding it
lsof -ti :3736 2>/dev/null | xargs kill -9 2>/dev/null || true

echo ""
echo "┌─────────────────────────────────────────────────────────┐"
echo "│  HEADLESS AUTH INSTRUCTIONS                             │"
echo "│                                                         │"
echo "│  1. In a separate terminal on your LOCAL machine, run:  │"
echo "│     ssh -L 3736:localhost:3736 <this-server>            │"
echo "│                                                         │"
echo "│  2. Copy the URL that appears below and open it         │"
echo "│     in your local browser                               │"
echo "│                                                         │"
echo "│  3. Complete the Atlassian OAuth flow                   │"
echo "│     The token will be cached for future runs            │"
echo "└─────────────────────────────────────────────────────────┘"
echo ""

exec npx -y mcp-remote https://mcp.atlassian.com/v1/mcp \
    2> >(tee /tmp/atlassian-auth-${USER}.log >&2)
