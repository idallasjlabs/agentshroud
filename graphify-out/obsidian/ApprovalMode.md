---
source_file: "gateway/security/egress_approval.py"
type: "code"
community: "RBAC & SOC Realtime"
location: "L37"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/RBAC__SOC_Realtime
---

# ApprovalMode

## Connections
- [[._load_rules()]] - `calls` [EXTRACTED]
- [[.add_rule()]] - `references` [EXTRACTED]
- [[.approve()]] - `references` [EXTRACTED]
- [[.deny()]] - `references` [EXTRACTED]
- [[Any_21]] - `uses` [INFERRED]
- [[Approval modes for rules.]] - `rationale_for` [EXTRACTED]
- [[AuthRequired]] - `uses` [INFERRED]
- [[Enum]] - `inherits` [EXTRACTED]
- [[Exception_1]] - `uses` [INFERRED]
- [[FakeAuditStore_1]] - `uses` [INFERRED]
- [[FakeCaller]] - `uses` [INFERRED]
- [[FakeGroup]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Request_2]] - `uses` [INFERRED]
- [[SSHExecRequest]] - `uses` [INFERRED]
- [[SSHWriteFileRequest]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[TestEgressApprovalAPI]] - `uses` [INFERRED]
- [[TestEgressApprovalQueue]] - `uses` [INFERRED]
- [[WebSocket_3]] - `uses` [INFERRED]
- [[_OutboundScan]] - `uses` [INFERRED]
- [[_Svc]] - `uses` [INFERRED]
- [[egress_approval.py]] - `contains` [EXTRACTED]
- [[main.py_2]] - `imports` [EXTRACTED]
- [[router.py_1]] - `imports` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_egress_approval.py]] - `imports` [EXTRACTED]
- [[test_soc_router_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/RBAC__SOC_Realtime