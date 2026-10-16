---
type: community
cohesion: 0.21
members: 13
---

# .inspect_tool_call

**Cohesion:** 0.21 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-_redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[Any_74]] - code - gateway/proxy/mcp_inspector.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/inspect_tool_call
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_MCPPermissionManager]]

## Top bridge nodes
- [[dot-inspect_tool_call()]] - degree 7, connects to 1 community
- [[dot-_scan_value()]] - degree 7, connects to 1 community
- [[dot-inspect_tool_result()]] - degree 6, connects to 1 community
- [[dot-_redact_pii()]] - degree 5, connects to 1 community
- [[dot-_scan_text()]] - degree 4, connects to 1 community
