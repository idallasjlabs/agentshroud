---
type: community
cohesion: 0.25
members: 8
---

# server.py

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[A final delta with no terminal punctuation is flushed once the SSE     stream en]] - rationale - gateway/tests/test_voice_gateway.py
- [[A malformedunexpected-shape SSE chunk is skipped, not fatal — a good     senten]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build OpenAI-shaped streaming SSE lines for a sequence of content deltas.]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_llm_stream posts to v1chatcompletions with streamtrue and     yields e]] - rationale - gateway/tests/test_voice_gateway.py
- [[_openai_delta_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_flushes_trailing_fragment()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_skips_malformed_chunks()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_yields_sentences()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/serverpy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 3 edges to [[_COMMUNITY_test_voice_latency_guard.py]]

## Top bridge nodes
- [[test_call_llm_stream_flushes_trailing_fragment()]] - degree 4, connects to 2 communities
- [[test_call_llm_stream_skips_malformed_chunks()]] - degree 4, connects to 2 communities
- [[test_call_llm_stream_yields_sentences()]] - degree 4, connects to 2 communities
- [[_openai_delta_lines()]] - degree 5, connects to 1 community
