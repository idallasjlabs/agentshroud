---
type: community
members: 142
---

# test_voice_gateway.py

**Members:** 142 nodes

## Members
- [[usetellasktalk toswitch to... modelagent - ('model', gateway model…]] - rationale - gateway/tests/test_voice_gateway.py
- [[voice is the one endpoint reachable over the public internet (Tailscale…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A STOP arriving outside SPEAKING (e.g. the tap landed just as TTS ended) must…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A bare LISTEN after a stale partial upload must NOT prepend old audio.]] - rationale - gateway/tests/test_voice_gateway.py
- [[A connection-level error (not a statustimeout) also falls back to the trouble-…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A drop mid-upload must not force a full resend the next connection sends…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A final delta with no terminal punctuation is flushed once the SSE stream ends,…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A malformedunexpected-shape SSE chunk is skipped, not fatal — a good sentence…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A non-400 HTTP error (e.g. 500) is a real failure, not the OpenClaw no-…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A resume cache older than the freshness window must not replay.]] - rationale - gateway/tests/test_voice_gateway.py
- [[A single corrupted SSE line logs a warning and is skipped — it must not abort…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A stream that goes straight to 'done' with no sentence events (e.g. everything…]] - rationale - gateway/tests/test_voice_gateway.py
- [[After a set, the read query reports the tracked level in percent.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Agents with no streaming-compatible chat_path (OpenClaw) get a 400 from the…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Before any set, the read query reports an unknown-state calibration hint.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build OpenAI-shaped streaming SSE lines for a sequence of content deltas.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build a mock httpx.Response usable as the yield value of a mocked…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build a mock httpx.Response usable as the yield value of a mocked…_1]] - rationale - gateway/tests/test_voice_gateway.py
- [[Default _MODEL_SIZE is 'small.en' when WHISPER_MODEL_SIZE is not set.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Digit, percent, word-number and compound forms; clamping; non-commands.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Each synthesized sentence must ramp inout over ~5 ms so per-sentence Kokoro…]] - rationale - gateway/tests/test_voice_gateway.py
- [[GATEWAY_OWNER_USER_ID is sent as X-AgentShroud-User-Id header (not a body…]] - rationale - gateway/tests/test_voice_gateway.py
- [[If a device sends LISTEN but never sends END (crash  stuck firmware), the…]] - rationale - gateway/tests/test_voice_gateway.py
- [[If the pipeline raises mid-synthesis, synthesize() raises RuntimeError.]] - rationale - gateway/tests/test_voice_gateway.py
- [[LISTEN offset with an expired cache must behave like a fresh LISTEN (the…]] - rationale - gateway/tests/test_voice_gateway.py
- [[LISTEN → binary PCM → END → STT → forwardstream → TTS → PCM + END → idle.]] - rationale - gateway/tests/test_voice_gateway.py
- [[No fabricated version when the env var is genuinely unset — say 'unknown'…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Read phrasings match; set commands and unrelated speech do not.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Regression 2026-08-08 the voice assistant answered what version is…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Regression a single-sentence reply still produces exactly one synthesize call.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Request body must carry the configured model, max_tokens=150, and streamtrue…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Route a voice utterance to a proxied agent via the AgentShroud gateway's POST…]] - rationale - voice_gateway/server.py
- [[SSE keepalive comments (' ...') and blank lines are ignored, not treated as…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Sentence-chunked TTS synthesize() is called once per sentence; all PCM arrives…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Tests for the Voice Gateway FastAPI app (server.py, stt.py, tts.py). All…]] - rationale - gateway/tests/test_voice_gateway.py
- [[The full messages history (system + prior turns) is sent in the request body.]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_DIR (baked path) beats WHISPER_MODEL_SIZE — preserves offline…]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_DIR env var is honoured _MODEL_PATH resolves to the directory…]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_SIZE overrides the default when WHISPER_MODEL_DIR is unset.]] - rationale - gateway/tests/test_voice_gateway.py
- [[When agent= is absent the default agent must be 'direct' (fast local model) —…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When secret file is absent, _GATEWAY_TOKEN falls back to GATEWAY_AUTH_TOKEN env…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the LLM raises in the 'direct' agent path - the user message appended to…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the WS dirty-closes (code 1006) before the initial _send_state(IDLE) frame…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_GATEWAY_TOKEN is read from the secret file when it exists.]] - rationale - gateway/tests/test_voice_gateway.py
- [[__aenter__()_6]] - code - gateway/tests/test_voice_gateway.py
- [[__aexit__()_6]] - code - gateway/tests/test_voice_gateway.py
- [[__call__()]] - code - gateway/tests/test_voice_gateway.py
- [[__init__()_18]] - code - gateway/tests/test_voice_gateway.py
- [[_aiter_lines()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_aiter_lines()_2]] - code - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream POSTs to forwardstream and yields each sentence event as…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must POST to forwardstream with streamtrue, not the old…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must pass a structured httpx.Timeout to AsyncClient. The…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must yield a spoken fallback string and log a WARNING when…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream()]] - code - voice_gateway/server.py
- [[_call_llm_stream posts to v1chatcompletions with streamtrue and yields each…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_capture_transcribe()]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_transcribe()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_drain()]] - code - gateway/tests/test_voice_gateway.py
- [[_fail_llm()]] - code - gateway/tests/test_voice_gateway.py
- [[_load_ota_tokens merges env + secret file and falls back to the WS token.]] - rationale - gateway/tests/test_voice_gateway.py
- [[_mock_llm_stream_resp()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_stream_resp()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_synthesize()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_synthesize()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_openai_delta_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[_pipeline()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_receive_side_effect()]] - code - gateway/tests/test_voice_gateway.py
- [[_reset_reply_resume()]] - code - gateway/tests/test_voice_gateway.py
- [[_sse_body()]] - code - gateway/tests/test_voice_gateway.py
- [[asyncio_71]] - code
- [[fake_get_model()]] - code - gateway/tests/test_voice_gateway.py
- [[fixture_120]] - code
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
- [[mock_stream()_18]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_19]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_20]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_21]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_22]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_23]] - code - gateway/tests/test_voice_gateway.py
- [[mock_stream()_24]] - code - gateway/tests/test_voice_gateway.py
- [[pcm_chunks must stop growing once _PCM_MAX_BYTES is reached. A device that…]] - rationale - gateway/tests/test_voice_gateway.py
- [[stream()]] - code - gateway/tests/test_voice_gateway.py
- [[test_answer_volume_query_returns_tracked_level()]] - code - gateway/tests/test_voice_gateway.py
- [[test_answer_volume_query_unknown_before_any_set()]] - code - gateway/tests/test_voice_gateway.py
- [[test_bare_listen_starts_fresh()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_read_timeout_returns_fallback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_empty_stream_yields_nothing()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_generic_http_error_falls_back()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_non_400_http_error_falls_back()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_non_streaming_agent_returns_telegram_notice()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_posts_to_forward_stream_endpoint()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_skips_blank_and_comment_lines()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_yields_sentences_in_order()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_uses_structured_timeout()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_flushes_trailing_fragment()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_correct_model_and_max_tokens()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_full_history()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_skips_malformed_chunks()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_yields_sentences()]] - code - gateway/tests/test_voice_gateway.py
- [[test_is_volume_query_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_listen_offset_resumes_partial_upload()]] - code - gateway/tests/test_voice_gateway.py
- [[test_listen_offset_with_stale_cache_degrades_to_fresh()]] - code - gateway/tests/test_voice_gateway.py
- [[test_listen_without_end_times_out()]] - code - gateway/tests/test_voice_gateway.py
- [[test_load_ota_tokens_sources()]] - code - gateway/tests/test_voice_gateway.py
- [[test_owner_user_id_propagated_as_header()]] - code - gateway/tests/test_voice_gateway.py
- [[test_parse_model_switch_command_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_parse_volume_command_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_pcm_buffer_bounded()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_default_model_size_is_small_en()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_model_dir_wins_over_model_size()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_model_size_env_override()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_transcribe_mocked_model()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_uses_local_model_dir_when_env_set()]] - code - gateway/tests/test_voice_gateway.py
- [[test_token_falls_back_to_env_when_no_file()]] - code - gateway/tests/test_voice_gateway.py
- [[test_token_loaded_from_secret_file()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_kokoro_synthesis_failure_raises()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_resume_stale_cache_ignored()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_synthesize_fades_sentence_edges()]] - code - gateway/tests/test_voice_gateway.py
- [[test_voice_gateway.py]] - code - gateway/tests/test_voice_gateway.py
- [[test_voice_system_message_includes_agentshroud_version()]] - code - gateway/tests/test_voice_gateway.py
- [[test_voice_system_message_version_unknown_when_env_unset()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_default_agent_is_direct()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_direct_agent_pipeline_error_pops_history_and_recovery_send_fails()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_dirty_close_before_initial_state_is_handled_cleanly()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_full_utterance_state_sequence()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_one_sentence_reply_unchanged()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_sentence_chunked_tts_calls_synthesize_per_sentence()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_stale_stop_when_idle_is_ignored()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_token_check_uses_constant_time_comparison()]] - code - gateway/tests/test_voice_gateway.py
- [[transcribe() calls the model and returns joined segment text.]] - rationale - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_voice_gatewaypy
SORT file.name ASC
```

## Connections to other communities
- 50 edges to [[_COMMUNITY__mock_ws]]
- 12 edges to [[_COMMUNITY_app]]
- 9 edges to [[_COMMUNITY_server.py]]
- 7 edges to [[_COMMUNITY_test_voice_latency_guard.py]]
- 7 edges to [[_COMMUNITY_tts.py]]
- 6 edges to [[_COMMUNITY__fw_client]]
- 5 edges to [[_COMMUNITY__fake_kokoro_pipeline]]
- 4 edges to [[_COMMUNITY_AsyncMock]]
- 3 edges to [[_COMMUNITY__run_disconnect_test]]
- 2 edges to [[_COMMUNITY_test_tts_kokoro_pipeline_load_failure_raises]]
- 2 edges to [[_COMMUNITY_test_voice_stt_model_ab.py]]
- 1 edge to [[_COMMUNITY_dot-_s]]
- 1 edge to [[_COMMUNITY_TestNormalizeForSpeech]]
- 1 edge to [[_COMMUNITY_test_ws_pipeline_error_logs_and_recovers_to_idle]]

## Top bridge nodes
- [[test_voice_gateway.py]] - degree 116, connects to 12 communities
- [[_call_agent_stream()]] - degree 18, connects to 2 communities
- [[test_ws_one_sentence_reply_unchanged()]] - degree 8, connects to 2 communities
- [[test_ws_sentence_chunked_tts_calls_synthesize_per_sentence()]] - degree 7, connects to 2 communities
- [[test_ws_full_utterance_state_sequence()]] - degree 6, connects to 2 communities
