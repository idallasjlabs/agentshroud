---
type: community
cohesion: 0.05
members: 56
---

# Module Group 69

**Cohesion:** 0.05 - loosely connected
**Members:** 56 nodes

## Members
- [[._make_proxy()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[._make_proxy()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collab_gets_alert_notice_at_3_blocks()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collab_gets_escalation_notice_at_5_blocks()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collab_gets_suspension_notice_at_10_blocks()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_collab_threshold_notices_fire_only_once_per_level()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_grant_immunity_bypasses_suspension()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_group_command_with_bot_suffix_eligible()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_group_message_with_mention_forwarded_and_eligible()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_group_message_without_mention_forwarded_but_flagged()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_immune_command_lists_immune_users()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_immune_command_no_immune_users()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_immune_user_lockdown_not_incremented()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_immune_user_message_passes_through_when_suspended()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_locked_no_active_lockdowns()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_locked_shows_suspended_users()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_no_bot_username_does_not_set_eligibility()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_private_message_does_not_set_eligibility_flag()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_revoke_immunity_restores_enforcement()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_revoke_immunity_unknown_user()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_suspended_drop_notice_fires_again_after_cooldown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_suspended_drop_notice_respects_cooldown()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_suspended_user_receives_drop_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unlock_calls_reset_on_lockdown()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unlock_clears_suspended_drop_cooldown()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_unlock_unknown_user_returns_no_state_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[command@botname marks chat as response-eligible.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[gi uid must grant immunity so the user bypasses lockdown suspension check.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[immune must list all immune user IDs.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[immune with no immune users must say so.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[locked must list users with non-normal lockdown state.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[locked with no active lockdowns must say so.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[ri uid must remove immunity and confirm to owner.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[ri for a user not in immune set must say so.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[unlock uid must call reset() on the lockdown module and confirm to owner.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[unlock for a user with no lockdown state must say so.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[unlock must clear the suspended-drop notice cooldown so user gets fresh notice]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[A dropped message past the cooldown window must produce a new notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Build a Telegram group message update.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator must receive escalation notice at block 5.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator must receive suspension notice at block 10.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator must receive warning text when they reach 3 security blocks.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[DMs don't interact with the group eligibility map.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Group messages with @mention are forwarded and mark chat as response-eligible.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Group messages without @mention are forwarded (for context) but mark chat as res]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Immune user must not be dropped by the suspension path (stub must not appear).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Integration tests for group at-mention filtering.      The bot reads ALL group m]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Second dropped message within cooldown window must NOT produce another notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Suspended user's dropped message must trigger a 'session suspended' notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestGroupMentionFilter]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestProgressiveLockdownUX]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Tests for lockdown UX unlock fix, collaborator notifications, locked, immunit]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Threshold notices must not repeat on subsequent blocks at the same level.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[When bot_username is unset the filter is bypassed entirely.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_make_group_update()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_quarantine_blocked_message must NOT increment lockdown count for immune users.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_69
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Module Group 64]]
- 20 edges to [[_COMMUNITY_Telegram Proxy Inbound Tests]]
- 5 edges to [[_COMMUNITY_Authentication & Rate Limiting]]
- 3 edges to [[_COMMUNITY_Module Group 74]]
- 2 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 2 edges to [[_COMMUNITY_Telegram Proxy Core]]

## Top bridge nodes
- [[TestGroupMentionFilter]] - degree 12, connects to 4 communities
- [[TestProgressiveLockdownUX]] - degree 25, connects to 3 communities
- [[.test_suspended_drop_notice_fires_again_after_cooldown()]] - degree 6, connects to 3 communities
- [[.test_suspended_drop_notice_respects_cooldown()_1]] - degree 6, connects to 3 communities
- [[.test_suspended_user_receives_drop_notice()]] - degree 6, connects to 3 communities
