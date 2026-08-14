---
source_file: "gateway/security/a2a_policy.py"
type: "code"
community: "Gateway Test Suite"
location: "L382"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# A2APolicyEngine

## Connections
- [[.__init__()_47]] - `method` [EXTRACTED]
- [[._decide()]] - `method` [EXTRACTED]
- [[._tier_for()]] - `method` [EXTRACTED]
- [[.enforce()]] - `method` [EXTRACTED]
- [[.evaluate()]] - `method` [EXTRACTED]
- [[.test_bare_config_denies_every_peer()]] - `calls` [EXTRACTED]
- [[.test_configured_allowlist_still_works_alongside_fail_closed_default()]] - `calls` [EXTRACTED]
- [[.test_engine_constructed_with_no_config_at_all_is_fail_closed()]] - `calls` [EXTRACTED]
- [[.test_from_dict_empty_dict_is_fail_closed()]] - `calls` [EXTRACTED]
- [[.test_from_dict_none_is_fail_closed()]] - `calls` [EXTRACTED]
- [[A2AMethod_1]] - `uses` [INFERRED]
- [[A2APeerTestDouble]] - `uses` [INFERRED]
- [[A2APolicyConfig_1]] - `uses` [INFERRED]
- [[A2APolicyEngine]] - `uses` [INFERRED]
- [[A2APolicyEngine_2]] - `uses` [INFERRED]
- [[A2APolicyEngine_3]] - `uses` [INFERRED]
- [[A2AProxy]] - `uses` [INFERRED]
- [[A2AProxy_1]] - `uses` [INFERRED]
- [[A2AProxyResult]] - `uses` [INFERRED]
- [[Any_11]] - `uses` [INFERRED]
- [[Decides allow  deny  require-approval for inbound A2A requests.      Usage]] - `rationale_for` [EXTRACTED]
- [[Hermes A2A Plugin Upstream Gaps (83701, 8053480779, 78298, 77872, 81042)]] - `implements` [EXTRACTED]
- [[HermesA2AForwarder]] - `uses` [INFERRED]
- [[ParsedA2ARequest]] - `uses` [INFERRED]
- [[Request_7]] - `uses` [INFERRED]
- [[Response]] - `uses` [INFERRED]
- [[Response_2]] - `uses` [INFERRED]
- [[TestDefaultA2APolicyIsFailClosed]] - `uses` [INFERRED]
- [[TrustManager_2]] - `uses` [INFERRED]
- [[_Event]] - `uses` [INFERRED]
- [[_LegacyStubApprovalQueue]] - `uses` [INFERRED]
- [[_StubApprovalQueue]] - `uses` [INFERRED]
- [[_StubAuditStore]] - `uses` [INFERRED]
- [[_StubForwarder]] - `uses` [INFERRED]
- [[_StubForwarder_1]] - `uses` [INFERRED]
- [[_base_policy_engine()]] - `calls` [EXTRACTED]
- [[a2a_policy.py]] - `contains` [EXTRACTED]
- [[a2a_proxy.py]] - `imports` [EXTRACTED]
- [[test_a2a_integration.py]] - `imports` [EXTRACTED]
- [[test_a2a_policy.py]] - `imports` [EXTRACTED]
- [[test_a2a_policy_default_failclosed.py]] - `imports` [EXTRACTED]
- [[test_a2a_proxy.py]] - `imports` [EXTRACTED]
- [[test_a2a_trust_scoring.py]] - `imports` [EXTRACTED]
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - `calls` [EXTRACTED]
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - `calls` [EXTRACTED]
- [[test_default_action_allow_lets_unlisted_peers_through_to_risk_tier_check()]] - `calls` [EXTRACTED]
- [[test_deny_wins_over_allow_for_a_peer_on_both_lists()]] - `calls` [EXTRACTED]
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - `calls` [EXTRACTED]
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - `calls` [EXTRACTED]
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - `calls` [EXTRACTED]
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - `calls` [EXTRACTED]
- [[test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk()]] - `calls` [EXTRACTED]
- [[test_proxy_without_trust_manager_does_not_raise()]] - `calls` [EXTRACTED]
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - `calls` [EXTRACTED]
- [[test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path()]] - `calls` [EXTRACTED]
- [[test_task_ownership_violation_records_a2a_violation_type()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite