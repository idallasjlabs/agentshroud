---
type: community
cohesion: 0.07
members: 63
---

# Progressive Lockdown

**Cohesion:** 0.07 - loosely connected
**Members:** 63 nodes

## Members
- [[.__init__()_30]] - code - gateway/proxy/telegram_proxy.py
- [[.__init__()_86]] - code - gateway/security/progressive_lockdown.py
- [[.__init__()_130]] - code - gateway/tests/test_progressive_lockdown.py
- [[._get_state()]] - code - gateway/security/progressive_lockdown.py
- [[._run_owner_cmd()]] - code - gateway/tests/test_progressive_lockdown.py
- [[._run_owner_cmd()_1]] - code - gateway/tests/test_progressive_lockdown.py
- [[.all_statuses()]] - code - gateway/security/progressive_lockdown.py
- [[.get_status()_2]] - code - gateway/security/progressive_lockdown.py
- [[.is_owner()_2]] - code - gateway/tests/test_progressive_lockdown.py
- [[.is_suspended()]] - code - gateway/security/progressive_lockdown.py
- [[.process_inbound()_4]] - code - gateway/tests/test_progressive_lockdown.py
- [[.record_block()]] - code - gateway/security/progressive_lockdown.py
- [[.reset()_1]] - code - gateway/security/progressive_lockdown.py
- [[.test_alert_level_at_3_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_all_statuses_empty_initially()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_all_statuses_excludes_reset_users()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_all_statuses_tracks_all_users()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_escalated_level_at_5_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_locked_includes_unlock_hint()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_locked_lists_suspended_user()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_locked_no_active_lockdowns()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_locked_shows_all_non_normal_users()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_no_notify_below_alert_threshold()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_notify_owner_fires_once_per_level()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_owner_messages_pass_despite_collab_suspension()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_reset_false_for_unknown_user()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_reset_removes_suspended_state()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_reset_true_for_known_user()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_suspended_drop_notice_respects_cooldown()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_suspended_level_at_10_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_suspended_user_gets_drop_notice()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_unlock_clears_suspended_drop_cooldown()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_unlock_known_user_succeeds()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_unlock_unknown_user_reports_no_state()]] - code - gateway/tests/test_progressive_lockdown.py
- [[.test_unlock_without_user_id_shows_usage()]] - code - gateway/tests/test_progressive_lockdown.py
- [[Drive a single owner command through the proxy and capture admin notices.]] - rationale - gateway/tests/test_progressive_lockdown.py
- [[FakePipelineResult]] - code - gateway/tests/test_progressive_lockdown.py
- [[FakeRBAC]] - code - gateway/tests/test_progressive_lockdown.py
- [[LockdownAction]] - code - gateway/security/progressive_lockdown.py
- [[LockdownLevel]] - code - gateway/security/progressive_lockdown.py
- [[Owner command reset lockdown state for a user. Returns True if existed.]] - rationale - gateway/security/progressive_lockdown.py
- [[Owner messages must never be blocked by the suspension logic.]] - rationale - gateway/tests/test_progressive_lockdown.py
- [[PassthroughPipeline]] - code - gateway/tests/test_progressive_lockdown.py
- [[ProgressiveLockdown]] - code - gateway/security/progressive_lockdown.py
- [[Record one blocked request for user_id and return the resulting action.]] - rationale - gateway/security/progressive_lockdown.py
- [[Return True if the user's session is currently suspended.]] - rationale - gateway/security/progressive_lockdown.py
- [[Return a TelegramAPIProxy wired with fake deps (no real HTTP).]] - rationale - gateway/tests/test_progressive_lockdown.py
- [[Return current lockdown state for a user (for collabs or owner inspection).]] - rationale - gateway/security/progressive_lockdown.py
- [[Return lockdown status for all tracked users.]] - rationale - gateway/security/progressive_lockdown.py
- [[TelegramAPIProxy_1]] - code - gateway/tests/test_progressive_lockdown.py
- [[TestLockedCommand]] - code - gateway/tests/test_progressive_lockdown.py
- [[TestProgressiveLockdownUnit]] - code - gateway/tests/test_progressive_lockdown.py
- [[TestSuspendedDropNotice]] - code - gateway/tests/test_progressive_lockdown.py
- [[TestUnlockCommand]] - code - gateway/tests/test_progressive_lockdown.py
- [[Tracks per-user block counts and returns escalation actions.      Thread-safe fo]] - rationale - gateway/security/progressive_lockdown.py
- [[UserLockdownState]] - code - gateway/security/progressive_lockdown.py
- [[Verify suspended users get a drop notice (rate-limited to avoid spam).]] - rationale - gateway/tests/test_progressive_lockdown.py
- [[What the caller should do in response to this block.]] - rationale - gateway/security/progressive_lockdown.py
- [[_make_proxy()]] - code - gateway/tests/test_progressive_lockdown.py
- [[_make_update()]] - code - gateway/tests/test_progressive_lockdown.py
- [[_wrap()]] - code - gateway/tests/test_progressive_lockdown.py
- [[progressive_lockdown.py]] - code - gateway/security/progressive_lockdown.py
- [[test_progressive_lockdown.py]] - code - gateway/tests/test_progressive_lockdown.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Progressive_Lockdown
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 4 edges to [[_COMMUNITY_Module Group 358]]
- 3 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 2 edges to [[_COMMUNITY_Module Group 208]]
- 1 edge to [[_COMMUNITY_Authentication & Rate Limiting]]
- 1 edge to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 1 edge to [[_COMMUNITY_Module Group 60]]

## Top bridge nodes
- [[ProgressiveLockdown]] - degree 35, connects to 4 communities
- [[.__init__()_30]] - degree 4, connects to 3 communities
- [[_make_proxy()]] - degree 18, connects to 2 communities
- [[test_progressive_lockdown.py]] - degree 14, connects to 2 communities
- [[LockdownLevel]] - degree 13, connects to 2 communities
