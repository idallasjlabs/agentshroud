---
type: community
cohesion: 0.07
members: 26
---

# Community 335

**Cohesion:** 0.07 - loosely connected
**Members:** 26 nodes

## Members
- [[dot-test_admin_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_collaborator_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_denied_tools_contains_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_allowed_tools_does_not_include_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_can_use_allowed_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_tools_includes_admin_and_private()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_collaborator_denied_unknown_by_default()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_any_unknown_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_can_use_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_owner_denied_tools_is_empty()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_per_minute_limit_exceeded_blocks()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_per_user_isolation()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_under_threshold_passes()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_unlisted_tool_always_passes()]] - code - gateway/tests/test_tool_acl.py
- [[Calls within limits should pass.]] - rationale - gateway/tests/test_tool_acl.py
- [[Exceeding per-minute limit should return False.]] - rationale - gateway/tests/test_tool_acl.py
- [[Rate limits are tracked independently per user.]] - rationale - gateway/tests/test_tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestCollaboratorAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py
- [[TestToolRateLimiting]] - code - gateway/tests/test_tool_acl.py
- [[Tools not in the rate-limit map should always pass.]] - rationale - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_335
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 134]]

## Top bridge nodes
- [[TestCollaboratorAccess]] - degree 7, connects to 1 community
- [[TestToolRateLimiting]] - degree 7, connects to 1 community
- [[TestAdminAccess]] - degree 5, connects to 1 community
- [[TestOwnerAccess]] - degree 5, connects to 1 community