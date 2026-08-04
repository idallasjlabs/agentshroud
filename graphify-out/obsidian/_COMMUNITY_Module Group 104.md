---
type: community
cohesion: 0.05
members: 42
---

# Module Group 104

**Cohesion:** 0.05 - loosely connected
**Members:** 42 nodes

## Members
- [[IDs  10000 should be treated as test fixtures by the pruner heuristic.]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Owner messages are now recorded with is_owner=True (not silently dropped).]] - rationale - gateway/tests/test_collaborator_tracker.py
- [[Real Telegram UIDs (9-10 digits) must NOT be pruned.]] - rationale - gateway/tests/test_collaborator_tracker.py
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
- [[test_owner_is_recorded_with_is_owner_flag()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_pruner_real_telegram_uids_not_flagged()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_pruner_short_numeric_ids_are_test_fixtures()]] - code - gateway/tests/test_collaborator_tracker.py
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
- [[test_unknown_user_is_skipped()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_username_is_normalized_for_log_safety()]] - code - gateway/tests/test_collaborator_tracker.py
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - code - gateway/tests/test_collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_104
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Module Group 140]]
- 2 edges to [[_COMMUNITY_Webhook Receiver]]

## Top bridge nodes
- [[test_collaborator_tracker.py]] - degree 40, connects to 2 communities
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - degree 3, connects to 1 community
