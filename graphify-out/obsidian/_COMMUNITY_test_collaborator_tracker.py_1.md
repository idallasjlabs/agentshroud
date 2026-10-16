---
type: community
cohesion: 0.04
members: 50
---

# test_collaborator_tracker.py

**Cohesion:** 0.04 - loosely connected
**Members:** 50 nodes

## Members
- [[10-digit real UID must still be written to JSONL and markdown.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[IDs  10000 should be treated as test fixtures by the pruner heuristic.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Owner messages are now recorded with is_owner=True (not silently dropped).]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Owner's Telegram first_name with pipe chars is replaced by owner_display_name.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Real Telegram UIDs (9-10 digits) must NOT be pruned.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Short numeric UIDs ( 7 digits) must be silently dropped before any write.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[UIDs matching test_user prefix must be silently dropped.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[get_activity(bot_id=...) returns only entries matching that bot_id.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[get_activity_summary returns a by_bot breakdown keyed by bot_id.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[get_activity_summary returns empty by_bot when no log file exists.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[log_file()]] - code - gateway/tests/test_collaborator_tracker.py
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
- [[test_message_preview_newlines_normalized()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_message_preview_truncated()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_multiple_entries_appended()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_owner_correlation_id_is_stored()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_owner_display_name_overrides_pipe()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_owner_is_recorded_with_is_owner_flag()]] - code - gateway/tests/test_collaborator_tracker.py
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
- [[tracker()]] - code - gateway/tests/test_collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_collaborator_trackerpy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_test_dashboard_endpoints.py]]

## Top bridge nodes
- [[test_collaborator_tracker.py]] - degree 40, connects to 2 communities
- [[test_fixture_uid_writes_blocked()]] - degree 3, connects to 1 community
- [[test_owner_display_name_overrides_pipe()]] - degree 3, connects to 1 community
- [[test_real_uid_writes_unblocked()]] - degree 3, connects to 1 community
- [[test_test_user_prefix_blocked()]] - degree 3, connects to 1 community
