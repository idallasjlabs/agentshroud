---
type: community
members: 50
---

# Community 115

**Members:** 50 nodes

## Members
- [[A response without choices0.message.content raises RuntimeError.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Best-effort model warm-up.      Preloading the STT model and TTS pipeline at sta]] - rationale - voice_gateway/server.py
- [[Build a mock httpx response with an OpenAI-shape body.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Build a system message with the current datetime for voice context.]] - rationale - voice_gateway/server.py
- [[Build the per-device OTA token allowlist (SCRUM-58).      Owner-gated rollout o]] - rationale - voice_gateway/server.py
- [[Constant-time allowlist check for an OTA ``token=`` value.      Returns True wh]] - rationale - voice_gateway/server.py
- [[FastAPI_3]] - code - voice_gateway/server.py
- [[Leadingtrailing whitespace in the model reply is stripped.]] - rationale - gateway/tests/test_voice_gateway.py
- [[POST conversation history to the gateway's OpenAI-compat endpoint.      Fast pat]] - rationale - voice_gateway/server.py
- [[Parse a spoken usetellaskswitch to modelagent command.      Returns (k]] - rationale - voice_gateway/server.py
- [[Request_9]] - code - voice_gateway/server.py
- [[Request body must carry the configured model and max_tokens=150.]] - rationale - gateway/tests/test_voice_gateway.py
- [[Response_1]] - code - voice_gateway/server.py
- [[Return the requested volume (0-100, clamped) for a spoken     set the volume]] - rationale - voice_gateway/server.py
- [[Send a heartbeat every 4 s to keep Tailscale Funnel relay and hotspot NAT alive.]] - rationale - voice_gateway/server.py
- [[Serve the current ESP32 firmware binary for OTA (SCRUM-58).      Contract expect]] - rationale - voice_gateway/server.py
- [[Spoken answer for a volume READ query the tracked level, or a     calibration h]] - rationale - voice_gateway/server.py
- [[The full messages history (system + prior turns) is sent in the request body.]] - rationale - gateway/tests/test_voice_gateway.py
- [[True for a spoken READ of the current volume (what's the volume,     current]] - rationale - voice_gateway/server.py
- [[WebSocket_8]] - code - voice_gateway/server.py
- [[_State]] - code - voice_gateway/server.py
- [[__init__.py_17]] - code - voice_gateway/__init__.py
- [[__main__.py]] - code - voice_gateway/__main__.py
- [[_answer_volume_query()]] - code - voice_gateway/server.py
- [[_call_llm posts to v1chatcompletions and returns stripped content.]] - rationale - gateway/tests/test_voice_gateway.py
- [[_call_llm()]] - code - voice_gateway/server.py
- [[_effective_voice_model()]] - code - voice_gateway/server.py
- [[_get_firmware_etag()]] - code - voice_gateway/server.py
- [[_get_model() — lazy-loads faster-whisper WhisperModel]] - code - voice_gateway/stt.py
- [[_get_pipeline() — lazy-inits Kokoro KPipeline singleton]] - code - voice_gateway/tts.py
- [[_is_volume_query()]] - code - voice_gateway/server.py
- [[_keepalive()]] - code - voice_gateway/server.py
- [[_lifespan()]] - code - voice_gateway/server.py
- [[_load_ota_tokens()]] - code - voice_gateway/server.py
- [[_openai_resp()]] - code - gateway/tests/test_voice_gateway.py
- [[_ota_token_ok()]] - code - voice_gateway/server.py
- [[_parse_model_switch_command()]] - code - voice_gateway/server.py
- [[_parse_volume_command()]] - code - voice_gateway/server.py
- [[_send_state()]] - code - voice_gateway/server.py
- [[_voice_system_message()]] - code - voice_gateway/server.py
- [[_warm()]] - code - voice_gateway/server.py
- [[firmware_bin()]] - code - voice_gateway/server.py
- [[health()]] - code - voice_gateway/server.py
- [[server.py]] - code - voice_gateway/server.py
- [[test_call_llm_malformed_response_raises()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_returns_content()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_sends_correct_model_and_max_tokens()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_sends_full_history()]] - code - gateway/tests/test_voice_gateway.py
- [[test_call_llm_strips_whitespace()]] - code - gateway/tests/test_voice_gateway.py
- [[voice_endpoint()]] - code - voice_gateway/server.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_115
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 37]]
- 5 edges to [[_COMMUNITY_Community 109]]
- 5 edges to [[_COMMUNITY_Community 103]]
- 2 edges to [[_COMMUNITY_Community 78]]
- 2 edges to [[_COMMUNITY_Community 740]]
- 2 edges to [[_COMMUNITY_Community 286]]
- 1 edge to [[_COMMUNITY_Community 101]]

## Top bridge nodes
- [[server.py]] - degree 29, connects to 5 communities
- [[_call_llm()]] - degree 11, connects to 2 communities
- [[test_call_llm_returns_content()]] - degree 5, connects to 2 communities
- [[test_call_llm_strips_whitespace()]] - degree 5, connects to 2 communities
- [[test_call_llm_malformed_response_raises()]] - degree 4, connects to 2 communities