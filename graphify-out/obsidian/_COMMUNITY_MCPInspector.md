---
type: community
cohesion: 0.10
members: 35
---

# MCPInspector

**Cohesion:** 0.10 - loosely connected
**Members:** 35 nodes

## Members
- [[dot-__init__()_98]] - code - gateway/proxy/mcp_inspector.py
- [[dot-__init__()_99]] - code - gateway/proxy/mcp_proxy.py
- [[dot-_redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-get_stats()_8]] - code - gateway/proxy/mcp_proxy.py
- [[dot-has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[Any_33]] - code - gateway/proxy/mcp_inspector.py
- [[Any_34]] - code - gateway/proxy/mcp_proxy.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[EnhancedApprovalQueue]] - code - gateway/proxy/mcp_proxy.py
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
- [[MCPProxyConfig]] - code - gateway/proxy/mcp_proxy.py
- [[MCPTransport]] - code - gateway/proxy/mcp_config.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py
- [[inspector()]] - code - gateway/tests/test_mcp_proxy.py
- [[strict_inspector()]] - code - gateway/tests/test_mcp_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPInspector
SORT file.name ASC
```

## Connections to other communities
- 48 edges to [[_COMMUNITY_MCPToolCall]]
- 25 edges to [[_COMMUNITY_test_bots_ssh_exec_wrapper.py]]
- 22 edges to [[_COMMUNITY_StdioConnection]]
- 21 edges to [[_COMMUNITY_CrossBotTrustLedger]]
- 20 edges to [[_COMMUNITY_What Does OpenClaw Actually Need to Write]]
- 11 edges to [[_COMMUNITY_MCPToolResult]]
- 7 edges to [[_COMMUNITY_MCPPermissionManager (2)_1]]
- 5 edges to [[_COMMUNITY_AgentShroud Security Value Proposition]]
- 2 edges to [[_COMMUNITY_TestInspectorEdgeCases]]
- 2 edges to [[_COMMUNITY_TestPIIDetection]]
- 2 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_Egress Filter Errors]]
- 1 edge to [[_COMMUNITY_ContextSegment]]

## Top bridge nodes
- [[MCPTransport]] - degree 63, connects to 11 communities
- [[MCPInspector_1]] - degree 77, connects to 10 communities
- [[InspectionResult]] - degree 22, connects to 6 communities
- [[Any_34]] - degree 13, connects to 5 communities
- [[EnhancedApprovalQueue]] - degree 8, connects to 3 communities
