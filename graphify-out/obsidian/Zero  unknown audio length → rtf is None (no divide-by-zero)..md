---
source_file: "gateway/tests/test_voice_stt_model_ab.py"
type: "rationale"
community: ".claude/settings.json (hook + permission wiring)"
location: "L98"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/claude/settingsjson_hook__permission_wiring
---

# Zero / unknown audio length → rtf is None (no divide-by-zero).

## Connections
- [[test_record_transcription_latency_handles_zero_audio()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/claude/settingsjson_hook__permission_wiring