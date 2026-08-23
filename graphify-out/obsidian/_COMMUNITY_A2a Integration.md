---
type: community
cohesion: 0.09
members: 53
---

# A2a Integration

**Cohesion:** 0.09 - loosely connected
**Members:** 53 nodes

## Members
- [[.__init__()_17]] - code - gateway/proxy/a2a_proxy.py
- [[.__init__()_18]] - code - gateway/proxy/a2a_proxy.py
- [[.__init__()_50]] - code - gateway/security/a2a_policy.py
- [[.__init__()_134]] - code - gateway/tests/test_a2a_integration.py
- [[._handle()_1]] - code - gateway/tests/test_a2a_integration.py
- [[.close()_7]] - code - gateway/proxy/a2a_proxy.py
- [[.forward()_3]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[.test_bare_config_denies_every_peer()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A plain default-deny (unknownunlisted peer) is a routing decision, not     evid]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[A2APeerTestDouble]] - code - gateway/tests/test_a2a_integration.py
- [[A2APolicyConfig]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig() with no arguments — the shape a fresh deploy gets         if n]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APolicyEngine]] - code - gateway/proxy/a2a_proxy.py
- [[A2APolicyEngine_1]] - code - gateway/security/a2a_policy.py
- [[A2AProxy]] - code - gateway/proxy/a2a_proxy.py
- [[Decides allow  deny  require-approval for inbound A2A requests.      Usage]] - rationale - gateway/security/a2a_policy.py
- [[Declarative A2A security policy.      Loaded from the ``a2a_policy`` section of]] - rationale - gateway/security/a2a_policy.py
- [[Hermes A2A Plugin Upstream Gaps (83701, 8053480779, 78298, 77872, 81042)]] - concept - docs/security/threat-model.md
- [[HermesA2AForwarder]] - code - gateway/proxy/a2a_proxy.py
- [[Minimal JSON-RPC 2.0 responder standing in for a real A2A peer.      Explicitly]] - rationale - gateway/tests/test_a2a_integration.py
- [[Negative control for the SSRF suite above — a genuinely public     callback URL]] - rationale - gateway/tests/test_a2a_integration.py
- [[ParsedA2ARequest]] - code - gateway/proxy/a2a_proxy.py
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
- [[a2a_proxy.py]] - code - gateway/proxy/a2a_proxy.py
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
- [[trust_manager()_1]] - code - gateway/tests/test_a2a_trust_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2a_Integration
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Progressive Trust Integration]]
- 18 edges to [[_COMMUNITY_A2a Policy]]
- 17 edges to [[_COMMUNITY_A2a Proxy (proxy)]]
- 17 edges to [[_COMMUNITY_A2a Proxy]]
- 14 edges to [[_COMMUNITY_A2a Policy (security)]]
- 10 edges to [[_COMMUNITY_A2a Policy Default Failclosed]]
- 9 edges to [[_COMMUNITY_Security Regressions V1 2]]
- 1 edge to [[_COMMUNITY_Subagent Monitor]]

## Top bridge nodes
- [[A2APolicyEngine_1]] - degree 58, connects to 6 communities
- [[A2AProxy]] - degree 38, connects to 5 communities
- [[A2APolicyConfig]] - degree 27, connects to 5 communities
- [[HermesA2AForwarder]] - degree 18, connects to 3 communities
- [[a2a_proxy.py]] - degree 10, connects to 3 communities