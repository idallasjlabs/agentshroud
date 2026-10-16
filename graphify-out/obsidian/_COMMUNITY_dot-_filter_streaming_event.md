---
type: community
cohesion: 0.22
members: 9
---

# ._filter_streaming_event

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[dot-_apply_filters()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_filter_outbound()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_filter_outbound_streaming()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_filter_streaming_event()]] - code - gateway/proxy/llm_proxy.py
- [[Any_6]] - code
- [[Apply XML and credential filters to text.]] - rationale - gateway/proxy/llm_proxy.py
- [[Apply outbound text filters to known streaming response formats. Also enforces…]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter buffered SSE-like streaming responses for XMLcredential leaks and…]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter outbound LLM response for credential leaks and XML.]] - rationale - gateway/proxy/llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_filter_streaming_event
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_LLMProxy]]
- 2 edges to [[_COMMUNITY_dot-proxy_messages]]

## Top bridge nodes
- [[dot-_filter_outbound()]] - degree 4, connects to 2 communities
- [[dot-_filter_outbound_streaming()]] - degree 4, connects to 2 communities
- [[dot-_filter_streaming_event()]] - degree 5, connects to 1 community
- [[dot-_apply_filters()]] - degree 4, connects to 1 community
