---
type: community
cohesion: 0.12
members: 23
---

# A2AMethod

**Cohesion:** 0.12 - loosely connected
**Members:** 23 nodes

## Members
- [[NOTE gatewaysecurityegress_filter.py_is_private_ip has the same class]] - rationale - gateway/security/a2a_policy.py
- [[dot-__post_init__()_4]] - code - gateway/security/a2a_policy.py
- [[dot-_decide()]] - code - gateway/security/a2a_policy.py
- [[dot-_tier_for()]] - code - gateway/security/a2a_policy.py
- [[dot-enforce()]] - code - gateway/security/a2a_policy.py
- [[dot-evaluate()]] - code - gateway/security/a2a_policy.py
- [[A2AMethod]] - code - gateway/security/a2a_policy.py
- [[Accept either the enum or its string value (JSON-RPC payloads arrive     as plai]] - rationale - gateway/security/a2a_policy.py
- [[Best-effort canonicalization of alternate IPv4 encodings that     ``ipaddress.ip]] - rationale - gateway/security/a2a_policy.py
- [[Canonical (v1.0 PascalCase) A2A JSON-RPC methods this engine governs.]] - rationale - gateway/security/a2a_policy.py
- [[Ergonomic recorder for enforcement points — never raises.      ``sanitized=True`]] - rationale - gateway/security/module_stats.py
- [[Evaluate a single A2A request. Pure — no IO, no side effects         beyond bes]] - rationale - gateway/security/a2a_policy.py
- [[Evaluate and resolve the decision to a terminal ALLOWDENY.          Identical f]] - rationale - gateway/security/a2a_policy.py
- [[IPv4Address]] - code - gateway/security/a2a_policy.py
- [[Normalize a peer-id reference for robust, evasion-resistant matching.      Same]] - rationale - gateway/security/a2a_policy.py
- [[_BaseAddress]] - code - gateway/security/a2a_policy.py
- [[_address_is_public()]] - code - gateway/security/a2a_policy.py
- [[_canonicalize_ip_literal()]] - code - gateway/security/a2a_policy.py
- [[_int_to_ipv4()]] - code - gateway/security/a2a_policy.py
- [[_method_of()]] - code - gateway/security/a2a_policy.py
- [[_norm()]] - code - gateway/security/a2a_policy.py
- [[a2a_policy.py]] - code - gateway/security/a2a_policy.py
- [[record_decision()]] - code - gateway/security/module_stats.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AMethod
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_A2APolicyEngine]]
- 15 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 5 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 5 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 5 edges to [[_COMMUNITY_A2AProxyResult]]
- 4 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_Action]]
- 2 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 1 edge to [[_COMMUNITY_AgentShroud Docker Configuration]]
- 1 edge to [[_COMMUNITY_EgressAttempt]]
- 1 edge to [[_COMMUNITY_RovoBlast Attack (Atlassian Rovo AI)]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy._process]]

## Top bridge nodes
- [[record_decision()]] - degree 20, connects to 9 communities
- [[A2AMethod]] - degree 29, connects to 6 communities
- [[a2a_policy.py]] - degree 16, connects to 4 communities
- [[dot-evaluate()]] - degree 8, connects to 2 communities
- [[dot-_decide()]] - degree 6, connects to 2 communities
