---
type: community
members: 50
---

# test_scanner_integration.py

**Members:** 50 nodes

## Members
- [[dot-test_baseline_at_least_two()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_baseline_three_when_openscap_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_baseline_three_without_daemon_config()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_defined_when_all_passing_no_report_on_disk()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_defined_when_oscap_binary_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_five_when_openscap_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_four_when_openscap_running_with_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_initial_when_not_run()_2]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_managed_when_has_criticals()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_managed_when_has_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_no_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_no_wazuh_no_fluent()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_optimizing_when_clean_zero_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_three_when_both_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_falco_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_wazuh_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_not_run()_1]] - code - gateway/tests/test_scanner_integration.py
- [[Any_70]] - code
- [[Score domain 10 Compliance Auditing (0-5). 0=not run, 2=has failures, 3=zero…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 12 Incident Response (0-5). 1=SOC exists, 2=Falco running,…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 4 Container Hardening (0-5). Baseline of 3 because docker-…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 5 Runtime Protection (0-5). 1=module exists, 2=running with…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 8 Secrets Management (0-5). 2=Docker secrets + key_vault…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 9 Logging & Monitoring (0-5). 1=SOC exists, 2=Wazuh running,…]] - rationale - gateway/security/scanner_integration.py
- [[TestScoreComplianceAuditing_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreContainerHardening_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreIncidentResponse_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreLoggingMonitoring_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreNetworkSegmentation_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreRuntimeProtection_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSecretsManagement_1]] - code - gateway/tests/test_scanner_integration.py
- [[Tests for gatewaysecurityscanner_integration.py — V9-T3 Scanner Aggregation.…]] - rationale - gateway/tests/test_scanner_integration.py
- [[_clamav_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_clamav_infected()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_openscap_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_openscap_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_openscap_warn()]] - code - gateway/tests/test_scanner_integration.py
- [[_score_compliance_auditing()]] - code - gateway/security/scanner_integration.py
- [[_score_container_hardening()]] - code - gateway/security/scanner_integration.py
- [[_score_incident_response()]] - code - gateway/security/scanner_integration.py
- [[_score_logging_monitoring()]] - code - gateway/security/scanner_integration.py
- [[_score_runtime_protection()]] - code - gateway/security/scanner_integration.py
- [[_score_secrets_management()]] - code - gateway/security/scanner_integration.py
- [[_trivy_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[test_scanner_integration.py]] - code - gateway/tests/test_scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_scanner_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_aggregate_results]]
- 16 edges to [[_COMMUNITY_compute_scorecard]]
- 12 edges to [[_COMMUNITY_scanner_integration.py]]
- 11 edges to [[_COMMUNITY_Any]]
- 8 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 8 edges to [[_COMMUNITY_get_trivy_image_summaries]]
- 6 edges to [[_COMMUNITY_get_trivy_summary]]
- 2 edges to [[_COMMUNITY__score_secure_development]]
- 2 edges to [[_COMMUNITY_get_wazuh_summary]]
- 2 edges to [[_COMMUNITY_generate_summary]]

## Top bridge nodes
- [[test_scanner_integration.py]] - degree 63, connects to 10 communities
- [[_score_compliance_auditing()]] - degree 10, connects to 4 communities
- [[_score_incident_response()]] - degree 9, connects to 3 communities
- [[_score_container_hardening()]] - degree 8, connects to 3 communities
- [[_score_logging_monitoring()]] - degree 8, connects to 3 communities
