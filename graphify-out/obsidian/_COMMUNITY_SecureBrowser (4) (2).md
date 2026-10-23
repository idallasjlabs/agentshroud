---
type: community
cohesion: 0.25
members: 8
---

# SecureBrowser (4) (2)

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[dot-_apply_filters()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_filter_outbound()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_filter_outbound_streaming()]] - code - gateway/proxy/llm_proxy.py
- [[dot-_filter_streaming_event()]] - code - gateway/proxy/llm_proxy.py
- [[Apply XML and credential filters to text.]] - rationale - gateway/proxy/llm_proxy.py
- [[Apply outbound text filters to known streaming response formats. Also enforces…]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter buffered SSE-like streaming responses for XMLcredential leaks and…]] - rationale - gateway/proxy/llm_proxy.py
- [[Filter outbound LLM response for credential leaks and XML.]] - rationale - gateway/proxy/llm_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SecureBrowser_4_2
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ModeRequest]]
- 2 edges to [[_COMMUNITY_SecureBrowser (4)]]
- 1 edge to [[_COMMUNITY_Common Queries]]

## Top bridge nodes
- [[dot-_filter_streaming_event()]] - degree 5, connects to 2 communities
- [[dot-_filter_outbound()]] - degree 4, connects to 2 communities
- [[dot-_filter_outbound_streaming()]] - degree 4, connects to 2 communities
- [[dot-_apply_filters()]] - degree 4, connects to 1 community
