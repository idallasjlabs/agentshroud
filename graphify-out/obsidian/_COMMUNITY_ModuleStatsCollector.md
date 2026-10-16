---
type: community
cohesion: 0.10
members: 36
---

# ModuleStatsCollector

**Cohesion:** 0.10 - loosely connected
**Members:** 36 nodes

## Members
- [[dot-__init__()_98]] - code - gateway/security/module_stats.py
- [[dot-record()_2]] - code - gateway/security/module_stats.py
- [[dot-reset()_1]] - code - gateway/security/module_stats.py
- [[dot-setup_method()_22]] - code - gateway/tests/test_module_stats.py
- [[dot-setup_method()_23]] - code - gateway/tests/test_module_stats.py
- [[dot-snapshot()]] - code - gateway/security/module_stats.py
- [[dot-test_allowed_egress_counts_as_allowed()]] - code - gateway/tests/test_module_stats.py
- [[dot-test_denied_egress_counts_as_blocked()]] - code - gateway/tests/test_module_stats.py
- [[dot-test_record_decision_helper()]] - code - gateway/tests/test_module_stats.py
- [[dot-test_record_decision_never_raises()]] - code - gateway/tests/test_module_stats.py
- [[dot-test_tool_acl_can_use_tool_records()]] - code - gateway/tests/test_module_stats.py
- [[Decision_2]] - code - gateway/security/module_stats.py
- [[Ergonomic recorder for enforcement points — never raises.      ``sanitized=True`]] - rationale - gateway/security/module_stats.py
- [[ModuleStatsCollector]] - code - gateway/security/module_stats.py
- [[Record one enforcement decision for ``module``.          Never raises an unknow]] - rationale - gateway/security/module_stats.py
- [[Return a per-module stats snapshot with totals and block rate.]] - rationale - gateway/security/module_stats.py
- [[SCRUM-80 F1 regression — a DENIED egress attempt must count as blocked.      The]] - rationale - gateway/tests/test_module_stats.py
- [[SCRUM-80 — the record helper + wrapped enforcement points feed real data.]] - rationale - gateway/tests/test_module_stats.py
- [[TestEgressWiringEndToEnd]] - code - gateway/tests/test_module_stats.py
- [[TestEnforcementWiring]] - code - gateway/tests/test_module_stats.py
- [[Thread-safe per-module allowblocksanitize counters.]] - rationale - gateway/security/module_stats.py
- [[ToolACLEnforcer.can_use_tool]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool_in_group_context]] - code - gateway/security/tool_acl.py
- [[can_use_tool_from_origin]] - code - gateway/security/tool_acl.py
- [[get_collector()]] - code - gateway/security/module_stats.py
- [[module_stats.py]] - code - gateway/security/module_stats.py
- [[record_decision()]] - code - gateway/security/module_stats.py
- [[test_block_rate_computed()]] - code - gateway/tests/test_module_stats.py
- [[test_empty_module_zero_rate_not_division_error()]] - code - gateway/tests/test_module_stats.py
- [[test_module_stats.py]] - code - gateway/tests/test_module_stats.py
- [[test_record_and_snapshot()]] - code - gateway/tests/test_module_stats.py
- [[test_record_ignores_invalid_decision_safely()]] - code - gateway/tests/test_module_stats.py
- [[test_reset()]] - code - gateway/tests/test_module_stats.py
- [[test_sanitize_decision()]] - code - gateway/tests/test_module_stats.py
- [[test_thread_safe_under_concurrency()]] - code - gateway/tests/test_module_stats.py
- [[test_unknown_module_created_on_demand()]] - code - gateway/tests/test_module_stats.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ModuleStatsCollector
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_RBACConfig_1]]
- 8 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_A2AMethod_1]]
- 2 edges to [[_COMMUNITY_A2APolicyEngine_1]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_AgentShroud Docker Configuration]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig_1]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_GitHub Copilot CLI Setup Guide_1]]
- 1 edge to [[_COMMUNITY_ModuleStatsCollector_1]]

## Top bridge nodes
- [[record_decision()]] - degree 20, connects to 8 communities
- [[test_module_stats.py]] - degree 18, connects to 2 communities
- [[TestEnforcementWiring]] - degree 11, connects to 2 communities
- [[TestEgressWiringEndToEnd]] - degree 10, connects to 2 communities
- [[Decision_2]] - degree 7, connects to 2 communities
