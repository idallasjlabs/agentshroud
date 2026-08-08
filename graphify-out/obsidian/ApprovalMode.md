---
source_file: "gateway/security/egress_approval.py"
type: "code"
community: "Auth & Exception Types"
location: "L37"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Auth__Exception_Types
---

# ApprovalMode

## Connections
- [[._load_rules()]] - `calls` [EXTRACTED]
- [[.add_rule()]] - `references` [EXTRACTED]
- [[.approve()]] - `references` [EXTRACTED]
- [[.deny()]] - `references` [EXTRACTED]
- [[Any_20]] - `uses` [INFERRED]
- [[Approval modes for rules.]] - `rationale_for` [EXTRACTED]
- [[AuthRequired_1]] - `uses` [INFERRED]
- [[Enum]] - `inherits` [EXTRACTED]
- [[Exception_1]] - `uses` [INFERRED]
- [[FakeAuditStore]] - `uses` [INFERRED]
- [[FakeCaller]] - `uses` [INFERRED]
- [[FakeGroup]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Request_3]] - `uses` [INFERRED]
- [[SSHExecRequest_1]] - `uses` [INFERRED]
- [[SSHWriteFileRequest_1]] - `uses` [INFERRED]
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

#graphify/code #graphify/INFERRED #community/Auth__Exception_Types