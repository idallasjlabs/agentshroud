---
type: community
cohesion: 0.25
members: 8
---

# PermissionLevel

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-test_allowed_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_denied_agent()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_disabled_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_not_in_allowlist()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_trust_sufficient_for_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_trust_too_low_for_server()]] - code - gateway/tests/test_mcp_permissions.py
- [[dot-test_unknown_server_default_allow()]] - code - gateway/tests/test_mcp_permissions.py
- [[TestServerAccess]] - code - gateway/tests/test_mcp_permissions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PermissionLevel
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_MCPPermissionManager]]

## Top bridge nodes
- [[TestServerAccess]] - degree 13, connects to 1 community
