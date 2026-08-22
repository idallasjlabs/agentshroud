---
source_file: "gateway/tests/test_a2a_policy.py"
type: "code"
community: "A2a Policy"
location: "L50"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2a_Policy
---

# A2APolicyEngine

## Connections
- [[A2AMethod]] - `uses` [INFERRED]
- [[A2APolicyAction]] - `uses` [INFERRED]
- [[A2APolicyConfig]] - `uses` [INFERRED]
- [[A2APolicyDecision]] - `uses` [INFERRED]
- [[A2APolicyEngine_1]] - `uses` [INFERRED]
- [[engine()]] - `references` [EXTRACTED]
- [[test_allowlisted_peer_low_risk_method_is_allowed()]] - `references` [EXTRACTED]
- [[test_default_action_allow_lets_unlisted_peers_through_to_risk_tier_check()]] - `calls` [EXTRACTED]
- [[test_deny_wins_over_allow_for_a_peer_on_both_lists()]] - `calls` [EXTRACTED]
- [[test_denylisted_peer_is_denied_even_if_method_safe()]] - `references` [EXTRACTED]
- [[test_enforce_denies_when_queue_downgrades_requires_wait_to_false()]] - `calls` [EXTRACTED]
- [[test_enforce_falls_back_to_legacy_queue_signature_without_force_tier()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_method_approved_resolves_to_allow()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_method_rejected_resolves_to_deny()]] - `calls` [EXTRACTED]
- [[test_enforce_high_risk_method_with_no_approval_queue_fails_closed()]] - `references` [EXTRACTED]
- [[test_enforce_low_risk_method_bypasses_approval_queue_entirely()]] - `references` [EXTRACTED]
- [[test_enforce_task_ownership_violation_never_reaches_approval_queue()]] - `calls` [EXTRACTED]
- [[test_evaluate_accepts_a_plain_string_method_not_just_the_enum()]] - `references` [EXTRACTED]
- [[test_high_risk_methods_require_approval()]] - `references` [EXTRACTED]
- [[test_low_risk_methods_are_allowed()]] - `references` [EXTRACTED]
- [[test_medium_risk_methods_are_allowed()]] - `references` [EXTRACTED]
- [[test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk()]] - `calls` [EXTRACTED]
- [[test_peer_cannot_access_another_peers_task()]] - `references` [EXTRACTED]
- [[test_peer_cannot_cancel_another_peers_task()]] - `references` [EXTRACTED]
- [[test_peer_cannot_subscribe_to_another_peers_task()]] - `references` [EXTRACTED]
- [[test_set_push_notification_config_with_safe_callback_still_requires_approval()]] - `references` [EXTRACTED]
- [[test_set_push_notification_config_with_unsafe_callback_is_denied_and_severe()]] - `references` [EXTRACTED]
- [[test_task_creator_can_access_their_own_task()]] - `references` [EXTRACTED]
- [[test_task_ownership_check_is_a_no_op_for_an_unknown_task_id()]] - `references` [EXTRACTED]
- [[test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path()]] - `calls` [EXTRACTED]
- [[test_unknown_peer_is_denied_by_default()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2a_Policy