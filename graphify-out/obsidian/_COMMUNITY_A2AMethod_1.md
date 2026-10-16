---
type: community
cohesion: 0.11
members: 26
---

# A2AMethod

**Cohesion:** 0.11 - loosely connected
**Members:** 26 nodes

## Members
- [[NOTE gatewaysecurityegress_filter.py_is_private_ip has the same class]] - rationale - gateway/security/a2a_policy.py
- [[dot-__post_init__()_1]] - code - gateway/security/a2a_policy.py
- [[dot-_decide()]] - code - gateway/security/a2a_policy.py
- [[dot-_tier_for()]] - code - gateway/security/a2a_policy.py
- [[dot-allowed()]] - code - gateway/security/a2a_policy.py
- [[dot-enforce()]] - code - gateway/security/a2a_policy.py
- [[dot-evaluate()]] - code - gateway/security/a2a_policy.py
- [[A2AMethod]] - code - gateway/security/a2a_policy.py
- [[A2APolicyDecision]] - code - gateway/security/a2a_policy.py
- [[Accept either the enum or its string value (JSON-RPC payloads arrive     as plai]] - rationale - gateway/security/a2a_policy.py
- [[Best-effort canonicalization of alternate IPv4 encodings that     ``ipaddress.ip]] - rationale - gateway/security/a2a_policy.py
- [[Canonical (v1.0 PascalCase) A2A JSON-RPC methods this engine governs.]] - rationale - gateway/security/a2a_policy.py
- [[Evaluate a single A2A request. Pure — no IO, no side effects         beyond bes]] - rationale - gateway/security/a2a_policy.py
- [[Evaluate and resolve the decision to a terminal ALLOWDENY.          Identical f]] - rationale - gateway/security/a2a_policy.py
- [[IPv4Address]] - code - gateway/security/a2a_policy.py
- [[Normalize a peer-id reference for robust, evasion-resistant matching.      Same]] - rationale - gateway/security/a2a_policy.py
- [[The result of evaluating a single A2A request against the policy.]] - rationale - gateway/security/a2a_policy.py
- [[True only for a terminal ALLOW. REQUIRE_APPROVAL is not allowed on         its o]] - rationale - gateway/security/a2a_policy.py
- [[_BaseAddress]] - code - gateway/security/a2a_policy.py
- [[_address_is_public()]] - code - gateway/security/a2a_policy.py
- [[_canonicalize_ip_literal()]] - code - gateway/security/a2a_policy.py
- [[_int_to_ipv4()]] - code - gateway/security/a2a_policy.py
- [[_method_of()]] - code - gateway/security/a2a_policy.py
- [[_norm()]] - code - gateway/security/a2a_policy.py
- [[a2a_policy.py]] - code - gateway/security/a2a_policy.py
- [[test_decision_allowed_property_only_true_for_terminal_allow()]] - code - gateway/tests/test_a2a_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AMethod
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 14 edges to [[_COMMUNITY_A2APolicyEngine_1]]
- 6 edges to [[_COMMUNITY_A2APolicyEngine]]
- 5 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 2 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_A2AMethod]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[A2AMethod]] - degree 29, connects to 6 communities
- [[a2a_policy.py]] - degree 16, connects to 6 communities
- [[dot-evaluate()]] - degree 8, connects to 2 communities
- [[dot-_decide()]] - degree 6, connects to 2 communities
- [[A2APolicyDecision]] - degree 13, connects to 1 community
