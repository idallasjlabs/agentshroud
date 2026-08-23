---
type: community
cohesion: 0.06
members: 63
---

# A2a Policy

**Cohesion:** 0.06 - loosely connected
**Members:** 63 nodes

## Members
- [[.__init__()_136]] - code - gateway/tests/test_a2a_policy.py
- [[.__init__()_135]] - code - gateway/tests/test_a2a_policy.py
- [[.submit_tool_request()_2]] - code - gateway/tests/test_a2a_policy.py
- [[.submit_tool_request()_1]] - code - gateway/tests/test_a2a_policy.py
- [[.wait_for_decision()_2]] - code - gateway/tests/test_a2a_policy.py
- [[.wait_for_decision()_1]] - code - gateway/tests/test_a2a_policy.py
- [[A 10-digit decimal string (matches the decimal-IPv4 pattern) whose     value exc]] - rationale - gateway/tests/test_a2a_policy.py
- [[A duck-typed queue predating the ``force_tier`` kwarg — enforce() must     fall]] - rationale - gateway/tests/test_a2a_policy.py
- [[A queue reporting requires_wait=False for a call the engine deemed     high-risk]] - rationale - gateway/tests/test_a2a_policy.py
- [[A task_id AgentShroud never saw created (e.g. the very first GetTask     against]] - rationale - gateway/tests/test_a2a_policy.py
- [[A2A peers are never equivalent to the human operator — unlike MCP,     owner_byp]] - rationale - gateway/tests/test_a2a_policy.py
- [[A2AMethod_1]] - code - gateway/tests/test_a2a_policy.py
- [[A2APolicyConfig_1]] - code - gateway/tests/test_a2a_policy.py
- [[A2APolicyEngine_2]] - code - gateway/tests/test_a2a_policy.py
- [[An operator who explicitly opts into default_action=allow gets normal     risk-t]] - rationale - gateway/tests/test_a2a_policy.py
- [[DNS rebinding a public-looking hostname that currently resolves to a     privat]] - rationale - gateway/tests/test_a2a_policy.py
- [[Hardened SSRF guard for A2A push-notification callback URLs.      Independent mi]] - rationale - gateway/security/a2a_policy.py
- [[Hostname resolution is mocked — this test asserts the validator's own     logic,]] - rationale - gateway/tests/test_a2a_policy.py
- [[Ownership is checked before the risk-tier gate — a mismatched peer must     be d]] - rationale - gateway/tests/test_a2a_policy.py
- [[Real JSON-RPC payloads deliver the method as a plain string — evaluate()     mus]] - rationale - gateway/tests/test_a2a_policy.py
- [[The `engine` fixture has no approval_queue configured at all — a     high-risk m]] - rationale - gateway/tests/test_a2a_policy.py
- [[Two allowlisted peers, one denylisted peer, default-deny for everyone else.]] - rationale - gateway/tests/test_a2a_policy.py
- [[_LegacyStubApprovalQueue]] - code - gateway/tests/test_a2a_policy.py
- [[_StubApprovalQueue]] - code - gateway/tests/test_a2a_policy.py
- [[_base_config()]] - code - gateway/tests/test_a2a_policy.py
- [[engine()]] - code - gateway/tests/test_a2a_policy.py
- [[is_safe_a2a_callback_url()]] - code - gateway/security/a2a_policy.py
- [[test_a2a_policy.py]] - code - gateway/tests/test_a2a_policy.py
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
- [[test_high_risk_methods_require_approval()]] - code - gateway/tests/test_a2a_policy.py
- [[test_low_risk_methods_are_allowed()]] - code - gateway/tests/test_a2a_policy.py
- [[test_medium_risk_methods_are_allowed()]] - code - gateway/tests/test_a2a_policy.py
- [[test_owner_bypass_defaults_false_and_does_not_bypass_a2a_high_risk()]] - code - gateway/tests/test_a2a_policy.py
- [[test_peer_cannot_access_another_peers_task()]] - code - gateway/tests/test_a2a_policy.py
- [[test_peer_cannot_cancel_another_peers_task()]] - code - gateway/tests/test_a2a_policy.py
- [[test_peer_cannot_subscribe_to_another_peers_task()]] - code - gateway/tests/test_a2a_policy.py
- [[test_set_push_notification_config_with_safe_callback_still_requires_approval()]] - code - gateway/tests/test_a2a_policy.py
- [[test_set_push_notification_config_with_unsafe_callback_is_denied_and_severe()]] - code - gateway/tests/test_a2a_policy.py
- [[test_task_creator_can_access_their_own_task()]] - code - gateway/tests/test_a2a_policy.py
- [[test_task_ownership_check_is_a_no_op_for_an_unknown_task_id()]] - code - gateway/tests/test_a2a_policy.py
- [[test_task_ownership_denial_is_not_bypassable_by_high_risk_approval_path()]] - code - gateway/tests/test_a2a_policy.py
- [[test_unknown_peer_is_denied_by_default()]] - code - gateway/tests/test_a2a_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2a_Policy
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_A2a Integration]]
- 17 edges to [[_COMMUNITY_A2a Policy (security)]]
- 6 edges to [[_COMMUNITY_A2a Policy Default Failclosed]]

## Top bridge nodes
- [[test_a2a_policy.py]] - degree 48, connects to 3 communities
- [[A2APolicyEngine_2]] - degree 31, connects to 3 communities
- [[_StubApprovalQueue]] - degree 13, connects to 3 communities
- [[_LegacyStubApprovalQueue]] - degree 11, connects to 3 communities
- [[A2AMethod_1]] - degree 8, connects to 3 communities