---
type: community
cohesion: 0.29
members: 7
---

# MCPPermissionManager

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-test_network_request_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_sensitive_blocked_strict_with_injection()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_sensitive_not_blocked_default()]] - code - gateway/tests/test_mcp_proxy.py
- [[dot-test_shell_command_flagged()]] - code - gateway/tests/test_mcp_proxy.py
- [[In strict mode, sensitive ops with injection ARE blocked.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[Sensitive ops are flagged but not blocked in default mode.]] - rationale - gateway/tests/test_mcp_proxy.py
- [[TestSensitiveOps]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPermissionManager
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 2 edges to [[_COMMUNITY_PermissionLevel]]
- 2 edges to [[_COMMUNITY_MCPInspector]]
- 1 edge to [[_COMMUNITY_MCPAuditTrail]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_2]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager_4]]

## Top bridge nodes
- [[TestSensitiveOps]] - degree 18, connects to 7 communities
