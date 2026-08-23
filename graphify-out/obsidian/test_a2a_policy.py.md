---
source_file: "gateway/tests/test_a2a_policy.py"
type: "code"
community: "A2a Policy"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2a_Policy
---

# test_a2a_policy.py

## Connections
- [[A2AMethod]] - `imports` [EXTRACTED]
- [[A2APolicyAction]] - `imports` [EXTRACTED]
- [[A2APolicyConfig]] - `imports` [EXTRACTED]
- [[A2APolicyDecision]] - `imports` [EXTRACTED]
- [[A2APolicyEngine_1]] - `imports` [EXTRACTED]
- [[Upstream A2A Gap 78298 — SSRF Push-Notification Callback URL Bypass]] - `references` [EXTRACTED]
- [[Upstream A2A Gap 83701 — TaskContextId Collision Hijack]] - `references` [EXTRACTED]
- [[_LegacyStubApprovalQueue]] - `contains` [EXTRACTED]
- [[_StubApprovalQueue]] - `contains` [EXTRACTED]
- [[_base_config()]] - `contains` [EXTRACTED]
- [[engine()]] - `contains` [EXTRACTED]
- [[is_safe_a2a_callback_url()]] - `imports` [EXTRACTED]
- [[test_allowlisted_peer_low_risk_method_is_allowed()]] - `contains` [EXTRACTED]
- [[test_callback_url_bare_dot_host_is_rejected()]] - `contains` [EXTRACTED]
- [[test_callback_url_hostname_resolving_to_a_private_ip_is_rejected()]] - `contains` [EXTRACTED]
- [[test_callback_url_ipv4_mapped_ipv6_loopback_is_rejected()]] - `contains` [EXTRACTED]
- [[test_callback_url_legitimate_public_urls_are_allowed()]] - `contains` [EXTRACTED]
- [[test_callback_url_malformed_url_is_rejected()]] - `contains` [EXTRACTED]
- [[test_callback_url_out_of_range_decimal_literal_is_not_treated_as_a_valid_ip()]] - `contains` [EXTRACTED]
- [[test_callback_url_rejects_non_http_schemes()]] - `contains` [EXTRACTED]
- [[test_callback_url_scheme_only_no_host_is_rejected()]] - `contains` [EXTRACTED]
- [[test_callback_url_ssrf_bypass_encodings_are_rejected()]] - `contains` [EXTRACTED]
- [[test_callback_url_unresolvable_hostname_fails_closed()]] - `contains` [EXTRACTED]
- [[test_decision_allowed_property_only_true_for_terminal_allow()]] - `contains` [EXTRACTED]
- [[test_default_action_allow_lets_unlisted_peers_through_to_risk_tier_check()]] - `contains` [EXTRACTED]
- [[test_deny_wins_over_allow_for_a_peer_on_both_lists()]] - `contains` [EXTRACTED]
- [[test_denylisted_peer_is_denied_even_if_method_safe()]] - `contains` [EXTRACTED]
- [[test_enforce_denies_when_queue_downgrades_requires_wait_to_false()]] - `contains` [EXTRACTED]
- [[test_enforce_falls_back_to_legacy_queue_signature_without_force_tier()]] - `contains` [EXTRACTED]
- [[test_enforce_high_risk_method_approved_resolves_to_allow()]] - `contains` [EXTRACTED]
- [[test_enforce_high_risk_method_rejected_resolves_to_deny()]] - `contains` [EXTRACTED]
- [[test_enforce_high_risk_method_with_no_approval_queue_fails_closed()]] - `contains` [EXTRACTED]
- [[test_enforce_low_risk_method_bypasses_approval_queue_entirely()]] - `contains` [EXTRACTED]
- [[test_enforce_task_ownership_violation_never_reaches_approval_queue()]] - `contains` [EXTRACTED]
- [[test_evaluate_accepts_a_plain_string_method_not_just_the_enum()]] - `contains` [EXTRACTED]
- [[test_high_risk_methods_require_approval()]] - `contains` [EXTRACTED]
- [[test_low_risk_methods_are_allowed()]] - `contains` [EXTRACTED]
- [[test_medium_risk_methods_are_allowed()]] - `contains` [EXTRACTED]
- [[test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk()]] - `contains` [EXTRACTED]
- [[test_peer_cannot_access_another_peers_task()]] - `contains` [EXTRACTED]
- [[test_peer_cannot_cancel_another_peers_task()]] - `contains` [EXTRACTED]
- [[test_peer_cannot_subscribe_to_another_peers_task()]] - `contains` [EXTRACTED]
- [[test_set_push_notification_config_with_safe_callback_still_requires_approval()]] - `contains` [EXTRACTED]
- [[test_set_push_notification_config_with_unsafe_callback_is_denied_and_severe()]] - `contains` [EXTRACTED]
- [[test_task_creator_can_access_their_own_task()]] - `contains` [EXTRACTED]
- [[test_task_ownership_check_is_a_no_op_for_an_unknown_task_id()]] - `contains` [EXTRACTED]
- [[test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path()]] - `contains` [EXTRACTED]
- [[test_unknown_peer_is_denied_by_default()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2a_Policy