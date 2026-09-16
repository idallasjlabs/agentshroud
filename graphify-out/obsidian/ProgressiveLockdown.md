---
source_file: "gateway/security/progressive_lockdown.py"
type: "code"
community: "Community 58"
location: "L63"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_58
---

# ProgressiveLockdown

## Connections
- [[dot-__init__()_99]] - `calls` [EXTRACTED]
- [[dot-__init__()_167]] - `method` [EXTRACTED]
- [[dot-_get_state()]] - `method` [EXTRACTED]
- [[dot-all_statuses()]] - `method` [EXTRACTED]
- [[dot-get_status()_2]] - `method` [EXTRACTED]
- [[dot-is_suspended()]] - `method` [EXTRACTED]
- [[dot-record_block()]] - `method` [EXTRACTED]
- [[dot-reset()_2]] - `method` [EXTRACTED]
- [[dot-test_alert_level_at_3_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_all_statuses_empty_initially()]] - `calls` [EXTRACTED]
- [[dot-test_all_statuses_excludes_reset_users()]] - `calls` [EXTRACTED]
- [[dot-test_all_statuses_tracks_all_users()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_defaults_to_normal_when_no_lockdown_state()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_reports_real_lockdown_level()]] - `calls` [EXTRACTED]
- [[dot-test_build_record_reports_suspended_level()]] - `calls` [EXTRACTED]
- [[dot-test_escalated_level_at_5_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_no_notify_below_alert_threshold()]] - `calls` [EXTRACTED]
- [[dot-test_notify_owner_fires_once_per_level()]] - `calls` [EXTRACTED]
- [[dot-test_paused_is_independent_of_lockdown_level()]] - `calls` [EXTRACTED]
- [[dot-test_reset_false_for_unknown_user()]] - `calls` [EXTRACTED]
- [[dot-test_reset_removes_suspended_state()]] - `calls` [EXTRACTED]
- [[dot-test_reset_true_for_known_user()]] - `calls` [EXTRACTED]
- [[dot-test_suspended_level_at_10_blocks()]] - `calls` [EXTRACTED]
- [[Any_67]] - `uses` [INFERRED]
- [[ContributorManager]] - `calls` [EXTRACTED]
- [[FakePipelineResult_1]] - `uses` [INFERRED]
- [[FakeRBAC_1]] - `uses` [INFERRED]
- [[LockdownAction]] - `references` [EXTRACTED]
- [[LockdownLevel]] - `references` [EXTRACTED]
- [[PassthroughPipeline_1]] - `uses` [INFERRED]
- [[Progressive Lockdown UX Tests]] - `references` [EXTRACTED]
- [[TelegramAPIProxy_1]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[TestCollabLockdownNotifications]] - `uses` [INFERRED]
- [[TestLockdownLevelWiring]] - `uses` [INFERRED]
- [[TestLockedCommand]] - `uses` [INFERRED]
- [[TestPausedFieldWiring]] - `uses` [INFERRED]
- [[TestProgressiveLockdownUnit]] - `uses` [INFERRED]
- [[TestSuspendedDropNotice]] - `uses` [INFERRED]
- [[TestUnlockCommand]] - `uses` [INFERRED]
- [[Tracks per-user block counts and returns escalation actions.      Thread-safe fo]] - `rationale_for` [EXTRACTED]
- [[TrustManager]] - `semantically_similar_to` [INFERRED]
- [[_FakeRBAC_1]] - `uses` [INFERRED]
- [[_OutboundScan]] - `uses` [INFERRED]
- [[progressive_lockdown.py]] - `contains` [EXTRACTED]
- [[telegram_proxy.py]] - `imports` [EXTRACTED]
- [[test_progressive_lockdown.py]] - `imports` [EXTRACTED]
- [[test_soc_contributors.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_58