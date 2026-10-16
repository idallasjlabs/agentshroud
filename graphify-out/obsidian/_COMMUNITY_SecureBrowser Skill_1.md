---
type: community
cohesion: 0.67
members: 6
---

# SecureBrowser Skill

**Cohesion:** 0.67 - moderately connected
**Members:** 6 nodes

## Members
- [[cmd_persist]] - code - scripts/tailscale-serve.sh
- [[cmd_start]] - code - scripts/tailscale-serve.sh
- [[cmd_status]] - code - scripts/tailscale-serve.sh
- [[cmd_stop]] - code - scripts/tailscale-serve.sh
- [[tailscale-serve.sh]] - code - scripts/tailscale-serve.sh
- [[tailscale-serve.sh script]] - code - scripts/tailscale-serve.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecureBrowser_Skill
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py_1]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]

## Top bridge nodes
- [[cmd_start]] - degree 5, connects to 2 communities
- [[tailscale-serve.sh]] - degree 6, connects to 1 community
