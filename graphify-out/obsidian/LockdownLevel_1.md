---
source_file: "gateway/security/progressive_lockdown.py"
type: "code"
community: "Community 25"
location: "L44"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_25
---

# LockdownLevel

## Connections
- [[._action()]] - `references` [EXTRACTED]
- [[._claim_notify()]] - `references` [EXTRACTED]
- [[._effective_level()]] - `references` [EXTRACTED]
- [[.escalate_to()]] - `references` [EXTRACTED]
- [[.level_of()]] - `references` [EXTRACTED]
- [[Any_6]] - `uses` [INFERRED]
- [[CallContext]] - `uses` [INFERRED]
- [[Clock_1]] - `uses` [INFERRED]
- [[EdgeCallPipeline]] - `uses` [INFERRED]
- [[EdgeDeps]] - `uses` [INFERRED]
- [[EdgePrincipal]] - `uses` [INFERRED]
- [[Enum]] - `inherits` [EXTRACTED]
- [[Facade]] - `uses` [INFERRED]
- [[FakeCaller]] - `uses` [INFERRED]
- [[FakeClock]] - `uses` [INFERRED]
- [[FakeFacade]] - `uses` [INFERRED]
- [[FakePipelineResult]] - `uses` [INFERRED]
- [[FakeRBAC]] - `uses` [INFERRED]
- [[LockdownLevel]] - `uses` [INFERRED]
- [[PassthroughPipeline]] - `uses` [INFERRED]
- [[ProgressiveLockdown]] - `references` [EXTRACTED]
- [[TelegramAPIProxy_1]] - `uses` [INFERRED]
- [[TestAgentsRegistry]] - `uses` [INFERRED]
- [[TestAuditRecord]] - `uses` [INFERRED]
- [[TestCollabLockdownNotifications]] - `uses` [INFERRED]
- [[TestCommandCenterStats]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestDecay]] - `uses` [INFERRED]
- [[TestEdgeEnroll]] - `uses` [INFERRED]
- [[TestEdgeEventOverWebSocket]] - `uses` [INFERRED]
- [[TestEdgeKill]] - `uses` [INFERRED]
- [[TestEdgeStatus]] - `uses` [INFERRED]
- [[TestEscalateTo]] - `uses` [INFERRED]
- [[TestLifespanWiring]] - `uses` [INFERRED]
- [[TestLocalAgentHealthHelper]] - `uses` [INFERRED]
- [[TestLockedCommand]] - `uses` [INFERRED]
- [[TestMonitorMode]] - `uses` [INFERRED]
- [[TestPrincipalKeys]] - `uses` [INFERRED]
- [[TestProgressiveLockdownUnit]] - `uses` [INFERRED]
- [[TestSuspendedDropNotice]] - `uses` [INFERRED]
- [[TestT1ToolAbuse]] - `uses` [INFERRED]
- [[TestT2Exfiltration]] - `uses` [INFERRED]
- [[TestT3Writes]] - `uses` [INFERRED]
- [[TestT4AuthN]] - `uses` [INFERRED]
- [[TestT9Abuse]] - `uses` [INFERRED]
- [[TestTelegramProxyInjection]] - `uses` [INFERRED]
- [[TestToolListing]] - `uses` [INFERRED]
- [[TestUnlockCommand]] - `uses` [INFERRED]
- [[VendorProfile]] - `uses` [INFERRED]
- [[VendorStats]] - `uses` [INFERRED]
- [[_Denied]] - `uses` [INFERRED]
- [[_Window]] - `uses` [INFERRED]
- [[_level_for_count()]] - `references` [EXTRACTED]
- [[_max_level()]] - `references` [EXTRACTED]
- [[call_pipeline.py]] - `imports` [EXTRACTED]
- [[progressive_lockdown.py]] - `contains` [EXTRACTED]
- [[str]] - `inherits` [EXTRACTED]
- [[test_edge_pipeline.py]] - `imports` [EXTRACTED]
- [[test_progressive_lockdown.py]] - `imports` [EXTRACTED]
- [[test_soc_edge.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Community_25