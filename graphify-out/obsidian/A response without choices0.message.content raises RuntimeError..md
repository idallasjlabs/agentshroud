---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "voice_gateway/server.py"
location: "L568"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/voice_gateway/serverpy
---

# A response without choices[0].message.content raises RuntimeError.

## Connections
- [[test_call_llm_malformed_response_raises()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/voice_gateway/serverpy