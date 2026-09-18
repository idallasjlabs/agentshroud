---
source_file: "gateway/tests/test_voice_stt_model_ab.py"
type: "rationale"
community: "test_voice_stt_model_ab.py"
location: "L122"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_voice_stt_model_abpy
---

# Setting WHISPER_MODEL_SIZE=base.en flips the resolved model (A/B).

## Connections
- [[test_module_model_size_env_override()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_voice_stt_model_abpy