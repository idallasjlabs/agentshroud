---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "Voice Gateway"
location: "L148"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Voice_Gateway
---

# When OUTPUT_SAMPLE_RATE (24000, Kokoro native) != TARGET_SAMPLE_RATE     (16000)

## Connections
- [[test_tts_resamples_24000_to_16000()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Voice_Gateway