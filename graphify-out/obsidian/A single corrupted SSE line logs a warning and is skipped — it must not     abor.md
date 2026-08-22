---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "Voice Latency Guard"
location: "L1146"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Voice_Latency_Guard
---

# A single corrupted SSE line logs a warning and is skipped — it must not     abor

## Connections
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Voice_Latency_Guard