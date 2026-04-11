#!/usr/bin/env bash
# One-time Atlassian OAuth 2.0 setup for the idallasj tenant.
# Opens browser consent page, captures authorization code, exchanges for
# access + refresh tokens, and caches them for mcp-atlassian to use.
#
# IMPORTANT: When the browser opens, make sure you are logged in as
#            therealidallasj@gmail.com — NOT any other Atlassian account.
#
# Run once:  .llm_settings/mcp-servers/atlassian/idallasj/oauth-setup.sh
# After success, /mcp → reconnect atlassian-idallasj in Claude Code.

set -euo pipefail

_OP_VAULT="Agent Shroud Bot Credentials"
_OP_ITEM="Google [therealidallasj]"

CLIENT_ID="$(op read "op://${_OP_VAULT}/${_OP_ITEM}/atlassian client id")"
CLIENT_SECRET="$(op read "op://${_OP_VAULT}/${_OP_ITEM}/atlassian secret")"

if [ -z "${CLIENT_ID}" ] || [ -z "${CLIENT_SECRET}" ]; then
  echo "ERROR: could not read OAuth credentials from 1Password vault '${_OP_VAULT}'" >&2
  exit 1
fi

exec uvx mcp-atlassian --oauth-setup \
  --jira-url "https://idallasj.atlassian.net" \
  --oauth-client-id "${CLIENT_ID}" \
  --oauth-client-secret "${CLIENT_SECRET}" \
  --oauth-redirect-uri "http://localhost:8182/callback" \
  --oauth-scope "read:jira-work write:jira-work read:jira-user offline_access" \
  --oauth-cloud-id "04064eb6-a6cd-46cf-93fe-410711108f1f"
