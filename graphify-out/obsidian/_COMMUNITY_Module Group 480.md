---
type: community
cohesion: 0.33
members: 6
---

# Module Group 480

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[._scan_inbound()]] - code - gateway/proxy/llm_proxy.py
- [[._scan_request_data()]] - code - gateway/proxy/llm_proxy.py
- [[.proxy_messages_streaming()]] - code - gateway/proxy/llm_proxy.py
- [[Proxy a streaming LLM API request, yielding SSE chunks as they arrive.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan inbound user message text for PII and injection.]] - rationale - gateway/proxy/llm_proxy.py
- [[Scan request data for PII and injection across different provider formats.]] - rationale - gateway/proxy/llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_480
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Module Group 73]]
- 1 edge to [[_COMMUNITY_Module Group 151]]

## Top bridge nodes
- [[._scan_request_data()]] - degree 5, connects to 2 communities
- [[.proxy_messages_streaming()]] - degree 3, connects to 1 community
- [[._scan_inbound()]] - degree 3, connects to 1 community
