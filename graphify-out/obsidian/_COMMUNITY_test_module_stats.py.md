---
type: community
members: 38
---

# test_module_stats.py

**Members:** 38 nodes

## Members
- [[dot-__init__()_111]] - code - gateway/security/module_stats.py
- [[dot-record()_2]] - code - gateway/security/module_stats.py
- [[dot-reset()]] - code - gateway/security/module_stats.py
- [[dot-setup_method()_20]] - code - gateway/tests/test_module_stats.py
- [[dot-setup_method()_21]] - code - gateway/tests/test_module_stats.py
- [[dot-snapshot()]] - code - gateway/security/module_stats.py
- [[dot-test_allowed_egress_counts_as_allowed()]] - code - gateway/tests/test_module_stats.py
- [[dot-test_denied_egress_counts_as_blocked()]] - code - gateway/tests/test_module_stats.py
- [[dot-test_record_decision_helper()]] - code - gateway/tests/test_module_stats.py
- [[dot-test_record_decision_never_raises()]] - code - gateway/tests/test_module_stats.py
- [[dot-test_tool_acl_can_use_tool_records()]] - code - gateway/tests/test_module_stats.py
- [[Decision]] - code - gateway/security/module_stats.py
- [[Enum_27]] - code
- [[Ergonomic recorder for enforcement points — never raises. ``sanitized=True``…]] - rationale - gateway/security/module_stats.py
- [[Live per-module enforcement counters (SCRUM-80). Feeds the SOC dashboard's per-…]] - rationale - gateway/security/module_stats.py
- [[ModuleStatsCollector]] - code - gateway/security/module_stats.py
- [[Record one enforcement decision for ``module``. Never raises an…]] - rationale - gateway/security/module_stats.py
- [[Return a per-module stats snapshot with totals and block rate.]] - rationale - gateway/security/module_stats.py
- [[SCRUM-80 F1 regression — a DENIED egress attempt must count as blocked. The…]] - rationale - gateway/tests/test_module_stats.py
- [[SCRUM-80 — the record helper + wrapped enforcement points feed real data.]] - rationale - gateway/tests/test_module_stats.py
- [[TestEgressWiringEndToEnd]] - code - gateway/tests/test_module_stats.py
- [[TestEnforcementWiring]] - code - gateway/tests/test_module_stats.py
- [[Tests for ModuleStatsCollector (SCRUM-80) — live per-module enforcement counts.]] - rationale - gateway/tests/test_module_stats.py
- [[Thread-safe per-module allowblocksanitize counters.]] - rationale - gateway/security/module_stats.py
- [[get_collector()]] - code - gateway/security/module_stats.py
- [[module_stats.py]] - code - gateway/security/module_stats.py
- [[record_decision()]] - code - gateway/security/module_stats.py
- [[str_11]] - code
- [[test_block_rate_computed()]] - code - gateway/tests/test_module_stats.py
- [[test_empty_module_zero_rate_not_division_error()]] - code - gateway/tests/test_module_stats.py
- [[test_module_stats.py]] - code - gateway/tests/test_module_stats.py
- [[test_record_and_snapshot()]] - code - gateway/tests/test_module_stats.py
- [[test_record_ignores_invalid_decision_safely()]] - code - gateway/tests/test_module_stats.py
- [[test_reset()]] - code - gateway/tests/test_module_stats.py
- [[test_sanitize_decision()]] - code - gateway/tests/test_module_stats.py
- [[test_thread_safe_under_concurrency()]] - code - gateway/tests/test_module_stats.py
- [[test_unknown_module_created_on_demand()]] - code - gateway/tests/test_module_stats.py
- [[worker()_1]] - code - gateway/tests/test_module_stats.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_module_statspy
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_EgressFilter]]
- 5 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 2 edges to [[_COMMUNITY_EgressAction]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_A2AProxy]]
- 2 edges to [[_COMMUNITY_A2APolicyEngine]]
- 2 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[record_decision()]] - degree 16, connects to 7 communities
- [[test_module_stats.py]] - degree 19, connects to 3 communities
- [[TestEgressWiringEndToEnd]] - degree 7, connects to 2 communities
- [[get_collector()]] - degree 11, connects to 1 community
- [[TestEnforcementWiring]] - degree 7, connects to 1 community
