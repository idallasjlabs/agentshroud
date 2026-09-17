---
type: community
cohesion: 0.40
members: 5
---

# TestOwnerAccess

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[.test_owner_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_any_unknown_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_can_use_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[.test_owner_denied_tools_is_empty()]] - code - gateway/tests/test_tool_acl.py
- [[TestOwnerAccess]] - code - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOwnerAccess
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]

## Top bridge nodes
- [[TestOwnerAccess]] - degree 5, connects to 1 community