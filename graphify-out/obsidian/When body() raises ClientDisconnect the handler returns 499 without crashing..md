---
source_file: "gateway/tests/test_security_fixes.py"
type: "rationale"
community: "gateway service (prod, sole egress point, 75-mod"
location: "L398"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/gateway_service_prod_sole_egress_point_75-mod
---

# When body() raises ClientDisconnect the handler returns 499 without crashing.

## Connections
- [[.test_client_disconnect_returns_499()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/gateway_service_prod_sole_egress_point_75-mod