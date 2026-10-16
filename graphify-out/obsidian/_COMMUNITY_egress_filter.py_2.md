---
type: community
cohesion: 0.20
members: 10
---

# egress_filter.py

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[AGENTSHROUD_CONFIG_1]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_CONFIG.md
- [[AGENTSHROUD_CONFIG]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_CONFIG.md
- [[AGENTSHROUD_MODE_1]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_MODE.md
- [[Default Search Order (when NOT set)]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_CONFIG.md
- [[Description_12]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_CONFIG.md
- [[HTTP_PROXY]] - document - docs/vault/04 - Environment Variables/HTTP_PROXY.md
- [[Related Notes_70]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_CONFIG.md
- [[Usage_130]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_CONFIG.md
- [[When to Set]] - document - docs/vault/04 - Environment Variables/AGENTSHROUD_CONFIG.md
- [[agentshroud.yaml_1]] - document - docs/vault/03 - Configuration/agentshroud.yaml.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/egress_filterpy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 1 edge to [[_COMMUNITY_egress_filter.py_3]]
- 1 edge to [[_COMMUNITY_egress_filter.py_4]]
- 1 edge to [[_COMMUNITY_egress_filter.py_5]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_WebProxyConfig]]
- 1 edge to [[_COMMUNITY_AuditChain]]
- 1 edge to [[_COMMUNITY_egress_filter.py_1]]
- 1 edge to [[_COMMUNITY_SSH Config]]

## Top bridge nodes
- [[agentshroud.yaml_1]] - degree 8, connects to 5 communities
- [[AGENTSHROUD_MODE_1]] - degree 6, connects to 5 communities
- [[HTTP_PROXY]] - degree 4, connects to 3 communities
