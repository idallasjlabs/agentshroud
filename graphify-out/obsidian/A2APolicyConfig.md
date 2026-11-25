---
source_file: "gateway/security/a2a_policy.py"
type: "code"
community: "A2APolicyEngine"
location: "L175"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/A2APolicyEngine
---

# A2APolicyConfig

## Connections
- [[dot-__init__()_189]] - `calls` [EXTRACTED]
- [[dot-__post_init__()_8]] - `method` [EXTRACTED]
- [[dot-from_dict()_10]] - `method` [EXTRACTED]
- [[dot-test_bare_config_denies_every_peer()]] - `calls` [EXTRACTED]
- [[Declarative A2A security policy. Loaded from the ``a2a_policy`` section of…]] - `rationale_for` [EXTRACTED]
- [[TestDefaultA2APolicyIsFailClosed]] - `uses` [INFERRED]
- [[_base_config()_1]] - `uses` [INFERRED]
- [[_base_policy_engine()]] - `uses` [INFERRED]
- [[a2a_policy.py]] - `contains` [EXTRACTED]
- [[test_a2a_integration.py]] - `imports` [EXTRACTED]
- [[test_a2a_policy.py]] - `imports` [EXTRACTED]
- [[test_a2a_policy_default_failclosed.py]] - `imports` [EXTRACTED]
- [[test_a2a_proxy.py]] - `imports` [EXTRACTED]
- [[test_a2a_trust_scoring.py]] - `imports` [EXTRACTED]
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - `uses` [INFERRED]
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - `uses` [INFERRED]
- [[test_default_action_allow_lets_unlisted_peers_through_to_risk_tier_check()]] - `uses` [INFERRED]
- [[test_deny_wins_over_allow_for_a_peer_on_both_lists()]] - `uses` [INFERRED]
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - `uses` [INFERRED]
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - `uses` [INFERRED]
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - `uses` [INFERRED]
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - `uses` [INFERRED]
- [[test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk()]] - `uses` [INFERRED]
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - `uses` [INFERRED]
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - `uses` [INFERRED]
- [[test_proxy_without_trust_manager_does_not_raise()]] - `uses` [INFERRED]
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - `uses` [INFERRED]
- [[test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path()]] - `uses` [INFERRED]
- [[test_task_ownership_violation_records_a2a_violation_type()]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/A2APolicyEngine
