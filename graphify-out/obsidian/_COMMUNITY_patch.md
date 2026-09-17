---
type: community
cohesion: 0.05
members: 73
---

# patch

**Cohesion:** 0.05 - loosely connected
**Members:** 73 nodes

## Members
- [[.test_run_binary_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_empty_stdout_is_error_not_clean()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_image_scan_type()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_nonzero_exit_code_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_parse_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_success()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_timeout()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_whitespace_only_stdout_is_error()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_trivy_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[.test_update_db_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[A 0-byteempty stdout means the scan failed to produce output -- it must never…]] - rationale - gateway/tests/test_security_toolchain.py
- [[A final delta with no terminal punctuation is flushed once the SSE stream ends,…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A malformedunexpected-shape SSE chunk is skipped, not fatal — a good sentence…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A non-400 HTTP error (e.g. 500) is a real failure, not the OpenClaw no-…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A single corrupted SSE line logs a warning and is skipped — it must not abort…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A stream that goes straight to 'done' with no sentence events (e.g. everything…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build a mock httpx.Response usable as the yield value of a mocked…]] - rationale - gateway/tests/test_voice_gateway.py
- [[GATEWAY_OWNER_USER_ID is sent as X-AgentShroud-User-Id header (not a body…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Request body must carry the configured model, max_tokens=150, and streamtrue…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Run a Trivy scan and return parsed results. Args target Scan target…]] - rationale - gateway/security/trivy_report.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestTrivyRun]] - code - gateway/tests/test_security_toolchain.py
- [[__aenter__()]] - code - gateway/tests/test_voice_gateway.py
- [[_aiter_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[_aiter_lines()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream POSTs to forwardstream and yields each sentence event as…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must POST to forwardstream with streamtrue, not the old…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must yield a spoken fallback string and log a WARNING when…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_llm_stream posts to v1chatcompletions with streamtrue and yields each…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_drain()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_llm_stream_resp()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_stream_resp()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_synthesize()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_synthesize()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_openai_delta_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[_sse_body()]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_1]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_2]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_3]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_4]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_6]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_7]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_8]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_9]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_10]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_11]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_12]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_13]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_14]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_15]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_16]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_17]] - code - gateway/tests/test_voice_gateway.py
- [[patch]] - code
- [[returncode 0 = clean, 1 = vulns found (both expected); anything else means…]] - rationale - gateway/tests/test_security_toolchain.py
- [[run_trivy_scan]] - code - gateway/security/trivy_report.py
- [[scan_type='image' is passed correctly to the trivy binary.]] - rationale - gateway/tests/test_security_toolchain.py
- [[test_call_agent_read_timeout_returns_fallback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_empty_stream_yields_nothing()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_non_400_http_error_falls_back()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_posts_to_forward_stream_endpoint()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_skips_blank_and_comment_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_yields_sentences_in_order()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_flushes_trailing_fragment()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_correct_model_and_max_tokens()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_full_history()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_skips_malformed_chunks()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_yields_sentences()]] - code - gateway/tests/test_voice_gateway.py
- [[test_owner_user_id_propagated_as_header()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_full_utterance_state_sequence()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_one_sentence_reply_unchanged()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_sentence_chunked_tts_calls_synthesize_per_sentence()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/patch
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 14 edges to [[_COMMUNITY_asyncio]]
- 11 edges to [[_COMMUNITY__call_agent_stream()]]
- 7 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 7 edges to [[_COMMUNITY_server.py]]
- 4 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_gateway.security.daily_cve_report]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]
- 1 edge to [[_COMMUNITY_test_call_agent_uses_structured_timeout()]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]

## Top bridge nodes
- [[run_trivy_scan]] - degree 17, connects to 5 communities
- [[test_call_agent_stream_empty_stream_yields_nothing()]] - degree 8, connects to 3 communities
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()]] - degree 8, connects to 3 communities
- [[test_call_agent_stream_skips_blank_and_comment_lines()]] - degree 8, connects to 3 communities
- [[test_call_agent_stream_yields_sentences_in_order()]] - degree 8, connects to 3 communities