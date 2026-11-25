---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "EgressAction"
location: "L270"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/EgressAction
---

# TestAuditStorePersistence

## Connections
- [[dot-test_allow_is_not_persisted_to_audit_store()]] - `method` [EXTRACTED]
- [[dot-test_deny_is_persisted_to_audit_store()]] - `method` [EXTRACTED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[FakeAuditStore_1]] - `contains` [EXTRACTED]
- [[Only DENY decisions are persisted to the tamper-evident audit store. ALLOW…]] - `rationale_for` [EXTRACTED]
- [[test_egress_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/EgressAction
