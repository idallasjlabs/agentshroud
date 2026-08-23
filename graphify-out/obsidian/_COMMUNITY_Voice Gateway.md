---
type: community
cohesion: 0.25
members: 8
---

# Voice Gateway

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[Stand-in for kokoro.KPipeline a callable yielding (graphemes, phonemes,     aud]] - rationale - gateway/tests/test_voice_gateway.py
- [[When OUTPUT_SAMPLE_RATE (24000, Kokoro native) != TARGET_SAMPLE_RATE     (16000)]] - rationale - gateway/tests/test_voice_gateway.py
- [[_fake_kokoro_pipeline()]] - code - gateway/tests/test_voice_gateway.py
- [[synthesize() feeds the normalised (no-markdown, no-token) text to Kokoro.      V]] - rationale - gateway/tests/test_voice_gateway.py
- [[synthesize() runs the Kokoro pipeline; when rates match no resampling occurs.]] - rationale - gateway/tests/test_voice_gateway.py
- [[test_tts_resamples_24000_to_16000()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_synthesize_passes_normalised_text_to_kokoro()]] - code - gateway/tests/test_voice_gateway.py
- [[test_tts_synthesize_via_kokoro()]] - code - gateway/tests/test_voice_gateway.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Voice_Gateway
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Voice Gateway]]

## Top bridge nodes
- [[_fake_kokoro_pipeline()]] - degree 5, connects to 1 community
- [[test_tts_resamples_24000_to_16000()]] - degree 3, connects to 1 community
- [[test_tts_synthesize_passes_normalised_text_to_kokoro()]] - degree 3, connects to 1 community
- [[test_tts_synthesize_via_kokoro()]] - degree 3, connects to 1 community