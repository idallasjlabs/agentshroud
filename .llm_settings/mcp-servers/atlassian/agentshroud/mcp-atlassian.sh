#!/usr/bin/env bash
set -euo pipefail

# Suppress Node deprecation warnings (punycode, etc.)
export NODE_OPTIONS="--no-deprecation ${NODE_OPTIONS:-}"

# ─────────────────────────────────────────────────────────────────────────────
# HARD RULE: Only the "Agent Shroud Bot Credentials" vault is permitted.
# Never read from the Personal / Private vault for AgentShroud credentials.
# ─────────────────────────────────────────────────────────────────────────────
_OP_VAULT="Agent Shroud Bot Credentials"
_OP_ITEM="AgentShroud - Google"

JIRA_TOKEN="$(op read "op://${_OP_VAULT}/${_OP_ITEM}/atlassian api token" 2>/dev/null || true)"

if [ -z "${JIRA_TOKEN}" ]; then
  echo "[atlassian-agentshroud] ERROR: missing API token in vault '${_OP_VAULT}'" >&2
  echo "[atlassian-agentshroud]   Expected field 'atlassian api token' in item '${_OP_ITEM}'" >&2
  echo "[atlassian-agentshroud]   Run: op signin && op item get '${_OP_ITEM}' --vault '${_OP_VAULT}'" >&2
  exit 1
fi

# sooperset/mcp-atlassian — API token auth against agentshroudai.atlassian.net
# Account: agentshroud.ai@gmail.com
# Tenant:  https://agentshroudai.atlassian.net
exec uvx mcp-atlassian \
  --transport stdio \
  --jira-url "https://agentshroudai.atlassian.net" \
  --jira-username "agentshroud.ai@gmail.com" \
  --jira-token "${JIRA_TOKEN}"
