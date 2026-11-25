---
type: community
members: 141
---

# A2APolicyEngine

**Members:** 141 nodes

## Members
- [[NOTE gatewaysecurityegress_filter.py_is_private_ip has the same class]] - rationale - gateway/security/a2a_policy.py
- [[dot-__init__()_188]] - code - gateway/proxy/a2a_proxy.py
- [[dot-__init__()_189]] - code - gateway/security/a2a_policy.py
- [[dot-__init__()_190]] - code - gateway/tests/test_a2a_policy.py
- [[dot-__post_init__()_8]] - code - gateway/security/a2a_policy.py
- [[dot-_decide()_1]] - code - gateway/security/a2a_policy.py
- [[dot-_tier_for()_1]] - code - gateway/security/a2a_policy.py
- [[dot-allowed()_1]] - code - gateway/security/a2a_policy.py
- [[dot-close()_16]] - code - gateway/proxy/a2a_proxy.py
- [[dot-enforce()_1]] - code - gateway/security/a2a_policy.py
- [[dot-evaluate()_1]] - code - gateway/security/a2a_policy.py
- [[dot-forward()_1]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[dot-from_dict()_10]] - code - gateway/security/a2a_policy.py
- [[dot-submit_tool_request()_4]] - code - gateway/tests/test_a2a_policy.py
- [[dot-test_bare_config_denies_every_peer()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_configured_allowlist_still_works_alongside_fail_closed_default()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_engine_constructed_with_no_config_at_all_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_from_dict_empty_dict_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_from_dict_none_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_invalid_default_action_string_falls_back_to_deny()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_owner_bypass_is_always_false_regardless_of_input()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-wait_for_decision()_4]] - code - gateway/tests/test_a2a_policy.py
- [[A 10-digit decimal string (matches the decimal-IPv4 pattern) whose value…]] - rationale - gateway/tests/test_a2a_policy.py
- [[A plain default-deny (unknownunlisted peer) is a routing decision, not…]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[A queue reporting requires_wait=False for a call the engine deemed high-risk…]] - rationale - gateway/tests/test_a2a_policy.py
- [[A task_id AgentShroud never saw created (e.g. the very first GetTask against a…]] - rationale - gateway/tests/test_a2a_policy.py
- [[A typo'd default_action (e.g. 'allow-all') must not silently open the gate —…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2A (Agent-to-Agent) security policy engine (SCRUM-129). Governance for Hermes…]] - rationale - gateway/security/a2a_policy.py
- [[A2A peers are never equivalent to the human operator — unlike MCP, owner_bypass…]] - rationale - gateway/tests/test_a2a_policy.py
- [[A2AMethod]] - code - gateway/security/a2a_policy.py
- [[A2APolicyAction]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig() with no arguments — the shape a fresh deploy gets if nothing…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APolicyDecision]] - code - gateway/security/a2a_policy.py
- [[A2APolicyEngine]] - code - gateway/security/a2a_policy.py
- [[Accept either the enum or its string value (JSON-RPC payloads arrive as plain…]] - rationale - gateway/security/a2a_policy.py
- [[An operator who explicitly opts into default_action=allow gets normal risk-tier…]] - rationale - gateway/tests/test_a2a_policy.py
- [[Any_74]] - code
- [[Best-effort canonicalization of alternate IPv4 encodings that…]] - rationale - gateway/security/a2a_policy.py
- [[Canonical (v1.0 PascalCase) A2A JSON-RPC methods this engine governs.]] - rationale - gateway/security/a2a_policy.py
- [[DNS rebinding a public-looking hostname that currently resolves to a…]] - rationale - gateway/tests/test_a2a_policy.py
- [[Decides allow  deny  require-approval for inbound A2A requests. Usage…]] - rationale - gateway/security/a2a_policy.py
- [[Declarative A2A security policy. Loaded from the ``a2a_policy`` section of…]] - rationale - gateway/security/a2a_policy.py
- [[Enum_40]] - code
- [[Evaluate a single A2A request. Pure — no IO, no side effects beyond best-…]] - rationale - gateway/security/a2a_policy.py
- [[Evaluate and resolve the decision to a terminal ALLOWDENY. Identical fail-…]] - rationale - gateway/security/a2a_policy.py
- [[Fail-closed-by-default must not mean impossible to allow anything — an…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Hardened SSRF guard for A2A push-notification callback URLs. Independent…]] - rationale - gateway/security/a2a_policy.py
- [[HermesA2AForwarder]] - code - gateway/proxy/a2a_proxy.py
- [[Hostname resolution is mocked — this test asserts the validator's own logic,…]] - rationale - gateway/tests/test_a2a_policy.py
- [[IPv4Address]] - code
- [[Negative control for the SSRF suite above — a genuinely public callback URL…]] - rationale - gateway/tests/test_a2a_integration.py
- [[Normalize a peer-id reference for robust, evasion-resistant matching. Same…]] - rationale - gateway/security/a2a_policy.py
- [[Ownership is checked before the risk-tier gate — a mismatched peer must be…]] - rationale - gateway/tests/test_a2a_policy.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML)._1]] - rationale - gateway/security/a2a_policy.py
- [[Real HTTP forwarder to Hermes's internal A2A JSON-RPC listener. Matches the…]] - rationale - gateway/proxy/a2a_proxy.py
- [[Real JSON-RPC payloads deliver the method as a plain string — evaluate() must…]] - rationale - gateway/tests/test_a2a_policy.py
- [[SCRUM-129 Phase 5 — real-HTTP integration tests for the A2A governance module,…]] - rationale - gateway/tests/test_a2a_integration.py
- [[SCRUM-129 — A2A policy engine must never ship dormant or default-open. Mirrors…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[TestDefaultA2APolicyIsFailClosed]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Tests for the A2A (Agent-to-Agent) security policy engine (SCRUM-129).…]] - rationale - gateway/tests/test_a2a_policy.py
- [[The `engine` fixture has no approval_queue configured at all — a high-risk…]] - rationale - gateway/tests/test_a2a_policy.py
- [[The result of evaluating a single A2A request against the policy.]] - rationale - gateway/security/a2a_policy.py
- [[The three terminal policy outcomes for an A2A request.]] - rationale - gateway/security/a2a_policy.py
- [[True only for a terminal ALLOW. REQUIRE_APPROVAL is not allowed on its own —…_1]] - rationale - gateway/security/a2a_policy.py
- [[Two allowlisted peers, one denylisted peer, default-deny for everyone else.]] - rationale - gateway/tests/test_a2a_policy.py
- [[Unlike MCP, owner_bypass is not operator-configurable for A2A at all — an…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[_BaseAddress]] - code
- [[_StubApprovalQueue]] - code - gateway/tests/test_a2a_policy.py
- [[_StubForwarder_1]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[_address_is_public()]] - code - gateway/security/a2a_policy.py
- [[_base_config()_1]] - code - gateway/tests/test_a2a_policy.py
- [[_canonicalize_ip_literal()]] - code - gateway/security/a2a_policy.py
- [[_int_to_ipv4()]] - code - gateway/security/a2a_policy.py
- [[_jsonrpc()]] - code - gateway/tests/test_a2a_integration.py
- [[_jsonrpc()_1]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[_method_of()]] - code - gateway/security/a2a_policy.py
- [[_norm()_1]] - code - gateway/security/a2a_policy.py
- [[`A2APolicyEngine()` with no config argument — the laziest possible call site —…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[a2a_policy.py]] - code - gateway/security/a2a_policy.py
- [[alice legitimately creates a task; bob (a distinct, also-allowlisted peer)…]] - rationale - gateway/tests/test_a2a_integration.py
- [[asyncio_72]] - code
- [[asyncio_73]] - code
- [[asyncio_74]] - code
- [[engine()_1]] - code - gateway/tests/test_a2a_policy.py
- [[fixture_122]] - code
- [[is_safe_a2a_callback_url()]] - code - gateway/security/a2a_policy.py
- [[load_config-style callers pass whatever the YAML section resolved to, which is…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[parametrize_22]] - code
- [[parametrize_23]] - code
- [[str_23]] - code
- [[test_a2a_integration.py]] - code - gateway/tests/test_a2a_integration.py
- [[test_a2a_policy.py]] - code - gateway/tests/test_a2a_policy.py
- [[test_a2a_policy_default_failclosed.py]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_allowlisted_peer_low_risk_method_is_allowed()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_bare_dot_host_is_rejected()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_hostname_resolving_to_a_private_ip_is_rejected()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_ipv4_mapped_ipv6_loopback_is_rejected()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_legitimate_public_urls_are_allowed()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_malformed_url_is_rejected()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_out_of_range_decimal_literal_is_not_treated_as_a_valid_ip()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_rejects_non_http_schemes()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_scheme_only_no_host_is_rejected()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_ssrf_bypass_encodings_are_rejected()]] - code - gateway/tests/test_a2a_policy.py
- [[test_callback_url_unresolvable_hostname_fails_closed()]] - code - gateway/tests/test_a2a_policy.py
- [[test_decision_allowed_property_only_true_for_terminal_allow()]] - code - gateway/tests/test_a2a_policy.py
- [[test_default_action_allow_lets_unlisted_peers_through_to_risk_tier_check()]] - code - gateway/tests/test_a2a_policy.py
- [[test_deny_wins_over_allow_for_a_peer_on_both_lists()]] - code - gateway/tests/test_a2a_policy.py
- [[test_denylisted_peer_is_denied_even_if_method_safe()]] - code - gateway/tests/test_a2a_policy.py
- [[test_enforce_denies_when_queue_downgrades_requires_wait_to_false()]] - code - gateway/tests/test_a2a_policy.py
- [[test_enforce_falls_back_to_legacy_queue_signature_without_force_tier()]] - code - gateway/tests/test_a2a_policy.py
- [[test_enforce_high_risk_method_approved_resolves_to_allow()]] - code - gateway/tests/test_a2a_policy.py
- [[test_enforce_high_risk_method_rejected_resolves_to_deny()]] - code - gateway/tests/test_a2a_policy.py
- [[test_enforce_high_risk_method_with_no_approval_queue_fails_closed()]] - code - gateway/tests/test_a2a_policy.py
- [[test_enforce_low_risk_method_bypasses_approval_queue_entirely()]] - code - gateway/tests/test_a2a_policy.py
- [[test_enforce_task_ownership_violation_never_reaches_approval_queue()]] - code - gateway/tests/test_a2a_policy.py
- [[test_evaluate_accepts_a_plain_string_method_not_just_the_enum()]] - code - gateway/tests/test_a2a_policy.py
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_high_risk_methods_require_approval()]] - code - gateway/tests/test_a2a_policy.py
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_low_risk_methods_are_allowed()]] - code - gateway/tests/test_a2a_policy.py
- [[test_medium_risk_methods_are_allowed()]] - code - gateway/tests/test_a2a_policy.py
- [[test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk()]] - code - gateway/tests/test_a2a_policy.py
- [[test_peer_cannot_access_another_peers_task()]] - code - gateway/tests/test_a2a_policy.py
- [[test_peer_cannot_cancel_another_peers_task()]] - code - gateway/tests/test_a2a_policy.py
- [[test_peer_cannot_subscribe_to_another_peers_task()]] - code - gateway/tests/test_a2a_policy.py
- [[test_proxy_without_trust_manager_does_not_raise()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_set_push_notification_config_with_safe_callback_still_requires_approval()]] - code - gateway/tests/test_a2a_policy.py
- [[test_set_push_notification_config_with_unsafe_callback_is_denied_and_severe()]] - code - gateway/tests/test_a2a_policy.py
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_task_creator_can_access_their_own_task()]] - code - gateway/tests/test_a2a_policy.py
- [[test_task_ownership_check_is_a_no_op_for_an_unknown_task_id()]] - code - gateway/tests/test_a2a_policy.py
- [[test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path()]] - code - gateway/tests/test_a2a_policy.py
- [[test_task_ownership_violation_records_a2a_violation_type()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_unknown_peer_is_denied_by_default()]] - code - gateway/tests/test_a2a_policy.py
- [[trust_manager is an optional dependency — a proxy built without one (e.g.…]] - rationale - gateway/tests/test_a2a_trust_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2APolicyEngine
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_A2AProxy]]
- 12 edges to [[_COMMUNITY_TrustLevel]]
- 4 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_A2APeerTestDouble]]
- 2 edges to [[_COMMUNITY__LegacyStubApprovalQueue]]
- 2 edges to [[_COMMUNITY_test_module_stats.py]]

## Top bridge nodes
- [[test_a2a_integration.py]] - degree 20, connects to 4 communities
- [[a2a_policy.py]] - degree 21, connects to 3 communities
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - degree 10, connects to 3 communities
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - degree 9, connects to 3 communities
- [[test_task_ownership_violation_records_a2a_violation_type()]] - degree 9, connects to 3 communities
