---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "_pcm_bytes"
location: "L925"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_pcm_bytes
---

# LISTEN → binary PCM → END → STT → /forward/stream → TTS → PCM + END → idle.

## Connections
- [[test_ws_full_utterance_state_sequence()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_pcm_bytes
