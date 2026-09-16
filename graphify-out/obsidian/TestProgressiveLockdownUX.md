---
source_file: "gateway/tests/test_telegram_proxy_inbound.py"
type: "code"
community: "Telegram Lockdown & Collaborator UX Tests"
location: "L8003"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Telegram_Lockdown__Collaborator_UX_Tests
---

# TestProgressiveLockdownUX

## Connections
- [[dot-_make_proxy()_3]] - `method` [EXTRACTED]
- [[dot-test_collab_gets_alert_notice_at_3_blocks()]] - `method` [EXTRACTED]
- [[dot-test_collab_gets_escalation_notice_at_5_blocks()]] - `method` [EXTRACTED]
- [[dot-test_collab_gets_suspension_notice_at_10_blocks()]] - `method` [EXTRACTED]
- [[dot-test_collab_threshold_notices_fire_only_once_per_level()]] - `method` [EXTRACTED]
- [[dot-test_grant_immunity_bypasses_suspension()]] - `method` [EXTRACTED]
- [[dot-test_immune_command_lists_immune_users()]] - `method` [EXTRACTED]
- [[dot-test_immune_command_no_immune_users()]] - `method` [EXTRACTED]
- [[dot-test_immune_user_lockdown_not_incremented()]] - `method` [EXTRACTED]
- [[dot-test_immune_user_message_passes_through_when_suspended()]] - `method` [EXTRACTED]
- [[dot-test_locked_no_active_lockdowns()]] - `method` [EXTRACTED]
- [[dot-test_locked_shows_suspended_users()]] - `method` [EXTRACTED]
- [[dot-test_proxy_seeds_runtime_revoked_from_persisted_paused_set()]] - `method` [EXTRACTED]
- [[dot-test_revoke_immunity_restores_enforcement()]] - `method` [EXTRACTED]
- [[dot-test_revoke_immunity_unknown_user()]] - `method` [EXTRACTED]
- [[dot-test_suspended_drop_notice_fires_again_after_cooldown()]] - `method` [EXTRACTED]
- [[dot-test_suspended_drop_notice_respects_cooldown()]] - `method` [EXTRACTED]
- [[dot-test_suspended_user_receives_drop_notice()]] - `method` [EXTRACTED]
- [[dot-test_unlock_calls_reset_on_lockdown()]] - `method` [EXTRACTED]
- [[dot-test_unlock_clears_manual_pause_without_prior_lockdown_state()]] - `method` [EXTRACTED]
- [[dot-test_unlock_clears_suspended_drop_cooldown()]] - `method` [EXTRACTED]
- [[dot-test_unlock_persists_unpause_to_disk()]] - `method` [EXTRACTED]
- [[dot-test_unlock_unknown_user_returns_no_state_notice()]] - `method` [EXTRACTED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RateLimiter]] - `uses` [INFERRED]
- [[TelegramAPIProxy_2]] - `uses` [INFERRED]
- [[Tests for lockdown UX unlock fix, collaborator notifications, locked, immunit]] - `rationale_for` [EXTRACTED]
- [[test_telegram_proxy_inbound.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Telegram_Lockdown__Collaborator_UX_Tests