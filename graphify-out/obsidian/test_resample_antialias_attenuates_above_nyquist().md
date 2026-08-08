---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "voice_gateway/tts.py"
location: "L1847"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/voice_gateway/ttspy
---

# test_resample_antialias_attenuates_above_nyquist()

## Connections
- [[Kaiser-windowed sinc anti-aliasing filter suppresses content above the output]] - `rationale_for` [EXTRACTED]
- [[_resample_s16le_mono()]] - `calls` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/voice_gateway/ttspy