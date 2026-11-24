---
type: community
members: 45
---

# server.py

**Members:** 45 nodes

## Members
- [[Best-effort model warm-up. Preloading the STT model and TTS pipeline at startup…]] - rationale - voice_gateway/server.py
- [[Build a system message with the current datetime for voice context.]] - rationale - voice_gateway/server.py
- [[Build the per-device OTA token allowlist (SCRUM-58). Owner-gated rollout only…]] - rationale - voice_gateway/server.py
- [[Constant-time allowlist check for an OTA ``token=`` value. Returns True when…]] - rationale - voice_gateway/server.py
- [[Enum_2]] - code
- [[FastAPI]] - code
- [[Parse a spoken usetellaskswitch to modelagent command. Returns (kind,…]] - rationale - voice_gateway/server.py
- [[Request]] - code
- [[Response]] - code
- [[Return the requested volume (0-100, clamped) for a spoken set the volume…]] - rationale - voice_gateway/server.py
- [[Send a heartbeat every 4 s to keep Tailscale Funnel relay and hotspot NAT alive.]] - rationale - voice_gateway/server.py
- [[Serve the current ESP32 firmware binary for OTA (SCRUM-58). Contract expected…]] - rationale - voice_gateway/server.py
- [[Spoken answer for a volume READ query the tracked level, or a calibration hint…]] - rationale - voice_gateway/server.py
- [[Stream conversation history through the gateway's OpenAI-compat endpoint,…]] - rationale - voice_gateway/server.py
- [[True for a spoken READ of the current volume (what's the volume, current…]] - rationale - voice_gateway/server.py
- [[Voice Gateway — FastAPI app exposing GET health and WebSocket voice. Per-…]] - rationale - voice_gateway/server.py
- [[WebSocket]] - code
- [[_State]] - code - voice_gateway/server.py
- [[__main__.py]] - code - voice_gateway/__main__.py
- [[_answer_volume_query()]] - code - voice_gateway/server.py
- [[_call_llm_stream()]] - code - voice_gateway/server.py
- [[_effective_voice_model()]] - code - voice_gateway/server.py
- [[_get_firmware_etag()]] - code - voice_gateway/server.py
- [[_is_volume_query()]] - code - voice_gateway/server.py
- [[_keepalive()]] - code - voice_gateway/server.py
- [[_lifespan()]] - code - voice_gateway/server.py
- [[_load_ota_tokens()]] - code - voice_gateway/server.py
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
- [[firmware_bin()]] - code - voice_gateway/server.py
- [[health()]] - code - voice_gateway/server.py
- [[omlx-keepwarm.sh]] - code - scripts/omlx-keepwarm.sh
- [[omlx-keepwarm.sh script]] - code - scripts/omlx-keepwarm.sh
- [[server.py]] - code - voice_gateway/server.py
- [[switch_model.sh main flow]] - code - scripts/switch_model.sh
- [[voice_endpoint()]] - code - voice_gateway/server.py
- [[voice_gateway__init__.py]] - code - voice_gateway/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/serverpy
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 3 edges to [[_COMMUNITY_test_voice_latency_guard.py]]
- 1 edge to [[_COMMUNITY_hermes_dashboard_ws_proxy]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_test_voice_stt_model_ab.py]]
- 1 edge to [[_COMMUNITY_tts.py]]

## Top bridge nodes
- [[server.py]] - degree 31, connects to 5 communities
- [[voice_endpoint()]] - degree 15, connects to 1 community
- [[_call_llm_stream()]] - degree 11, connects to 1 community
- [[health()]] - degree 3, connects to 1 community
