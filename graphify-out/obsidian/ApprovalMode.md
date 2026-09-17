---
source_file: "gateway/security/egress_approval.py"
type: "code"
community: "Ingest API & RBAC Core"
location: "L37"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Ingest_API__RBAC_Core
---

# ApprovalMode

## Connections
- [[dot-_load_rules()]] - `calls` [EXTRACTED]
- [[dot-add_rule()]] - `references` [EXTRACTED]
- [[dot-approve()]] - `references` [EXTRACTED]
- [[dot-deny()]] - `references` [EXTRACTED]
- [[Any_67]] - `uses` [INFERRED]
- [[Approval modes for rules.]] - `rationale_for` [EXTRACTED]
- [[AuthRequired]] - `uses` [INFERRED]
- [[Enum_3]] - `inherits` [EXTRACTED]
- [[Exception]] - `uses` [INFERRED]
- [[FakeAuditStore_1]] - `uses` [INFERRED]
- [[FakeCaller]] - `uses` [INFERRED]
- [[FakeGroup]] - `uses` [INFERRED]
- [[MCPProxyRequest]] - `uses` [INFERRED]
- [[MCPResultRequest]] - `uses` [INFERRED]
- [[OpProxyRequest]] - `uses` [INFERRED]
- [[Request]] - `uses` [INFERRED]
- [[SSHExecRequest_1]] - `uses` [INFERRED]
- [[SSHWriteFileRequest_1]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[TestEgressApprovalAPI]] - `uses` [INFERRED]
- [[TestEgressApprovalQueue]] - `uses` [INFERRED]
- [[WebSocket]] - `uses` [INFERRED]
- [[_OutboundScan]] - `uses` [INFERRED]
- [[_Svc]] - `uses` [INFERRED]
- [[egress_approval.py]] - `contains` [EXTRACTED]
- [[ingest_apimain.py]] - `imports` [EXTRACTED]
- [[socrouter.py]] - `imports` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_egress_approval.py]] - `imports` [EXTRACTED]
- [[test_soc_router_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Ingest_API__RBAC_Core