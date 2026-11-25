---
source_file: "gateway/security/a2a_policy.py"
type: "code"
community: "A2APolicyEngine"
location: "L134"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/A2APolicyEngine
---

# A2APolicyAction

## Connections
- [[dot-from_dict()_10]] - `calls` [EXTRACTED]
- [[Enum_40]] - `inherits` [EXTRACTED]
- [[TestDefaultA2APolicyIsFailClosed]] - `uses` [INFERRED]
- [[The three terminal policy outcomes for an A2A request.]] - `rationale_for` [EXTRACTED]
- [[a2a_policy.py]] - `contains` [EXTRACTED]
- [[str_23]] - `inherits` [EXTRACTED]
- [[test_a2a_policy.py]] - `imports` [EXTRACTED]
- [[test_a2a_policy_default_failclosed.py]] - `imports` [EXTRACTED]
- [[test_allowlisted_peer_low_risk_method_is_allowed()]] - `uses` [INFERRED]
- [[test_decision_allowed_property_only_true_for_terminal_allow()]] - `uses` [INFERRED]
- [[test_default_action_allow_lets_unlisted_peers_through_to_risk_tier_check()]] - `uses` [INFERRED]
- [[test_deny_wins_over_allow_for_a_peer_on_both_lists()]] - `uses` [INFERRED]
- [[test_denylisted_peer_is_denied_even_if_method_safe()]] - `uses` [INFERRED]
- [[test_enforce_denies_when_queue_downgrades_requires_wait_to_false()]] - `uses` [INFERRED]
- [[test_enforce_falls_back_to_legacy_queue_signature_without_force_tier()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_method_approved_resolves_to_allow()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_method_rejected_resolves_to_deny()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_method_with_no_approval_queue_fails_closed()]] - `uses` [INFERRED]
- [[test_enforce_low_risk_method_bypasses_approval_queue_entirely()]] - `uses` [INFERRED]
- [[test_enforce_task_ownership_violation_never_reaches_approval_queue()]] - `uses` [INFERRED]
- [[test_evaluate_accepts_a_plain_string_method_not_just_the_enum()]] - `uses` [INFERRED]
- [[test_high_risk_methods_require_approval()]] - `uses` [INFERRED]
- [[test_low_risk_methods_are_allowed()]] - `uses` [INFERRED]
- [[test_medium_risk_methods_are_allowed()]] - `uses` [INFERRED]
- [[test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk()]] - `uses` [INFERRED]
- [[test_peer_cannot_access_another_peers_task()]] - `uses` [INFERRED]
- [[test_peer_cannot_cancel_another_peers_task()]] - `uses` [INFERRED]
- [[test_peer_cannot_subscribe_to_another_peers_task()]] - `uses` [INFERRED]
- [[test_set_push_notification_config_with_safe_callback_still_requires_approval()]] - `uses` [INFERRED]
- [[test_set_push_notification_config_with_unsafe_callback_is_denied_and_severe()]] - `uses` [INFERRED]
- [[test_task_creator_can_access_their_own_task()]] - `uses` [INFERRED]
- [[test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path()]] - `uses` [INFERRED]
- [[test_unknown_peer_is_denied_by_default()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/A2APolicyEngine
