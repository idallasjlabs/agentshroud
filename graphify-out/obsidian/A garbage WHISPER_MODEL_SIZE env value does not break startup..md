---
source_file: "gateway/tests/test_voice_stt_model_ab.py"
type: "rationale"
community: ".claude/settings.json (hook + permission wiring)"
location: "L128"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/claude/settingsjson_hook__permission_wiring
---

# A garbage WHISPER_MODEL_SIZE env value does not break startup.

## Connections
- [[test_module_model_size_invalid_env_falls_back()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/claude/settingsjson_hook__permission_wiring