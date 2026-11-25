---
source_file: "gateway/security/a2a_policy.py"
type: "code"
community: "A2APolicyEngine"
location: "L382"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/A2APolicyEngine
---

# A2APolicyEngine

## Connections
- [[dot-__init__()_225]] - `references` [EXTRACTED]
- [[dot-__init__()_189]] - `method` [EXTRACTED]
- [[dot-_decide()_1]] - `method` [EXTRACTED]
- [[dot-_tier_for()_1]] - `method` [EXTRACTED]
- [[dot-enforce()_1]] - `method` [EXTRACTED]
- [[dot-evaluate()_1]] - `method` [EXTRACTED]
- [[dot-test_bare_config_denies_every_peer()]] - `calls` [EXTRACTED]
- [[dot-test_configured_allowlist_still_works_alongside_fail_closed_default()]] - `calls` [EXTRACTED]
- [[dot-test_engine_constructed_with_no_config_at_all_is_fail_closed()]] - `calls` [EXTRACTED]
- [[dot-test_from_dict_empty_dict_is_fail_closed()]] - `calls` [EXTRACTED]
- [[dot-test_from_dict_none_is_fail_closed()]] - `calls` [EXTRACTED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[Decides allow  deny  require-approval for inbound A2A requests. Usage…]] - `rationale_for` [EXTRACTED]
- [[TestDefaultA2APolicyIsFailClosed]] - `uses` [INFERRED]
- [[_base_policy_engine()]] - `calls` [EXTRACTED]
- [[a2a_policy.py]] - `contains` [EXTRACTED]
- [[a2a_proxy.py]] - `imports` [EXTRACTED]
- [[engine()_1]] - `uses` [INFERRED]
- [[test_a2a_integration.py]] - `imports` [EXTRACTED]
- [[test_a2a_policy.py]] - `imports` [EXTRACTED]
- [[test_a2a_policy_default_failclosed.py]] - `imports` [EXTRACTED]
- [[test_a2a_proxy.py]] - `imports` [EXTRACTED]
- [[test_a2a_trust_scoring.py]] - `imports` [EXTRACTED]
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - `uses` [INFERRED]
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - `uses` [INFERRED]
- [[test_allowlisted_peer_low_risk_method_is_allowed()]] - `uses` [INFERRED]
- [[test_default_action_allow_lets_unlisted_peers_through_to_risk_tier_check()]] - `calls` [EXTRACTED]
- [[test_deny_wins_over_allow_for_a_peer_on_both_lists()]] - `calls` [EXTRACTED]
- [[test_denylisted_peer_is_denied_even_if_method_safe()]] - `uses` [INFERRED]
- [[test_enforce_denies_when_queue_downgrades_requires_wait_to_false()]] - `uses` [INFERRED]
- [[test_enforce_falls_back_to_legacy_queue_signature_without_force_tier()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_method_approved_resolves_to_allow()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_method_rejected_resolves_to_deny()]] - `uses` [INFERRED]
- [[test_enforce_high_risk_method_with_no_approval_queue_fails_closed()]] - `uses` [INFERRED]
- [[test_enforce_low_risk_method_bypasses_approval_queue_entirely()]] - `uses` [INFERRED]
- [[test_enforce_task_ownership_violation_never_reaches_approval_queue()]] - `uses` [INFERRED]
- [[test_evaluate_accepts_a_plain_string_method_not_just_the_enum()]] - `uses` [INFERRED]
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - `uses` [INFERRED]
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - `uses` [INFERRED]
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - `uses` [INFERRED]
- [[test_high_risk_methods_require_approval()]] - `uses` [INFERRED]
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - `uses` [INFERRED]
- [[test_low_risk_methods_are_allowed()]] - `uses` [INFERRED]
- [[test_medium_risk_methods_are_allowed()]] - `uses` [INFERRED]
- [[test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk()]] - `calls` [EXTRACTED]
- [[test_peer_cannot_access_another_peers_task()]] - `uses` [INFERRED]
- [[test_peer_cannot_cancel_another_peers_task()]] - `uses` [INFERRED]
- [[test_peer_cannot_subscribe_to_another_peers_task()]] - `uses` [INFERRED]
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - `uses` [INFERRED]
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - `uses` [INFERRED]
- [[test_proxy_without_trust_manager_does_not_raise()]] - `calls` [EXTRACTED]
- [[test_set_push_notification_config_with_safe_callback_still_requires_approval()]] - `uses` [INFERRED]
- [[test_set_push_notification_config_with_unsafe_callback_is_denied_and_severe()]] - `uses` [INFERRED]
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - `uses` [INFERRED]
- [[test_task_creator_can_access_their_own_task()]] - `uses` [INFERRED]
- [[test_task_ownership_check_is_a_no_op_for_an_unknown_task_id()]] - `uses` [INFERRED]
- [[test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path()]] - `calls` [EXTRACTED]
- [[test_task_ownership_violation_records_a2a_violation_type()]] - `uses` [INFERRED]
- [[test_unknown_peer_is_denied_by_default()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/A2APolicyEngine
