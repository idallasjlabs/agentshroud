---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "test_voice_gateway.py"
location: "L3532"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_voice_gatewaypy
---

# Each synthesized sentence must ramp in/out over ~5 ms so per-sentence     Kokoro

## Connections
- [[test_tts_synthesize_fades_sentence_edges()]] - `rationale_for` [EXTRACTED]
- [[test_tts_synthesize_fades_sentence_edges()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_voice_gatewaypy