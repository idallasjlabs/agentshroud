---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "test_voice_gateway.py"
location: "L925"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_voice_gatewaypy
---

# LISTEN → binary PCM → END → STT → /forward/stream → TTS → PCM + END → idle.

## Connections
- [[test_ws_full_utterance_state_sequence()]] - `rationale_for` [EXTRACTED]
- [[test_ws_full_utterance_state_sequence()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_voice_gatewaypy