---
type: community
cohesion: 0.15
members: 13
---

# agent_cve_registry.py

**Cohesion:** 0.15 - loosely connected
**Members:** 13 nodes

## Members
- [[Collaborator Setup Checklist]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
- [[Executive Summary_13]] - document - docs/security/SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST.md
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

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agent_cve_registrypy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_GroupConfig]]
- 1 edge to [[_COMMUNITY_Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT (3)]]

## Top bridge nodes
- [[SECRETS_USAGE_AND_COLLABORATOR_CHECKLIST]] - degree 5, connects to 3 communities
- [[Secret Management Hierarchy (1Password → Docker Secrets → Env)]] - degree 2, connects to 1 community
