---
type: community
cohesion: 0.22
members: 9
---

# ._filter_streaming_event()

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[._apply_filters()_1]] - code - gateway/proxy/llm_proxy.py
- [[._filter_outbound()_2]] - code - gateway/proxy/llm_proxy.py
- [[._filter_outbound_streaming()_1]] - code - gateway/proxy/llm_proxy.py
- [[._filter_streaming_event()_1]] - code - gateway/proxy/llm_proxy.py
- [[Any_49]] - code
- [[Apply XML and credential filters to text.]] - rationale - gateway/proxy/llm_proxy.py
- [[Apply outbound text filters to known streaming response formats.          Also e]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter buffered SSE-like streaming responses for XMLcredential leaks and ToolAC]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter outbound LLM response for credential leaks and XML.]] - rationale - gateway/proxy/llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_filter_streaming_event
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_LLMProxy]]
- 3 edges to [[_COMMUNITY_LLMProxy]]
- 2 edges to [[_COMMUNITY_.proxy_messages()]]

## Top bridge nodes
- [[._filter_outbound()_2]] - degree 4, connects to 2 communities
- [[._filter_outbound_streaming()_1]] - degree 4, connects to 2 communities
- [[._filter_streaming_event()_1]] - degree 5, connects to 1 community
- [[._apply_filters()_1]] - degree 4, connects to 1 community
- [[Any_49]] - degree 2, connects to 1 community