---
type: community
members: 5
---

# TestAdminAccess

**Members:** 5 nodes

## Members
- [[dot-test_admin_blocked_from_private_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_admin_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_can_use_collaborator_tool()]] - code - gateway/tests/test_tool_acl.py
- [[dot-test_admin_denied_tools_contains_private()]] - code - gateway/tests/test_tool_acl.py
- [[TestAdminAccess]] - code - gateway/tests/test_tool_acl.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAdminAccess
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_tool_acl.py]]

## Top bridge nodes
- [[TestAdminAccess]] - degree 5, connects to 1 community
