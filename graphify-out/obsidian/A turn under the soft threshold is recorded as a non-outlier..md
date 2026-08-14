---
source_file: "gateway/tests/test_voice_latency_guard.py"
type: "rationale"
community: "voice_gateway/server.py"
location: "L54"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/voice_gateway/serverpy
---

# A turn under the soft threshold is recorded as a non-outlier.

## Connections
- [[test_record_turn_latency_normal_not_outlier()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/voice_gateway/serverpy