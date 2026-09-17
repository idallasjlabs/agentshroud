---
source_file: "gateway/tests/test_voice_stt_model_ab.py"
type: "rationale"
community: "test_voice_stt_model_ab.py"
location: "L98"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_voice_stt_model_abpy
---

# Zero / unknown audio length → rtf is None (no divide-by-zero).

## Connections
- [[test_record_transcription_latency_handles_zero_audio()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_voice_stt_model_abpy