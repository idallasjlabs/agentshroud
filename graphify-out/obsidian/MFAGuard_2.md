---
source_file: "gateway/security/mfa_guard.py"
type: "code"
community: "Enforce-Mode Auto-Revert"
location: "L99"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Enforce-Mode_Auto-Revert
---

# MFAGuard

## Connections
- [[.__init__()_95]] - `method` [EXTRACTED]
- [[._decode_secret()]] - `method` [EXTRACTED]
- [[._prune_used()]] - `method` [EXTRACTED]
- [[._totp_for_counter()]] - `method` [EXTRACTED]
- [[.from_env()_3]] - `method` [EXTRACTED]
- [[.is_required()]] - `method` [EXTRACTED]
- [[.verify()_1]] - `method` [EXTRACTED]
- [[Any]] - `uses` [INFERRED]
- [[ApprovalQueue_1]] - `uses` [INFERRED]
- [[ApprovalQueueConfig]] - `uses` [INFERRED]
- [[ApprovalQueueItem]] - `uses` [INFERRED]
- [[ApprovalRequest]] - `uses` [INFERRED]
- [[ApprovalStore]] - `uses` [INFERRED]
- [[Daily CVE Triage & Remediation Scan (OpenClaw cron job)]] - `conceptually_related_to` [AMBIGUOUS]
- [[EnhancedApprovalQueue]] - `uses` [INFERRED]
- [[EnhancedApprovalQueue_2]] - `uses` [INFERRED]
- [[MFA for High-Risk Approvals — IEC 62443 FR1 (SCRUM-93)]] - `references` [EXTRACTED]
- [[MFAGuard]] - `uses` [INFERRED]
- [[OAuthSecurityValidator]] - `semantically_similar_to` [INFERRED]
- [[ToolRiskConfig]] - `uses` [INFERRED]
- [[ToolRiskPolicy]] - `uses` [INFERRED]
- [[Verify a TOTP second factor for high-risk operations (fail-closed).      Args]] - `rationale_for` [EXTRACTED]
- [[WebSocket]] - `uses` [INFERRED]
- [[_queue()]] - `calls` [EXTRACTED]
- [[enhanced_mfa_queue()]] - `calls` [EXTRACTED]
- [[enhanced_queue.py]] - `imports` [EXTRACTED]
- [[mfa_guard.py]] - `contains` [EXTRACTED]
- [[queue.py]] - `imports` [EXTRACTED]
- [[test_counter_below_zero_skipped()]] - `calls` [EXTRACTED]
- [[test_custom_high_risk_action_types()]] - `calls` [EXTRACTED]
- [[test_disabled_allows_even_high_risk_with_no_code()]] - `calls` [EXTRACTED]
- [[test_disabled_by_default_allows_without_factor()]] - `calls` [EXTRACTED]
- [[test_empty_code_denies()]] - `calls` [EXTRACTED]
- [[test_enabled_without_secret_denies_fail_closed()]] - `calls` [EXTRACTED]
- [[test_expired_window_code_denies()]] - `calls` [EXTRACTED]
- [[test_invalid_base32_secret_treated_as_unconfigured()]] - `calls` [EXTRACTED]
- [[test_invalid_code_denies()]] - `calls` [EXTRACTED]
- [[test_is_required_tool_call_disabled_never_required()]] - `calls` [EXTRACTED]
- [[test_is_required_tool_call_tier_parsing()]] - `calls` [EXTRACTED]
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

#graphify/code #graphify/EXTRACTED #community/Enforce-Mode_Auto-Revert