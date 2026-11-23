---
source_file: "voice_gateway/stt.py"
type: "code"
community: "test_voice_stt_model_ab.py"
location: "L50"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_voice_stt_model_abpy
---

# _resolve_model_size()

## Connections
- [[Read WHISPER_MODEL_SIZE from the environment and validate it (AB knob).]] - `rationale_for` [EXTRACTED]
- [[select_model_size()]] - `calls` [EXTRACTED]
- [[stt.py]] - `contains` [EXTRACTED]
- [[test_module_model_size_defaults_to_small_en()]] - `calls` [EXTRACTED]
- [[test_module_model_size_env_override()]] - `calls` [EXTRACTED]
- [[test_module_model_size_invalid_env_falls_back()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_voice_stt_model_abpy
