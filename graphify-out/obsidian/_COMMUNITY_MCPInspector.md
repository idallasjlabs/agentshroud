---
type: community
members: 18
---

# MCPInspector

**Members:** 18 nodes

## Members
- [[dot-__init__()_14]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Any_11]] - code
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[Inspects MCP tool calls and responses for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[MCPInspector]] - code - gateway/proxy/mcp_inspector.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPInspector
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 3 edges to [[_COMMUNITY_MCPToolCall]]
- 1 edge to [[_COMMUNITY_make_proxy]]

## Top bridge nodes
- [[MCPInspector]] - degree 22, connects to 3 communities
- [[dot-inspect_tool_call()]] - degree 7, connects to 1 community
- [[InspectionFinding]] - degree 6, connects to 1 community
- [[dot-inspect_tool_result()]] - degree 6, connects to 1 community
