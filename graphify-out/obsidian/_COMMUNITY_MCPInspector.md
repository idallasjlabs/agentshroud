---
type: community
cohesion: 0.10
members: 35
---

# MCPInspector

**Cohesion:** 0.10 - loosely connected
**Members:** 35 nodes

## Members
- [[dot-__init__()_114]] - code - gateway/proxy/mcp_inspector.py
- [[dot-__init__()_115]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-get_stats()_7]] - code - gateway/proxy/mcp_proxy.py
- [[dot-has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-send_request()_2]] - code - gateway/proxy/mcp_proxy.py
- [[Any_38]] - code - gateway/proxy/mcp_inspector.py
- [[Any_39]] - code - gateway/proxy/mcp_proxy.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[EnhancedApprovalQueue_2]] - code - gateway/proxy/mcp_proxy.py
- [[Get proxy statistics._1]] - rationale - gateway/proxy/mcp_proxy.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[InspectionResult]] - code - gateway/proxy/mcp_inspector.py
- [[Inspects MCP tool calls and responses for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[MCPAuditTrail_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector_1]] - code - gateway/proxy/mcp_inspector.py
- [[MCPPermissionManager_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy.process_tool_call]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxy.process_tool_result]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig_3]] - code - gateway/proxy/mcp_proxy.py
- [[MCPTransport]] - code - gateway/proxy/mcp_config.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Send an HTTP request to the MCP server.]] - rationale - gateway/proxy/mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPInspector
SORT file.name ASC
```

## Connections to other communities
- 48 edges to [[_COMMUNITY_MCPPermissionManager]]
- 31 edges to [[_COMMUNITY_StdioConnection_1]]
- 25 edges to [[_COMMUNITY_MCPPermissionManager_1]]
- 19 edges to [[_COMMUNITY_StdioConnection]]
- 11 edges to [[_COMMUNITY_MCPPermissionManager_4]]
- 9 edges to [[_COMMUNITY_MCPAuditTrail]]
- 7 edges to [[_COMMUNITY_MCPPermissionManager_2]]
- 3 edges to [[_COMMUNITY_TestMCPProxyEndpoint]]
- 2 edges to [[_COMMUNITY_MCPToolResult]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_5]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_6]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager_7]]
- 2 edges to [[_COMMUNITY_Athena — Knowledge Distiller_4]]
- 2 edges to [[_COMMUNITY_TestAuditTrail]]
- 1 edge to [[_COMMUNITY_PermissionLevel]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_1]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[MCPTransport]] - degree 63, connects to 16 communities
- [[MCPInspector_1]] - degree 77, connects to 13 communities
- [[InspectionResult]] - degree 22, connects to 5 communities
- [[Any_39]] - degree 13, connects to 5 communities
- [[EnhancedApprovalQueue_2]] - degree 8, connects to 3 communities
