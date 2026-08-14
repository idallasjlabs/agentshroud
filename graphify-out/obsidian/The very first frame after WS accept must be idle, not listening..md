---
source_file: "gateway/tests/test_voice_gateway.py"
type: "rationale"
community: "Security Pipeline Core"
location: "L880"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Security_Pipeline_Core
---

# The very first frame after WS accept must be idle, not listening.

## Connections
- [[test_ws_connect_sends_idle_first()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Security_Pipeline_Core