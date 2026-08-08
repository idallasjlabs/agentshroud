---
source_file: "gateway/tests/test_voice_gateway.py"
type: "code"
community: "voice_gateway/server.py"
location: "L600"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/voice_gateway/serverpy
---

# test_call_llm_sends_full_history()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[The full messages history (system + prior turns) is sent in the request body.]] - `rationale_for` [EXTRACTED]
- [[_call_llm()]] - `calls` [EXTRACTED]
- [[test_voice_gateway.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/voice_gateway/serverpy