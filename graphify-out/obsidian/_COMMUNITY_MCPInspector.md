---
type: community
cohesion: 0.10
members: 27
---

# MCPInspector

**Cohesion:** 0.10 - loosely connected
**Members:** 27 nodes

## Members
- [[.__init__()_95]] - code - gateway/proxy/mcp_inspector.py
- [[._redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[._scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[._scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[._should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[.inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[.inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[.test_blocked_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_failed_entries()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_filter_by_agent()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_filter_by_server()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_filter_by_tool()]] - code - gateway/tests/test_mcp_proxy.py
- [[.test_generate_report()_1]] - code - gateway/tests/test_mcp_proxy.py
- [[Any_33]] - code - gateway/proxy/mcp_inspector.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspects MCP tool calls and responses for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[MCPInspector_1]] - code - gateway/proxy/mcp_inspector.py
- [[MCPProxy.process_tool_call]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy.process_tool_result]] - code - gateway/proxy/mcp_proxy.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py
- [[TestAuditQueries]] - code - gateway/tests/test_mcp_proxy.py
- [[inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[strict_inspector()]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPInspector
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_MCPToolCall]]
- 20 edges to [[_COMMUNITY_MCPServerConfig]]
- 18 edges to [[_COMMUNITY_StdioConnection]]
- 5 edges to [[_COMMUNITY_MCPToolResult]]
- 3 edges to [[_COMMUNITY_FakeProcess]]
- 3 edges to [[_COMMUNITY_PermissionLevel]]
- 3 edges to [[_COMMUNITY_MCPAuditTrail]]
- 2 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_TestInjectionDetection]]
- 1 edge to [[_COMMUNITY_ApprovalRequest]]

## Top bridge nodes
- [[MCPInspector_1]] - degree 77, connects to 10 communities
- [[TestAuditQueries]] - degree 20, connects to 6 communities
- [[MCPProxy.process_tool_call]] - degree 4, connects to 3 communities
- [[.inspect_tool_call()]] - degree 7, connects to 1 community
- [[._scan_value()]] - degree 7, connects to 1 community