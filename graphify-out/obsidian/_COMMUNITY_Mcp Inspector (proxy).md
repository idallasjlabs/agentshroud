---
type: community
cohesion: 0.11
members: 26
---

# Mcp Inspector (proxy)

**Cohesion:** 0.11 - loosely connected
**Members:** 26 nodes

## Members
- [[.__init__()_31]] - code - gateway/proxy/mcp_proxy.py
- [[._redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[._scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[._scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[._should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[.has_findings()]] - code - gateway/proxy/mcp_inspector.py
- [[.highest_threat()]] - code - gateway/proxy/mcp_inspector.py
- [[.inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[.inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Any_17]] - code - gateway/proxy/mcp_inspector.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[EnhancedApprovalQueue_1]] - code - gateway/proxy/mcp_proxy.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[InspectionResult]] - code - gateway/proxy/mcp_inspector.py
- [[MCPAuditTrail_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPInspector_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPPermissionManager_1]] - code - gateway/proxy/mcp_proxy.py
- [[MCPProxyConfig_2]] - code - gateway/proxy/mcp_proxy.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Result of inspecting a tool call or response.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Return the highest threat level from all findings.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Mcp_Inspector_proxy
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Mcp Proxy]]
- 14 edges to [[_COMMUNITY_Mcp Permissions]]
- 5 edges to [[_COMMUNITY_Mcp Audit (proxy)]]
- 5 edges to [[_COMMUNITY_Mcp Permissions (proxy)]]
- 3 edges to [[_COMMUNITY_Mcp Proxy Coverage]]
- 2 edges to [[_COMMUNITY_Mcp Proxy Coverage]]
- 1 edge to [[_COMMUNITY_Mcp Proxy (proxy)]]
- 1 edge to [[_COMMUNITY_Mcp Proxy]]

## Top bridge nodes
- [[InspectionResult]] - degree 22, connects to 6 communities
- [[EnhancedApprovalQueue_1]] - degree 8, connects to 4 communities
- [[MCPProxyConfig_2]] - degree 8, connects to 4 communities
- [[MCPAuditTrail_1]] - degree 8, connects to 4 communities
- [[MCPInspector_1]] - degree 8, connects to 4 communities