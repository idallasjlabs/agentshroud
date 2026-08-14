---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "rationale"
community: "Gateway Security Module"
location: "L308"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# rot13 decode is NOT applied to benign prose (no injection indicators).

## Connections
- [[test_encoding_detector_rot13_ignores_benign_prose()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Security_Module