---
source_file: "gateway/tests/test_voice_latency_guard.py"
type: "rationale"
community: "voice_gateway/server.py"
location: "L164"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/voice_gateway/serverpy
---

# _call_agent_stream emits a latency record on the success path.

## Connections
- [[test_call_agent_records_latency_on_success()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/voice_gateway/serverpy