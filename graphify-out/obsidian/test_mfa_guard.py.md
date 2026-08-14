---
source_file: "gateway/tests/test_mfa_guard.py"
type: "code"
community: "Gateway Test Suite"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# test_mfa_guard.py

## Connections
- [[ApprovalQueue]] - `imports` [EXTRACTED]
- [[ApprovalQueueConfig_2]] - `imports` [EXTRACTED]
- [[ApprovalRequest_3]] - `imports` [EXTRACTED]
- [[ApprovalStore_1]] - `imports` [EXTRACTED]
- [[EnhancedApprovalQueue]] - `imports` [EXTRACTED]
- [[MFAGuard_2]] - `imports` [EXTRACTED]
- [[MFAResult]] - `imports` [EXTRACTED]
- [[ToolRiskConfig_1]] - `imports` [EXTRACTED]
- [[_queue()]] - `contains` [EXTRACTED]
- [[_ref_totp()]] - `contains` [EXTRACTED]
- [[_submit_enhanced_high_risk()]] - `contains` [EXTRACTED]
- [[_submit_high_risk()]] - `contains` [EXTRACTED]
- [[_submit_tool_call()]] - `contains` [EXTRACTED]
- [[enhanced_mfa_queue()]] - `contains` [EXTRACTED]
- [[enhanced_queue.py]] - `references` [EXTRACTED]
- [[mfa_guard.py]] - `references` [EXTRACTED]
- [[now()_1]] - `contains` [EXTRACTED]
- [[queue.py]] - `references` [EXTRACTED]
- [[store.py]] - `references` [EXTRACTED]
- [[test_counter_below_zero_skipped()]] - `contains` [EXTRACTED]
- [[test_custom_high_risk_action_types()]] - `contains` [EXTRACTED]
- [[test_decide_mfa_disabled_approves_without_code()]] - `contains` [EXTRACTED]
- [[test_decide_mfa_enabled_invalid_code_denied()]] - `contains` [EXTRACTED]
- [[test_decide_mfa_enabled_missing_code_denied()]] - `contains` [EXTRACTED]
- [[test_decide_mfa_enabled_replayed_code_denied()]] - `contains` [EXTRACTED]
- [[test_decide_mfa_enabled_valid_code_approves()]] - `contains` [EXTRACTED]
- [[test_decide_reject_never_requires_mfa()]] - `contains` [EXTRACTED]
- [[test_disabled_allows_even_high_risk_with_no_code()]] - `contains` [EXTRACTED]
- [[test_disabled_by_default_allows_without_factor()]] - `contains` [EXTRACTED]
- [[test_empty_code_denies()]] - `contains` [EXTRACTED]
- [[test_enabled_without_secret_denies_fail_closed()]] - `contains` [EXTRACTED]
- [[test_enhanced_decide_missing_code_denied()]] - `contains` [EXTRACTED]
- [[test_enhanced_decide_missing_item_fail_closed()]] - `contains` [EXTRACTED]
- [[test_enhanced_decide_reject_no_mfa()]] - `contains` [EXTRACTED]
- [[test_enhanced_decide_valid_code_approves()]] - `contains` [EXTRACTED]
- [[test_enhanced_tool_call_critical_allowed_with_mfa()]] - `contains` [EXTRACTED]
- [[test_enhanced_tool_call_critical_blocked_without_mfa()]] - `contains` [EXTRACTED]
- [[test_enhanced_tool_call_high_allowed_with_mfa()]] - `contains` [EXTRACTED]
- [[test_enhanced_tool_call_high_blocked_without_mfa()]] - `contains` [EXTRACTED]
- [[test_enhanced_tool_call_medium_not_gated()]] - `contains` [EXTRACTED]
- [[test_expired_window_code_denies()]] - `contains` [EXTRACTED]
- [[test_from_env_bad_window_defaults_to_one()]] - `contains` [EXTRACTED]
- [[test_from_env_disabled_when_flag_unset()]] - `contains` [EXTRACTED]
- [[test_from_env_enabled_no_secret_warns()]] - `contains` [EXTRACTED]
- [[test_from_env_reads_secret_and_flag()]] - `contains` [EXTRACTED]
- [[test_from_env_reads_secret_file()]] - `contains` [EXTRACTED]
- [[test_from_env_unreadable_secret_file()]] - `contains` [EXTRACTED]
- [[test_invalid_base32_secret_treated_as_unconfigured()]] - `contains` [EXTRACTED]
- [[test_invalid_code_denies()]] - `contains` [EXTRACTED]
- [[test_is_required_tool_call_disabled_never_required()]] - `contains` [EXTRACTED]
- [[test_is_required_tool_call_tier_parsing()]] - `contains` [EXTRACTED]
- [[test_missing_code_denies_high_risk()]] - `contains` [EXTRACTED]
- [[test_non_high_risk_action_not_required()]] - `contains` [EXTRACTED]
- [[test_prune_used_drops_stale_entries()]] - `contains` [EXTRACTED]
- [[test_real_time_default_now()]] - `contains` [EXTRACTED]
- [[test_replayed_code_denies()]] - `contains` [EXTRACTED]
- [[test_uses_constant_time_compare()]] - `contains` [EXTRACTED]
- [[test_valid_totp_allows_high_risk()]] - `contains` [EXTRACTED]
- [[test_valid_totp_prev_window_allowed()]] - `contains` [EXTRACTED]
- [[test_wrong_length_code_denies()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite