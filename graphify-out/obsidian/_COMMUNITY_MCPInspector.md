---
type: community
members: 43
---

# MCPInspector

**Members:** 43 nodes

## Members
- [[dot-__init__()_59]] - code - gateway/proxy/mcp_inspector.py
- [[dot-__init__()_60]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_execute_tool_call()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-get_stats()_5]] - code - gateway/proxy/mcp_proxy.py
- [[dot-has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-send_request()]] - code - gateway/proxy/mcp_proxy.py
- [[dot-send_request()_1]] - code - gateway/proxy/mcp_proxy.py
- [[dot-start()_1]] - code - gateway/proxy/mcp_proxy.py
- [[Actually execute the tool call against the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Any_21]] - code - gateway/proxy/mcp_inspector.py
- [[Any_22]] - code - gateway/proxy/mcp_proxy.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[EnhancedApprovalQueue]] - code - gateway/proxy/mcp_proxy.py
- [[Get proxy statistics.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[InspectionResult]] - code - gateway/proxy/mcp_inspector.py
- [[Inspects MCP tool calls and responses for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[MCPAuditTrail]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector_1]] - code - gateway/proxy/mcp_inspector.py
- [[MCPPermissionManager]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy.process_tool_call]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy.process_tool_result]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig]] - code - gateway/proxy/mcp_proxy.py
- [[MCPTransport]] - code - gateway/proxy/mcp_config.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Send a JSON-RPC request and read the response.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Send an HTTP request to the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py
- [[Start the MCP server process.]] - rationale - gateway/proxy/mcp_proxy.py
- [[inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[strict_inspector()]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPInspector
SORT file.name ASC
```

## Connections to other communities
- 59 edges to [[_COMMUNITY_StdioConnection]]
- 48 edges to [[_COMMUNITY_MCPPermissionManager]]
- 22 edges to [[_COMMUNITY_MCPPermissionManager (2)]]
- 13 edges to [[_COMMUNITY_StdioConnection (2)]]
- 9 edges to [[_COMMUNITY_MCPAuditTrail]]
- 8 edges to [[_COMMUNITY_MCPPermissionManager (3)]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager (5)]]
- 2 edges to [[_COMMUNITY_MCPToolResult]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager (6)]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager (7)]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (2)]]

## Top bridge nodes
- [[MCPTransport]] - degree 63, connects to 11 communities
- [[MCPInspector_1]] - degree 77, connects to 10 communities
- [[InspectionResult]] - degree 22, connects to 4 communities
- [[Any_22]] - degree 13, connects to 4 communities
- [[dot-_execute_tool_call()]] - degree 8, connects to 4 communities
