---
source_file: "voice_gateway/tts.py"
type: "code"
community: "Tts (voice_gateway)"
location: "L346"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Tts_voice_gateway
---

# synthesize()

## Connections
- [[Synthesize text to raw S16LE PCM mono audio bytes at TARGET_SAMPLE_RATE.]] - `rationale_for` [EXTRACTED]
- [[_get_pipeline()]] - `calls` [EXTRACTED]
- [[_get_pipeline() — lazy-inits Kokoro KPipeline singleton]] - `calls` [EXTRACTED]
- [[_resample_s16le_mono()]] - `calls` [EXTRACTED]
- [[_resample_s16le_mono() — Kaiser-windowed sinc resampler]] - `calls` [EXTRACTED]
- [[normalize_for_speech()]] - `calls` [EXTRACTED]
- [[normalize_for_speech() — redaction-token + markdown normalization]] - `calls` [EXTRACTED]
- [[tts.py]] - `contains` [EXTRACTED]
- [[voice_endpoint() — voice WebSocket handler (IDLE→LISTENING→THINKING→SPEAKING state machine)]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Tts_voice_gateway