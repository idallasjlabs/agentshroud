---
type: community
cohesion: 0.08
members: 51
---

# test_scanner_integration.py

**Cohesion:** 0.08 - loosely connected
**Members:** 51 nodes

## Members
- [[._patch_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_baseline_at_least_two()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_baseline_three_without_daemon_config()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_capped_at_five()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_four_when_sbom_and_clean_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_initial_when_not_run()_2]] - code - gateway/tests/test_scanner_integration.py
- [[.test_managed_when_has_criticals()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_one_when_no_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_one_when_no_wazuh_no_fluent()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_one_when_sbom_exists()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_optimizing_when_clean_zero_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_clean_when_all_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_critical_when_any_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_not_configured_when_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_overall_warning_when_high_only()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_scanners_dict_has_all_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_three_when_both_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_timestamp_present()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_totals_sum_across_scanners()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_two_when_falco_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_two_when_wazuh_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_zero_when_no_sbom_no_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[Aggregate results from all security scanners into a unified dict.      Returns]] - rationale - gateway/security/scanner_integration.py
- [[Any_72]] - code - gateway/tests/test_scanner_integration.py
- [[Score domain 12 Incident Response (0-5).      1=SOC exists, 2=Falco running, 3=]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 1 Image Integrity (0-5).      1=SBOM exists, 2=Trivy ran, 3=zero c]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 5 Runtime Protection (0-5).      1=module exists, 2=running with c]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 9 Logging & Monitoring (0-5).      1=SOC exists, 2=Wazuh running,]] - rationale - gateway/security/scanner_integration.py
- [[TestAggregateResults_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreImageIntegrity_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreIncidentResponse_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreLoggingMonitoring_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreNetworkSegmentation_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreRuntimeProtection_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSecretsManagement_1]] - code - gateway/tests/test_scanner_integration.py
- [[_clamav_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_clamav_infected()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_score_image_integrity()]] - code - gateway/security/scanner_integration.py
- [[_score_incident_response()]] - code - gateway/security/scanner_integration.py
- [[_score_logging_monitoring()]] - code - gateway/security/scanner_integration.py
- [[_score_runtime_protection()]] - code - gateway/security/scanner_integration.py
- [[_trivy_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_trivy_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[_trivy_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[aggregate_results()]] - code - gateway/security/scanner_integration.py
- [[test_scanner_integration.py]] - code - gateway/tests/test_scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_scanner_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_compute_scorecard()]]
- 14 edges to [[_COMMUNITY_Any]]
- 13 edges to [[_COMMUNITY_scanner_integration.py]]
- 12 edges to [[_COMMUNITY__score_compliance_auditing()]]
- 10 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 8 edges to [[_COMMUNITY_Path]]
- 7 edges to [[_COMMUNITY_get_trivy_summary()]]
- 6 edges to [[_COMMUNITY_wazuh_client.py]]
- 2 edges to [[_COMMUNITY__score_secure_development()]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_test_soc_bots.py]]

## Top bridge nodes
- [[test_scanner_integration.py]] - degree 61, connects to 9 communities
- [[aggregate_results()]] - degree 19, connects to 6 communities
- [[_score_image_integrity()]] - degree 10, connects to 4 communities
- [[_score_incident_response()]] - degree 10, connects to 3 communities
- [[_score_logging_monitoring()]] - degree 9, connects to 3 communities