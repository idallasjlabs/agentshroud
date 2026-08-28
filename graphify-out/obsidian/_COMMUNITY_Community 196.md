---
type: community
cohesion: 0.10
members: 36
---

# Community 196

**Cohesion:** 0.10 - loosely connected
**Members:** 36 nodes

## Members
- [[._patch_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_initial_when_not_run()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_managed_when_has_criticals()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_one_when_no_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_one_when_no_wazuh_no_fluent()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_optimizing_when_clean_zero_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_clean_when_all_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_critical_when_any_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_not_configured_when_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_warning_when_high_only()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_scanners_dict_has_all_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_three_when_both_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_timestamp_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_totals_sum_across_scanners()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_two_when_falco_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_two_when_wazuh_running()]] - code - gateway/tests/test_scanner_integration.py
- [[Aggregate results from all security scanners into a unified dict.      Returns]] - rationale - gateway/security/scanner_integration.py
- [[Any_58]] - code - gateway/security/scanner_integration.py
- [[Return Fluent Bit log collector status.      Fluent Bit is a log shipper, not a]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 12 Incident Response (0-5).      1=SOC exists, 2=Falco running, 3=]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 5 Runtime Protection (0-5).      1=module exists, 2=running with c]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 9 Logging & Monitoring (0-5).      1=SOC exists, 2=Wazuh running,]] - rationale - gateway/security/scanner_integration.py
- [[TestAggregateResults]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreIncidentResponse]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreLoggingMonitoring]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreRuntimeProtection]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_score_incident_response()]] - code - gateway/security/scanner_integration.py
- [[_score_logging_monitoring()]] - code - gateway/security/scanner_integration.py
- [[_score_runtime_protection()]] - code - gateway/security/scanner_integration.py
- [[_wazuh_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[aggregate_results()]] - code - gateway/security/scanner_integration.py
- [[get_fluent_bit_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_196
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_Community 187]]
- 13 edges to [[_COMMUNITY_Community 72]]
- 8 edges to [[_COMMUNITY_Community 201]]
- 4 edges to [[_COMMUNITY_Community 216]]
- 3 edges to [[_COMMUNITY_Community 539]]
- 2 edges to [[_COMMUNITY_Community 42]]
- 2 edges to [[_COMMUNITY_Community 983]]
- 2 edges to [[_COMMUNITY_Community 863]]
- 2 edges to [[_COMMUNITY_Community 183]]
- 1 edge to [[_COMMUNITY_Community 771]]
- 1 edge to [[_COMMUNITY_Community 399]]
- 1 edge to [[_COMMUNITY_SOC Collaborators]]

## Top bridge nodes
- [[Any_58]] - degree 22, connects to 11 communities
- [[aggregate_results()]] - degree 19, connects to 8 communities
- [[_score_incident_response()]] - degree 10, connects to 3 communities
- [[_score_logging_monitoring()]] - degree 9, connects to 3 communities
- [[_score_runtime_protection()]] - degree 8, connects to 3 communities