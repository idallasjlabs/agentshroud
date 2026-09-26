---
source_file: "docker/config/openclaw/apply-patches.js"
type: "code"
community: "AuditChain"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AuditChain
---

# apply-patches.js

## Connections
- [[COLLABORATOR_IDS]] - `contains` [EXTRACTED]
- [[COLLAB_LOCAL_INFO_ONLY]] - `contains` [EXTRACTED]
- [[GROUP_CHAT_IDS]] - `contains` [EXTRACTED]
- [[LOCAL_PROVIDER_KEY derivation (mode-derived, not ref-derived)]] - `references` [EXTRACTED]
- [[LOCAL_PROVIDER_KEY mode-derivation design]] - `rationale_for` [EXTRACTED]
- [[MODEL_MODE]] - `contains` [EXTRACTED]
- [[OpenClaw Cron Jobs Configuration]] - `conceptually_related_to` [INFERRED]
- [[Per-chat group agent + binding reconciliation (Patch 1e)]] - `references` [EXTRACTED]
- [[Telegram channel tokendmPolicyallowlist patch (Patch 3)]] - `references` [EXTRACTED]
- [[Telegram channel-wide fallback binding design]] - `rationale_for` [EXTRACTED]
- [[Telegram dmPolicy=open security tradeoff]] - `rationale_for` [EXTRACTED]
- [[_COLLAB_TOOL_DENY]] - `contains` [EXTRACTED]
- [[_COLLAB_TOOL_DENY_FULL_ACCESS]] - `contains` [EXTRACTED]
- [[_GROUP_TOOL_DENY]] - `contains` [EXTRACTED]
- [[_is_global_full_access]] - `contains` [EXTRACTED]
- [[_rawGroupIds]] - `contains` [EXTRACTED]
- [[_resolveCollabDenyList()]] - `contains` [EXTRACTED]
- [[_resolveCollabToolConfig()]] - `references` [EXTRACTED]
- [[_userOverrides]] - `contains` [EXTRACTED]
- [[allAllowedOrigins]] - `contains` [EXTRACTED]
- [[allowedOrigins]] - `contains` [EXTRACTED]
- [[cIdx]] - `contains` [EXTRACTED]
- [[config]] - `contains` [EXTRACTED]
- [[desiredAllowFrom]] - `contains` [EXTRACTED]
- [[desiredProvider]] - `contains` [EXTRACTED]
- [[extraOrigins]] - `contains` [EXTRACTED]
- [[fs_2]] - `contains` [EXTRACTED]
- [[gpIdx]] - `contains` [EXTRACTED]
- [[hasChannelWideFallback]] - `contains` [EXTRACTED]
- [[hasMain]] - `contains` [EXTRACTED]
- [[hasOwnerBinding]] - `contains` [EXTRACTED]
- [[init-openclaw-config.sh]] - `calls` [EXTRACTED]
- [[missingOrigins]] - `contains` [EXTRACTED]
- [[missingProxies]] - `contains` [EXTRACTED]
- [[path_2]] - `contains` [EXTRACTED]
- [[providerModels]] - `contains` [EXTRACTED]
- [[staleGroupBindings]] - `contains` [EXTRACTED]
- [[trustedProxies]] - `contains` [EXTRACTED]
- [[{ profile _genericProfile, deny _genericCollabDeny }]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AuditChain