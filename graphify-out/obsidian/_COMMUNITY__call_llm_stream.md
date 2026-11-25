---
type: community
members: 27
---

# _call_llm_stream

**Members:** 27 nodes

## Members
- [[A final delta with no terminal punctuation is flushed once the SSE stream ends,…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A malformedunexpected-shape SSE chunk is skipped, not fatal — a good sentence…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build OpenAI-shaped streaming SSE lines for a sequence of content deltas.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build a mock httpx.Response usable as the yield value of a mocked…_1]] - rationale - gateway/tests/test_voice_gateway.py
- [[GATEWAY_OWNER_USER_ID is sent as X-AgentShroud-User-Id header (not a body…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Request body must carry the configured model, max_tokens=150, and streamtrue…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Stream conversation history through the gateway's OpenAI-compat endpoint,…]] - rationale - voice_gateway/server.py
- [[The full messages history (system + prior turns) is sent in the request body.]] - rationale - gateway/tests/test_voice_gateway.py
- [[_aiter_lines()_2]] - code - gateway/tests/test_voice_gateway.py
- [[_call_llm_stream posts to v1chatcompletions with streamtrue and yields each…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_llm_stream()]] - code - voice_gateway/server.py
- [[_drain()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_llm_stream_resp()]] - code - gateway/tests/test_voice_gateway.py
- [[_openai_delta_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_19]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_20]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_21]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_22]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_23]] - code - gateway/tests/test_voice_gateway.py
- [[omlx-keepwarm.sh]] - code - scripts/omlx-keepwarm.sh
- [[omlx-keepwarm.sh script]] - code - scripts/omlx-keepwarm.sh
- [[test_call_llm_stream_flushes_trailing_fragment()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_correct_model_and_max_tokens()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_full_history()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_skips_malformed_chunks()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_yields_sentences()]] - code - gateway/tests/test_voice_gateway.py
- [[test_owner_user_id_propagated_as_header()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_call_llm_stream
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 8 edges to [[_COMMUNITY_mock_stream]]
- 5 edges to [[_COMMUNITY_asyncio_8]]
- 3 edges to [[_COMMUNITY_server.py]]

## Top bridge nodes
- [[test_call_llm_stream_flushes_trailing_fragment()]] - degree 7, connects to 3 communities
- [[test_call_llm_stream_skips_malformed_chunks()]] - degree 7, connects to 3 communities
- [[test_call_llm_stream_sends_correct_model_and_max_tokens()]] - degree 6, connects to 3 communities
- [[test_call_llm_stream_sends_full_history()]] - degree 6, connects to 3 communities
- [[test_call_llm_stream_yields_sentences()]] - degree 6, connects to 3 communities
