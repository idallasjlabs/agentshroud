---
type: community
members: 37
---

# ProgressiveLockdown

**Members:** 37 nodes

## Members
- [[dot-__init__()_113]] - code - gateway/security/progressive_lockdown.py
- [[dot-all_statuses()]] - code - gateway/security/progressive_lockdown.py
- [[dot-get_status()_1]] - code - gateway/security/progressive_lockdown.py
- [[dot-reset()_1]] - code - gateway/security/progressive_lockdown.py
- [[dot-test_accepts_string_level()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_alert_level_at_3_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_all_statuses_empty_initially()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_all_statuses_excludes_reset_users()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_all_statuses_tracks_all_users()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_arbitrary_string_principals_are_isolated()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_async_gather_record_block_counts_exactly()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_escalated_floor_holds_against_later_low_block_counts()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_escalated_level_at_5_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_jumps_directly_to_requested_level()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_never_lowers_level()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_no_notify_below_alert_threshold()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_notify_owner_fires_once_per_level()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_rejects_unknown_level()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_reset_clears_escalation()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_reset_false_for_unknown_user()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_reset_removes_suspended_state()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_reset_true_for_known_user()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_same_level_does_not_renotify()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_suspended_level_at_10_blocks()]] - code - gateway/tests/test_progressive_lockdown.py
- [[dot-test_threaded_record_block_counts_exactly()]] - code - gateway/tests/test_progressive_lockdown.py
- [[Args decay_window_seconds When set, only blocks recorded within this many…]] - rationale - gateway/security/progressive_lockdown.py
- [[Owner command reset lockdown state for a principal. Returns True if existed.]] - rationale - gateway/security/progressive_lockdown.py
- [[ProgressiveLockdown]] - code - gateway/security/progressive_lockdown.py
- [[Return current lockdown state for a principal (for collabs or owner…]] - rationale - gateway/security/progressive_lockdown.py
- [[Return lockdown status for all tracked principals.]] - rationale - gateway/security/progressive_lockdown.py
- [[TestConcurrency]] - code - gateway/tests/test_progressive_lockdown.py
- [[TestEscalateTo]] - code - gateway/tests/test_progressive_lockdown.py
- [[TestPrincipalKeys]] - code - gateway/tests/test_progressive_lockdown.py
- [[TestProgressiveLockdownUnit]] - code - gateway/tests/test_progressive_lockdown.py
- [[Tracks per-principal block counts and returns escalation actions. Thread-safe…]] - rationale - gateway/security/progressive_lockdown.py
- [[hammer()]] - code - gateway/tests/test_progressive_lockdown.py
- [[one()]] - code - gateway/tests/test_progressive_lockdown.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ProgressiveLockdown
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_LockdownLevel]]
- 10 edges to [[_COMMUNITY_test_progressive_lockdown.py]]
- 8 edges to [[_COMMUNITY_FakeClock]]
- 8 edges to [[_COMMUNITY_ContributorManager]]
- 2 edges to [[_COMMUNITY_test_edge_service_routes.py]]
- 2 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 2 edges to [[_COMMUNITY_test_edge_pipeline.py]]
- 2 edges to [[_COMMUNITY_test_soc_edge.py]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[ProgressiveLockdown]] - degree 75, connects to 13 communities
- [[TestProgressiveLockdownUnit]] - degree 14, connects to 2 communities
- [[TestEscalateTo]] - degree 10, connects to 2 communities
- [[TestPrincipalKeys]] - degree 4, connects to 2 communities
- [[TestConcurrency]] - degree 4, connects to 1 community
