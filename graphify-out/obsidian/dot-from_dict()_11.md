---
source_file: "gateway/security/a2a_policy.py"
type: "code"
community: "A2APolicyConfig"
location: "L210"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/A2APolicyConfig
---

# .from_dict()

## Connections
- [[dot-test_configured_allowlist_still_works_alongside_fail_closed_default()]] - `calls` [EXTRACTED]
- [[dot-test_from_dict_empty_dict_is_fail_closed()]] - `calls` [EXTRACTED]
- [[dot-test_from_dict_none_is_fail_closed()]] - `calls` [EXTRACTED]
- [[dot-test_invalid_default_action_string_falls_back_to_deny()]] - `calls` [EXTRACTED]
- [[dot-test_owner_bypass_is_always_false_regardless_of_input()]] - `calls` [EXTRACTED]
- [[A2APolicyAction]] - `calls` [EXTRACTED]
- [[A2APolicyConfig]] - `method` [EXTRACTED]
- [[Any_90]] - `references` [EXTRACTED]
- [[Parse a policy config from a plain dict (e.g. loaded from YAML)._1]] - `rationale_for` [EXTRACTED]
- [[_base_config()_1]] - `calls` [EXTRACTED]
- [[_base_policy_engine()]] - `calls` [EXTRACTED]
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - `calls` [EXTRACTED]
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - `calls` [EXTRACTED]
- [[test_default_action_allow_lets_unlisted_peers_through_to_risk_tier_check()]] - `calls` [EXTRACTED]
- [[test_deny_wins_over_allow_for_a_peer_on_both_lists()]] - `calls` [EXTRACTED]
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - `calls` [EXTRACTED]
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - `calls` [EXTRACTED]
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - `calls` [EXTRACTED]
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - `calls` [EXTRACTED]
- [[test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - `calls` [EXTRACTED]
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - `calls` [EXTRACTED]
- [[test_proxy_without_trust_manager_does_not_raise()]] - `calls` [EXTRACTED]
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - `calls` [EXTRACTED]
- [[test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path()]] - `calls` [EXTRACTED]
- [[test_task_ownership_violation_records_a2a_violation_type()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/A2APolicyConfig
