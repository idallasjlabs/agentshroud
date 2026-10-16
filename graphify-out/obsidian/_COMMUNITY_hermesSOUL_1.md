---
type: community
cohesion: 0.20
members: 10
---

# hermes/SOUL.md

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[dot-enforcer()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_per_minute_limit_exceeded_blocks()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_per_user_isolation()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_under_threshold_passes()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_unlisted_tool_always_passes()]] - code - gateway/tests/test_tool_acl.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/hermes/SOULmd
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_RBACConfig_1]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[TestToolRateLimiting]] - degree 11, connects to 3 communities
- [[dot-enforcer()]] - degree 2, connects to 1 community
