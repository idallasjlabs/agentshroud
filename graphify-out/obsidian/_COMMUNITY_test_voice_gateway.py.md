---
type: community
cohesion: 0.02
members: 86
---

# test_voice_gateway.py

**Cohesion:** 0.02 - loosely connected
**Members:** 86 nodes

## Members
- [[usetellasktalk toswitch to... modelagent - ('model', gateway model…]] - rationale - gateway/tests/test_voice_gateway.py
- [[voice is the one endpoint reachable over the public internet (Tailscale…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A modelpipeline warm-up failure at startup must NOT down the gateway.…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Before any set, the read query reports an unknown-state calibration hint.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Connection with correct token= query param is accepted and gets idle state.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Connection with no token is rejected when auth is configured.]] - rationale - gateway/tests/test_voice_gateway.py
- [[ConnectionClosedError (WS code 1006 — ungraceful ESP disconnect, e.g. device]] - rationale - gateway/tests/test_voice_gateway.py
- [[ConnectionClosedOK (WS code 10001001 — clean websockets-library close path)]] - rationale - gateway/tests/test_voice_gateway.py
- [[Directly invoke ``voice_endpoint`` with a mocked WebSocket whose second     ``re]] - rationale - gateway/tests/test_voice_gateway.py
- [[Directly invoke ``voice_endpoint`` with a mocked WebSocket whose second…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Each synthesized sentence must ramp inout over ~5 ms so per-sentence     Kokoro]] - rationale - gateway/tests/test_voice_gateway.py
- [[External uptime monitors (e.g. UptimeRobot) probe with HEAD; a 405 makes a…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Frequencies well below the Nyquist (≤3 kHz) must pass through with minimal…]] - rationale - gateway/tests/test_voice_gateway.py
- [[If the Kokoro pipeline can't be constructed, synthesize() raises RuntimeError.]] - rationale - gateway/tests/test_voice_gateway.py
- [[If the pipeline raises mid-synthesis, synthesize() raises RuntimeError.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Kaiser-windowed sinc anti-aliasing filter suppresses content above the output]] - rationale - gateway/tests/test_voice_gateway.py
- [[No agent= param → _DEFAULT_AGENT is used for routing.]] - rationale - gateway/tests/test_voice_gateway.py
- [[No fabricated version when the env var is genuinely unset — say 'unknown'…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Regression 2026-08-08 the voice assistant answered what version is…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Tests for the Voice Gateway FastAPI app (server.py, stt.py, tts.py). All…]] - rationale - gateway/tests/test_voice_gateway.py
- [[The very first frame after WS accept must be idle, not listening.]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_DIR (baked path) beats WHISPER_MODEL_SIZE — preserves offline…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When agent= is absent the default agent must be 'direct' (fast local     model)]] - rationale - gateway/tests/test_voice_gateway.py
- [[When _VG_AUTH_TOKEN is empty, any connection is accepted (dev  backward…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When secret file is absent, _GATEWAY_TOKEN falls back to GATEWAY_AUTH_TOKEN env]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the LLM raises in the 'direct' agent path - the user message appended to…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the STT→LLM→TTS pipeline raises, the inner exception handler must 1. log…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the WS dirty-closes (code 1006) before the initial _send_state(IDLE) frame]] - rationale - gateway/tests/test_voice_gateway.py
- [[__call__()]] - code - gateway/tests/test_voice_gateway.py
- [[_boom()]] - code - gateway/tests/test_voice_gateway.py
- [[_boom()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_fail_llm()]] - code - gateway/tests/test_voice_gateway.py
- [[_failing_transcribe()]] - code - gateway/tests/test_voice_gateway.py
- [[_pipeline()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_receive_side_effect()]] - code - gateway/tests/test_voice_gateway.py
- [[_reset_reply_resume()]] - code - gateway/tests/test_voice_gateway.py
- [[_run_disconnect_test()]] - code - gateway/tests/test_voice_gateway.py
- [[_run_disconnect_test()_1]] - code - gateway/tests/test_voice_gateway.py
- [[fake_get_model()]] - code - gateway/tests/test_voice_gateway.py
- [[fixture_5]] - code
- [[test_answer_volume_query_unknown_before_any_set()]] - code - gateway/tests/test_voice_gateway.py
- [[test_answer_volume_query_unknown_before_any_set()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_health_returns_ok()]] - code - gateway/tests/test_voice_gateway.py
- [[test_health_supports_head()]] - code - gateway/tests/test_voice_gateway.py
- [[test_lifespan_tolerates_warmup_failure()]] - code - gateway/tests/test_voice_gateway.py
- [[test_parse_model_switch_command_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_resample_antialias_attenuates_above_nyquist()]] - code - gateway/tests/test_voice_gateway.py
- [[test_resample_antialias_attenuates_above_nyquist()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_resample_passband_preserved()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_model_dir_wins_over_model_size()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_transcribe_empty_bytes_returns_empty()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_transcribe_mocked_model()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_transcribe_mocked_model()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_token_falls_back_to_env_when_no_file()]] - code - gateway/tests/test_voice_gateway.py
- [[test_token_falls_back_to_env_when_no_file()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_empty_text_returns_empty()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_kokoro_pipeline_load_failure_raises()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_kokoro_pipeline_load_failure_raises()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_kokoro_synthesis_failure_raises()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_kokoro_synthesis_failure_raises()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_synthesize_fades_sentence_edges()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_synthesize_fades_sentence_edges()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_voice_gateway.py]] - code - gateway/tests/test_voice_gateway.py
- [[test_voice_system_message_includes_agentshroud_version()]] - code - gateway/tests/test_voice_gateway.py
- [[test_voice_system_message_version_unknown_when_env_unset()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_accepts_correct_token()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_accepts_correct_token()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_accepts_when_auth_not_configured()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_agent_query_param_absent_uses_default()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_agent_query_param_absent_uses_default()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connect_sends_idle_first()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connect_sends_idle_first()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connectionclosed_error_logs_info_no_traceback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connectionclosed_error_logs_info_no_traceback()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connectionclosed_ok_logs_info_no_traceback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connectionclosed_ok_logs_info_no_traceback()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_default_agent_is_direct()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_default_agent_is_direct()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_direct_agent_pipeline_error_pops_history_and_recovery_send_fails()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_dirty_close_before_initial_state_is_handled_cleanly()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_dirty_close_before_initial_state_is_handled_cleanly()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_pipeline_error_logs_and_recovers_to_idle()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_rejects_missing_token()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_rejects_missing_token()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_token_check_uses_constant_time_comparison()]] - code - gateway/tests/test_voice_gateway.py
- [[transcribe() calls the model and returns joined segment text.]] - rationale - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_voice_gatewaypy
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 26 edges to [[_COMMUNITY_asyncio]]
- 20 edges to [[_COMMUNITY_patch]]
- 6 edges to [[_COMMUNITY__fw_client()]]
- 5 edges to [[_COMMUNITY__fake_kokoro_pipeline()]]
- 3 edges to [[_COMMUNITY__call_agent_stream()]]
- 2 edges to [[_COMMUNITY_test_listen_offset_resumes_partial_upload()]]
- 2 edges to [[_COMMUNITY_server.py]]
- 1 edge to [[_COMMUNITY_TestNormalizeForSpeech]]
- 1 edge to [[_COMMUNITY_TestSplitForSpeech]]
- 1 edge to [[_COMMUNITY_test_call_agent_uses_structured_timeout()]]
- 1 edge to [[_COMMUNITY_test_voice_stt_model_ab.py]]
- 1 edge to [[_COMMUNITY_tts.py]]

## Top bridge nodes
- [[test_voice_gateway.py]] - degree 113, connects to 13 communities
- [[_run_disconnect_test()_1]] - degree 4, connects to 1 community
- [[test_ws_connectionclosed_error_logs_info_no_traceback()_1]] - degree 3, connects to 1 community
- [[test_ws_connectionclosed_ok_logs_info_no_traceback()_1]] - degree 3, connects to 1 community
- [[test_answer_volume_query_unknown_before_any_set()_1]] - degree 2, connects to 1 community