---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "_fake_kokoro_pipeline()"
location: "L142"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_fake_kokoro_pipeline
---

# synthesize() runs the Kokoro pipeline; when rates match no resampling occurs.

## Connections
- [[test_tts_synthesize_via_kokoro()]] - `rationale_for` [EXTRACTED]
- [[test_tts_synthesize_via_kokoro()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_fake_kokoro_pipeline