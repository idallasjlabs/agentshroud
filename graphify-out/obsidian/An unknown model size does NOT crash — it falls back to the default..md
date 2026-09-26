---
source_file: "gateway/tests/test_voice_stt_model_ab.py"
type: "rationale"
community: ".claude/settings.json (hook + permission wiring)"
location: "L53"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/claude/settingsjson_hook__permission_wiring
---

# An unknown model size does NOT crash — it falls back to the default.

## Connections
- [[test_select_model_size_invalid_falls_back_to_default()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/claude/settingsjson_hook__permission_wiring