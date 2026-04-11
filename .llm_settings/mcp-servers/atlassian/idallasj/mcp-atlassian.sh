#!/usr/bin/env bash
set -euo pipefail

# Suppress Node deprecation warnings (punycode, etc.)
export NODE_OPTIONS="--no-deprecation ${NODE_OPTIONS:-}"

_OP_VAULT="Agent Shroud Bot Credentials"
_OP_ITEM="Google [therealidallasj]"

CLIENT_ID="$(op read "op://${_OP_VAULT}/${_OP_ITEM}/atlassian client id" 2>/dev/null || true)"
CLIENT_SECRET="$(op read "op://${_OP_VAULT}/${_OP_ITEM}/atlassian secret" 2>/dev/null || true)"

if [ -z "${CLIENT_ID}" ] || [ -z "${CLIENT_SECRET}" ]; then
  echo "[atlassian-idallasj] ERROR: missing OAuth credentials in vault '${_OP_VAULT}'" >&2
  echo "[atlassian-idallasj]   Expected fields in item '${_OP_ITEM}':" >&2
  echo "[atlassian-idallasj]     'atlassian client id'  and  'atlassian secret'" >&2
  echo "[atlassian-idallasj]   Run: op signin && op item get '${_OP_ITEM}' --vault '${_OP_VAULT}'" >&2
  echo "[atlassian-idallasj]   First-time auth: .llm_settings/mcp-servers/atlassian/idallasj/oauth-setup.sh" >&2
  exit 1
fi

# sooperset/mcp-atlassian — OAuth 2.0 against idallasj.atlassian.net
# Account:  therealidallasj@gmail.com
# Tenant:   https://idallasj.atlassian.net
# Cloud ID: 04064eb6-a6cd-46cf-93fe-410711108f1f
# Callback: http://localhost:8182/callback
# First-time auth: run oauth-setup.sh in this directory
exec uvx mcp-atlassian \
  --transport stdio \
  --jira-url "https://idallasj.atlassian.net" \
  --oauth-client-id "${CLIENT_ID}" \
  --oauth-client-secret "${CLIENT_SECRET}" \
  --oauth-redirect-uri "http://localhost:8182/callback" \
  --oauth-scope "read:jira-work write:jira-work read:jira-user offline_access" \
  --oauth-cloud-id "04064eb6-a6cd-46cf-93fe-410711108f1f"
