---
source_file: "voice_gateway/server.py"
type: "code"
community: "Tts (voice_gateway)"
location: "L827-1333"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Tts_voice_gateway
---

# voice_endpoint() — /voice WebSocket handler (IDLE→LISTENING→THINKING→SPEAKING state machine)

## Connections
- [[_TTS_LEAD_SILENCE — 0.8s leading silence pad constant]] - `references` [EXTRACTED]
- [[_TTS_SENTENCE_GAP — 60ms inter-sentence silence constant]] - `references` [EXTRACTED]
- [[_call_agent_stream() — SSE streaming from gateway forwardstream]] - `calls` [EXTRACTED]
- [[_call_llm() — fast-path POST to gateway v1chatcompletions]] - `calls` [EXTRACTED]
- [[_parse_model_switch_command() — parses spoken usetellswitch commands]] - `calls` [EXTRACTED]
- [[_parse_volume_command() — parses spoken 'set volume X%' command]] - `calls` [EXTRACTED]
- [[_voice_system_message() — AGENTSHROUD_VERSION-grounded system prompt]] - `calls` [EXTRACTED]
- [[split_for_speech() — splits reply into sentence-sized TTS chunks]] - `calls` [EXTRACTED]
- [[synthesize()]] - `calls` [EXTRACTED]
- [[transcribe()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Tts_voice_gateway