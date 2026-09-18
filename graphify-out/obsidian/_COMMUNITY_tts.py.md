---
type: community
cohesion: 0.17
members: 15
---

# tts.py

**Cohesion:** 0.17 - loosely connected
**Members:** 15 nodes

## Members
- [[Any_68]] - code - voice_gateway/tts.py
- [[Resample raw S16LE mono PCM from src_rate Hz to dst_rate Hz.      For downsa]] - rationale - voice_gateway/tts.py
- [[Return text suitable for TTS synthesis on the ESP32 voice interface.      Two]] - rationale - voice_gateway/tts.py
- [[Split an agent reply into ordered sentence-sized TTS chunks.      Applies normal]] - rationale - voice_gateway/tts.py
- [[Synthesize text to raw S16LE PCM mono audio bytes at TARGET_SAMPLE_RATE.]] - rationale - voice_gateway/tts.py
- [[_get_pipeline()]] - code - voice_gateway/tts.py
- [[_get_pipeline() — lazy-inits Kokoro KPipeline singleton]] - code - voice_gateway/tts.py
- [[_resample_s16le_mono()]] - code - voice_gateway/tts.py
- [[_resample_s16le_mono() — Kaiser-windowed sinc resampler]] - code - voice_gateway/tts.py
- [[normalize_for_speech()]] - code - voice_gateway/tts.py
- [[normalize_for_speech() — redaction-token + markdown normalization]] - code - voice_gateway/tts.py
- [[split_for_speech()]] - code - voice_gateway/tts.py
- [[split_for_speech() — splits reply into sentence-sized TTS chunks]] - code - voice_gateway/tts.py
- [[synthesize()]] - code - voice_gateway/tts.py
- [[tts.py]] - code - voice_gateway/tts.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ttspy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]
- 1 edge to [[_COMMUNITY_server.py]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]

## Top bridge nodes
- [[tts.py]] - degree 8, connects to 3 communities