---
type: community
members: 15
---

# egress_filter.py (2)

**Members:** 15 nodes

## Members
- [[dot-_redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-_should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[dot-inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[A single finding from inspection.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Any_68]] - code - gateway/proxy/mcp_inspector.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[InspectionFinding]] - code - gateway/proxy/mcp_inspector.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/egress_filterpy_2
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_CrossBotTrustLedger]]

## Top bridge nodes
- [[dot-inspect_tool_call()]] - degree 7, connects to 1 community
- [[dot-_scan_value()]] - degree 7, connects to 1 community
- [[InspectionFinding]] - degree 6, connects to 1 community
- [[dot-inspect_tool_result()]] - degree 6, connects to 1 community
- [[dot-_redact_pii()]] - degree 5, connects to 1 community
