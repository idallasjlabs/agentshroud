---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "rationale"
community: "SOC RBAC & Auth"
location: "L316"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SOC_RBAC__Auth
---

# Cleartext injection is not re-rotated into noise (indicator already present).

## Connections
- [[test_encoding_detector_rot13_skips_already_visible_injection()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SOC_RBAC__Auth