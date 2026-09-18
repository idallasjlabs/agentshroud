---
source_file: "gateway/security/rbac.py"
type: "code"
community: "ingest_api/main.py"
location: "L23"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/ingest_api/mainpy
---

# PermissionResult

## Connections
- [[.__init__()_11]] - `calls` [EXTRACTED]
- [[.check_group_permission()]] - `references` [EXTRACTED]
- [[.check_permission()]] - `references` [EXTRACTED]
- [[.check_tool_permission()]] - `references` [EXTRACTED]
- [[.list_users_and_roles()]] - `references` [EXTRACTED]
- [[.set_user_role()_1]] - `references` [EXTRACTED]
- [[Any_1]] - `uses` [INFERRED]
- [[RBACConfig_2]] - `uses` [INFERRED]
- [[Result of permission check.]] - `rationale_for` [EXTRACTED]
- [[Role_1]] - `uses` [INFERRED]
- [[SOCWebSocketHandler]] - `uses` [INFERRED]
- [[SimpleNamespace]] - `uses` [INFERRED]
- [[TestCoerceToWSEventExtra]] - `uses` [INFERRED]
- [[TestCollectRecentEvents]] - `uses` [INFERRED]
- [[TestEventFanOut]] - `uses` [INFERRED]
- [[TestFromAnomalyAlert]] - `uses` [INFERRED]
- [[TestFromAuditChainEntry]] - `uses` [INFERRED]
- [[TestFromDict]] - `uses` [INFERRED]
- [[TestFromEgressAttempt]] - `uses` [INFERRED]
- [[TestFromPipelineResult]] - `uses` [INFERRED]
- [[TestGetConfigToken]] - `uses` [INFERRED]
- [[TestHandlerRun]] - `uses` [INFERRED]
- [[TestMapSeverity]] - `uses` [INFERRED]
- [[TestResolveCaller]] - `uses` [INFERRED]
- [[TestSCLCaller]] - `uses` [INFERRED]
- [[TestSendEventAndKeepalive]] - `uses` [INFERRED]
- [[TestTokenStorePruning]] - `uses` [INFERRED]
- [[TestVerifyBearer]] - `uses` [INFERRED]
- [[TestWSSOCEndpoint]] - `uses` [INFERRED]
- [[ToolTier_1]] - `uses` [INFERRED]
- [[_FakeBus]] - `uses` [INFERRED]
- [[_FakeRBAC]] - `uses` [INFERRED]
- [[rbac.py]] - `contains` [EXTRACTED]
- [[test_soc_realtime_coverage.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/ingest_api/mainpy