---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Module Group 69"
location: "L7903"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Module_Group_69
---

# TestProgressiveLockdownUX

## Connections
- [[._make_proxy()]] - `method` [EXTRACTED]
- [[.test_collab_gets_alert_notice_at_3_blocks()]] - `method` [EXTRACTED]
- [[.test_collab_gets_escalation_notice_at_5_blocks()]] - `method` [EXTRACTED]
- [[.test_collab_gets_suspension_notice_at_10_blocks()]] - `method` [EXTRACTED]
- [[.test_collab_threshold_notices_fire_only_once_per_level()]] - `method` [EXTRACTED]
- [[.test_grant_immunity_bypasses_suspension()]] - `method` [EXTRACTED]
- [[.test_immune_command_lists_immune_users()]] - `method` [EXTRACTED]
- [[.test_immune_command_no_immune_users()]] - `method` [EXTRACTED]
- [[.test_immune_user_lockdown_not_incremented()]] - `method` [EXTRACTED]
- [[.test_immune_user_message_passes_through_when_suspended()]] - `method` [EXTRACTED]
- [[.test_locked_no_active_lockdowns()_1]] - `method` [EXTRACTED]
- [[.test_locked_shows_suspended_users()]] - `method` [EXTRACTED]
- [[.test_revoke_immunity_restores_enforcement()]] - `method` [EXTRACTED]
- [[.test_revoke_immunity_unknown_user()]] - `method` [EXTRACTED]
- [[.test_suspended_drop_notice_fires_again_after_cooldown()]] - `method` [EXTRACTED]
- [[.test_suspended_drop_notice_respects_cooldown()_1]] - `method` [EXTRACTED]
- [[.test_suspended_user_receives_drop_notice()]] - `method` [EXTRACTED]
- [[.test_unlock_calls_reset_on_lockdown()]] - `method` [EXTRACTED]
- [[.test_unlock_clears_suspended_drop_cooldown()_1]] - `method` [EXTRACTED]
- [[.test_unlock_unknown_user_returns_no_state_notice()]] - `method` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[Tests for lockdown UX unlock fix, collaborator notifications, locked, immunit]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Module_Group_69