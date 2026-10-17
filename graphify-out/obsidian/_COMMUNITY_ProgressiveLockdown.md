---
type: community
members: 50
---

# ProgressiveLockdown

**Members:** 50 nodes

## Members
- [[dot-__init__()_47]] - code - gateway/security/progressive_lockdown.py
- [[dot-__init__()_48]] - code - gateway/tests/test_soc_contributors.py
- [[dot-__init__()_49]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_get_state()]] - code - gateway/security/progressive_lockdown.py
- [[dot-all_statuses()]] - code - gateway/security/progressive_lockdown.py
- [[dot-get_status()]] - code - gateway/security/progressive_lockdown.py
- [[dot-get_user_role()_1]] - code - gateway/tests/test_soc_contributors.py
- [[dot-is_suspended()]] - code - gateway/security/progressive_lockdown.py
- [[dot-record_block()]] - code - gateway/security/progressive_lockdown.py
- [[dot-reset()_1]] - code - gateway/security/progressive_lockdown.py
- [[dot-test_alert_level_at_3_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_all_statuses_empty_initially()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_all_statuses_excludes_reset_users()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_all_statuses_tracks_all_users()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_build_record_defaults_to_normal_when_no_lockdown_state()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_does_not_crash_if_lockdown_missing()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_real_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_build_record_reports_suspended_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_escalated_level_at_5_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_list_contributors_populates_paused_per_user()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_load_paused_ids_defaults_to_empty_set_on_error()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_no_notify_below_alert_threshold()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_non_paused_user_reports_paused_false()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_notify_owner_fires_once_per_level()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_paused_is_independent_of_lockdown_level()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_paused_user_reports_paused_true()]] - code - gateway/tests/test_soc_contributors.py
- [[dot-test_reset_false_for_unknown_user()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_reset_removes_suspended_state()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_reset_true_for_known_user()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_suspended_level_at_10_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[Bug 2 contributors.py must call get_status(), not the nonexistent get_level().]] - rationale - gateway/tests/test_soc_contributors.py
- [[Constraint check paused (owner-initiated) and lockdown_level         (auto-esca]] - rationale - gateway/tests/test_soc_contributors.py
- [[LockdownAction]] - code - gateway/security/progressive_lockdown.py
- [[Owner command reset lockdown state for a user. Returns True if existed.]] - rationale - gateway/security/progressive_lockdown.py
- [[Progressive Lockdown UX Tests]] - code - gateway/tests/test_progressive_lockdown.py
- [[ProgressiveLockdown]] - code - gateway/security/progressive_lockdown.py
- [[Record one blocked request for user_id and return the resulting action.]] - rationale - gateway/security/progressive_lockdown.py
- [[Return True if the user's session is currently suspended.]] - rationale - gateway/security/progressive_lockdown.py
- [[Return current lockdown state for a user (for collabs or owner inspection).]] - rationale - gateway/security/progressive_lockdown.py
- [[Return lockdown status for all tracked users.]] - rationale - gateway/security/progressive_lockdown.py
- [[TestLockdownLevelWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestPausedFieldWiring]] - code - gateway/tests/test_soc_contributors.py
- [[TestProgressiveLockdownUnit]] - code - gateway/tests/test_progressive_lockdown.py
- [[Tracks per-user block counts and returns escalation actions.      Thread-safe fo]] - rationale - gateway/security/progressive_lockdown.py
- [[UserLockdownState]] - code - gateway/security/progressive_lockdown.py
- [[What the caller should do in response to this block.]] - rationale - gateway/security/progressive_lockdown.py
- [[_FakeRBAC_1]] - code - gateway/tests/test_soc_contributors.py
- [[_load_paused_ids must never crash record-building if the persisted         store]] - rationale - gateway/tests/test_soc_contributors.py
- [[paused feature ContributorRecord.paused reflects the persisted paused set.]] - rationale - gateway/tests/test_soc_contributors.py
- [[test_soc_contributors.py]] - code - gateway/tests/test_soc_contributors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProgressiveLockdown
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_socrouter.py]]
- 9 edges to [[_COMMUNITY_ProgressiveLockdown (2)]]
- 5 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 5 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_telegram_proxy.py (3)]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 1 edge to [[_COMMUNITY_dot-_filter_outbound]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown (2)_1]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]

## Top bridge nodes
- [[ProgressiveLockdown]] - degree 47, connects to 7 communities
- [[dot-__init__()_49]] - degree 5, connects to 4 communities
- [[TestProgressiveLockdownUnit]] - degree 15, connects to 3 communities
- [[_FakeRBAC_1]] - degree 14, connects to 2 communities
- [[TestPausedFieldWiring]] - degree 10, connects to 2 communities
