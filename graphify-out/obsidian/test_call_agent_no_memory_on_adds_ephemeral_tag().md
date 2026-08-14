---
source_file: "gateway/tests/test_voice_latency_guard.py"
type: "code"
community: "voice_gateway/server.py"
location: "L142"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/voice_gateway/serverpy
---

# test_call_agent_no_memory_on_adds_ephemeral_tag()

## Connections
- [[AsyncMock]] - `calls` [INFERRED]
- [[ON forwardstream body carries metadata={no_memory True}.]] - `rationale_for` [EXTRACTED]
- [[_call_agent_stream()]] - `calls` [EXTRACTED]
- [[test_voice_latency_guard.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/voice_gateway/serverpy