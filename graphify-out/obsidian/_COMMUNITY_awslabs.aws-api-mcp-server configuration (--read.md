---
type: community
cohesion: 0.73
members: 10
---

# awslabs.aws-api-mcp-server configuration (--read

**Cohesion:** 0.73 - tightly connected
**Members:** 10 nodes

## Members
- [[fail()_5]] - code - scripts/verify-proxy.sh
- [[info()_2]] - code - scripts/verify-proxy.sh
- [[pass()_3]] - code - scripts/verify-proxy.sh
- [[run_bypass()]] - code - scripts/verify-proxy.sh
- [[run_canary()_1]] - code - scripts/verify-proxy.sh
- [[run_chain()]] - code - scripts/verify-proxy.sh
- [[run_full()]] - code - scripts/verify-proxy.sh
- [[run_quick()]] - code - scripts/verify-proxy.sh
- [[verify-proxy.sh]] - code - scripts/verify-proxy.sh
- [[verify-proxy.sh script]] - code - scripts/verify-proxy.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/awslabsaws-api-mcp-server_configuration_--read
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_RBACConfig]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_test_bots_ssh_exec_wrapper.py]]
- 1 edge to [[_COMMUNITY_.send()]]

## Top bridge nodes
- [[run_canary()_1]] - degree 11, connects to 4 communities
- [[run_quick()]] - degree 9, connects to 3 communities
- [[run_chain()]] - degree 8, connects to 2 communities
- [[verify-proxy.sh]] - degree 10, connects to 1 community
- [[run_full()]] - degree 10, connects to 1 community