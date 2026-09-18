---
source_file: "gateway/tests/test_egress_filter.py"
type: "code"
community: "EgressPolicy"
location: "L277"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/EgressPolicy
---

# FakeAuditStore

## Connections
- [[.__init__()_71]] - `method` [EXTRACTED]
- [[.log_event()]] - `method` [EXTRACTED]
- [[.test_allow_is_not_persisted_to_audit_store()]] - `calls` [EXTRACTED]
- [[.test_deny_is_persisted_to_audit_store()]] - `calls` [EXTRACTED]
- [[ApprovalResult]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressAttempt]] - `uses` [INFERRED]
- [[EgressFilter]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[test_egress_filter.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/EgressPolicy