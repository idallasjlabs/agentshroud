---
type: community
cohesion: 0.08
members: 59
---

# A2APolicyEngine

**Cohesion:** 0.08 - loosely connected
**Members:** 59 nodes

## Members
- [[.__init__()_76]] - code - gateway/proxy/a2a_proxy.py
- [[.__init__()_52]] - code - gateway/proxy/a2a_proxy.py
- [[.__init__()_53]] - code - gateway/tests/test_a2a_integration.py
- [[._handle()]] - code - gateway/tests/test_a2a_integration.py
- [[.close()_4]] - code - gateway/proxy/a2a_proxy.py
- [[.forward()_3]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[.get_next_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[.get_previous_trust_level()]] - code - gateway/security/progressive_trust_config.py
- [[.get_trust_level_order()]] - code - gateway/security/progressive_trust_config.py
- [[.is_tool_allowed()_1]] - code - gateway/security/progressive_trust_config.py
- [[A plain default-deny (unknownunlisted peer) is a routing decision, not     evid]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[A2APeerTestDouble]] - code - gateway/tests/test_a2a_integration.py
- [[A2APolicyEngine_2]] - code - gateway/proxy/a2a_proxy.py
- [[A2APolicyEngine_1]] - code - gateway/security/a2a_policy.py
- [[A2AProxy_1]] - code - gateway/proxy/a2a_proxy.py
- [[Check if a tool is allowed for the given trust level.]] - rationale - gateway/security/progressive_trust_config.py
- [[Configuration for the progressive trust system.]] - rationale - gateway/security/progressive_trust_config.py
- [[Decides allow  deny  require-approval for inbound A2A requests.      Usage]] - rationale - gateway/security/a2a_policy.py
- [[Get the next trust level for promotion, or None if already at max.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get the previous trust level for demotion, or None if already at min.]] - rationale - gateway/security/progressive_trust_config.py
- [[Get trust levels in ascending order.]] - rationale - gateway/security/progressive_trust_config.py
- [[Hermes A2A Plugin Upstream Gaps (83701, 8053480779, 78298, 77872, 81042)]] - concept - docs/security/threat-model.md
- [[HermesA2AForwarder]] - code - gateway/proxy/a2a_proxy.py
- [[Minimal JSON-RPC 2.0 responder standing in for a real A2A peer.      Explicitly]] - rationale - gateway/tests/test_a2a_integration.py
- [[Negative control for the SSRF suite above — a genuinely public     callback URL]] - rationale - gateway/tests/test_a2a_integration.py
- [[ParsedA2ARequest]] - code - gateway/proxy/a2a_proxy.py
- [[ProgressiveTrustConfig_1]] - code - gateway/security/progressive_trust_config.py
- [[Real HTTP forwarder to Hermes's internal A2A JSON-RPC listener.      Matches the]] - rationale - gateway/proxy/a2a_proxy.py
- [[Request_2]] - code - gateway/tests/test_a2a_integration.py
- [[Response_1]] - code - gateway/tests/test_a2a_integration.py
- [[Terminates inbound A2A HTTP requests, enforces policy, forwards.      Usage]] - rationale - gateway/proxy/a2a_proxy.py
- [[TrustManager_1]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[Unambiguous malicious intent — immediate demotion, not a slow decay.]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[Upstream A2A Gap 78298 — SSRF Push-Notification Callback URL Bypass]] - concept - gateway/tests/test_a2a_integration.py
- [[Upstream A2A Gap 83701 — TaskContextId Collision Hijack]] - concept - gateway/tests/test_a2a_integration.py
- [[_StubForwarder_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[_jsonrpc()_1]] - code - gateway/tests/test_a2a_integration.py
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
- [[trust_manager()]] - code - gateway/tests/test_a2a_integration.py
- [[trust_manager()_1]] - code - gateway/tests/test_a2a_trust_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2APolicyEngine
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_A2AMethod]]
- 16 edges to [[_COMMUNITY_A2AProxyResult]]
- 12 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 10 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 9 edges to [[_COMMUNITY_TrustManager]]
- 8 edges to [[_COMMUNITY_PipelineAction]]
- 5 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TestAuth]]
- 1 edge to [[_COMMUNITY_record_decision]]

## Top bridge nodes
- [[A2APolicyEngine_1]] - degree 58, connects to 5 communities
- [[A2AProxy_1]] - degree 38, connects to 5 communities
- [[a2a_proxy.py]] - degree 10, connects to 4 communities
- [[test_a2a_trust_scoring.py]] - degree 19, connects to 3 communities
- [[HermesA2AForwarder]] - degree 18, connects to 3 communities