---
type: community
cohesion: 0.12
members: 16
---

# iMessage Integration Fix - Using imsg + imessage-exporter

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[Collaborator Setup Checklist]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Executive Summary_11]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Files intentionally not for collaborators]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Optional local tooling]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Required for local model-profile persistence]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Required for standard Docker runtime]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Required if using 1Password-backed secret retrieval]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Required if using external LLM providers]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Restore Priority After Clean Build]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Root `.env`]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Secret Management Hierarchy (1Password → Docker Secrets → Env)]] - rationale - docs/security/container-policy.md
- [[Secrets Usage and Collaborator Checklist]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Wazuh CVE-2025-24016 (CVSS 9.9)]] - concept - docs/security/security-supply-chain.md
- [[container-policy]] - document - docs/security/container-policy.md
- [[security-supply-chain]] - document - docs/security/security-supply-chain.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/iMessage_Integration_Fix_-_Using_imsg__imessage-exporter
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_gatewayingest_apimain.py (hermes-dashboard HTTP + WebSocket reverse proxy)]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_2]]
- 1 edge to [[_COMMUNITY_Kill Switch]]
- 1 edge to [[_COMMUNITY_Container Security Policy — AgentShroud]]
- 1 edge to [[_COMMUNITY_Detailed Profiles]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Value Proposition - Revised_1]]
- 1 edge to [[_COMMUNITY_iMessage Integration Fix - Using imsg + imessage-exporter_1]]
- 1 edge to [[_COMMUNITY_Git History Purge Plan]]

## Top bridge nodes
- [[container-policy]] - degree 6, connects to 4 communities
- [[SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST]] - degree 5, connects to 3 communities
- [[security-supply-chain]] - degree 4, connects to 2 communities
