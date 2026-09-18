---
source_file: "voice_gateway/stt.py"
type: "rationale"
community: "test_voice_stt_model_ab.py"
location: "L51"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_voice_stt_model_abpy
---

# Read WHISPER_MODEL_SIZE from the environment and validate it (A/B knob).

## Connections
- [[_resolve_model_size()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_voice_stt_model_abpy