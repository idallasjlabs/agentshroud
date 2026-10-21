---
type: community
members: 10
---

# Path (3)

**Members:** 10 nodes

## Members
- [[dot-test_all_mapped_layers_exist_in_registry()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[dot-test_proactive_only_layers_have_real_gateway_implementation()]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[Every layer the engine can emit must already be used by a mitigated entry in…]] - rationale - gateway/tests/test_triage_cve_mitigations.py
- [[Every name in _PROACTIVE_ONLY_LAYERS must be independently proven wired into…]] - rationale - gateway/tests/test_triage_cve_mitigations.py
- [[TestDefenseLayerVocabulary]] - code - gateway/tests/test_triage_cve_mitigations.py
- [[_AGENT_CVE_REGISTRIES]] - code - gateway/security/agent_cve_registry.py
- [[_HERMES_CVE_REGISTRY]] - code - gateway/security/agent_cve_registry.py
- [[_OPENCLAW_CVE_REGISTRY]] - code - gateway/security/agent_cve_registry.py
- [[test_no_entry_id_looks_like_a_cve]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_real_registry_plan_is_internally_consistent]] - code - gateway/tests/test_auto_remediate_cves.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Path_3
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Path]]
- 2 edges to [[_COMMUNITY_test_daily_cve_report.py (2)]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py]]
- 1 edge to [[_COMMUNITY_dot-_run_and_read]]
- 1 edge to [[_COMMUNITY_A2APolicyEngine]]
- 1 edge to [[_COMMUNITY_check_upstream_cves() (2)]]
- 1 edge to [[_COMMUNITY_api.py]]

## Top bridge nodes
- [[_AGENT_CVE_REGISTRIES]] - degree 8, connects to 5 communities
- [[TestDefenseLayerVocabulary]] - degree 5, connects to 2 communities
- [[_OPENCLAW_CVE_REGISTRY]] - degree 5, connects to 1 community
- [[dot-test_all_mapped_layers_exist_in_registry()]] - degree 3, connects to 1 community
- [[test_real_registry_plan_is_internally_consistent]] - degree 2, connects to 1 community
