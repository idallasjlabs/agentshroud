---
type: community
cohesion: 0.08
members: 33
---

# A2AMethod

**Cohesion:** 0.08 - loosely connected
**Members:** 33 nodes

## Members
- [[NOTE gatewaysecurityegress_filter.py_is_private_ip has the same class]] - rationale - gateway/security/a2a_policy.py
- [[dot-__post_init__()_2]] - code - gateway/security/a2a_policy.py
- [[dot-_decide()]] - code - gateway/security/a2a_policy.py
- [[dot-allowed()]] - code - gateway/security/a2a_policy.py
- [[dot-enforce()]] - code - gateway/security/a2a_policy.py
- [[dot-evaluate()]] - code - gateway/security/a2a_policy.py
- [[A2APolicyDecision]] - code - gateway/security/a2a_policy.py
- [[Accept either the enum or its string value (JSON-RPC payloads arrive     as plai]] - rationale - gateway/security/a2a_policy.py
- [[Best-effort canonicalization of alternate IPv4 encodings that     ``ipaddress.ip]] - rationale - gateway/security/a2a_policy.py
- [[Cross-Turn Correlation Capability]] - concept - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[EgressFilter.check()]] - code - gateway/security/egress_filter.py
- [[Evaluate a single A2A request. Pure — no IO, no side effects         beyond bes]] - rationale - gateway/security/a2a_policy.py
- [[Evaluate and resolve the decision to a terminal ALLOWDENY.          Identical f]] - rationale - gateway/security/a2a_policy.py
- [[IPv4Address]] - code - gateway/security/a2a_policy.py
- [[Normalize a peer-id reference for robust, evasion-resistant matching.      Same]] - rationale - gateway/security/a2a_policy.py
- [[OpenAI Agent Message-Board Coordination Attack]] - concept - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[PromptArmor Atlassian Rovo Content-Borne Injection Disclosure]] - document - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[RovoBlast Attack (Atlassian Rovo AI)]] - concept - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[The result of evaluating a single A2A request against the policy.]] - rationale - gateway/security/a2a_policy.py
- [[True only for a terminal ALLOW. REQUIRE_APPROVAL is not allowed on         its o]] - rationale - gateway/security/a2a_policy.py
- [[UK AISI Rogue Agent Actions Findings]] - concept - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[Varonis RovoBlast How One Click Triggered Atlassian's AI Assistant to Leak Data]] - document - docs/papers/attack-teardowns-rovoblast-cross-turn.md
- [[_BaseAddress]] - code - gateway/security/a2a_policy.py
- [[_address_is_public()]] - code - gateway/security/a2a_policy.py
- [[_canonicalize_ip_literal()]] - code - gateway/security/a2a_policy.py
- [[_int_to_ipv4()]] - code - gateway/security/a2a_policy.py
- [[_method_of()]] - code - gateway/security/a2a_policy.py
- [[_norm()]] - code - gateway/security/a2a_policy.py
- [[a2a_policy.py]] - code - gateway/security/a2a_policy.py
- [[context_guard.py Provenance Tagging (ContextSegment)]] - code - gateway/security/context_guard.py
- [[egress_filter.py_is_private_ip SSRF Encoding-Bypass Bug]] - rationale - gateway/security/egress_filter.py
- [[multi_turn_tracker.py  SubagentMonitor]] - code - gateway/security/multi_turn_tracker.py
- [[test_decision_allowed_property_only_true_for_terminal_allow()]] - code - gateway/tests/test_a2a_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AMethod
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_A2APolicyEngine]]
- 10 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 2 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 1 edge to [[_COMMUNITY_TestToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_DifferentialPIIDetector]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[a2a_policy.py]] - degree 16, connects to 4 communities
- [[A2APolicyDecision]] - degree 13, connects to 2 communities
- [[dot-evaluate()]] - degree 8, connects to 2 communities
- [[RovoBlast Attack (Atlassian Rovo AI)]] - degree 7, connects to 2 communities
- [[dot-_decide()]] - degree 6, connects to 2 communities
