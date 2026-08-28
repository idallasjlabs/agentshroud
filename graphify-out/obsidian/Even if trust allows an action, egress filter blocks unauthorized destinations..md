---
source_file: "gateway/tests/test_security_integration.py"
type: "rationale"
community: "PII Sanitizer & E2E Tests"
location: "L288"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/PII_Sanitizer__E2E_Tests
---

# Even if trust allows an action, egress filter blocks unauthorized destinations.

## Connections
- [[test_egress_blocks_unauthorized_after_trust_check()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/PII_Sanitizer__E2E_Tests