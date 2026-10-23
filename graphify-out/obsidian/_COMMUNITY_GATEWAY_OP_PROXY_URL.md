---
type: community
cohesion: 0.22
members: 9
---

# GATEWAY_OP_PROXY_URL

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[A single corrupted SSE line logs a warning and is skipped — it must not     abor]] - rationale - gateway/tests/test_voice_gateway.py
- [[A stream that goes straight to 'done' with no sentence events (e.g.     everythi]] - rationale - gateway/tests/test_voice_gateway.py
- [[SSE keepalive comments (' ...') and blank lines are ignored, not     treated as]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream POSTs to forwardstream and yields each sentence     event a]] - rationale - gateway/tests/test_voice_gateway.py
- [[_sse_body()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_empty_stream_yields_nothing()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_skips_blank_and_comment_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_yields_sentences_in_order()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GATEWAY_OP_PROXY_URL
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_main.rs]]
- 4 edges to [[_COMMUNITY_ProgressiveLockdown]]

## Top bridge nodes
- [[test_call_agent_stream_empty_stream_yields_nothing()]] - degree 4, connects to 2 communities
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()]] - degree 4, connects to 2 communities
- [[test_call_agent_stream_skips_blank_and_comment_lines()]] - degree 4, connects to 2 communities
- [[test_call_agent_stream_yields_sentences_in_order()]] - degree 4, connects to 2 communities
- [[_sse_body()]] - degree 5, connects to 1 community
