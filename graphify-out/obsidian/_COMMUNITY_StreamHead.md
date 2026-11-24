---
type: community
members: 9
---

# StreamHead

**Members:** 9 nodes

## Members
- [[dot-_gen()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-_patches()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_upstream_200_streams_sse_as_before()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_upstream_400_returns_400_with_body()]] - code - gateway/tests/test_main_endpoints.py
- [[2026-10-16 a streaming request whose upstream answers 4xx must get that status…]] - rationale - gateway/tests/test_main_endpoints.py
- [[First item yielded by proxy_messages_streaming(with_head=True). Carries the…]] - rationale - gateway/proxy/llm_proxy.py
- [[StreamHead]] - code - gateway/proxy/llm_proxy.py
- [[TestStreamingProxyStatusPropagation]] - code - gateway/tests/test_main_endpoints.py
- [[_g()]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/StreamHead
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 2 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_app]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_test_anthropic_openai_translator.py]]

## Top bridge nodes
- [[StreamHead]] - degree 13, connects to 4 communities
- [[dot-test_upstream_200_streams_sse_as_before()]] - degree 6, connects to 2 communities
- [[dot-test_upstream_400_returns_400_with_body()]] - degree 6, connects to 2 communities
- [[TestStreamingProxyStatusPropagation]] - degree 7, connects to 1 community
