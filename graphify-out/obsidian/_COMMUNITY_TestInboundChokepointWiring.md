---
type: community
cohesion: 0.18
members: 11
---

# TestInboundChokepointWiring

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[dot-proxy()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_cross_group_member_blocked()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_disabled_gate_returns_none_manager()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_manager_is_wired()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_member_allowed_in_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_member_contextvar_preserved()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_non_member_blocked_in_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_non_member_contextvar_isolated_to_none()]] - code - gateway/tests/test_group_workspace_manager.py
- [[dot-test_owner_allowed_in_any_group()]] - code - gateway/tests/test_group_workspace_manager.py
- [[Simulate the chokepoint a non-member's active group id is cleared.]] - rationale - gateway/tests/test_group_workspace_manager.py
- [[TestInboundChokepointWiring]] - code - gateway/tests/test_group_workspace_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestInboundChokepointWiring
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy_1]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]

## Top bridge nodes
- [[TestInboundChokepointWiring]] - degree 17, connects to 3 communities
- [[dot-proxy()]] - degree 2, connects to 1 community
