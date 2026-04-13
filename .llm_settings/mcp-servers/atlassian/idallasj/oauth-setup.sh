#!/usr/bin/env bash
# One-time Atlassian OAuth 2.0 setup for the idallasj tenant.
# Opens browser consent page, captures authorization code, exchanges for
# access + refresh tokens, and caches them for mcp-atlassian to use.
#
# IMPORTANT: When the browser opens, make sure you are logged in as
#            therealidallasj@gmail.com — NOT any other Atlassian account.
#
# Credential resolution order:
#   1. ATLASSIAN_CLIENT_ID / ATLASSIAN_CLIENT_SECRET env vars already exported
#   2. .env file in this directory (sourced via `set -a`) — use this on Linux hosts
#   3. 1Password: op read 'op://Agent Shroud Bot Credentials/Google [therealidallasj]/...'
#
# Run once:  .llm_settings/mcp-servers/atlassian/idallasj/oauth-setup.sh
# After success: /mcp → reconnect atlassian-idallasj in Claude Code.

set -euo pipefail

_script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
_env_file="${_script_dir}/.env"

# Tier 2: source .env if present
if [ -f "${_env_file}" ]; then
  # shellcheck disable=SC1090
  set -a; source "${_env_file}"; set +a
fi

# Tier 3: 1Password fallback for any var still unset
if [ -z "${ATLASSIAN_CLIENT_ID:-}" ] && command -v op >/dev/null 2>&1; then
  ATLASSIAN_CLIENT_ID="$(op read 'op://Agent Shroud Bot Credentials/Google [therealidallasj]/atlassian client id' 2>/dev/null || true)"
fi

if [ -z "${ATLASSIAN_CLIENT_SECRET:-}" ] && command -v op >/dev/null 2>&1; then
  ATLASSIAN_CLIENT_SECRET="$(op read 'op://Agent Shroud Bot Credentials/Google [therealidallasj]/atlassian secret' 2>/dev/null || true)"
fi

if [ -z "${ATLASSIAN_CLIENT_ID:-}" ] || [ -z "${ATLASSIAN_CLIENT_SECRET:-}" ]; then
  echo "[oauth-setup] ERROR: ATLASSIAN_CLIENT_ID or ATLASSIAN_CLIENT_SECRET not available" >&2
  echo "[oauth-setup] Resolution order: env vars → ${_env_file} → 1Password" >&2
  echo "[oauth-setup]   Option 1: export ATLASSIAN_CLIENT_ID=... ATLASSIAN_CLIENT_SECRET=..." >&2
  echo "[oauth-setup]   Option 2: cp ${_script_dir}/.env.example ${_env_file} && edit" >&2
  echo "[oauth-setup]   Option 3: op signin  (vault 'Agent Shroud Bot Credentials', item 'Google [therealidallasj]')" >&2
  exit 1
fi

exec uvx mcp-atlassian --oauth-setup \
  --jira-url "https://idallasj.atlassian.net" \
  --oauth-client-id "${ATLASSIAN_CLIENT_ID}" \
  --oauth-client-secret "${ATLASSIAN_CLIENT_SECRET}" \
  --oauth-redirect-uri "http://localhost:8182/callback" \
  --oauth-scope "read:jira-work write:jira-work read:jira-user offline_access" \
  --oauth-cloud-id "04064eb6-a6cd-46cf-93fe-410711108f1f"
