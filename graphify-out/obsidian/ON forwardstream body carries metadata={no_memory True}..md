---
source_file: "gateway/tests/test_voice_latency_guard.py"
type: "rationale"
community: "voice_gateway/server.py"
location: "L143"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/voice_gateway/serverpy
---

# ON: /forward/stream body carries metadata={"no_memory": True}.

## Connections
- [[test_call_agent_no_memory_on_adds_ephemeral_tag()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/voice_gateway/serverpy