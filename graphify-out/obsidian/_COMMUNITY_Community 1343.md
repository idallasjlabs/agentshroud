---
type: community
members: 4
---

# Community 1343

**Members:** 4 nodes

## Members
- [[Bot Container (starts with ZERO 1Password access)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Gateway Container (has service account)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[POST credentialsop-proxy endpoint]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[op_proxy_read_with_retry() (cascading retries 5s,10s,15s,30s,60s)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1343
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 320]]

## Top bridge nodes
- [[op_proxy_read_with_retry() (cascading retries 5s,10s,15s,30s,60s)]] - degree 2, connects to 1 community