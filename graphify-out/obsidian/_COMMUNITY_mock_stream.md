---
type: community
members: 46
---

# mock_stream

**Members:** 46 nodes

## Members
- [[A non-400 HTTP error (e.g. 500) is a real failure, not the OpenClaw no-…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A single corrupted SSE line logs a warning and is skipped — it must not abort…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A stream that goes straight to 'done' with no sentence events (e.g. everything…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Agents with no streaming-compatible chat_path (OpenClaw) get a 400 from the…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build a mock httpx.Response usable as the yield value of a mocked…]] - rationale - gateway/tests/test_voice_gateway.py
- [[LISTEN → binary PCM → END → STT → forwardstream → TTS → PCM + END → idle.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Regression a single-sentence reply still produces exactly one synthesize call.]] - rationale - gateway/tests/test_voice_gateway.py
- [[SSE keepalive comments (' ...') and blank lines are ignored, not treated as…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Sentence-chunked TTS synthesize() is called once per sentence; all PCM arrives…]] - rationale - gateway/tests/test_voice_gateway.py
- [[__aenter__()_4]] - code - gateway/tests/test_voice_gateway.py
- [[__aexit__()_4]] - code - gateway/tests/test_voice_gateway.py
- [[__init__()_14]] - code - gateway/tests/test_voice_gateway.py
- [[_aiter_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream POSTs to forwardstream and yields each sentence event as…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must POST to forwardstream with streamtrue, not the old…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must pass a structured httpx.Timeout to AsyncClient. The…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must yield a spoken fallback string and log a WARNING when…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_mock_stream_resp()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_synthesize()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_synthesize()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_sse_body()]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_1]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_2]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_3]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_4]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_5]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_6]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_7]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_8]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_9]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_10]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_11]] - code - gateway/tests/test_voice_gateway.py
- [[stream()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_read_timeout_returns_fallback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_empty_stream_yields_nothing()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_non_400_http_error_falls_back()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_non_streaming_agent_returns_telegram_notice()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_posts_to_forward_stream_endpoint()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_skips_blank_and_comment_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_yields_sentences_in_order()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_uses_structured_timeout()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_full_utterance_state_sequence()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_one_sentence_reply_unchanged()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_sentence_chunked_tts_calls_synthesize_per_sentence()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/mock_stream
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 11 edges to [[_COMMUNITY_asyncio_8]]
- 8 edges to [[_COMMUNITY__call_llm_stream]]
- 7 edges to [[_COMMUNITY_test_voice_latency_guard.py]]
- 3 edges to [[_COMMUNITY_app]]

## Top bridge nodes
- [[test_ws_one_sentence_reply_unchanged()]] - degree 8, connects to 3 communities
- [[test_call_agent_stream_empty_stream_yields_nothing()]] - degree 7, connects to 3 communities
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()]] - degree 7, connects to 3 communities
- [[test_call_agent_stream_skips_blank_and_comment_lines()]] - degree 7, connects to 3 communities
- [[test_call_agent_stream_yields_sentences_in_order()]] - degree 7, connects to 3 communities
