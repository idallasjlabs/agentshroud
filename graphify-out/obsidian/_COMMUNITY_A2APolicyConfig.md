---
type: community
members: 52
---

# A2APolicyConfig

**Members:** 52 nodes

## Members
- [[dot-__init__()_226]] - code - gateway/proxy/a2a_proxy.py
- [[dot-__init__()_227]] - code - gateway/security/a2a_policy.py
- [[dot-__init__()_228]] - code - gateway/tests/test_a2a_integration.py
- [[dot-_handle()_1]] - code - gateway/tests/test_a2a_integration.py
- [[dot-close()_23]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()_3]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()_4]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[dot-from_dict()_11]] - code - gateway/security/a2a_policy.py
- [[dot-test_invalid_default_action_string_falls_back_to_deny()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[dot-test_owner_bypass_is_always_false_regardless_of_input()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A plain default-deny (unknownunlisted peer) is a routing decision, not…]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[A typo'd default_action (e.g. 'allow-all') must not silently open the gate —…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APeerTestDouble]] - code - gateway/tests/test_a2a_integration.py
- [[A2APolicyConfig]] - code - gateway/security/a2a_policy.py
- [[Any_90]] - code
- [[Declarative A2A security policy. Loaded from the ``a2a_policy`` section of…]] - rationale - gateway/security/a2a_policy.py
- [[HermesA2AForwarder]] - code - gateway/proxy/a2a_proxy.py
- [[Minimal JSON-RPC 2.0 responder standing in for a real A2A peer. Explicitly NOT…]] - rationale - gateway/tests/test_a2a_integration.py
- [[Negative control for the SSRF suite above — a genuinely public callback URL…]] - rationale - gateway/tests/test_a2a_integration.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML)._1]] - rationale - gateway/security/a2a_policy.py
- [[Real HTTP forwarder to Hermes's internal A2A JSON-RPC listener. Matches the…]] - rationale - gateway/proxy/a2a_proxy.py
- [[Request_9]] - code
- [[Response_1]] - code
- [[SCRUM-129 Phase 4 — A2A trust-scoring wiring. Reuses TrustManager as-is…]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[SCRUM-129 Phase 5 — real-HTTP integration tests for the A2A governance module,…]] - rationale - gateway/tests/test_a2a_integration.py
- [[Unlike MCP, owner_bypass is not operator-configurable for A2A at all — an…]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[_StubForwarder_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[_jsonrpc()_1]] - code - gateway/tests/test_a2a_integration.py
- [[_jsonrpc()_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[a2a_proxy.py]] - code - gateway/proxy/a2a_proxy.py
- [[alice legitimately creates a task; bob (a distinct, also-allowlisted peer)…]] - rationale - gateway/tests/test_a2a_integration.py
- [[asyncio_86]] - code
- [[asyncio_87]] - code
- [[fixture_141]] - code
- [[parametrize_31]] - code
- [[test_a2a_integration.py]] - code - gateway/tests/test_a2a_integration.py
- [[test_a2a_trust_scoring.py]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_violation_types_exist()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_double_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_proxy_without_trust_manager_does_not_raise()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_task_ownership_violation_records_a2a_violation_type()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[trust_manager is an optional dependency — a proxy built without one (e.g.…]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[trust_manager()_5]] - code - gateway/tests/test_a2a_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2APolicyConfig
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_A2APolicyEngine]]
- 29 edges to [[_COMMUNITY_A2AProxy]]
- 12 edges to [[_COMMUNITY_ProgressiveTrustConfig]]
- 8 edges to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_test_module_stats.py]]

## Top bridge nodes
- [[test_a2a_trust_scoring.py]] - degree 22, connects to 4 communities
- [[test_a2a_integration.py]] - degree 20, connects to 4 communities
- [[a2a_proxy.py]] - degree 13, connects to 4 communities
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - degree 10, connects to 3 communities
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - degree 9, connects to 3 communities
