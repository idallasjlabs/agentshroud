---
type: community
members: 56
---

# Community 300

**Members:** 56 nodes

## Members
- [[.__init__()_114]] - code - gateway/security/module_stats.py
- [[.can_use_tool()]] - code - gateway/security/tool_acl.py
- [[.can_use_tool_from_origin()]] - code - gateway/security/tool_acl.py
- [[.can_use_tool_in_group_context()]] - code - gateway/security/tool_acl.py
- [[.record()_2]] - code - gateway/security/module_stats.py
- [[.reset()_1]] - code - gateway/security/module_stats.py
- [[.setup_method()_13]] - code - gateway/tests/test_module_stats.py
- [[.setup_method()_14]] - code - gateway/tests/test_module_stats.py
- [[.snapshot()]] - code - gateway/security/module_stats.py
- [[.test_allowed_egress_counts_as_allowed()]] - code - gateway/tests/test_module_stats.py
- [[.test_denied_egress_counts_as_blocked()]] - code - gateway/tests/test_module_stats.py
- [[.test_record_decision_helper()]] - code - gateway/tests/test_module_stats.py
- [[.test_record_decision_never_raises()]] - code - gateway/tests/test_module_stats.py
- [[.test_tool_acl_can_use_tool_records()]] - code - gateway/tests/test_module_stats.py
- [[A2AGovernanceProxy._check_peer]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._process]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy._sanitize_message]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_inbound]] - code - gateway/security/a2a_governance.py
- [[A2AGovernanceProxy.process_outbound]] - code - gateway/security/a2a_governance.py
- [[Authorize a tool call, refusing owner elevation over an unverified origin.]] - rationale - gateway/security/tool_acl.py
- [[Check whether user_id may invoke tool_name when acting inside a group workspace.]] - rationale - gateway/security/tool_acl.py
- [[Decision]] - code - gateway/security/module_stats.py
- [[Ergonomic recorder for enforcement points — never raises.      ``sanitized=True`]] - rationale - gateway/security/module_stats.py
- [[GHSA-58qx-6m8p-wh2j — Slack group DMs skip sender allowlists]] - document - gateway/security/tool_acl.py
- [[GHSA-7cp7-87pj-p32v — skill dispatch skips owner-only policy]] - document - gateway/security/tool_acl.py
- [[GHSA-hpg5-cq3m-phqp — agent cron tool reaches operator command jobs]] - document - gateway/security/tool_acl.py
- [[GHSA-rrxp-5mx8-mvhh — inbound voice calls inherit owner tool authorization]] - document - gateway/security/tool_acl.py
- [[GHSA-wwcw-jfpp-gpxw — native tools ignore per-chat policy]] - document - gateway/security/tool_acl.py
- [[ModuleStatsCollector]] - code - gateway/security/module_stats.py
- [[Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)]] - rationale - gateway/security/tool_acl.py
- [[Public entry — records the decision for the SOC heat-map (SCRUM-80),         the_1]] - rationale - gateway/security/tool_acl.py
- [[Record one enforcement decision for ``module``.          Never raises an unknow]] - rationale - gateway/security/module_stats.py
- [[Return a per-module stats snapshot with totals and block rate.]] - rationale - gateway/security/module_stats.py
- [[SCRUM-80 F1 regression — a DENIED egress attempt must count as blocked.      The]] - rationale - gateway/tests/test_module_stats.py
- [[SCRUM-80 — the record helper + wrapped enforcement points feed real data.]] - rationale - gateway/tests/test_module_stats.py
- [[TestEgressWiringEndToEnd]] - code - gateway/tests/test_module_stats.py
- [[TestEnforcementWiring]] - code - gateway/tests/test_module_stats.py
- [[Thread-safe per-module allowblocksanitize counters.]] - rationale - gateway/security/module_stats.py
- [[ToolACLEnforcer._can_use_tool_impl]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool]] - code - gateway/security/tool_acl.py
- [[ToolACLEnforcer.can_use_tool_in_group_context]] - code - gateway/security/tool_acl.py
- [[TrustManager.get_trust]] - code - gateway/security/trust_manager.py
- [[TrustManager.is_tool_allowed]] - code - gateway/security/trust_manager.py
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
TABLE source_file, type FROM #community/Community_300
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 11]]
- 6 edges to [[_COMMUNITY_Community 1119]]
- 3 edges to [[_COMMUNITY_Community 8]]
- 3 edges to [[_COMMUNITY_Community 17]]
- 2 edges to [[_COMMUNITY_Community 307]]
- 2 edges to [[_COMMUNITY_Community 221]]
- 2 edges to [[_COMMUNITY_Community 35]]
- 2 edges to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 73]]
- 1 edge to [[_COMMUNITY_Community 213]]
- 1 edge to [[_COMMUNITY_Community 6]]
- 1 edge to [[_COMMUNITY_Community 1566]]
- 1 edge to [[_COMMUNITY_Community 33]]

## Top bridge nodes
- [[record_decision()]] - degree 20, connects to 7 communities
- [[test_module_stats.py]] - degree 18, connects to 3 communities
- [[TestEnforcementWiring]] - degree 11, connects to 3 communities
- [[TestEgressWiringEndToEnd]] - degree 10, connects to 3 communities
- [[.can_use_tool()]] - degree 6, connects to 2 communities