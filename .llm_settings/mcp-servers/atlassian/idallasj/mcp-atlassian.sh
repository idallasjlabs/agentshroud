#!/usr/bin/env bash
# MCP wrapper — Atlassian (idallasj tenant)
#
# Tenant:   https://idallasj.atlassian.net
# Account:  therealidallasj@gmail.com
# Auth:     OAuth 2.0 (sooperset/mcp-atlassian)
# Cloud ID: 04064eb6-a6cd-46cf-93fe-410711108f1f
# Callback: http://localhost:8182/callback
# First-time auth: run oauth-setup.sh in this directory
#
# Credential resolution order:
#   1. ATLASSIAN_CLIENT_ID / ATLASSIAN_CLIENT_SECRET env vars already exported
#   2. .env file in this directory (sourced via `set -a`) — use this on Linux hosts
#   3. 1Password: op read 'op://Agent Shroud Bot Credentials/Google [therealidallasj]/...'
#
# Hard rule: only the "Agent Shroud Bot Credentials" vault is permitted.

set -euo pipefail

_script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
_env_file="${_script_dir}/.env"

# Tier 2: source .env if present (may set ATLASSIAN_CLIENT_ID and ATLASSIAN_CLIENT_SECRET)
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
  echo "[atlassian-idallasj] ERROR: ATLASSIAN_CLIENT_ID or ATLASSIAN_CLIENT_SECRET not available" >&2
  echo "[atlassian-idallasj] Resolution order: env vars → ${_env_file} → 1Password" >&2
  echo "[atlassian-idallasj]   Option 1: export ATLASSIAN_CLIENT_ID=... ATLASSIAN_CLIENT_SECRET=..." >&2
  echo "[atlassian-idallasj]   Option 2: cp ${_script_dir}/.env.example ${_env_file} && edit" >&2
  echo "[atlassian-idallasj]   Option 3: op signin  (vault 'Agent Shroud Bot Credentials', item 'Google [therealidallasj]')" >&2
  echo "[atlassian-idallasj]   First-time OAuth consent: ${_script_dir}/oauth-setup.sh" >&2
  exit 1
fi

exec uvx mcp-atlassian \
  --transport stdio \
  --jira-url "https://idallasj.atlassian.net" \
  --oauth-client-id "${ATLASSIAN_CLIENT_ID}" \
  --oauth-client-secret "${ATLASSIAN_CLIENT_SECRET}" \
  --oauth-redirect-uri "http://localhost:8182/callback" \
  --oauth-scope "read:jira-work write:jira-work read:jira-user offline_access" \
  --oauth-cloud-id "04064eb6-a6cd-46cf-93fe-410711108f1f"
