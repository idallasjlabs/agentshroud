---
type: community
members: 10
---

# Community 1424

**Members:** 10 nodes

## Members
- [[.enforcer()]] - code - gateway/tests/test_tool_acl.py
- [[.test_per_minute_limit_exceeded_blocks()]] - code - gateway/tests/test_tool_acl.py
- [[.test_per_user_isolation()]] - code - gateway/tests/test_tool_acl.py
- [[.test_under_threshold_passes()]] - code - gateway/tests/test_tool_acl.py
- [[.test_unlisted_tool_always_passes()]] - code - gateway/tests/test_tool_acl.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1424
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 6]]
- 2 edges to [[_COMMUNITY_Community 194]]
- 2 edges to [[_COMMUNITY_Community 11]]
- 1 edge to [[_COMMUNITY_Community 196]]

## Top bridge nodes
- [[TestToolRateLimiting]] - degree 11, connects to 4 communities
- [[.enforcer()]] - degree 2, connects to 1 community