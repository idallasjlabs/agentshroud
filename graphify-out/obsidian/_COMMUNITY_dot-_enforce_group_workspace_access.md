---
type: community
cohesion: 0.50
members: 4
---

# ._enforce_group_workspace_access

**Cohesion:** 0.50 - moderately connected
**Members:** 4 nodes

## Members
- [[dot-_enforce_group_workspace_access()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_group_workspace_manager()]] - code - gateway/proxy/telegram_proxy.py
- [[Build a GroupWorkspaceManager from current teamsRBAC config.          Returns a]] - rationale - gateway/proxy/telegram_proxy.py
- [[Fail-closed member check for a group-context inbound message.          Returns T]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_enforce_group_workspace_access
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[dot-_group_workspace_manager()]] - degree 4, connects to 2 communities
- [[dot-_enforce_group_workspace_access()]] - degree 4, connects to 1 community
