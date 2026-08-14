---
source_file: "gateway/tests/test_voice_latency_guard.py"
type: "rationale"
community: "voice_gateway/server.py"
location: "L125"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/voice_gateway/serverpy
---

# DEFAULT OFF: /forward/stream body carries NO metadata key — byte-for-byte legacy

## Connections
- [[test_call_agent_default_body_has_no_metadata()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/voice_gateway/serverpy