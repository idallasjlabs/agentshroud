---
type: community
cohesion: 0.07
members: 34
---

# Module Group 140

**Cohesion:** 0.07 - loosely connected
**Members:** 34 nodes

## Members
- [[.__init__()_50]] - code - gateway/security/collaborator_tracker.py
- [[._append_contributor_log()]] - code - gateway/security/collaborator_tracker.py
- [[._coerce_timestamp()]] - code - gateway/security/collaborator_tracker.py
- [[._normalize_preview()]] - code - gateway/security/collaborator_tracker.py
- [[._normalize_username()]] - code - gateway/security/collaborator_tracker.py
- [[.get_activity()]] - code - gateway/security/collaborator_tracker.py
- [[.get_activity_summary()]] - code - gateway/security/collaborator_tracker.py
- [[.get_health()_1]] - code - gateway/security/collaborator_tracker.py
- [[.record_activity()]] - code - gateway/security/collaborator_tracker.py
- [[.test_failed_write_makes_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_initial_state_healthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[10-digit real UID must still be written to JSONL and markdown.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Append one activity entry for any tracked collaborator or the owner.          Ar]] - rationale - gateway/security/collaborator_tracker.py
- [[Best-effort float timestamp coercion for resilient log reads.]] - rationale - gateway/security/collaborator_tracker.py
- [[CollaboratorActivityTracker]] - code - gateway/security/collaborator_tracker.py
- [[CollaboratorActivityTracker.get_health() must return accurate counters.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Mirror activity into workspace contributor logs used by daily digests.]] - rationale - gateway/security/collaborator_tracker.py
- [[Normalize previews to single-line safe text for JSONL + markdown mirrors.]] - rationale - gateway/security/collaborator_tracker.py
- [[Normalize username for safe contributor-log tokenization.]] - rationale - gateway/security/collaborator_tracker.py
- [[Owner's Telegram first_name with pipe chars is replaced by owner_display_name.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Path_8]] - code - gateway/security/collaborator_tracker.py
- [[Return a health snapshot suitable for statusdetail.]] - rationale - gateway/security/collaborator_tracker.py
- [[Return activity entries sorted newest-first.          Args             since U]] - rationale - gateway/security/collaborator_tracker.py
- [[Return aggregated statistics over all recorded activity.          Returns]] - rationale - gateway/security/collaborator_tracker.py
- [[Short numeric UIDs ( 7 digits) must be silently dropped before any write.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[TestTrackerGetHealth]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tracks collaborator messages at the gateway level.      Records every inbound me]] - rationale - gateway/security/collaborator_tracker.py
- [[UIDs matching test_user prefix must be silently dropped.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[test_fixture_uid_writes_blocked()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_owner_display_name_overrides_pipe()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_real_uid_writes_unblocked()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_test_user_prefix_blocked()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_unknown_user_recorded_when_dynamic_tracking_enabled()]] - code - gateway/tests/test_collaborator_tracker.py
- [[tracker()]] - code - gateway/tests/test_collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_140
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 7 edges to [[_COMMUNITY_Module Group 263]]
- 7 edges to [[_COMMUNITY_Module Group 104]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Telegram Proxy Outbound Tests]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 235]]
- 1 edge to [[_COMMUNITY_Module Group 249]]
- 1 edge to [[_COMMUNITY_Module Group 225]]
- 1 edge to [[_COMMUNITY_Module Group 309]]
- 1 edge to [[_COMMUNITY_Module Group 234]]
- 1 edge to [[_COMMUNITY_Module Group 217]]
- 1 edge to [[_COMMUNITY_Module Group 187]]
- 1 edge to [[_COMMUNITY_Telegram Outbound Test Rationale]]
- 1 edge to [[_COMMUNITY_Module Group 287]]
- 1 edge to [[_COMMUNITY_Module Group 446]]
- 1 edge to [[_COMMUNITY_Module Group 339]]
- 1 edge to [[_COMMUNITY_Module Group 472]]
- 1 edge to [[_COMMUNITY_Module Group 338]]

## Top bridge nodes
- [[CollaboratorActivityTracker]] - degree 50, connects to 18 communities
- [[TestTrackerGetHealth]] - degree 8, connects to 2 communities
- [[.record_activity()]] - degree 6, connects to 1 community
- [[test_fixture_uid_writes_blocked()]] - degree 3, connects to 1 community
- [[test_owner_display_name_overrides_pipe()]] - degree 3, connects to 1 community
