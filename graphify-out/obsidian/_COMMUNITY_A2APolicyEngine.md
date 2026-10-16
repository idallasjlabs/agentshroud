---
type: community
cohesion: 0.09
members: 50
---

# A2APolicyEngine

**Cohesion:** 0.09 - loosely connected
**Members:** 50 nodes

## Members
- [[dot-__init__()_161]] - code - gateway/proxy/a2a_proxy.py
- [[dot-__init__()_162]] - code - gateway/proxy/a2a_proxy.py
- [[dot-__init__()_163]] - code - gateway/tests/test_a2a_integration.py
- [[dot-_handle()_1]] - code - gateway/tests/test_a2a_integration.py
- [[dot-close()_11]] - code - gateway/proxy/a2a_proxy.py
- [[dot-forward()]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[dot-parse_jsonrpc_request()]] - code - gateway/proxy/a2a_proxy.py
- [[A plain default-deny (unknownunlisted peer) is a routing decision, not     evid]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[A2APeerTestDouble]] - code - gateway/tests/test_a2a_integration.py
- [[A2APolicyEngine]] - code - gateway/proxy/a2a_proxy.py
- [[A2APolicyEngine_1]] - code - gateway/security/a2a_policy.py
- [[A2AProxy]] - code - gateway/proxy/a2a_proxy.py
- [[Decides allow  deny  require-approval for inbound A2A requests.      Usage]] - rationale - gateway/security/a2a_policy.py
- [[Hermes A2A Plugin Upstream Gaps (83701, 8053480779, 78298, 77872, 81042)]] - concept - docs/security/threat-model.md
- [[HermesA2AForwarder]] - code - gateway/proxy/a2a_proxy.py
- [[Minimal JSON-RPC 2.0 responder standing in for a real A2A peer.      Explicitly]] - rationale - gateway/tests/test_a2a_integration.py
- [[Negative control for the SSRF suite above — a genuinely public     callback URL]] - rationale - gateway/tests/test_a2a_integration.py
- [[Parse a JSON-RPC 2.0 A2A request body into methodtask_id         callback_url.]] - rationale - gateway/proxy/a2a_proxy.py
- [[ParsedA2ARequest]] - code - gateway/proxy/a2a_proxy.py
- [[Real HTTP forwarder to Hermes's internal A2A JSON-RPC listener.      Matches the]] - rationale - gateway/proxy/a2a_proxy.py
- [[Request_6]] - code - gateway/tests/test_a2a_integration.py
- [[Response_1]] - code - gateway/tests/test_a2a_integration.py
- [[Terminates inbound A2A HTTP requests, enforces policy, forwards.      Usage]] - rationale - gateway/proxy/a2a_proxy.py
- [[TrustManager_4]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[Upstream A2A Gap 78298 — SSRF Push-Notification Callback URL Bypass]] - concept - gateway/tests/test_a2a_integration.py
- [[Upstream A2A Gap 83701 — TaskContextId Collision Hijack]] - concept - gateway/tests/test_a2a_integration.py
- [[Upstream Hermes Gap 80534 — Peer Identity Resolved From SocketX-Forwarded-For Instead Of Bearer Token]] - concept - gateway/tests/test_a2a_proxy.py
- [[_StubForwarder]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[_jsonrpc()]] - code - gateway/tests/test_a2a_integration.py
- [[_jsonrpc()_1]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[a2a_proxy.py]] - code - gateway/proxy/a2a_proxy.py
- [[alice legitimately creates a task; bob (a distinct, also-allowlisted     peer) a]] - rationale - gateway/tests/test_a2a_integration.py
- [[test_a2a_integration.py]] - code - gateway/tests/test_a2a_integration.py
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
- [[trust_manager()_3]] - code - gateway/tests/test_a2a_integration.py
- [[trust_manager()_4]] - code - gateway/tests/test_a2a_trust_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2APolicyEngine
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_TrustConfig]]
- 15 edges to [[_COMMUNITY_A2AMethod]]
- 15 edges to [[_COMMUNITY_A2APolicyConfig]]
- 14 edges to [[_COMMUNITY_A2AProxyResult]]
- 14 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 10 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 8 edges to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_SubagentMonitor]]

## Top bridge nodes
- [[A2APolicyEngine_1]] - degree 58, connects to 6 communities
- [[A2AProxy]] - degree 37, connects to 4 communities
- [[test_a2a_trust_scoring.py]] - degree 19, connects to 3 communities
- [[HermesA2AForwarder]] - degree 18, connects to 3 communities
- [[test_a2a_integration.py]] - degree 17, connects to 3 communities
