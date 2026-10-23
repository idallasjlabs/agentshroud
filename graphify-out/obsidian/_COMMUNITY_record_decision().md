---
type: community
cohesion: 0.07
members: 36
---

# record_decision()

**Cohesion:** 0.07 - loosely connected
**Members:** 36 nodes

## Members
- [[NOTE gatewaysecurityegress_filter.py_is_private_ip has the same class]] - rationale - gateway/security/a2a_policy.py
- [[dot-__post_init__()_5]] - code - gateway/security/a2a_policy.py
- [[dot-_decide()]] - code - gateway/security/a2a_policy.py
- [[dot-_tier_for()]] - code - gateway/security/a2a_policy.py
- [[dot-allowed()]] - code - gateway/security/a2a_policy.py
- [[dot-enforce()]] - code - gateway/security/a2a_policy.py
- [[dot-evaluate()]] - code - gateway/security/a2a_policy.py
- [[A2APolicyDecision]] - code - gateway/security/a2a_policy.py
- [[Accept either the enum or its string value (JSON-RPC payloads arrive     as plai]] - rationale - gateway/security/a2a_policy.py
- [[Best-effort canonicalization of alternate IPv4 encodings that     ``ipaddress.ip]] - rationale - gateway/security/a2a_policy.py
- [[Ergonomic recorder for enforcement points — never raises.      ``sanitized=True`]] - rationale - gateway/security/module_stats.py
- [[Evaluate a single A2A request. Pure — no IO, no side effects         beyond bes]] - rationale - gateway/security/a2a_policy.py
- [[Evaluate and resolve the decision to a terminal ALLOWDENY.          Identical f]] - rationale - gateway/security/a2a_policy.py
- [[GHSA-58qx-6m8p-wh2j — Slack group DMs skip sender allowlists]] - document - gateway/security/tool_acl.py
- [[GHSA-7cp7-87pj-p32v — skill dispatch skips owner-only policy]] - document - gateway/security/tool_acl.py
- [[GHSA-hpg5-cq3m-phqp — agent cron tool reaches operator command jobs]] - document - gateway/security/tool_acl.py
- [[GHSA-rrxp-5mx8-mvhh — inbound voice calls inherit owner tool authorization]] - document - gateway/security/tool_acl.py
- [[GHSA-wwcw-jfpp-gpxw — native tools ignore per-chat policy]] - document - gateway/security/tool_acl.py
- [[Hermes A2A Plugin Upstream Gaps (83701, 8053480779, 78298, 77872, 81042)]] - concept - docs/security/threat-model.md
- [[IPv4Address]] - code - gateway/security/a2a_policy.py
- [[Normalize a peer-id reference for robust, evasion-resistant matching.      Same]] - rationale - gateway/security/a2a_policy.py
- [[Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)]] - rationale - gateway/security/tool_acl.py
- [[The result of evaluating a single A2A request against the policy.]] - rationale - gateway/security/a2a_policy.py
- [[ToolACLEnforcer.can_use_tool]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool_in_group_context]] - code - gateway/security/tool_acl.py
- [[True only for a terminal ALLOW. REQUIRE_APPROVAL is not allowed on         its o]] - rationale - gateway/security/a2a_policy.py
- [[_BaseAddress]] - code - gateway/security/a2a_policy.py
- [[_address_is_public()]] - code - gateway/security/a2a_policy.py
- [[_canonicalize_ip_literal()]] - code - gateway/security/a2a_policy.py
- [[_int_to_ipv4()]] - code - gateway/security/a2a_policy.py
- [[_method_of()]] - code - gateway/security/a2a_policy.py
- [[_norm()]] - code - gateway/security/a2a_policy.py
- [[a2a_policy.py]] - code - gateway/security/a2a_policy.py
- [[can_use_tool_from_origin]] - code - gateway/security/tool_acl.py
- [[record_decision()]] - code - gateway/security/module_stats.py
- [[test_decision_allowed_property_only_true_for_terminal_allow()]] - code - gateway/tests/test_a2a_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/record_decision
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_hermesskillsi-bsREADME]]
- 7 edges to [[_COMMUNITY_UserSessionManager (2)]]
- 6 edges to [[_COMMUNITY_UserSessionManager]]
- 5 edges to [[_COMMUNITY_A2APolicyConfig]]
- 4 edges to [[_COMMUNITY_ModuleStatsCollector]]
- 2 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_dot-can_use_tool()]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY_TestMultilingualInjection]]
- 1 edge to [[_COMMUNITY_Security Module Inventory]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (2)]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_hermes_model_resolver.py (2)]]

## Top bridge nodes
- [[record_decision()]] - degree 20, connects to 9 communities
- [[a2a_policy.py]] - degree 16, connects to 6 communities
- [[dot-_decide()]] - degree 6, connects to 3 communities
- [[A2APolicyDecision]] - degree 13, connects to 2 communities
- [[can_use_tool_from_origin]] - degree 5, connects to 2 communities
