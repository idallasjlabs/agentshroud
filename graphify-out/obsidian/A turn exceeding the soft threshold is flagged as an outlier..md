---
source_file: "gateway/tests/test_voice_latency_guard.py"
type: "rationale"
community: "_call_agent_stream()"
location: "L64"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/_call_agent_stream
---

# A turn exceeding the soft threshold is flagged as an outlier.

## Connections
- [[test_record_turn_latency_over_threshold_is_outlier()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/_call_agent_stream