---
type: community
cohesion: 0.03
members: 101
---

# Voice Gateway Routing Tests

**Cohesion:** 0.03 - loosely connected
**Members:** 101 nodes

## Members
- [[agent=direct must route to _call_llm (fast path), not forward.]] - rationale - gateway/tests/test_voice_gateway.py
- [[agent=hermes must route to _call_agent (gateway forward), not _call_llm.]] - rationale - gateway/tests/test_voice_gateway.py
- [[A 'set volume' updates the tracked level so a later query reports it — proves…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A 'use Claude' override must survive a reconnect a later connection with no…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A STOP arriving outside SPEAKING (e.g. the tap landed just as TTS ended) must…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A bare 'tell Hermes' must NOT reach any agent yet it only sets the sticky…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A bare 'use Claude' must NOT reach any agent the server updates the sticky…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A bare LISTEN after a stale partial upload must NOT prepend old audio.]] - rationale - gateway/tests/test_voice_gateway.py
- [[A device 'STOP' text frame during the TTS send phase must abort the remaining…]] - rationale - gateway/tests/test_voice_gateway.py
- [[A resume cache older than the freshness window must not replay.]] - rationale - gateway/tests/test_voice_gateway.py
- [[A wedged TTS synthesis (e.g. blocked voice-pack download — live incident…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Before any set, 'what is the volume' speaks the unknown-state reply and still…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build a MagicMock WebSocket for direct voice_endpoint() tests. Frames are…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Direct-path replies must start TTS synthesis on the first sentence while the…]] - rationale - gateway/tests/test_voice_gateway.py
- [[If a device sends LISTEN but never sends END (crash  stuck firmware), the…]] - rationale - gateway/tests/test_voice_gateway.py
- [[If the socket dies during the TTS downlink, the NEXT connection must receive…]] - rationale - gateway/tests/test_voice_gateway.py
- [[LISTEN offset with an expired cache must behave like a fresh LISTEN (the…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Minimal S16LE silence.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Remote-diag {log...} frames arriving DURING the TTS send phase must be…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Set volume 80. What time is it' must apply the volume AND route the remaining…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Tell Hermes to check my email.' must switch the agent AND route the remaining…]] - rationale - gateway/tests/test_voice_gateway.py
- [[Use Claude. What's on my calendar' must switch the model AND route the…]] - rationale - gateway/tests/test_voice_gateway.py
- [[What's the volume' must NOT reach the agent after a prior set the server…]] - rationale - gateway/tests/test_voice_gateway.py
- [[When split_for_speech returns multiple sentences, the pipelined TTS loop must…]] - rationale - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()]] - code - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()_2]] - code - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()_3]] - code - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()_4]] - code - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()_5]] - code - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()_6]] - code - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()_7]] - code - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()_8]] - code - gateway/tests/test_voice_gateway.py
- [[_agent_must_not_be_called()_9]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_2]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_3]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_4]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_5]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_6]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_7]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_8]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_9]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_10]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth()_11]] - code - gateway/tests/test_voice_gateway.py
- [[_capture_synth2()]] - code - gateway/tests/test_voice_gateway.py
- [[_hung_synthesize()]] - code - gateway/tests/test_voice_gateway.py
- [[_llm_must_not_be_called()]] - code - gateway/tests/test_voice_gateway.py
- [[_llm_must_not_be_called()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_llm_must_not_be_called()_2]] - code - gateway/tests/test_voice_gateway.py
- [[_llm_must_not_be_called()_3]] - code - gateway/tests/test_voice_gateway.py
- [[_llm_must_not_be_called()_4]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_agent()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_agent()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_agent()_2]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_agent()_3]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_agent()_4]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_agent()_5]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_agent()_6]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_agent()_7]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_agent()_8]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_llm()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_llm()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_llm()_2]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_llm()_3]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_llm_stream()]] - code - gateway/tests/test_voice_gateway.py
- [[_mock_ws()]] - code - gateway/tests/test_voice_gateway.py
- [[_pcm_bytes()]] - code - gateway/tests/test_voice_gateway.py
- [[_push_stop_on_first_pcm()]] - code - gateway/tests/test_voice_gateway.py
- [[_receive()]] - code - gateway/tests/test_voice_gateway.py
- [[_send_bytes_then_die()]] - code - gateway/tests/test_voice_gateway.py
- [[asyncio_1]] - code
- [[set volume X%' must NOT reach the agent the server sends a…]] - rationale - gateway/tests/test_voice_gateway.py
- [[test_bare_listen_starts_fresh()]] - code - gateway/tests/test_voice_gateway.py
- [[test_listen_offset_with_stale_cache_degrades_to_fresh()]] - code - gateway/tests/test_voice_gateway.py
- [[test_listen_without_end_times_out()]] - code - gateway/tests/test_voice_gateway.py
- [[test_switch_overrides_persist_across_reconnect()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_resume_after_mid_stream_disconnect()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_resume_stale_cache_ignored()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_device_log_during_speaking_still_recorded()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_direct_agent_calls_call_llm()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_direct_agent_streams_tts_before_full_reply()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_hermes_agent_calls_call_agent()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_hung_tts_synthesis_still_returns_idle()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_set_then_query_reports_the_set_level()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_stale_stop_when_idle_is_ignored()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_stop_during_speaking_aborts_tts()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_tell_agent_command_intercepted()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_tell_agent_command_with_chained_instruction()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_tts_pipeline_sends_all_sentences()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_use_local_command_confirms_with_model_name()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_use_local_command_reflects_live_voice_model()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_use_model_command_intercepted()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_use_model_command_with_chained_question()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_volume_command_intercepted()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_volume_command_with_chained_question()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_volume_query_intercepted_returns_tracked_level()]] - code - gateway/tests/test_voice_gateway.py
- [[test_ws_volume_query_unknown_state_intercepted()]] - code - gateway/tests/test_voice_gateway.py
- [[use local' must confirm with and display whatever _VOICE_MODEL currently is,…]] - rationale - gateway/tests/test_voice_gateway.py
- [[use qwen' sets agent='direct', model='qwen3-14b', and confirms with the actual…]] - rationale - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Voice_Gateway_Routing_Tests
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_Voice Gateway Test Fixtures]]
- 15 edges to [[_COMMUNITY_Community 47]]
- 3 edges to [[_COMMUNITY_Community 1156]]
- 1 edge to [[_COMMUNITY_Community 176]]
- 1 edge to [[_COMMUNITY_Voice Gateway STT & Browser Security]]

## Top bridge nodes
- [[asyncio_1]] - degree 42, connects to 4 communities
- [[_pcm_bytes()]] - degree 26, connects to 3 communities
- [[_mock_ws()]] - degree 25, connects to 2 communities
- [[test_switch_overrides_persist_across_reconnect()]] - degree 11, connects to 1 community
- [[test_ws_tell_agent_command_with_chained_instruction()]] - degree 11, connects to 1 community