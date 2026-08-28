---
type: community
cohesion: 0.06
members: 64
---

# Community 81

**Cohesion:** 0.06 - loosely connected
**Members:** 64 nodes

## Members
- [[.__init__()_18]] - code - gateway/proxy/a2a_proxy.py
- [[.__init__()_50]] - code - gateway/security/a2a_policy.py
- [[.__init__()_134]] - code - gateway/tests/test_a2a_integration.py
- [[._handle()_1]] - code - gateway/tests/test_a2a_integration.py
- [[.close()_7]] - code - gateway/proxy/a2a_proxy.py
- [[.forward()_3]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[.from_dict()_2]] - code - gateway/security/a2a_policy.py
- [[.test_bare_config_denies_every_peer()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_configured_allowlist_still_works_alongside_fail_closed_default()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_engine_constructed_with_no_config_at_all_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_from_dict_empty_dict_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_from_dict_none_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_invalid_default_action_string_falls_back_to_deny()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_owner_bypass_is_always_false_regardless_of_input()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A plain default-deny (unknownunlisted peer) is a routing decision, not     evid]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[A typo'd default_action (e.g. 'allow-all') must not silently open         the ga]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APeerTestDouble]] - code - gateway/tests/test_a2a_integration.py
- [[A2APolicyAction]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig() with no arguments — the shape a fresh deploy gets         if n]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APolicyEngine_1]] - code - gateway/security/a2a_policy.py
- [[Any_29]] - code - gateway/security/a2a_policy.py
- [[Decides allow  deny  require-approval for inbound A2A requests.      Usage]] - rationale - gateway/security/a2a_policy.py
- [[Declarative A2A security policy.      Loaded from the ``a2a_policy`` section of]] - rationale - gateway/security/a2a_policy.py
- [[Fail-closed-by-default must not mean impossible to allow anything         — an]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[HermesA2AForwarder]] - code - gateway/proxy/a2a_proxy.py
- [[Minimal JSON-RPC 2.0 responder standing in for a real A2A peer.      Explicitly]] - rationale - gateway/tests/test_a2a_integration.py
- [[Negative control for the SSRF suite above — a genuinely public     callback URL]] - rationale - gateway/tests/test_a2a_integration.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML).]] - rationale - gateway/security/a2a_policy.py
- [[Real HTTP forwarder to Hermes's internal A2A JSON-RPC listener.      Matches the]] - rationale - gateway/proxy/a2a_proxy.py
- [[Request_8]] - code - gateway/tests/test_a2a_integration.py
- [[Response_1]] - code - gateway/tests/test_a2a_integration.py
- [[TestDefaultA2APolicyIsFailClosed]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[The three terminal policy outcomes for an MCP tool call.]] - rationale - gateway/security/mcp_policy.py
- [[TrustManager_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[Unambiguous malicious intent — immediate demotion, not a slow decay.]] - rationale - gateway/tests/test_a2a_trust_scoring.py
- [[Unlike MCP, owner_bypass is not operator-configurable for A2A at         all — a]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[Upstream A2A Gap 78298 — SSRF Push-Notification Callback URL Bypass]] - concept - gateway/tests/test_a2a_integration.py
- [[Upstream A2A Gap 83701 — TaskContextId Collision Hijack]] - concept - gateway/tests/test_a2a_integration.py
- [[_StubForwarder_1]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[_jsonrpc()]] - code - gateway/tests/test_a2a_integration.py
- [[_jsonrpc()_2]] - code - gateway/tests/test_a2a_trust_scoring.py
- [[`A2APolicyEngine()` with no config argument — the laziest possible         call]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[alice legitimately creates a task; bob (a distinct, also-allowlisted     peer) a]] - rationale - gateway/tests/test_a2a_integration.py
- [[load_config-style callers pass whatever the YAML section resolved         to, wh]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[test_a2a_integration.py]] - code - gateway/tests/test_a2a_integration.py
- [[test_a2a_policy_default_failclosed.py]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
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
TABLE source_file, type FROM #community/Community_81
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_Community 205]]
- 24 edges to [[_COMMUNITY_Community 71]]
- 23 edges to [[_COMMUNITY_Progressive Trust]]
- 11 edges to [[_COMMUNITY_Community 110]]
- 7 edges to [[_COMMUNITY_Community 281]]
- 2 edges to [[_COMMUNITY_Community 19]]
- 1 edge to [[_COMMUNITY_Community 553]]
- 1 edge to [[_COMMUNITY_Community 97]]
- 1 edge to [[_COMMUNITY_Community 33]]

## Top bridge nodes
- [[A2APolicyEngine_1]] - degree 58, connects to 5 communities
- [[A2APolicyConfig]] - degree 27, connects to 4 communities
- [[A2APolicyAction]] - degree 13, connects to 3 communities
- [[test_a2a_trust_scoring.py]] - degree 19, connects to 2 communities
- [[HermesA2AForwarder]] - degree 18, connects to 2 communities