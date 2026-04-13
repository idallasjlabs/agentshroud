#!/usr/bin/env bash
# MCP wrapper — Atlassian (agentshroud tenant)
#
# Tenant:  https://agentshroudai.atlassian.net
# Account: agentshroud.ai@gmail.com
# Auth:    API token (sooperset/mcp-atlassian)
#
# Credential resolution order:
#   1. JIRA_TOKEN env var already exported in the caller's shell
#   2. .env file in this directory (sourced via `set -a`) — use this on Linux hosts
#   3. 1Password: op read 'op://Agent Shroud Bot Credentials/AgentShroud - Google/atlassian api token'
#
# Hard rule: only the "Agent Shroud Bot Credentials" vault is permitted.
# Never read from the Personal / Private vault for AgentShroud credentials.

set -euo pipefail

_script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
_env_file="${_script_dir}/.env"

# Tier 2: source .env if present (may set JIRA_TOKEN)
if [ -f "${_env_file}" ]; then
  # shellcheck disable=SC1090
  set -a; source "${_env_file}"; set +a
fi

# Tier 3: 1Password fallback if JIRA_TOKEN still unset
if [ -z "${JIRA_TOKEN:-}" ] && command -v op >/dev/null 2>&1; then
  JIRA_TOKEN="$(op read 'op://Agent Shroud Bot Credentials/AgentShroud - Google/atlassian api token' 2>/dev/null || true)"
fi

if [ -z "${JIRA_TOKEN:-}" ]; then
  echo "[atlassian-agentshroud] ERROR: JIRA_TOKEN not available" >&2
  echo "[atlassian-agentshroud] Resolution order: env var → ${_env_file} → 1Password" >&2
  echo "[atlassian-agentshroud]   Option 1: export JIRA_TOKEN=<token>  (before starting Claude/Codex/Gemini)" >&2
  echo "[atlassian-agentshroud]   Option 2: cp ${_script_dir}/.env.example ${_env_file} && edit" >&2
  echo "[atlassian-agentshroud]   Option 3: op signin  (vault 'Agent Shroud Bot Credentials', item 'AgentShroud - Google')" >&2
  exit 1
fi

exec uvx mcp-atlassian \
  --transport stdio \
  --jira-url "https://agentshroudai.atlassian.net" \
  --jira-username "agentshroud.ai@gmail.com" \
  --jira-token "${JIRA_TOKEN}"
