---
source_file: "gateway/tests/test_voice_latency_guard.py"
type: "rationale"
community: "voice_gateway/server.py"
location: "L104"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/voice_gateway/serverpy
---

# DEFAULT OFF: no_memory=False → empty metadata (request unchanged).

## Connections
- [[test_voice_forward_metadata_default_off_is_empty()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/voice_gateway/serverpy