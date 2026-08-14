---
type: community
members: 96
---

# Security Pipeline Core

**Members:** 96 nodes

## Members
- [[usetellasktalk toswitch to... modelagent - ('model', gateway     mo]] - rationale - gateway/tests/test_voice_gateway.py
- [[voice is the one endpoint reachable over the public internet (Tailscale     Fun]] - rationale - gateway/tests/test_voice_gateway.py
- [[A modelpipeline warm-up failure at startup must NOT down the gateway.      Regr]] - rationale - gateway/tests/test_voice_gateway.py
- [[After a set, the read query reports the tracked level in percent.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Before any set, the read query reports an unknown-state calibration hint.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build a mock httpx.Response usable as the yield value of a mocked     AsyncClien]] - rationale - gateway/tests/test_voice_gateway.py
- [[Connection with correct token= query param is accepted and gets idle state.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Connection with no token is rejected when auth is configured.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Connection with wrong token= is closed (server returns no state frame).]] - rationale - gateway/tests/test_voice_gateway.py
- [[ConnectionClosedError (WS code 1006 — ungraceful ESP disconnect, e.g. device]] - rationale - gateway/tests/test_voice_gateway.py
- [[ConnectionClosedOK (WS code 10001001 — clean websockets-library close path)]] - rationale - gateway/tests/test_voice_gateway.py
- [[Default _MODEL_SIZE is 'small.en' when WHISPER_MODEL_SIZE is not set.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Digit, percent, word-number and compound forms; clamping; non-commands.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Directly invoke ``voice_endpoint`` with a mocked WebSocket whose second     ``re]] - rationale - gateway/tests/test_voice_gateway.py
- [[Each synthesized sentence must ramp inout over ~5 ms so per-sentence     Kokoro]] - rationale - gateway/tests/test_voice_gateway.py
- [[GATEWAY_OWNER_USER_ID is sent as X-AgentShroud-User-Id header (not a body field)]] - rationale - gateway/tests/test_voice_gateway.py
- [[If a device sends LISTEN but never sends END (crash  stuck firmware), the     s]] - rationale - gateway/tests/test_voice_gateway.py
- [[If the Kokoro pipeline can't be constructed, synthesize() raises RuntimeError.]] - rationale - gateway/tests/test_voice_gateway.py
- [[If the pipeline raises mid-synthesis, synthesize() raises RuntimeError.]] - rationale - gateway/tests/test_voice_gateway.py
- [[No agent= param → _DEFAULT_AGENT is used for routing.]] - rationale - gateway/tests/test_voice_gateway.py
- [[No fabricated version when the env var is genuinely unset — say     'unknown' ra]] - rationale - gateway/tests/test_voice_gateway.py
- [[Read phrasings match; set commands and unrelated speech do not.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Regression 2026-08-08 the voice assistant answered what version is     AgentSh]] - rationale - gateway/tests/test_voice_gateway.py
- [[Stand-in for kokoro.KPipeline a callable yielding (graphemes, phonemes,     aud]] - rationale - gateway/tests/test_voice_gateway.py
- [[Text that normalises to emptywhitespace returns b'' without invoking Kokoro.]] - rationale - gateway/tests/test_voice_gateway.py
- [[The very first frame after WS accept must be idle, not listening.]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_DIR (baked path) beats WHISPER_MODEL_SIZE — preserves offline guar]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_DIR env var is honoured _MODEL_PATH resolves to the directory]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_SIZE overrides the default when WHISPER_MODEL_DIR is unset.]] - rationale - gateway/tests/test_voice_gateway.py
- [[When agent= is absent the default agent must be 'direct' (fast local     model)]] - rationale - gateway/tests/test_voice_gateway.py
- [[When OUTPUT_SAMPLE_RATE (24000, Kokoro native) != TARGET_SAMPLE_RATE     (16000)]] - rationale - gateway/tests/test_voice_gateway.py
- [[When _VG_AUTH_TOKEN is empty, any connection is accepted (dev  backward compat)]] - rationale - gateway/tests/test_voice_gateway.py
- [[When secret file is absent, _GATEWAY_TOKEN falls back to GATEWAY_AUTH_TOKEN env]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the LLM raises in the 'direct' agent path       - the user message appende]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the STT→LLM→TTS pipeline raises, the inner exception handler must       1.]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the WS dirty-closes (code 1006) before the initial _send_state(IDLE) frame]] - rationale - gateway/tests/test_voice_gateway.py
- [[_GATEWAY_TOKEN is read from the secret file when it exists.]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must POST to forwardstream with streamtrue, not     the ol]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must pass a structured httpx.Timeout to AsyncClient.      The]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_agent_stream must yield a spoken fallback string and log a WARNING     whe]] - rationale - gateway/tests/test_voice_gateway.py
- [[_fake_kokoro_pipeline()]] - code - gateway/tests/test_voice_gateway.py
- [[_load_ota_tokens merges env + secret file and falls back to the WS token.]] - rationale - gateway/tests/test_voice_gateway.py
- [[_mock_stream_resp()]] - code - gateway/tests/test_voice_gateway.py
- [[_reset_reply_resume()]] - code - gateway/tests/test_voice_gateway.py
- [[_run_disconnect_test()]] - code - gateway/tests/test_voice_gateway.py
- [[pcm_chunks must stop growing once _PCM_MAX_BYTES is reached.      A device that]] - rationale - gateway/tests/test_voice_gateway.py
- [[synthesize() feeds the normalised (no-markdown, no-token) text to Kokoro.      V]] - rationale - gateway/tests/test_voice_gateway.py
- [[synthesize() runs the Kokoro pipeline; when rates match no resampling occurs.]] - rationale - gateway/tests/test_voice_gateway.py
- [[test_answer_volume_query_returns_tracked_level()]] - code - gateway/tests/test_voice_gateway.py
- [[test_answer_volume_query_unknown_before_any_set()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_read_timeout_returns_fallback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_posts_to_forward_stream_endpoint()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_uses_structured_timeout()]] - code - gateway/tests/test_voice_gateway.py
- [[test_health_returns_ok()]] - code - gateway/tests/test_voice_gateway.py
- [[test_is_volume_query_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_lifespan_tolerates_warmup_failure()]] - code - gateway/tests/test_voice_gateway.py
- [[test_listen_without_end_times_out()]] - code - gateway/tests/test_voice_gateway.py
- [[test_load_ota_tokens_sources()]] - code - gateway/tests/test_voice_gateway.py
- [[test_owner_user_id_propagated_as_header()]] - code - gateway/tests/test_voice_gateway.py
- [[test_parse_model_switch_command_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_parse_volume_command_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_pcm_buffer_bounded()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_default_model_size_is_small_en()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_model_dir_wins_over_model_size()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_model_size_env_override()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_transcribe_empty_bytes_returns_empty()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_transcribe_mocked_model()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_uses_local_model_dir_when_env_set()]] - code - gateway/tests/test_voice_gateway.py
- [[test_token_falls_back_to_env_when_no_file()]] - code - gateway/tests/test_voice_gateway.py
- [[test_token_loaded_from_secret_file()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_empty_text_returns_empty()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_kokoro_pipeline_load_failure_raises()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_kokoro_synthesis_failure_raises()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_resamples_24000_to_16000()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_synthesize_fades_sentence_edges()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_synthesize_only_whitespace_after_normalise_returns_empty()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_synthesize_passes_normalised_text_to_kokoro()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_synthesize_via_kokoro()]] - code - gateway/tests/test_voice_gateway.py
- [[test_voice_gateway.py]] - code - gateway/tests/test_voice_gateway.py
- [[test_voice_system_message_includes_agentshroud_version()]] - code - gateway/tests/test_voice_gateway.py
- [[test_voice_system_message_version_unknown_when_env_unset()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_accepts_correct_token()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_accepts_when_auth_not_configured()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_agent_query_param_absent_uses_default()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connect_sends_idle_first()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connectionclosed_error_logs_info_no_traceback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connectionclosed_ok_logs_info_no_traceback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_default_agent_is_direct()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_direct_agent_pipeline_error_pops_history_and_recovery_send_fails()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_dirty_close_before_initial_state_is_handled_cleanly()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_pipeline_error_logs_and_recovers_to_idle()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_rejects_missing_token()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_rejects_wrong_token()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_token_check_uses_constant_time_comparison()]] - code - gateway/tests/test_voice_gateway.py
- [[transcribe() calls the model and returns joined segment text.]] - rationale - gateway/tests/test_voice_gateway.py
- [[voice_gatewaystt.py]] - code - voice_gateway/stt.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Pipeline_Core
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_Gateway Test Suite]]
- 11 edges to [[_COMMUNITY_voice_gatewayserver.py]]
- 8 edges to [[_COMMUNITY_Gateway Test Suite]]
- 6 edges to [[_COMMUNITY_Gateway Test Suite]]
- 6 edges to [[_COMMUNITY_Planning Docs]]
- 5 edges to [[_COMMUNITY_Planning Docs]]
- 4 edges to [[_COMMUNITY_Planning Docs]]
- 1 edge to [[_COMMUNITY_Competitive Intel Store]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Security Docs]]
- 1 edge to [[_COMMUNITY_Security Docs]]

## Top bridge nodes
- [[test_voice_gateway.py]] - degree 113, connects to 10 communities
- [[_run_disconnect_test()]] - degree 5, connects to 1 community
- [[test_owner_user_id_propagated_as_header()]] - degree 3, connects to 1 community
- [[test_ws_pipeline_error_logs_and_recovers_to_idle()]] - degree 3, connects to 1 community
- [[test_call_agent_read_timeout_returns_fallback()]] - degree 3, connects to 1 community