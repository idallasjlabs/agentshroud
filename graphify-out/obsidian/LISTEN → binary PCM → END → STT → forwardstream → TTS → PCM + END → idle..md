---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "mock_stream"
location: "L925"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/mock_stream
---

# LISTEN → binary PCM → END → STT → /forward/stream → TTS → PCM + END → idle.

## Connections
- [[test_ws_full_utterance_state_sequence()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/mock_stream
