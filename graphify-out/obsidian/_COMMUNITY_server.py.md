---
type: community
cohesion: 0.05
members: 63
---

# server.py

**Cohesion:** 0.05 - loosely connected
**Members:** 63 nodes

## Members
- [[A final delta with no terminal punctuation is flushed once the SSE     stream en]] - rationale - gateway/tests/test_voice_gateway.py
- [[A malformedunexpected-shape SSE chunk is skipped, not fatal — a good     senten]] - rationale - gateway/tests/test_voice_gateway.py
- [[Best-effort model warm-up. Preloading the STT model and TTS pipeline at startup…]] - rationale - voice_gateway/server.py
- [[Build OpenAI-shaped streaming SSE lines for a sequence of content deltas.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build a system message with the current datetime for voice context.]] - rationale - voice_gateway/server.py
- [[Build the per-device OTA token allowlist (SCRUM-58). Owner-gated rollout only…]] - rationale - voice_gateway/server.py
- [[Constant-time allowlist check for an OTA ``token=`` value. Returns True when…]] - rationale - voice_gateway/server.py
- [[Enum]] - code
- [[FastAPI]] - code
- [[Parse a spoken usetellaskswitch to modelagent command. Returns (kind,…]] - rationale - voice_gateway/server.py
- [[Request_1]] - code
- [[Request body must carry the configured model, max_tokens=150, and     streamtru]] - rationale - gateway/tests/test_voice_gateway.py
- [[Response]] - code
- [[Return the requested volume (0-100, clamped) for a spoken set the volume…]] - rationale - voice_gateway/server.py
- [[Send a heartbeat every 4 s to keep Tailscale Funnel relay and hotspot NAT alive.]] - rationale - voice_gateway/server.py
- [[Serve the current ESP32 firmware binary for OTA (SCRUM-58). Contract expected…]] - rationale - voice_gateway/server.py
- [[Spoken answer for a volume READ query the tracked level, or a calibration hint…]] - rationale - voice_gateway/server.py
- [[Stream conversation history through the gateway's OpenAI-compat endpoint,…]] - rationale - voice_gateway/server.py
- [[The full messages history (system + prior turns) is sent in the request body.]] - rationale - gateway/tests/test_voice_gateway.py
- [[True for a spoken READ of the current volume (what's the volume, current…]] - rationale - voice_gateway/server.py
- [[Voice Gateway — FastAPI app exposing GET health and WebSocket voice. Per-…]] - rationale - voice_gateway/server.py
- [[WebSocket_1]] - code
- [[_State]] - code - voice_gateway/server.py
- [[__main__.py]] - code - voice_gateway/__main__.py
- [[_answer_volume_query()]] - code - voice_gateway/server.py
- [[_call_llm_stream posts to v1chatcompletions with streamtrue and     yields e]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_llm_stream()]] - code - voice_gateway/server.py
- [[_effective_voice_model()]] - code - voice_gateway/server.py
- [[_get_firmware_etag()]] - code - voice_gateway/server.py
- [[_is_volume_query()]] - code - voice_gateway/server.py
- [[_keepalive()]] - code - voice_gateway/server.py
- [[_lifespan()]] - code - voice_gateway/server.py
- [[_load_ota_tokens()]] - code - voice_gateway/server.py
- [[_openai_delta_lines()_1]] - code - gateway/tests/test_voice_gateway.py
- [[_ota_token_ok()]] - code - voice_gateway/server.py
- [[_parse_model_switch_command()]] - code - voice_gateway/server.py
- [[_parse_volume_command()]] - code - voice_gateway/server.py
- [[_raw_text_chunks()]] - code - voice_gateway/server.py
- [[_send_state()]] - code - voice_gateway/server.py
- [[_synthesize_all()]] - code - voice_gateway/server.py
- [[_voice_system_message()]] - code - voice_gateway/server.py
- [[_warm()]] - code - voice_gateway/server.py
- [[_watch_for_stop()]] - code - voice_gateway/server.py
- [[api_route]] - code
- [[cmd_persist()]] - code - scripts/tailscale-serve.sh
- [[cmd_start()]] - code - scripts/tailscale-serve.sh
- [[cmd_status()]] - code - scripts/tailscale-serve.sh
- [[cmd_stop()]] - code - scripts/tailscale-serve.sh
- [[firmware_bin()]] - code - voice_gateway/server.py
- [[health()]] - code - voice_gateway/server.py
- [[omlx-keepwarm.sh]] - code - scripts/omlx-keepwarm.sh
- [[omlx-keepwarm.sh script]] - code - scripts/omlx-keepwarm.sh
- [[server.py]] - code - voice_gateway/server.py
- [[switch_model.sh main flow]] - code - scripts/switch_model.sh
- [[tailscale-serve.sh]] - code - scripts/tailscale-serve.sh
- [[tailscale-serve.sh script]] - code - scripts/tailscale-serve.sh
- [[test_call_llm_stream_flushes_trailing_fragment()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_correct_model_and_max_tokens()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_sends_full_history()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_skips_malformed_chunks()_1]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_stream_yields_sentences()_1]] - code - gateway/tests/test_voice_gateway.py
- [[voice_endpoint()]] - code - voice_gateway/server.py
- [[voice_gateway__init__.py]] - code - voice_gateway/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/serverpy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 7 edges to [[_COMMUNITY_patch]]
- 5 edges to [[_COMMUNITY__call_agent_stream()]]
- 2 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_test_voice_stt_model_ab.py]]
- 1 edge to [[_COMMUNITY_tts.py]]

## Top bridge nodes
- [[server.py]] - degree 33, connects to 7 communities
- [[_call_llm_stream()]] - degree 17, connects to 3 communities
- [[voice_endpoint()]] - degree 16, connects to 1 community
- [[_openai_delta_lines()_1]] - degree 5, connects to 1 community
- [[test_call_llm_stream_flushes_trailing_fragment()_1]] - degree 4, connects to 1 community