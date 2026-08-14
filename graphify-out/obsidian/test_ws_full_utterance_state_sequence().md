---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "Planning Docs"
location: "L813"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Planning_Docs
---

# test_ws_full_utterance_state_sequence()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[LISTEN → binary PCM → END → STT → forwardstream → TTS → PCM + END → idle.]] - `rationale_for` [EXTRACTED]
- [[_openai_resp()]] - `calls` [EXTRACTED]
- [[_pcm_bytes()]] - `calls` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Planning_Docs