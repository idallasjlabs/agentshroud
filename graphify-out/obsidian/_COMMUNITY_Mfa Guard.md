---
type: community
cohesion: 0.06
members: 70
---

# Mfa Guard

**Cohesion:** 0.06 - loosely connected
**Members:** 70 nodes

## Members
- [[.__init__()_98]] - code - gateway/security/mfa_guard.py
- [[._decode_secret()]] - code - gateway/security/mfa_guard.py
- [[._prune_used()]] - code - gateway/security/mfa_guard.py
- [[._totp_for_counter()]] - code - gateway/security/mfa_guard.py
- [[.from_env()_3]] - code - gateway/security/mfa_guard.py
- [[.is_required()]] - code - gateway/security/mfa_guard.py
- [[.verify()_1]] - code - gateway/security/mfa_guard.py
- [[ApprovalQueue_1]] - code - gateway/tests/test_mfa_guard.py
- [[Build an MFAGuard from environment variables  Docker secret file.          Reco]] - rationale - gateway/security/mfa_guard.py
- [[Compute the RFC 6238 TOTP value for a specific time-step counter.]] - rationale - gateway/security/mfa_guard.py
- [[Decode a base32 secret; return b on emptyinvalid input.]] - rationale - gateway/security/mfa_guard.py
- [[Drop replay records older than the accepted window (bounded memory).]] - rationale - gateway/security/mfa_guard.py
- [[EnhancedApprovalQueue_2]] - code - gateway/tests/test_mfa_guard.py
- [[MFAGuard_2]] - code - gateway/security/mfa_guard.py
- [[MFAResult]] - code - gateway/security/mfa_guard.py
- [[Outcome of an MFA verification.      Attributes         allowed True if the ac]] - rationale - gateway/security/mfa_guard.py
- [[Return True if ``action_type`` requires a second factor right now.          Two]] - rationale - gateway/security/mfa_guard.py
- [[Submit via the real tool-call path - action_type == f'tool_call_{tier}'.]] - rationale - gateway/tests/test_mfa_guard.py
- [[Verify a TOTP second factor for high-risk operations (fail-closed).      Args]] - rationale - gateway/security/mfa_guard.py
- [[Verify the second factor for a high-risk action.          Args             acti]] - rationale - gateway/security/mfa_guard.py
- [[_queue()]] - code - gateway/tests/test_mfa_guard.py
- [[_ref_totp()]] - code - gateway/tests/test_mfa_guard.py
- [[_submit_enhanced_high_risk()]] - code - gateway/tests/test_mfa_guard.py
- [[_submit_high_risk()]] - code - gateway/tests/test_mfa_guard.py
- [[_submit_tool_call()]] - code - gateway/tests/test_mfa_guard.py
- [[_truthy()]] - code - gateway/security/mfa_guard.py
- [[enhanced_mfa_queue()]] - code - gateway/tests/test_mfa_guard.py
- [[mfa_guard.py]] - code - gateway/security/mfa_guard.py
- [[now()_1]] - code - gateway/tests/test_mfa_guard.py
- [[test_counter_below_zero_skipped()]] - code - gateway/tests/test_mfa_guard.py
- [[test_custom_high_risk_action_types()]] - code - gateway/tests/test_mfa_guard.py
- [[test_decide_mfa_disabled_approves_without_code()]] - code - gateway/tests/test_mfa_guard.py
- [[test_decide_mfa_enabled_invalid_code_denied()]] - code - gateway/tests/test_mfa_guard.py
- [[test_decide_mfa_enabled_missing_code_denied()]] - code - gateway/tests/test_mfa_guard.py
- [[test_decide_mfa_enabled_replayed_code_denied()]] - code - gateway/tests/test_mfa_guard.py
- [[test_decide_mfa_enabled_valid_code_approves()]] - code - gateway/tests/test_mfa_guard.py
- [[test_decide_reject_never_requires_mfa()]] - code - gateway/tests/test_mfa_guard.py
- [[test_disabled_allows_even_high_risk_with_no_code()]] - code - gateway/tests/test_mfa_guard.py
- [[test_disabled_by_default_allows_without_factor()]] - code - gateway/tests/test_mfa_guard.py
- [[test_empty_code_denies()]] - code - gateway/tests/test_mfa_guard.py
- [[test_enabled_without_secret_denies_fail_closed()]] - code - gateway/tests/test_mfa_guard.py
- [[test_enhanced_decide_missing_code_denied()]] - code - gateway/tests/test_mfa_guard.py
- [[test_enhanced_decide_missing_item_fail_closed()]] - code - gateway/tests/test_mfa_guard.py
- [[test_enhanced_decide_reject_no_mfa()]] - code - gateway/tests/test_mfa_guard.py
- [[test_enhanced_decide_valid_code_approves()]] - code - gateway/tests/test_mfa_guard.py
- [[test_enhanced_tool_call_critical_allowed_with_mfa()]] - code - gateway/tests/test_mfa_guard.py
- [[test_enhanced_tool_call_critical_blocked_without_mfa()]] - code - gateway/tests/test_mfa_guard.py
- [[test_enhanced_tool_call_high_allowed_with_mfa()]] - code - gateway/tests/test_mfa_guard.py
- [[test_enhanced_tool_call_high_blocked_without_mfa()]] - code - gateway/tests/test_mfa_guard.py
- [[test_expired_window_code_denies()]] - code - gateway/tests/test_mfa_guard.py
- [[test_from_env_bad_window_defaults_to_one()]] - code - gateway/tests/test_mfa_guard.py
- [[test_from_env_disabled_when_flag_unset()]] - code - gateway/tests/test_mfa_guard.py
- [[test_from_env_enabled_no_secret_warns()]] - code - gateway/tests/test_mfa_guard.py
- [[test_from_env_reads_secret_and_flag()]] - code - gateway/tests/test_mfa_guard.py
- [[test_from_env_reads_secret_file()]] - code - gateway/tests/test_mfa_guard.py
- [[test_from_env_unreadable_secret_file()]] - code - gateway/tests/test_mfa_guard.py
- [[test_invalid_base32_secret_treated_as_unconfigured()]] - code - gateway/tests/test_mfa_guard.py
- [[test_invalid_code_denies()]] - code - gateway/tests/test_mfa_guard.py
- [[test_is_required_tool_call_disabled_never_required()]] - code - gateway/tests/test_mfa_guard.py
- [[test_is_required_tool_call_tier_parsing()]] - code - gateway/tests/test_mfa_guard.py
- [[test_mfa_guard.py]] - code - gateway/tests/test_mfa_guard.py
- [[test_missing_code_denies_high_risk()]] - code - gateway/tests/test_mfa_guard.py
- [[test_non_high_risk_action_not_required()]] - code - gateway/tests/test_mfa_guard.py
- [[test_prune_used_drops_stale_entries()]] - code - gateway/tests/test_mfa_guard.py
- [[test_real_time_default_now()]] - code - gateway/tests/test_mfa_guard.py
- [[test_replayed_code_denies()]] - code - gateway/tests/test_mfa_guard.py
- [[test_uses_constant_time_compare()]] - code - gateway/tests/test_mfa_guard.py
- [[test_valid_totp_allows_high_risk()]] - code - gateway/tests/test_mfa_guard.py
- [[test_valid_totp_prev_window_allowed()]] - code - gateway/tests/test_mfa_guard.py
- [[test_wrong_length_code_denies()]] - code - gateway/tests/test_mfa_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Mfa_Guard
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_Enhanced Approval]]
- 7 edges to [[_COMMUNITY_Queue (approval_queue)]]
- 6 edges to [[_COMMUNITY_Approval Queue]]
- 1 edge to [[_COMMUNITY_Manifest (skills)]]
- 1 edge to [[_COMMUNITY_Aiosqlite (05 - Dependencies)]]
- 1 edge to [[_COMMUNITY_Mcp Policy]]
- 1 edge to [[_COMMUNITY_Readme (docker)]]
- 1 edge to [[_COMMUNITY_OAuth & Metadata Guard]]

## Top bridge nodes
- [[test_mfa_guard.py]] - degree 60, connects to 4 communities
- [[MFAGuard_2]] - degree 48, connects to 4 communities
- [[EnhancedApprovalQueue_2]] - degree 11, connects to 3 communities
- [[ApprovalQueue_1]] - degree 10, connects to 3 communities
- [[_queue()]] - degree 11, connects to 2 communities