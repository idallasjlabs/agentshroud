---
source_file: "gateway/security/egress_approval.py"
type: "code"
community: "Gateway Test Suite"
location: "L46"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# EgressRequest

## Connections
- [[.request_approval()]] - `calls` [EXTRACTED]
- [[.test_approved_status()]] - `calls` [INFERRED]
- [[.test_cleanup_expired_requests()]] - `calls` [EXTRACTED]
- [[.test_construction()]] - `calls` [INFERRED]
- [[.test_pending_status_default()]] - `calls` [INFERRED]
- [[.test_red_risk_high_threat()]] - `calls` [INFERRED]
- [[Represents a pending egress approval request.]] - `rationale_for` [EXTRACTED]
- [[TestEgressApprovalAPI]] - `uses` [INFERRED]
- [[TestEgressApprovalQueue]] - `uses` [INFERRED]
- [[egress_approval.py]] - `contains` [EXTRACTED]
- [[test_egress_approval.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite