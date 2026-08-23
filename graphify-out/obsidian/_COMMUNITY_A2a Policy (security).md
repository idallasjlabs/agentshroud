---
type: community
cohesion: 0.10
members: 29
---

# A2a Policy (security)

**Cohesion:** 0.10 - loosely connected
**Members:** 29 nodes

## Members
- [[NOTE gatewaysecurityegress_filter.py_is_private_ip has the same class]] - rationale - gateway/security/a2a_policy.py
- [[.__post_init__()_2]] - code - gateway/security/a2a_policy.py
- [[._decide()]] - code - gateway/security/a2a_policy.py
- [[._tier_for()]] - code - gateway/security/a2a_policy.py
- [[.allowed()]] - code - gateway/security/a2a_policy.py
- [[.enforce()]] - code - gateway/security/a2a_policy.py
- [[.evaluate()]] - code - gateway/security/a2a_policy.py
- [[A2AMethod]] - code - gateway/security/a2a_policy.py
- [[A2APolicyDecision]] - code - gateway/security/a2a_policy.py
- [[Accept either the enum or its string value (JSON-RPC payloads arrive     as plai]] - rationale - gateway/security/a2a_policy.py
- [[Best-effort canonicalization of alternate IPv4 encodings that     ``ipaddress.ip]] - rationale - gateway/security/a2a_policy.py
- [[Canonical (v1.0 PascalCase) A2A JSON-RPC methods this engine governs.]] - rationale - gateway/security/a2a_policy.py
- [[Ergonomic recorder for enforcement points — never raises.      ``sanitized=True`]] - rationale - gateway/security/module_stats.py
- [[Evaluate a single A2A request. Pure — no IO, no side effects         beyond bes]] - rationale - gateway/security/a2a_policy.py
- [[Evaluate and resolve the decision to a terminal ALLOWDENY.          Identical f]] - rationale - gateway/security/a2a_policy.py
- [[IPv4Address]] - code - gateway/security/a2a_policy.py
- [[Normalize a peer-id reference for robust, evasion-resistant matching.      Same]] - rationale - gateway/security/a2a_policy.py
- [[SOC Per-Module Enforcement Heat-Map (SCRUM-80)]] - document - docker/README.md
- [[The result of evaluating a single A2A request against the policy.]] - rationale - gateway/security/a2a_policy.py
- [[True only for a terminal ALLOW. REQUIRE_APPROVAL is not allowed on         its o]] - rationale - gateway/security/a2a_policy.py
- [[_BaseAddress]] - code - gateway/security/a2a_policy.py
- [[_address_is_public()]] - code - gateway/security/a2a_policy.py
- [[_canonicalize_ip_literal()]] - code - gateway/security/a2a_policy.py
- [[_int_to_ipv4()]] - code - gateway/security/a2a_policy.py
- [[_method_of()]] - code - gateway/security/a2a_policy.py
- [[_norm()]] - code - gateway/security/a2a_policy.py
- [[a2a_policy.py]] - code - gateway/security/a2a_policy.py
- [[record_decision()]] - code - gateway/security/module_stats.py
- [[test_decision_allowed_property_only_true_for_terminal_allow()]] - code - gateway/tests/test_a2a_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2a_Policy_security
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_A2a Policy]]
- 14 edges to [[_COMMUNITY_A2a Integration]]
- 5 edges to [[_COMMUNITY_A2a Proxy (proxy)]]
- 5 edges to [[_COMMUNITY_A2a Proxy]]
- 5 edges to [[_COMMUNITY_Module Stats]]
- 3 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 3 edges to [[_COMMUNITY_A2a Policy Default Failclosed]]
- 2 edges to [[_COMMUNITY_Mcp Policy]]
- 2 edges to [[_COMMUNITY_Tool ACL & Group RBAC]]
- 1 edge to [[_COMMUNITY_Attack Teardowns Rovoblast Cross (papers)]]
- 1 edge to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 1 edge to [[_COMMUNITY_Egress Filter (security)]]
- 1 edge to [[_COMMUNITY_Readme (docker)]]

## Top bridge nodes
- [[record_decision()]] - degree 17, connects to 7 communities
- [[A2AMethod]] - degree 29, connects to 6 communities
- [[a2a_policy.py]] - degree 16, connects to 5 communities
- [[._decide()]] - degree 6, connects to 2 communities
- [[A2APolicyDecision]] - degree 13, connects to 1 community