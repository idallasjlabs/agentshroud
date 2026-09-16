---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Telegram Lockdown & Collaborator UX Tests"
location: "L9149"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Telegram_Lockdown__Collaborator_UX_Tests
---

# ._make_proxy()

## Connections
- [[dot-test_collab_gets_alert_notice_at_3_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_collab_gets_escalation_notice_at_5_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_collab_gets_suspension_notice_at_10_blocks()]] - `calls` [EXTRACTED]
- [[dot-test_collab_threshold_notices_fire_only_once_per_level()]] - `calls` [EXTRACTED]
- [[dot-test_cooldown_suppresses_second_ack()]] - `calls` [EXTRACTED]
- [[dot-test_dm_hello_does_not_trigger_probe()]] - `calls` [EXTRACTED]
- [[dot-test_filter_disabled_does_not_set_eligibility()]] - `calls` [EXTRACTED]
- [[dot-test_grant_immunity_bypasses_suspension()]] - `calls` [EXTRACTED]
- [[dot-test_group_command_with_bot_suffix_eligible()]] - `calls` [EXTRACTED]
- [[dot-test_group_message_with_mention_forwarded_and_eligible()]] - `calls` [EXTRACTED]
- [[dot-test_group_message_without_mention_forwarded_but_flagged()]] - `calls` [EXTRACTED]
- [[dot-test_hello_in_group_sends_hermes_ack()]] - `calls` [EXTRACTED]
- [[dot-test_hello_in_group_sends_openclaw_ack()]] - `calls` [EXTRACTED]
- [[dot-test_hermes_mention_ignored_when_processed_as_openclaw()]] - `calls` [EXTRACTED]
- [[dot-test_hermes_mention_sets_hermes_eligibility()]] - `calls` [EXTRACTED]
- [[dot-test_immune_command_lists_immune_users()]] - `calls` [EXTRACTED]
- [[dot-test_immune_command_no_immune_users()]] - `calls` [EXTRACTED]
- [[dot-test_immune_user_lockdown_not_incremented()]] - `calls` [EXTRACTED]
- [[dot-test_immune_user_message_passes_through_when_suspended()]] - `calls` [EXTRACTED]
- [[dot-test_locked_no_active_lockdowns()]] - `calls` [EXTRACTED]
- [[dot-test_locked_shows_suspended_users()]] - `calls` [EXTRACTED]
- [[dot-test_no_bot_username_does_not_set_eligibility()]] - `calls` [EXTRACTED]
- [[dot-test_openclaw_mention_does_not_affect_hermes_eligibility()]] - `calls` [EXTRACTED]
- [[dot-test_partial_phrase_does_not_trigger_probe()]] - `calls` [EXTRACTED]
- [[dot-test_predicate_hello_matches()]] - `calls` [EXTRACTED]
- [[dot-test_predicate_hi_matches()]] - `calls` [EXTRACTED]
- [[dot-test_predicate_partial_match_does_not_fire()]] - `calls` [EXTRACTED]
- [[dot-test_predicate_status_matches()]] - `calls` [EXTRACTED]
- [[dot-test_predicate_strips_leading_bot_mention()]] - `calls` [EXTRACTED]
- [[dot-test_predicate_trailing_punctuation_stripped()]] - `calls` [EXTRACTED]
- [[dot-test_predicate_whos_there_matches()]] - `calls` [EXTRACTED]
- [[dot-test_private_message_does_not_set_eligibility_flag()]] - `calls` [EXTRACTED]
- [[dot-test_revoke_immunity_restores_enforcement()]] - `calls` [EXTRACTED]
- [[dot-test_revoke_immunity_unknown_user()]] - `calls` [EXTRACTED]
- [[dot-test_status_in_group_sends_short_ack_not_full_status()]] - `calls` [EXTRACTED]
- [[dot-test_stranger_hello_in_group_receives_ack()]] - `calls` [EXTRACTED]
- [[dot-test_suspended_drop_notice_fires_again_after_cooldown()]] - `calls` [EXTRACTED]
- [[dot-test_suspended_drop_notice_respects_cooldown()]] - `calls` [EXTRACTED]
- [[dot-test_suspended_user_receives_drop_notice()]] - `calls` [EXTRACTED]
- [[dot-test_two_bots_same_group_independent_eligibility()]] - `calls` [EXTRACTED]
- [[dot-test_unlock_calls_reset_on_lockdown()]] - `calls` [EXTRACTED]
- [[dot-test_unlock_clears_manual_pause_without_prior_lockdown_state()]] - `calls` [EXTRACTED]
- [[dot-test_unlock_clears_suspended_drop_cooldown()]] - `calls` [EXTRACTED]
- [[dot-test_unlock_persists_unpause_to_disk()]] - `calls` [EXTRACTED]
- [[dot-test_unlock_unknown_user_returns_no_state_notice()]] - `calls` [EXTRACTED]
- [[dot-test_username_for_bot_falls_back_to_default()]] - `calls` [EXTRACTED]
- [[dot-test_username_for_bot_returns_per_bot_username()]] - `calls` [EXTRACTED]
- [[FakeRBAC]] - `calls` [EXTRACTED]
- [[TelegramAPIProxy]] - `references` [EXTRACTED]
- [[TestGroupPresenceProbe]] - `method` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Telegram_Lockdown__Collaborator_UX_Tests