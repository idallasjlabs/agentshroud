---
type: community
cohesion: 0.25
members: 20
---

# egress_filter.py

**Cohesion:** 0.25 - loosely connected
**Members:** 20 nodes

## Members
- [[check()_12]] - code - scripts/preflight-check.sh
- [[fail()_3]] - code - scripts/tailscale-check.sh
- [[fail()_4]] - code - scripts/verify-proxy.sh
- [[info()_1]] - code - scripts/verify-proxy.sh
- [[infra-check.sh]] - code - scripts/infra-check.sh
- [[infra-check.sh script]] - code - scripts/infra-check.sh
- [[ok()_1]] - code - scripts/tailscale-check.sh
- [[pass()_2]] - code - scripts/verify-proxy.sh
- [[preflight-check.sh]] - code - scripts/preflight-check.sh
- [[preflight-check.sh script]] - code - scripts/preflight-check.sh
- [[run_bypass()]] - code - scripts/verify-proxy.sh
- [[run_canary()_1]] - code - scripts/verify-proxy.sh
- [[run_chain()]] - code - scripts/verify-proxy.sh
- [[run_full()]] - code - scripts/verify-proxy.sh
- [[run_quick()]] - code - scripts/verify-proxy.sh
- [[tailscale-check.sh]] - code - scripts/tailscale-check.sh
- [[tailscale-check.sh script]] - code - scripts/tailscale-check.sh
- [[verify-proxy.sh]] - code - scripts/verify-proxy.sh
- [[verify-proxy.sh script]] - code - scripts/verify-proxy.sh
- [[warn()_5]] - code - scripts/tailscale-check.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/egress_filterpy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig_2]]
- 1 edge to [[_COMMUNITY_ProxyDashboard]]

## Top bridge nodes
- [[run_canary()_1]] - degree 11, connects to 5 communities
- [[run_quick()]] - degree 9, connects to 3 communities
- [[run_chain()]] - degree 8, connects to 2 communities
- [[run_full()]] - degree 10, connects to 1 community
