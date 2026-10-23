---
type: community
cohesion: 0.04
members: 74
---

# ProgressiveLockdown

**Cohesion:** 0.04 - loosely connected
**Members:** 74 nodes

## Members
- [[A non-400 HTTP error (e.g. 500) is a real failure, not the OpenClaw     no-strea]] - rationale - gateway/tests/test_voice_gateway.py
- [[A read-timeout (worst-case latency) is still recorded, then falls back.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[A turn exceeding the soft threshold is flagged as an outlier.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[A turn under the soft threshold is recorded as a non-outlier.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Agents with no streaming-compatible chat_path (OpenClaw) get a 400 from     the]] - rationale - gateway/tests/test_voice_gateway.py
- [[Best-effort model warm-up.      Preloading the STT model and TTS pipeline at sta]] - rationale - voice_gateway/server.py
- [[Build a system message with the current datetime for voice context.]] - rationale - voice_gateway/server.py
- [[Build the ``metadata`` dict attached to a voice ``forward`` request.      Defau]] - rationale - voice_gateway/server.py
- [[DEFAULT OFF forwardstream body carries NO metadata key — byte-for-byte legacy]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[DEFAULT OFF no_memory=False → empty metadata (request unchanged).]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Emit a structured per-turn latency record for a voice ``forward`` call.      Re]] - rationale - voice_gateway/server.py
- [[Exactly at the threshold is NOT an outlier (strict , not =).]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[FastAPI_3]] - code - voice_gateway/server.py
- [[Mock httpx.Response usable as the yield value of a mocked     AsyncClient.stream]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Normal (sub-threshold) turns log at INFO, not WARNING.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[ON forwardstream body carries metadata={no_memory True}.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[ON no_memory=True → {no_memory True} ephemeral tag.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Outliers log at WARNING; normal turns do not.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[Parse a spoken usetellaskswitch to modelagent command.      Returns (k]] - rationale - voice_gateway/server.py
- [[Request body must carry the configured model, max_tokens=150, and     streamtru]] - rationale - gateway/tests/test_voice_gateway.py
- [[Return the requested volume (0-100, clamped) for a spoken     set the volume]] - rationale - voice_gateway/server.py
- [[Route a voice utterance to a proxied agent via the AgentShroud gateway's     POS]] - rationale - voice_gateway/server.py
- [[Send a heartbeat every 4 s to keep Tailscale Funnel relay and hotspot NAT alive.]] - rationale - voice_gateway/server.py
- [[Spoken answer for a volume READ query the tracked level, or a     calibration h]] - rationale - voice_gateway/server.py
- [[Stream conversation history through the gateway's OpenAI-compat     endpoint, yi]] - rationale - voice_gateway/server.py
- [[The full messages history (system + prior turns) is sent in the request body.]] - rationale - gateway/tests/test_voice_gateway.py
- [[The module-level default flag is OFF unless VG_VOICE_NO_MEMORY is set.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[True for a spoken READ of the current volume (what's the volume,     current]] - rationale - voice_gateway/server.py
- [[WebSocket_7]] - code - voice_gateway/server.py
- [[When soft_threshold_s is omitted it is read from the module config at call time.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[_State]] - code - voice_gateway/server.py
- [[__main__.py]] - code - voice_gateway/__main__.py
- [[_answer_volume_query()]] - code - voice_gateway/server.py
- [[_call_agent_stream emits a latency record on the success path.]] - rationale - gateway/tests/test_voice_latency_guard.py
- [[_call_agent_stream()]] - code - voice_gateway/server.py
- [[_call_llm_stream()]] - code - voice_gateway/server.py
- [[_effective_voice_model()]] - code - voice_gateway/server.py
- [[_is_volume_query()]] - code - voice_gateway/server.py
- [[_keepalive()]] - code - voice_gateway/server.py
- [[_lifespan()]] - code - voice_gateway/server.py
- [[_mock_stream_resp()_1]] - code - gateway/tests/test_voice_latency_guard.py
- [[_parse_model_switch_command()]] - code - voice_gateway/server.py
- [[_parse_volume_command()]] - code - voice_gateway/server.py
- [[_record_turn_latency()]] - code - voice_gateway/server.py
- [[_send_state()]] - code - voice_gateway/server.py
- [[_sse_body()_1]] - code - gateway/tests/test_voice_latency_guard.py
- [[_voice_forward_metadata()]] - code - voice_gateway/server.py
- [[_voice_system_message()]] - code - voice_gateway/server.py
- [[_warm()]] - code - voice_gateway/server.py
- [[health()]] - code - voice_gateway/server.py
- [[omlx-keepwarm.sh]] - code - scripts/omlx-keepwarm.sh
- [[omlx-keepwarm.sh script]] - code - scripts/omlx-keepwarm.sh
- [[server.py]] - code - voice_gateway/server.py
- [[switch_model.sh main flow]] - code - scripts/switch_model.sh
- [[test_call_agent_default_body_has_no_metadata()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_no_memory_on_adds_ephemeral_tag()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_records_latency_on_read_timeout()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_records_latency_on_success()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_call_agent_stream_non_400_http_error_falls_back()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_agent_stream_non_streaming_agent_returns_telegram_notice()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_correct_model_and_max_tokens()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_full_history()]] - code - gateway/tests/test_voice_gateway.py
- [[test_record_turn_latency_boundary_is_not_outlier()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_default_threshold_from_module()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_normal_logs_info()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_normal_not_outlier()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_outlier_logs_warning()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_record_turn_latency_over_threshold_is_outlier()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_voice_forward_metadata_default_off_is_empty()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_voice_forward_metadata_module_default_is_off()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_voice_forward_metadata_on_sets_no_memory_tag()]] - code - gateway/tests/test_voice_latency_guard.py
- [[test_voice_latency_guard.py]] - code - gateway/tests/test_voice_latency_guard.py
- [[voice_endpoint()]] - code - voice_gateway/server.py
- [[voice_gateway__init__.py]] - code - voice_gateway/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProgressiveLockdown
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_main.rs]]
- 4 edges to [[_COMMUNITY_GATEWAY_OP_PROXY_URL]]
- 4 edges to [[_COMMUNITY_AgentShroud (system, C4 context) (2) (2)]]
- 3 edges to [[_COMMUNITY_i-gg SKILL — Git Workflow Guardian (GIT-GUARD)]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Verification (13-check driver)]]
- 1 edge to [[_COMMUNITY_proxy_status.py]]

## Top bridge nodes
- [[server.py]] - degree 29, connects to 5 communities
- [[_call_agent_stream()]] - degree 18, connects to 2 communities
- [[_call_llm_stream()]] - degree 11, connects to 2 communities
- [[test_call_agent_stream_non_400_http_error_falls_back()]] - degree 3, connects to 1 community
- [[test_call_agent_stream_non_streaming_agent_returns_telegram_notice()]] - degree 3, connects to 1 community
