---
type: community
cohesion: 0.50
members: 4
---

# Gateway Container (has service account)

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[Bot Container (starts with ZERO 1Password access)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[Gateway Container (has service account)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[POST credentialsop-proxy endpoint]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg
- [[op_proxy_read_with_retry() (cascading retries 5s,10s,15s,30s,60s)]] - concept - docs/diagrams/images/diagram-12-credential-flow.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Gateway_Container_has_service_account
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]]

## Top bridge nodes
- [[op_proxy_read_with_retry() (cascading retries 5s,10s,15s,30s,60s)]] - degree 2, connects to 1 community
