---
type: community
members: 7
---

# TestSensitiveOps

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
TABLE source_file, type FROM #community/TestSensitiveOps
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_test_mcp_proxy.py]]

## Top bridge nodes
- [[TestSensitiveOps]] - degree 6, connects to 1 community
