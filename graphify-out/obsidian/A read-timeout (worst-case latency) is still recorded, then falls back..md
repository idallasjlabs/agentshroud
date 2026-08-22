---
source_file: "gateway/tests/test_voice_latency_guard.py"
type: "rationale"
community: "Voice Latency Guard"
location: "L185"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Voice_Latency_Guard
---

# A read-timeout (worst-case latency) is still recorded, then falls back.

## Connections
- [[test_call_agent_records_latency_on_read_timeout()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Voice_Latency_Guard