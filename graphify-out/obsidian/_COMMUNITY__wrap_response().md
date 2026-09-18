---
type: community
cohesion: 0.04
members: 104
---

# _wrap_response()

**Cohesion:** 0.04 - loosely connected
**Members:** 104 nodes

## Members
- [[._make_proxy()_4]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collab_gets_alert_notice_at_3_blocks()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collab_gets_escalation_notice_at_5_blocks()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collab_gets_suspension_notice_at_10_blocks()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collab_threshold_notices_fire_only_once_per_level()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_cooldown_suppresses_second_ack()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_dm_hello_does_not_trigger_probe()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_filter_disabled_does_not_set_eligibility()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_grant_immunity_bypasses_suspension()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_group_command_with_bot_suffix_eligible()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_group_message_with_mention_forwarded_and_eligible()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_group_message_without_mention_forwarded_but_flagged()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_hello_in_group_sends_hermes_ack()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_hello_in_group_sends_openclaw_ack()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_hermes_mention_ignored_when_processed_as_openclaw()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_hermes_mention_sets_hermes_eligibility()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_immune_command_lists_immune_users()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_immune_command_no_immune_users()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_immune_user_lockdown_not_incremented()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_immune_user_message_passes_through_when_suspended()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_locked_no_active_lockdowns()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_locked_shows_suspended_users()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_no_bot_username_does_not_set_eligibility()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_openclaw_mention_does_not_affect_hermes_eligibility()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_partial_phrase_does_not_trigger_probe()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_predicate_hello_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_predicate_hi_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_predicate_partial_match_does_not_fire()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_predicate_status_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_predicate_strips_leading_bot_mention()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_predicate_trailing_punctuation_stripped()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_predicate_whos_there_matches()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_private_message_does_not_set_eligibility_flag()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_revoke_immunity_restores_enforcement()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_revoke_immunity_unknown_user()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_status_in_group_sends_short_ack_not_full_status()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_stranger_hello_in_group_receives_ack()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_suspended_drop_notice_fires_again_after_cooldown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_suspended_drop_notice_respects_cooldown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_suspended_user_receives_drop_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_two_bots_same_group_independent_eligibility()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unlock_calls_reset_on_lockdown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unlock_clears_manual_pause_without_prior_lockdown_state()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unlock_clears_suspended_drop_cooldown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unlock_persists_unpause_to_disk()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unlock_unknown_user_returns_no_state_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_username_for_bot_falls_back_to_default()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_username_for_bot_returns_per_bot_username()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[command@botname marks chat as response-eligible.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[gi uid must grant immunity so the user bypasses lockdown suspension check.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[immune must list all immune user IDs.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[immune with no immune users must say so.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[locked must list users with non-normal lockdown state.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[locked with no active lockdowns must say so.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[ri uid must remove immunity and confirm to owner.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[status in a group sends only the short liveness ack (no operational details).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[unlock uid must call reset() on the lockdown module and confirm to owner.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[unlock for a user with no lockdown state must say so.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[unlock must clear the suspended-drop notice cooldown so user gets fresh notice]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[unlock must persist through unpause_collaborator() so resume survives         a]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[@agentshroud_bot mention sets only openclaw eligible; hermes entry is absent.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[@agentshroud_hermes_bot hello' normalises to 'hello' → matches.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[@agentshroud_hermes_bot mention sets hermes eligibility, not openclaw.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[@agentshroud_hermes_bot message processed as openclaw yields ineligible for open]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[A dropped message past the cooldown window must produce a new notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[A stranger (not owner, not collaborator) typing 'hello' in a group still gets th]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[A user manually revoke'd (paused) with no ProgressiveLockdown block         his]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Build a Telegram group message update.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator must receive escalation notice at block 5.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator must receive suspension notice at block 10.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator must receive warning text when they reach 3 security blocks.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[DMs don't interact with the group eligibility map.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Group messages with @mention are forwarded and mark chat as response-eligible.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Group messages without @mention are forwarded (for context) but mark chat as res]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Group presence probe bare trigger phrases make each bot reply with a short live]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Immune user must not be dropped by the suspension path (stub must not appear).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Integration tests for group at-mention filtering.      The bot reads ALL group m]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Per-bot eligibility — each bot in a shared group tracks mention state independen]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Second 'hello' within the cooldown window must NOT send a second ack.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Second dropped message within cooldown window must NOT produce another notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Stub the fire-and-forget owner activity mirror.      The mirror runs via asyncio]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Suspended user's dropped message must trigger a 'session suspended' notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestGroupMentionFilter]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestGroupPresenceProbe]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestPerBotGroupMentionFilter]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestProgressiveLockdownUX]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Tests for lockdown UX unlock fix, collaborator notifications, locked, immunit]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[The probe is group-only; 'hello' in a DM chat must not fire the ack.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Threshold notices must not repeat on subsequent blocks at the same level.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Two bots in the same group track eligibility independently.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknown bot_id falls back to _bot_username.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[When bot_username is unset the filter is bypassed entirely.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[When group_mention_only is disabled, eligibility map is not populated.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_make_group_update()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_no_owner_mirror()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_quarantine_blocked_message must NOT increment lockdown count for immune users.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_username_for_bot returns the correct @username for each bot_id.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_wrap_response()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[hello!' and 'hello' should both match.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[hello' (bare) in a group triggers '✅ @agentshroud_bot online' from openclaw.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[hello' in a group triggers '✅ @agentshroud_hermes_bot online' when processed as]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[hello, can you help' must NOT match — exact-match guard.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[hello, can you help' must reach the LLM path, not be swallowed by the probe.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[test_telegram_proxy_inbound.py]] - code - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_wrap_response
SORT file.name ASC
```

## Connections to other communities
- 174 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 11 edges to [[_COMMUNITY_RateLimiter]]
- 8 edges to [[_COMMUNITY_BlockingPipeline]]
- 7 edges to [[_COMMUNITY_TestNoResponseGuarantee]]
- 5 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 4 edges to [[_COMMUNITY_.test_collaborator_allowlist_bypass_request_is_b]]
- 4 edges to [[_COMMUNITY_AsyncMock]]
- 4 edges to [[_COMMUNITY_TestFileDownload]]
- 4 edges to [[_COMMUNITY_TestFullAccessMiddlewareBypass]]
- 4 edges to [[_COMMUNITY_TestStrangerRateLimit]]
- 3 edges to [[_COMMUNITY_.test_collaborator_cross_user_messaging_request_]]
- 2 edges to [[_COMMUNITY_.test_owner_deny_without_target_auto_selects_sin]]
- 2 edges to [[_COMMUNITY_.test_blocked_command_with_zero_width_mention_an]]
- 2 edges to [[_COMMUNITY_.test_allowed_collaborator_model_command_with_me]]
- 2 edges to [[_COMMUNITY_.test_collaborator_web_access_request_queues_own]]
- 2 edges to [[_COMMUNITY_.test_collaborator_sensitive_path_probe_shell_st]]
- 2 edges to [[_COMMUNITY_.test_collaborator_metadata_endpoint_probe_is_bl]]
- 2 edges to [[_COMMUNITY_.test_collaborator_incremental_exfil_request_is_]]
- 2 edges to [[_COMMUNITY_.test_collaborator_plugin_discovery_request_is_b]]
- 2 edges to [[_COMMUNITY_.test_collaborator_hidden_channel_exfil_request_]]
- 2 edges to [[_COMMUNITY_.test_collaborator_service_control_request_is_bl]]
- 2 edges to [[_COMMUNITY_.test_collaborator_approval_action_request_is_bl]]
- 2 edges to [[_COMMUNITY_.test_owner_revoke_command_requires_target_user_]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_TestBotIsMentioned]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]

## Top bridge nodes
- [[_wrap_response()]] - degree 233, connects to 21 communities
- [[test_telegram_proxy_inbound.py]] - degree 28, connects to 13 communities
- [[TestProgressiveLockdownUX]] - degree 28, connects to 4 communities
- [[TestGroupMentionFilter]] - degree 12, connects to 4 communities
- [[TestPerBotGroupMentionFilter]] - degree 12, connects to 4 communities