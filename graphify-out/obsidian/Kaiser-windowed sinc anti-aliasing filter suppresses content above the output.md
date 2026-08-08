---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "voice_gateway/tts.py"
location: "L1848"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/voice_gateway/ttspy
---

# Kaiser-windowed sinc anti-aliasing filter suppresses content above the output

## Connections
- [[test_resample_antialias_attenuates_above_nyquist()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/voice_gateway/ttspy