---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "_call_agent_stream()"
location: "L1257"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_call_agent_stream
---

# A single corrupted SSE line logs a warning and is skipped — it must not     abor

## Connections
- [[test_call_agent_stream_malformed_json_line_skipped_not_fatal()_1]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_call_agent_stream