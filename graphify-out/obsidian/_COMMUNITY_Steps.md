---
type: community
cohesion: 0.21
members: 13
---

# Steps

**Cohesion:** 0.21 - loosely connected
**Members:** 13 nodes

## Members
- [[._redact_pii()]] - code - gateway/proxy/mcp_inspector.py
- [[._scan_text()]] - code - gateway/proxy/mcp_inspector.py
- [[._scan_value()]] - code - gateway/proxy/mcp_inspector.py
- [[._should_block()]] - code - gateway/proxy/mcp_inspector.py
- [[.inspect_tool_call()]] - code - gateway/proxy/mcp_inspector.py
- [[.inspect_tool_result()]] - code - gateway/proxy/mcp_inspector.py
- [[Any_17]] - code - gateway/proxy/mcp_inspector.py
- [[Decide whether to block based on findings and mode.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect a tool result for PII and encoding issues.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Inspect an outgoing tool call for security threats.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively redact HIGH-severity PII from a value.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Recursively scan a value, appending findings in-place.]] - rationale - gateway/proxy/mcp_inspector.py
- [[Scan a single string for all threat types.]] - rationale - gateway/proxy/mcp_inspector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Steps
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py]]
- 3 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_TestParanoidConfig]]

## Top bridge nodes
- [[.inspect_tool_call()]] - degree 7, connects to 2 communities
- [[._scan_value()]] - degree 7, connects to 2 communities
- [[.inspect_tool_result()]] - degree 6, connects to 2 communities
- [[._scan_text()]] - degree 4, connects to 2 communities
- [[._should_block()]] - degree 4, connects to 2 communities