---
type: community
cohesion: 0.05
members: 55
---

# A2AMethod

**Cohesion:** 0.05 - loosely connected
**Members:** 55 nodes

## Members
- [[NOTE gatewaysecurityegress_filter.py_is_private_ip has the same class]] - rationale - gateway/security/a2a_policy.py
- [[.__init__()_120]] - code - gateway/security/a2a_policy.py
- [[.__init__()_121]] - code - gateway/tests/test_a2a_policy.py
- [[.__post_init__()_3]] - code - gateway/security/a2a_policy.py
- [[._decide()]] - code - gateway/security/a2a_policy.py
- [[._tier_for()]] - code - gateway/security/a2a_policy.py
- [[.allowed()_1]] - code - gateway/security/a2a_policy.py
- [[.enforce()]] - code - gateway/security/a2a_policy.py
- [[.evaluate()]] - code - gateway/security/a2a_policy.py
- [[.from_dict()_2]] - code - gateway/security/a2a_policy.py
- [[.submit_tool_request()_2]] - code - gateway/tests/test_a2a_policy.py
- [[.test_bare_config_denies_every_peer()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_configured_allowlist_still_works_alongside_fail_closed_default()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_engine_constructed_with_no_config_at_all_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_from_dict_empty_dict_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_from_dict_none_is_fail_closed()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_invalid_default_action_string_falls_back_to_deny()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.test_owner_bypass_is_always_false_regardless_of_input()]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[.wait_for_decision()_2]] - code - gateway/tests/test_a2a_policy.py
- [[A duck-typed queue predating the ``force_tier`` kwarg — enforce() must     fall]] - rationale - gateway/tests/test_a2a_policy.py
- [[A typo'd default_action (e.g. 'allow-all') must not silently open         the ga]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2AMethod]] - code - gateway/security/a2a_policy.py
- [[A2APolicyAction]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig_1]] - code - gateway/tests/test_a2a_policy.py
- [[A2APolicyConfig]] - code - gateway/security/a2a_policy.py
- [[A2APolicyConfig() with no arguments — the shape a fresh deploy gets         if n]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[A2APolicyDecision]] - code - gateway/security/a2a_policy.py
- [[Accept either the enum or its string value (JSON-RPC payloads arrive     as plai]] - rationale - gateway/security/a2a_policy.py
- [[Any_41]] - code - gateway/security/a2a_policy.py
- [[Best-effort canonicalization of alternate IPv4 encodings that     ``ipaddress.ip]] - rationale - gateway/security/a2a_policy.py
- [[Canonical (v1.0 PascalCase) A2A JSON-RPC methods this engine governs.]] - rationale - gateway/security/a2a_policy.py
- [[Declarative A2A security policy.      Loaded from the ``a2a_policy`` section of]] - rationale - gateway/security/a2a_policy.py
- [[Evaluate a single A2A request. Pure — no IO, no side effects         beyond bes]] - rationale - gateway/security/a2a_policy.py
- [[Evaluate and resolve the decision to a terminal ALLOWDENY.          Identical f]] - rationale - gateway/security/a2a_policy.py
- [[Fail-closed-by-default must not mean impossible to allow anything         — an]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[IPv4Address]] - code - gateway/security/a2a_policy.py
- [[Normalize a peer-id reference for robust, evasion-resistant matching.      Same]] - rationale - gateway/security/a2a_policy.py
- [[Parse a policy config from a plain dict (e.g. loaded from YAML).]] - rationale - gateway/security/a2a_policy.py
- [[TestDefaultA2APolicyIsFailClosed]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[The result of evaluating a single A2A request against the policy.]] - rationale - gateway/security/a2a_policy.py
- [[The three terminal policy outcomes for an MCP tool call.]] - rationale - gateway/security/mcp_policy.py
- [[True only for a terminal ALLOW. REQUIRE_APPROVAL is not allowed on         its o]] - rationale - gateway/security/a2a_policy.py
- [[Unlike MCP, owner_bypass is not operator-configurable for A2A at         all — a]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[_BaseAddress]] - code - gateway/security/a2a_policy.py
- [[_LegacyStubApprovalQueue]] - code - gateway/tests/test_a2a_policy.py
- [[_address_is_public()]] - code - gateway/security/a2a_policy.py
- [[_canonicalize_ip_literal()]] - code - gateway/security/a2a_policy.py
- [[_int_to_ipv4()]] - code - gateway/security/a2a_policy.py
- [[_method_of()]] - code - gateway/security/a2a_policy.py
- [[_norm()]] - code - gateway/security/a2a_policy.py
- [[`A2APolicyEngine()` with no config argument — the laziest possible         call]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[a2a_policy.py]] - code - gateway/security/a2a_policy.py
- [[load_config-style callers pass whatever the YAML section resolved         to, wh]] - rationale - gateway/tests/test_a2a_policy_default_failclosed.py
- [[test_a2a_policy_default_failclosed.py]] - code - gateway/tests/test_a2a_policy_default_failclosed.py
- [[test_decision_allowed_property_only_true_for_terminal_allow()]] - code - gateway/tests/test_a2a_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AMethod
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_A2APolicyEngine]]
- 24 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 10 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 5 edges to [[_COMMUNITY_A2AProxyResult]]
- 5 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_record_decision]]
- 1 edge to [[_COMMUNITY_RovoBlast Attack (Atlassian Rovo AI)]]
- 1 edge to [[_COMMUNITY_cls]]
- 1 edge to [[_COMMUNITY_load_config()]]

## Top bridge nodes
- [[A2AMethod]] - degree 29, connects to 5 communities
- [[a2a_policy.py]] - degree 16, connects to 5 communities
- [[A2APolicyConfig]] - degree 27, connects to 4 communities
- [[A2APolicyAction]] - degree 13, connects to 2 communities
- [[_LegacyStubApprovalQueue]] - degree 11, connects to 2 communities