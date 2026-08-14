---
source_file: "gateway/tests/test_collaborator_tracker.py"
type: "code"
community: "Bot Skill Config"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# test_collaborator_tracker.py

## Connections
- [[CollaboratorActivityTracker]] - `imports` [EXTRACTED]
- [[WebhookReceiver]] - `imports` [EXTRACTED]
- [[log_file()]] - `contains` [EXTRACTED]
- [[test_collaborator_entry_has_is_owner_false()]] - `contains` [EXTRACTED]
- [[test_correlation_id_absent_when_not_provided()]] - `contains` [EXTRACTED]
- [[test_correlation_id_included_when_provided()]] - `contains` [EXTRACTED]
- [[test_fixture_uid_writes_blocked()]] - `contains` [EXTRACTED]
- [[test_get_activity_filters_by_bot_id()]] - `contains` [EXTRACTED]
- [[test_get_activity_ignores_non_numeric_timestamps()]] - `contains` [EXTRACTED]
- [[test_get_activity_respects_limit()]] - `contains` [EXTRACTED]
- [[test_get_activity_respects_since()]] - `contains` [EXTRACTED]
- [[test_get_activity_returns_empty_when_no_file()]] - `contains` [EXTRACTED]
- [[test_get_activity_returns_entries_newest_first()]] - `contains` [EXTRACTED]
- [[test_get_activity_summary_by_bot_empty_when_no_file()]] - `contains` [EXTRACTED]
- [[test_get_activity_summary_includes_by_bot()]] - `contains` [EXTRACTED]
- [[test_message_preview_newlines_normalized()]] - `contains` [EXTRACTED]
- [[test_message_preview_truncated()]] - `contains` [EXTRACTED]
- [[test_multiple_entries_appended()]] - `contains` [EXTRACTED]
- [[test_owner_correlation_id_is_stored()]] - `contains` [EXTRACTED]
- [[test_owner_display_name_overrides_pipe()]] - `contains` [EXTRACTED]
- [[test_owner_is_recorded_with_is_owner_flag()]] - `contains` [EXTRACTED]
- [[test_pruner_real_telegram_uids_not_flagged()]] - `contains` [EXTRACTED]
- [[test_pruner_short_numeric_ids_are_test_fixtures()]] - `contains` [EXTRACTED]
- [[test_real_uid_writes_unblocked()]] - `contains` [EXTRACTED]
- [[test_record_activity_mirror_handles_delimiter_chars_in_username()]] - `contains` [EXTRACTED]
- [[test_record_activity_mirror_is_single_line_for_multiline_message()]] - `contains` [EXTRACTED]
- [[test_record_activity_mirrors_to_contributor_daily_log()]] - `contains` [EXTRACTED]
- [[test_record_activity_stores_bot_id_none_when_omitted()]] - `contains` [EXTRACTED]
- [[test_record_activity_stores_bot_id_when_provided()]] - `contains` [EXTRACTED]
- [[test_records_known_collaborator()]] - `contains` [EXTRACTED]
- [[test_summary_counts()]] - `contains` [EXTRACTED]
- [[test_summary_empty_when_no_file()]] - `contains` [EXTRACTED]
- [[test_summary_handles_non_numeric_timestamps()]] - `contains` [EXTRACTED]
- [[test_summary_last_activity_is_latest_timestamp()]] - `contains` [EXTRACTED]
- [[test_test_user_prefix_blocked()]] - `contains` [EXTRACTED]
- [[test_unknown_user_is_skipped()]] - `contains` [EXTRACTED]
- [[test_unknown_user_recorded_when_dynamic_tracking_enabled()]] - `contains` [EXTRACTED]
- [[test_username_is_normalized_for_log_safety()]] - `contains` [EXTRACTED]
- [[test_webhook_receiver_passes_agent_id_as_bot_id()]] - `contains` [EXTRACTED]
- [[tracker()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Bot_Skill_Config