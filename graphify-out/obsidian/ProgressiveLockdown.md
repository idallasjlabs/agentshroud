---
source_file: "gateway/security/progressive_lockdown.py"
type: "code"
community: "Progressive Lockdown"
location: "L63"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Progressive_Lockdown
---

# ProgressiveLockdown

## Connections
- [[.__init__()_30]] - `calls` [EXTRACTED]
- [[.__init__()_86]] - `method` [EXTRACTED]
- [[._get_state()]] - `method` [EXTRACTED]
- [[.all_statuses()]] - `method` [EXTRACTED]
- [[.get_status()_2]] - `method` [EXTRACTED]
- [[.is_suspended()]] - `method` [EXTRACTED]
- [[.record_block()]] - `method` [EXTRACTED]
- [[.reset()_1]] - `method` [EXTRACTED]
- [[.test_alert_level_at_3_blocks()]] - `calls` [EXTRACTED]
- [[.test_all_statuses_empty_initially()]] - `calls` [EXTRACTED]
- [[.test_all_statuses_excludes_reset_users()]] - `calls` [EXTRACTED]
- [[.test_all_statuses_tracks_all_users()]] - `calls` [EXTRACTED]
- [[.test_escalated_level_at_5_blocks()]] - `calls` [EXTRACTED]
- [[.test_no_notify_below_alert_threshold()]] - `calls` [EXTRACTED]
- [[.test_notify_owner_fires_once_per_level()]] - `calls` [EXTRACTED]
- [[.test_reset_false_for_unknown_user()]] - `calls` [EXTRACTED]
- [[.test_reset_removes_suspended_state()]] - `calls` [EXTRACTED]
- [[.test_reset_true_for_known_user()]] - `calls` [EXTRACTED]
- [[.test_suspended_level_at_10_blocks()]] - `calls` [EXTRACTED]
- [[Any_18]] - `uses` [INFERRED]
- [[FakePipelineResult]] - `uses` [INFERRED]
- [[FakeRBAC]] - `uses` [INFERRED]
- [[PassthroughPipeline]] - `uses` [INFERRED]
- [[TelegramAPIProxy_1]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[TestCollabLockdownNotifications]] - `uses` [INFERRED]
- [[TestLockedCommand]] - `uses` [INFERRED]
- [[TestProgressiveLockdownUnit]] - `uses` [INFERRED]
- [[TestSuspendedDropNotice]] - `uses` [INFERRED]
- [[TestUnlockCommand]] - `uses` [INFERRED]
- [[Tracks per-user block counts and returns escalation actions.      Thread-safe fo]] - `rationale_for` [EXTRACTED]
- [[_OutboundScan]] - `uses` [INFERRED]
- [[progressive_lockdown.py]] - `contains` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_progressive_lockdown.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Progressive_Lockdown