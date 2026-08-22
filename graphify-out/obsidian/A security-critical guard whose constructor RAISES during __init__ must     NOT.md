---
source_file: "gateway/tests/test_middleware_coverage.py"
type: "rationale"
community: "Middleware & Session Isolation"
location: "L1027"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Middleware__Session_Isolation
---

# A security-critical guard whose constructor RAISES during __init__ must     NOT

## Connections
- [[TestCriticalGuardInitFailClosed]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Middleware__Session_Isolation