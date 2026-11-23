---
type: community
members: 92
---

# test_voice_gateway.py

**Members:** 92 nodes

## Members
- [[usetellasktalk toswitch to... modelagent - ('model', gateway model…]] - rationale - gateway/tests/test_voice_gateway.py
- [[voice is the one endpoint reachable over the public internet (Tailscale…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A modelpipeline warm-up failure at startup must NOT down the gateway.…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A stalemismatched If-None-Match must serve the full new binary (200).]] - rationale - gateway/tests/test_voice_gateway.py
- [[After a set, the read query reports the tracked level in percent.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Authenticated request but no firmware on disk → 404 (not a 500empty 200).]] - rationale - gateway/tests/test_voice_gateway.py
- [[Before any set, the read query reports an unknown-state calibration hint.]] - rationale - gateway/tests/test_voice_gateway.py
- [[ConnectionClosedError (WS code 1006 — ungraceful ESP disconnect, e.g. device…]] - rationale - gateway/tests/test_voice_gateway.py
- [[ConnectionClosedOK (WS code 10001001 — clean websockets-library close path)…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Default _MODEL_SIZE is 'small.en' when WHISPER_MODEL_SIZE is not set.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Digit, percent, word-number and compound forms; clamping; non-commands.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Directly invoke ``voice_endpoint`` with a mocked WebSocket whose second…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Each synthesized sentence must ramp inout over ~5 ms so per-sentence Kokoro…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Empty STT result no LLM call, state goes directly to idle.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Empty allowlist = OTA un-gated any non-empty token is accepted (200).]] - rationale - gateway/tests/test_voice_gateway.py
- [[GET firmwarebin token gate, 200 + quoted SHA-256 ETag, HEAD ETag parity.…]] - rationale - gateway/tests/test_voice_gateway.py
- [[If the Kokoro pipeline can't be constructed, synthesize() raises RuntimeError.]] - rationale - gateway/tests/test_voice_gateway.py
- [[If the pipeline raises mid-synthesis, synthesize() raises RuntimeError.]] - rationale - gateway/tests/test_voice_gateway.py
- [[If-None-Match equal to the current ETag → 304 with no body. This is the whole…]] - rationale - gateway/tests/test_voice_gateway.py
- [[No fabricated version when the env var is genuinely unset — say 'unknown'…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Read phrasings match; set commands and unrelated speech do not.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Regression 2026-08-08 the voice assistant answered what version is…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Stand-in for kokoro.KPipeline a callable yielding (graphemes, phonemes, audio)…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Tests for the Voice Gateway FastAPI app (server.py, stt.py, tts.py). All…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Text that normalises to emptywhitespace returns b'' without invoking Kokoro.]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_DIR (baked path) beats WHISPER_MODEL_SIZE — preserves offline…]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_DIR env var is honoured _MODEL_PATH resolves to the directory…]] - rationale - gateway/tests/test_voice_gateway.py
- [[WHISPER_MODEL_SIZE overrides the default when WHISPER_MODEL_DIR is unset.]] - rationale - gateway/tests/test_voice_gateway.py
- [[When agent= is absent the default agent must be 'direct' (fast local model) —…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When OUTPUT_SAMPLE_RATE (24000, Kokoro native) != TARGET_SAMPLE_RATE (16000),…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When secret file is absent, _GATEWAY_TOKEN falls back to GATEWAY_AUTH_TOKEN env…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the LLM raises in the 'direct' agent path - the user message appended to…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the STT→LLM→TTS pipeline raises, the inner exception handler must 1. log…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When the WS dirty-closes (code 1006) before the initial _send_state(IDLE) frame…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Wire the firmwarebin route to a fake binary + a fixed OTA token allowlist.…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_GATEWAY_TOKEN is read from the secret file when it exists.]] - rationale - gateway/tests/test_voice_gateway.py
- [[__call__()]] - code - gateway/tests/test_voice_gateway.py
- [[_boom()_25]] - code - gateway/tests/test_voice_gateway.py
- [[_boom()_26]] - code - gateway/tests/test_voice_gateway.py
- [[_fail_llm()]] - code - gateway/tests/test_voice_gateway.py
- [[_failing_transcribe()]] - code - gateway/tests/test_voice_gateway.py
- [[_fake_kokoro_pipeline()]] - code - gateway/tests/test_voice_gateway.py
- [[_fw_client()]] - code - gateway/tests/test_voice_gateway.py
- [[_load_ota_tokens merges env + secret file and falls back to the WS token.]] - rationale - gateway/tests/test_voice_gateway.py
- [[_pipeline()]] - code - gateway/tests/test_voice_gateway.py
- [[_pipeline()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_receive_side_effect()]] - code - gateway/tests/test_voice_gateway.py
- [[_reset_reply_resume()]] - code - gateway/tests/test_voice_gateway.py
- [[_run_disconnect_test()]] - code - gateway/tests/test_voice_gateway.py
- [[_spy_get_pipeline()]] - code - gateway/tests/test_voice_gateway.py
- [[fake_get_model()]] - code - gateway/tests/test_voice_gateway.py
- [[fixture_118]] - code
- [[synthesize() feeds the normalised (no-markdown, no-token) text to Kokoro.…]] - rationale - gateway/tests/test_voice_gateway.py
- [[synthesize() runs the Kokoro pipeline; when rates match no resampling occurs.]] - rationale - gateway/tests/test_voice_gateway.py
- [[test_answer_volume_query_returns_tracked_level()]] - code - gateway/tests/test_voice_gateway.py
- [[test_answer_volume_query_unknown_before_any_set()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_304_on_matching_if_none_match()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_404_when_absent()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_auth_and_etag()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_stale_if_none_match_returns_body()]] - code - gateway/tests/test_voice_gateway.py
- [[test_firmware_bin_ungated_when_allowlist_empty()]] - code - gateway/tests/test_voice_gateway.py
- [[test_is_volume_query_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_lifespan_tolerates_warmup_failure()]] - code - gateway/tests/test_voice_gateway.py
- [[test_load_ota_tokens_sources()]] - code - gateway/tests/test_voice_gateway.py
- [[test_parse_model_switch_command_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_parse_volume_command_forms()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_default_model_size_is_small_en()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_model_dir_wins_over_model_size()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_model_size_env_override()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_transcribe_mocked_model()]] - code - gateway/tests/test_voice_gateway.py
- [[test_stt_uses_local_model_dir_when_env_set()]] - code - gateway/tests/test_voice_gateway.py
- [[test_token_falls_back_to_env_when_no_file()]] - code - gateway/tests/test_voice_gateway.py
- [[test_token_loaded_from_secret_file()]] - code - gateway/tests/test_voice_gateway.py
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
- [[test_ws_connectionclosed_error_logs_info_no_traceback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_connectionclosed_ok_logs_info_no_traceback()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_default_agent_is_direct()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_direct_agent_pipeline_error_pops_history_and_recovery_send_fails()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_dirty_close_before_initial_state_is_handled_cleanly()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_empty_transcript_goes_idle()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_pipeline_error_logs_and_recovers_to_idle()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_token_check_uses_constant_time_comparison()]] - code - gateway/tests/test_voice_gateway.py
- [[transcribe() calls the model and returns joined segment text.]] - rationale - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_voice_gatewaypy
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_asyncio_8]]
- 14 edges to [[_COMMUNITY_mock_stream]]
- 10 edges to [[_COMMUNITY_app]]
- 9 edges to [[_COMMUNITY__call_llm_stream]]
- 7 edges to [[_COMMUNITY_tts.py]]
- 5 edges to [[_COMMUNITY_AsyncMock]]
- 2 edges to [[_COMMUNITY_test_voice_latency_guard.py]]
- 2 edges to [[_COMMUNITY_test_voice_stt_model_ab.py]]
- 1 edge to [[_COMMUNITY_TestNormalizeForSpeech]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_server.py]]

## Top bridge nodes
- [[test_voice_gateway.py]] - degree 116, connects to 10 communities
- [[test_ws_empty_transcript_goes_idle()]] - degree 5, connects to 3 communities
- [[_fw_client()]] - degree 8, connects to 1 community
- [[_run_disconnect_test()]] - degree 5, connects to 1 community
- [[test_ws_direct_agent_pipeline_error_pops_history_and_recovery_send_fails()]] - degree 5, connects to 1 community
