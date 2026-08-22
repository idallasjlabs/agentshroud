---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "Voice Gateway"
location: "L814"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Voice_Gateway
---

# LISTEN → binary PCM → END → STT → /forward/stream → TTS → PCM + END → idle.

## Connections
- [[test_ws_full_utterance_state_sequence()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Voice_Gateway