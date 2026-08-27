---
type: community
members: 49
---

# Community 104

**Members:** 49 nodes

## Members
- [[.__init__()_18]] - code - gateway/proxy/a2a_proxy.py
- [[.__init__()_50]] - code - gateway/security/a2a_policy.py
- [[.__init__()_134]] - code - gateway/tests/test_a2a_integration.py
- [[.__post_init__()_2]] - code - gateway/security/a2a_policy.py
- [[._handle()_1]] - code - gateway/tests/test_a2a_integration.py
- [[.close()_7]] - code - gateway/proxy/a2a_proxy.py
- [[.forward()_3]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[.from_dict()_2]] - code - gateway/security/a2a_policy.py
- [[A plain default-deny (unknownunlisted peer) is a routing decision, not     evid]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[A2APeerTestDouble]] - code - gateway/tests/test_a2a_integration.py
- [[A2APolicyConfig]] - code - gateway/security/a2a_policy.py
- [[A2AProxy]] - code - gateway/proxy/a2a_proxy.py
- [[Any_29]] - code - gateway/security/a2a_policy.py
- [[Declarative A2A security policy.      Loaded from the ``a2a_policy`` section of]] - rationale - gateway/security/a2a_policy.py
- [[HermesA2AForwarder]] - code - gateway/proxy/a2a_proxy.py
- [[Minimal JSON-RPC 2.0 responder standing in for a real A2A peer.      Explicitly]] - rationale - gateway/tests/test_a2a_integration.py
- [[Negative control for the SSRF suite above — a genuinely public     callback URL]] - rationale - gateway/tests/test_a2a_integration.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML).]] - rationale - gateway/security/a2a_policy.py
- [[Real HTTP forwarder to Hermes's internal A2A JSON-RPC listener.      Matches the]] - rationale - gateway/proxy/a2a_proxy.py
- [[Request_7]] - code - gateway/tests/test_a2a_integration.py
- [[Response]] - code - gateway/tests/test_a2a_integration.py
- [[Terminates inbound A2A HTTP requests, enforces policy, forwards.      Usage]] - rationale - gateway/proxy/a2a_proxy.py
- [[TrustManager_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[Unambiguous malicious intent — immediate demotion, not a slow decay.]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[Upstream A2A Gap 78298 — SSRF Push-Notification Callback URL Bypass]] - concept - gateway/tests/test_a2a_integration.py
- [[Upstream A2A Gap 83701 — TaskContextId Collision Hijack]] - concept - gateway/tests/test_a2a_integration.py
- [[_StubForwarder_1]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[_jsonrpc()]] - code - gateway/tests/test_a2a_integration.py
- [[_jsonrpc()_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[alice legitimately creates a task; bob (a distinct, also-allowlisted     peer) a]] - rationale - gateway/tests/test_a2a_integration.py
- [[test_a2a_integration.py]] - code - gateway/tests/test_a2a_integration.py
- [[test_a2a_ssrf_callback_is_a_severe_violation_by_default()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_ssrf_callback_penalty_matches_malicious_intent_tier()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_task_ownership_violation_has_a_configured_penalty_heavier_than_generic_policy()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_trust_scoring.py]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_a2a_violation_types_exist()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_adversarial_ssrf_callback_bypass_attempts_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_adversarial_task_ownership_hijack_attempt_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_double_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_full_round_trip_allowed_request_reaches_the_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_full_round_trip_denied_request_never_reaches_the_peer()]] - code - gateway/tests/test_a2a_integration.py
- [[test_generic_denial_does_not_record_a2a_specific_violation_types()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_legitimate_callback_url_is_forwarded_over_real_http()]] - code - gateway/tests/test_a2a_integration.py
- [[test_proxy_without_trust_manager_does_not_raise()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_ssrf_callback_rejection_triggers_severe_demotion()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[test_task_ownership_violation_records_a2a_violation_type()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[trust_manager is an optional dependency — a proxy built without one     (e.g. be]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[trust_manager()]] - code - gateway/tests/test_a2a_integration.py
- [[trust_manager()_1]] - code - gateway/tests/test_a2a_trust_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_104
SORT file.name ASC
```

## Connections to other communities
- 35 edges to [[_COMMUNITY_Community 1001]]
- 26 edges to [[_COMMUNITY_Community 35]]
- 13 edges to [[_COMMUNITY_Community 107]]
- 7 edges to [[_COMMUNITY_Community 158]]
- 6 edges to [[_COMMUNITY_Community 82]]
- 1 edge to [[_COMMUNITY_Community 557]]

## Top bridge nodes
- [[A2AProxy]] - degree 38, connects to 4 communities
- [[A2APolicyConfig]] - degree 27, connects to 3 communities
- [[HermesA2AForwarder]] - degree 18, connects to 3 communities
- [[test_a2a_trust_scoring.py]] - degree 19, connects to 2 communities
- [[test_a2a_integration.py]] - degree 17, connects to 2 communities