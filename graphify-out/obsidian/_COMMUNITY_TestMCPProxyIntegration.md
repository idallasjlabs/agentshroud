---
type: community
members: 10
---

# TestMCPProxyIntegration

**Members:** 10 nodes

## Members
- [[dot-mcp_proxy_with_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_critical_tool_requires_approval()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_low_risk_tool_allowed()]] - code - gateway/tests/test_enhanced_approval.py
- [[dot-test_owner_bypass()_1]] - code - gateway/tests/test_enhanced_approval.py
- [[Create an MCP proxy with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test MCP proxy integration with approval queue.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test owner bypass for high-tier tools.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that critical tools are identified as requiring approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[Test that low-risk tools are allowed without approval.]] - rationale - gateway/tests/test_enhanced_approval.py
- [[TestMCPProxyIntegration]] - code - gateway/tests/test_enhanced_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMCPProxyIntegration
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 3 edges to [[_COMMUNITY_MCPToolCall]]
- 2 edges to [[_COMMUNITY_test_mcp_proxy.py]]

## Top bridge nodes
- [[TestMCPProxyIntegration]] - degree 8, connects to 3 communities
- [[dot-mcp_proxy_with_approval()]] - degree 4, connects to 2 communities
- [[dot-test_low_risk_tool_allowed()]] - degree 4, connects to 2 communities
- [[dot-test_owner_bypass()_1]] - degree 4, connects to 2 communities
- [[dot-test_critical_tool_requires_approval()]] - degree 3, connects to 1 community
