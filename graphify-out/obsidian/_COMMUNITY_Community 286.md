---
type: community
members: 28
---

# Community 286

**Members:** 28 nodes

## Members
- [[Any_79]] - code - voice_gateway/tts.py
- [[Frequencies well below the Nyquist (≤3 kHz) must pass through with minimal     a]] - rationale - gateway/tests/test_voice_gateway.py
- [[Kaiser-windowed sinc anti-aliasing filter suppresses content above the output]] - rationale - gateway/tests/test_voice_gateway.py
- [[Resample raw S16LE mono PCM from src_rate Hz to dst_rate Hz.      For downsa]] - rationale - voice_gateway/tts.py
- [[Return text suitable for TTS synthesis on the ESP32 voice interface.      Two]] - rationale - voice_gateway/tts.py
- [[Split an agent reply into ordered sentence-sized TTS chunks.      Applies normal]] - rationale - voice_gateway/tts.py
- [[Synthesize text to raw S16LE PCM mono audio bytes at TARGET_SAMPLE_RATE.]] - rationale - voice_gateway/tts.py
- [[_TTS_LEAD_SILENCE — 0.8s leading silence pad constant]] - code - voice_gateway/server.py
- [[_TTS_SENTENCE_GAP — 60ms inter-sentence silence constant]] - code - voice_gateway/server.py
- [[_call_agent_stream() — SSE streaming from gateway forwardstream]] - code - voice_gateway/server.py
- [[_call_llm() — fast-path POST to gateway v1chatcompletions]] - code - voice_gateway/server.py
- [[_get_pipeline()]] - code - voice_gateway/tts.py
- [[_parse_model_switch_command() — parses spoken usetellswitch commands]] - code - voice_gateway/server.py
- [[_parse_volume_command() — parses spoken 'set volume X%' command]] - code - voice_gateway/server.py
- [[_record_turn_latency() — structured per-turn latency logging]] - code - voice_gateway/server.py
- [[_resample_s16le_mono()]] - code - voice_gateway/tts.py
- [[_resample_s16le_mono() — Kaiser-windowed sinc resampler]] - code - voice_gateway/tts.py
- [[_voice_forward_metadata() — builds no_memory metadata for forward]] - code - voice_gateway/server.py
- [[_voice_system_message() — AGENTSHROUD_VERSION-grounded system prompt]] - code - voice_gateway/server.py
- [[normalize_for_speech()]] - code - voice_gateway/tts.py
- [[normalize_for_speech() — redaction-token + markdown normalization]] - code - voice_gateway/tts.py
- [[split_for_speech()]] - code - voice_gateway/tts.py
- [[split_for_speech() — splits reply into sentence-sized TTS chunks]] - code - voice_gateway/tts.py
- [[synthesize()]] - code - voice_gateway/tts.py
- [[test_resample_antialias_attenuates_above_nyquist()]] - code - gateway/tests/test_voice_gateway.py
- [[test_resample_passband_preserved()]] - code - gateway/tests/test_voice_gateway.py
- [[tts.py]] - code - voice_gateway/tts.py
- [[voice_endpoint() — voice WebSocket handler (IDLE→LISTENING→THINKING→SPEAKING state machine)]] - code - voice_gateway/server.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_286
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 37]]
- 2 edges to [[_COMMUNITY_Community 115]]
- 1 edge to [[_COMMUNITY_Community 145]]
- 1 edge to [[_COMMUNITY_Community 781]]
- 1 edge to [[_COMMUNITY_Community 740]]

## Top bridge nodes
- [[tts.py]] - degree 7, connects to 2 communities
- [[normalize_for_speech()]] - degree 6, connects to 2 communities
- [[split_for_speech()]] - degree 5, connects to 2 communities
- [[voice_endpoint() — voice WebSocket handler (IDLE→LISTENING→THINKING→SPEAKING state machine)]] - degree 10, connects to 1 community
- [[synthesize()]] - degree 9, connects to 1 community