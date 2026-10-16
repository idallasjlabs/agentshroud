---
type: community
cohesion: 0.29
members: 7
---

# PermissionLevel

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-test_default_write()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_explicit_config()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_pattern_delete()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_pattern_list()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_pattern_read()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_pattern_sensitive()]] - code - gateway/tests/test_mcp_permissions.py
- [[TestInferPermission]] - code - gateway/tests/test_mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PermissionLevel
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_MCPPermissionManager]]

## Top bridge nodes
- [[TestInferPermission]] - degree 12, connects to 1 community
