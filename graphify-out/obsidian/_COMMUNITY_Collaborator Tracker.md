---
type: community
cohesion: 0.03
members: 94
---

# Collaborator Tracker

**Cohesion:** 0.03 - loosely connected
**Members:** 94 nodes

## Members
- [[.__init__()_62]] - code - gateway/security/collaborator_tracker.py
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
- [[Collaborator Tracker Tests]] - code - gateway/tests/test_collaborator_tracker.py
- [[CollaboratorActivityTracker_1]] - code - gateway/tests/test_lifespan_prune.py
- [[CollaboratorActivityTracker]] - code - gateway/security/collaborator_tracker.py
- [[CollaboratorActivityTracker.get_health() must return accurate counters.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a fake contributor markdown file for the given uid.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[IDs  10000 should be treated as test fixtures by the pruner heuristic.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Mirror activity into workspace contributor logs used by daily digests.]] - rationale - gateway/security/collaborator_tracker.py
- [[Normalize previews to single-line safe text for JSONL + markdown mirrors.]] - rationale - gateway/security/collaborator_tracker.py
- [[Normalize username for safe contributor-log tokenization.]] - rationale - gateway/security/collaborator_tracker.py
- [[Owner messages are now recorded with is_owner=True (not silently dropped).]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Owner's Telegram first_name with pipe chars is replaced by owner_display_name.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Path_9]] - code - gateway/security/collaborator_tracker.py
- [[Path_31]] - code - gateway/tests/test_lifespan_prune.py
- [[Real Telegram UIDs (9-10 digits) must NOT be pruned.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Real-UID markdown files must never be deleted by the prune pass.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Return True when uid looks like a test fixture that should be silently dropped.]] - rationale - gateway/security/collaborator_tracker.py
- [[Return a health snapshot suitable for statusdetail.]] - rationale - gateway/security/collaborator_tracker.py
- [[Return activity entries sorted newest-first.          Args             since U]] - rationale - gateway/security/collaborator_tracker.py
- [[Return aggregated statistics over all recorded activity.          Returns]] - rationale - gateway/security/collaborator_tracker.py
- [[Run the same markdown-prune logic as lifespan.py and return pruned count.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Short numeric UIDs ( 7 digits) must be silently dropped before any write.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Startup prune must remove fixture markdown files from every contributor dir.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[TestTrackerGetHealth]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tracks collaborator messages at the gateway level.      Records every inbound me]] - rationale - gateway/security/collaborator_tracker.py
- [[UIDs matching test_user prefix must be silently dropped.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[_is_fixture_uid()]] - code - gateway/security/collaborator_tracker.py
- [[_make_md()]] - code - gateway/tests/test_lifespan_prune.py
- [[_prune_fixture_markdown()]] - code - gateway/tests/test_lifespan_prune.py
- [[collaborator_tracker.py]] - code - gateway/security/collaborator_tracker.py
- [[get_activity(bot_id=...) returns only entries matching that bot_id.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[get_activity_summary returns a by_bot breakdown keyed by bot_id.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[get_activity_summary returns empty by_bot when no log file exists.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[log_file()]] - code - gateway/tests/test_collaborator_tracker.py
- [[process_webhook passes agent_id as bot_id to record_activity.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[record_activity with bot_id='hermes' stores bot_id in the entry.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[record_activity without bot_id stores bot_id=None in the entry.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[test_collaborator_entry_has_is_owner_false()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_collaborator_tracker.py]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_correlation_id_absent_when_not_provided()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_correlation_id_included_when_provided()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_fixture_uid_writes_blocked()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_get_activity_filters_by_bot_id()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_get_activity_ignores_non_numeric_timestamps()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_get_activity_respects_limit()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_get_activity_respects_since()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_get_activity_returns_empty_when_no_file()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_get_activity_returns_entries_newest_first()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_get_activity_summary_by_bot_empty_when_no_file()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_get_activity_summary_includes_by_bot()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_is_fixture_uid_blocks_short_numeric()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_is_fixture_uid_blocks_test_user_prefix()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_is_fixture_uid_passes_real_uids()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_lifespan_prune.py]] - code - gateway/tests/test_lifespan_prune.py
- [[test_message_preview_newlines_normalized()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_message_preview_truncated()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_multiple_entries_appended()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_owner_correlation_id_is_stored()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_owner_display_name_overrides_pipe()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_owner_is_recorded_with_is_owner_flag()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_prune_keeps_real_uid_markdown()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_prune_walks_all_contributor_dirs()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_pruner_real_telegram_uids_not_flagged()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_pruner_short_numeric_ids_are_test_fixtures()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_real_uid_writes_unblocked()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_record_activity_mirror_handles_delimiter_chars_in_username()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_record_activity_mirror_is_single_line_for_multiline_message()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_record_activity_mirrors_to_contributor_daily_log()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_record_activity_stores_bot_id_none_when_omitted()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_record_activity_stores_bot_id_when_provided()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_records_known_collaborator()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_summary_counts()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_summary_empty_when_no_file()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_summary_handles_non_numeric_timestamps()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_summary_last_activity_is_latest_timestamp()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_test_user_prefix_blocked()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_unknown_user_is_skipped()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_unknown_user_recorded_when_dynamic_tracking_enabled()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_username_is_normalized_for_log_safety()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - code - gateway/tests/test_collaborator_tracker.py
- [[tracker()]] - code - gateway/tests/test_collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Collaborator_Tracker
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 9 edges to [[_COMMUNITY_Telegram Proxy Outbound]]
- 3 edges to [[_COMMUNITY_Middleware & Session Isolation]]
- 3 edges to [[_COMMUNITY_Telegram Outbound Proxy Tests]]
- 2 edges to [[_COMMUNITY_Telegram Proxy Outbound]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Outbound]]

## Top bridge nodes
- [[CollaboratorActivityTracker]] - degree 52, connects to 12 communities
- [[TestTrackerGetHealth]] - degree 8, connects to 3 communities
- [[test_collaborator_tracker.py]] - degree 40, connects to 1 community
- [[test_lifespan_prune.py]] - degree 10, connects to 1 community
- [[_is_fixture_uid()]] - degree 9, connects to 1 community