---
source_file: "gateway/security/egress_approval.py"
type: "code"
community: "Egress Filter"
location: "L21"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Egress_Filter
---

# ApprovalResult

## Connections
- [[.request_approval()]] - `references` [EXTRACTED]
- [[EgressFilter_2]] - `uses` [INFERRED]
- [[Enum]] - `inherits` [EXTRACTED]
- [[FakeAuditStore]] - `uses` [INFERRED]
- [[Result of an approval request.]] - `rationale_for` [EXTRACTED]
- [[TestAuditStorePersistence]] - `uses` [INFERRED]
- [[TestEgressApprovalAPI]] - `uses` [INFERRED]
- [[TestEgressApprovalQueue]] - `uses` [INFERRED]
- [[TestEgressAttempt]] - `uses` [INFERRED]
- [[TestEgressPolicy]] - `uses` [INFERRED]
- [[TestEnforceMode]] - `uses` [INFERRED]
- [[TestIPRules]] - `uses` [INFERRED]
- [[TestInteractiveApproval]] - `uses` [INFERRED]
- [[TestLogging]] - `uses` [INFERRED]
- [[TestMonitorMode]] - `uses` [INFERRED]
- [[TestOpenClawResearchDomainsAllowlisted]] - `uses` [INFERRED]
- [[TestPerAgentPolicy]] - `uses` [INFERRED]
- [[TestSMTPIMAPPorts]] - `uses` [INFERRED]
- [[TestURLParsing]] - `uses` [INFERRED]
- [[egress_approval.py]] - `contains` [EXTRACTED]
- [[test_egress_approval.py]] - `imports` [EXTRACTED]
- [[test_egress_filter.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Egress_Filter