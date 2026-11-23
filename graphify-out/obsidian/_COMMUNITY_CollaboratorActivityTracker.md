---
type: community
members: 25
---

# CollaboratorActivityTracker

**Members:** 25 nodes

## Members
- [[dot-__init__()_156]] - code - gateway/security/collaborator_tracker.py
- [[dot-_coerce_timestamp()]] - code - gateway/security/collaborator_tracker.py
- [[dot-get_activity()]] - code - gateway/security/collaborator_tracker.py
- [[dot-get_activity_summary()]] - code - gateway/security/collaborator_tracker.py
- [[dot-get_health()_1]] - code - gateway/security/collaborator_tracker.py
- [[dot-test_failed_write_makes_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_initial_state_healthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[10-digit real UID must still be written to JSONL and markdown.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Best-effort float timestamp coercion for resilient log reads.]] - rationale - gateway/security/collaborator_tracker.py
- [[CollaboratorActivityTracker]] - code - gateway/security/collaborator_tracker.py
- [[CollaboratorActivityTracker.get_health() must return accurate counters.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner's Telegram first_name with pipe chars is replaced by owner_display_name.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Path_51]] - code
- [[Return a health snapshot suitable for statusdetail.]] - rationale - gateway/security/collaborator_tracker.py
- [[Return activity entries sorted newest-first. Args since Unix timestamp — only…]] - rationale - gateway/security/collaborator_tracker.py
- [[Return aggregated statistics over all recorded activity. Returns Dict with…]] - rationale - gateway/security/collaborator_tracker.py
- [[Short numeric UIDs ( 7 digits) must be silently dropped before any write.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[TestTrackerGetHealth]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tracks collaborator messages at the gateway level. Records every inbound…]] - rationale - gateway/security/collaborator_tracker.py
- [[UIDs matching test_user prefix must be silently dropped.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[test_fixture_uid_writes_blocked()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_owner_display_name_overrides_pipe()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_real_uid_writes_unblocked()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_test_user_prefix_blocked()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_unknown_user_recorded_when_dynamic_tracking_enabled()]] - code - gateway/tests/test_collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CollaboratorActivityTracker
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 5 edges to [[_COMMUNITY_test_lifespan_prune.py]]
- 4 edges to [[_COMMUNITY_dot-record_activity]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[CollaboratorActivityTracker]] - degree 28, connects to 6 communities
- [[TestTrackerGetHealth]] - degree 5, connects to 1 community
- [[test_fixture_uid_writes_blocked()]] - degree 3, connects to 1 community
- [[test_owner_display_name_overrides_pipe()]] - degree 3, connects to 1 community
- [[test_real_uid_writes_unblocked()]] - degree 3, connects to 1 community
