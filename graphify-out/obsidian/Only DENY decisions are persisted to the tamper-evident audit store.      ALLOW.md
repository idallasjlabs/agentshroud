---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "Gateway Test Suite"
location: "L271"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# Only DENY decisions are persisted to the tamper-evident audit store.      ALLOW

## Connections
- [[TestAuditStorePersistence]] - `rationale_for` [EXTRACTED]
- [[TestInteractiveApproval]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Gateway_Test_Suite