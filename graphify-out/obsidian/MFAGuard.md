---
source_file: "gateway/security/mfa_guard.py"
type: "code"
community: "test_mfa_guard.py"
location: "L99"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_mfa_guardpy
---

# MFAGuard

## Connections
- [[dot-__init__()_117]] - `references` [EXTRACTED]
- [[dot-__init__()_97]] - `references` [EXTRACTED]
- [[dot-__init__()_3]] - `method` [EXTRACTED]
- [[dot-_decode_secret()]] - `method` [EXTRACTED]
- [[dot-_prune_used()]] - `method` [EXTRACTED]
- [[dot-_totp_for_counter()]] - `method` [EXTRACTED]
- [[dot-from_env()]] - `method` [EXTRACTED]
- [[dot-is_required()]] - `method` [EXTRACTED]
- [[dot-verify()]] - `method` [EXTRACTED]
- [[ApprovalQueue]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[Verify a TOTP second factor for high-risk operations (fail-closed). Args…]] - `rationale_for` [EXTRACTED]
- [[_queue()]] - `calls` [EXTRACTED]
- [[edge()]] - `uses` [INFERRED]
- [[enhanced_mfa_queue()]] - `uses` [INFERRED]
- [[enhanced_queue.py]] - `imports` [EXTRACTED]
- [[env()]] - `uses` [INFERRED]
- [[mfa_guard.py]] - `contains` [EXTRACTED]
- [[queue.py]] - `imports` [EXTRACTED]
- [[stack()]] - `uses` [INFERRED]
- [[test_counter_below_zero_skipped()]] - `calls` [EXTRACTED]
- [[test_custom_high_risk_action_types()]] - `calls` [EXTRACTED]
- [[test_disabled_allows_even_high_risk_with_no_code()]] - `calls` [EXTRACTED]
- [[test_disabled_by_default_allows_without_factor()]] - `calls` [EXTRACTED]
- [[test_edge_approvals.py]] - `imports` [EXTRACTED]
- [[test_edge_e2e_sdk.py]] - `imports` [EXTRACTED]
- [[test_edge_pipeline.py]] - `imports` [EXTRACTED]
- [[test_empty_code_denies()]] - `calls` [EXTRACTED]
- [[test_enabled_without_secret_denies_fail_closed()]] - `calls` [EXTRACTED]
- [[test_expired_window_code_denies()]] - `calls` [EXTRACTED]
- [[test_from_env_bad_window_defaults_to_one()]] - `uses` [INFERRED]
- [[test_from_env_disabled_when_flag_unset()]] - `uses` [INFERRED]
- [[test_from_env_enabled_no_secret_warns()]] - `uses` [INFERRED]
- [[test_from_env_reads_secret_and_flag()]] - `uses` [INFERRED]
- [[test_from_env_reads_secret_file()]] - `uses` [INFERRED]
- [[test_from_env_unreadable_secret_file()]] - `uses` [INFERRED]
- [[test_invalid_base32_secret_treated_as_unconfigured()]] - `calls` [EXTRACTED]
- [[test_invalid_code_denies()]] - `calls` [EXTRACTED]
- [[test_is_required_tool_call_disabled_never_required()]] - `calls` [EXTRACTED]
- [[test_is_required_tool_call_tier_parsing()]] - `uses` [INFERRED]
- [[test_mfa_guard.py]] - `imports` [EXTRACTED]
- [[test_missing_code_denies_high_risk()]] - `calls` [EXTRACTED]
- [[test_non_high_risk_action_not_required()]] - `calls` [EXTRACTED]
- [[test_prune_used_drops_stale_entries()]] - `calls` [EXTRACTED]
- [[test_real_time_default_now()]] - `calls` [EXTRACTED]
- [[test_replayed_code_denies()]] - `calls` [EXTRACTED]
- [[test_uses_constant_time_compare()]] - `calls` [EXTRACTED]
- [[test_valid_totp_allows_high_risk()]] - `calls` [EXTRACTED]
- [[test_valid_totp_prev_window_allowed()]] - `calls` [EXTRACTED]
- [[test_wrong_length_code_denies()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_mfa_guardpy
