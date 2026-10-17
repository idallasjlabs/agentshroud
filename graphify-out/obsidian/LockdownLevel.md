---
source_file: "gateway/security/progressive_lockdown.py"
type: "code"
community: "TestToolChainAnalyzer"
location: "L27"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/TestToolChainAnalyzer
---

# LockdownLevel

## Connections
- [[Enum]] - `inherits` [EXTRACTED]
- [[FakePipelineResult_1]] - `uses` [INFERRED]
- [[FakeRBAC_1]] - `uses` [INFERRED]
- [[PassthroughPipeline_1]] - `uses` [INFERRED]
- [[ProgressiveLockdown]] - `references` [EXTRACTED]
- [[TelegramAPIProxy_3]] - `uses` [INFERRED]
- [[TestCollabLockdownNotifications]] - `uses` [INFERRED]
- [[TestLockedCommand]] - `uses` [INFERRED]
- [[TestProgressiveLockdownUnit]] - `uses` [INFERRED]
- [[TestSuspendedDropNotice]] - `uses` [INFERRED]
- [[TestUnlockCommand]] - `uses` [INFERRED]
- [[progressive_lockdown.py]] - `contains` [EXTRACTED]
- [[str]] - `inherits` [EXTRACTED]
- [[test_progressive_lockdown.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/TestToolChainAnalyzer
