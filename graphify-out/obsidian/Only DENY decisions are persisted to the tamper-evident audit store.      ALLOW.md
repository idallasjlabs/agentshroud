---
source_file: "gateway/tests/test_egress_filter.py"
type: "rationale"
community: "EgressApprovalQueue"
location: "L271"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/EgressApprovalQueue
---

# Only DENY decisions are persisted to the tamper-evident audit store.      ALLOW

## Connections
- [[TestAuditStorePersistence]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/EgressApprovalQueue