---
source_file: "gateway/tests/test_ws_e_rt2_inbound_encoding.py"
type: "rationale"
community: "SOC RBAC & Auth"
location: "L216"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/SOC_RBAC__Auth
---

# If the encoding detector raises, non-owner traffic is blocked (fail-closed).

## Connections
- [[test_inbound_encoding_detector_error_fails_closed()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/SOC_RBAC__Auth