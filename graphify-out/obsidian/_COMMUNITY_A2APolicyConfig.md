---
type: community
members: 50
---

# A2APolicyConfig

**Members:** 50 nodes

## Members
- [[dot-__init__()_224]] - code - gateway/proxy/a2a_proxy.py
- [[dot-__init__()_225]] - code - gateway/security/a2a_policy.py
- [[dot-close()_23]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()_3]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()_4]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[dot-from_dict()_11]] - code - gateway/security/a2a_policy.py
- [[dot-test_bare_config_denies_every_peer()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_configured_allowlist_still_works_alongside_fail_closed_default()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_engine_constructed_with_no_config_at_all_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_from_dict_empty_dict_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_from_dict_none_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_invalid_default_action_string_falls_back_to_deny()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_owner_bypass_is_always_false_regardless_of_input()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A plain default-deny (unknownunlisted peer) is a routing decision, not…]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[A typo'd default_action (e.g. 'allow-all') must not silently open the gate —…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APolicyConfig]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig() with no arguments — the shape a fresh deploy gets if nothing…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Any_90]] - code
- [[Declarative A2A security policy. Loaded from the ``a2a_policy`` section of…]] - rationale - gateway/security/a2a_policy.py
- [[Fail-closed-by-default must not mean impossible to allow anything — an…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[HermesA2AForwarder]] - code - gateway/proxy/a2a_proxy.py
- [[Negative control for the SSRF suite above — a genuinely public callback URL…]] - rationale - gateway/tests/test_a2a_integration.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML)._1]] - rationale - gateway/security/a2a_policy.py
- [[Real HTTP forwarder to Hermes's internal A2A JSON-RPC listener. Matches the…]] - rationale - gateway/proxy/a2a_proxy.py
- [[SCRUM-129 Phase 4 — A2A trust-scoring wiring. Reuses TrustManager as-is…]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[SCRUM-129 Phase 5 — real-HTTP integration tests for the A2A governance module,…]] - rationale - gateway/tests/test_a2a_integration.py
- [[TestDefaultA2APolicyIsFailClosed]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Unlike MCP, owner_bypass is not operator-configurable for A2A at all — an…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[_StubForwarder_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[_jsonrpc()_1]] - code - gateway/tests/test_a2a_integration.py
- [[_jsonrpc()_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[`A2APolicyEngine()` with no config argument — the laziest possible call site —…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[alice legitimately creates a task; bob (a distinct, also-allowlisted peer)…]] - rationale - gateway/tests/test_a2a_integration.py
- [[asyncio_86]] - code
- [[asyncio_87]] - code
- [[load_config-style callers pass whatever the YAML section resolved to, which is…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[parametrize_31]] - code
- [[test_a2a_integration.py]] - code - gateway/tests/test_a2a_integration.py
- [[test_a2a_trust_scoring.py]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_violation_types_exist()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_proxy_without_trust_manager_does_not_raise()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_task_ownership_violation_records_a2a_violation_type()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[trust_manager is an optional dependency — a proxy built without one (e.g.…]] - rationale - gateway/tests/test_a2a_trust_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2APolicyConfig
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_A2APolicyEngine]]
- 21 edges to [[_COMMUNITY_A2AProxy]]
- 13 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_A2APeerTestDouble]]

## Top bridge nodes
- [[test_a2a_integration.py]] - degree 20, connects to 5 communities
- [[test_a2a_trust_scoring.py]] - degree 22, connects to 4 communities
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - degree 10, connects to 3 communities
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - degree 9, connects to 3 communities
- [[test_task_ownership_violation_records_a2a_violation_type()]] - degree 9, connects to 3 communities
