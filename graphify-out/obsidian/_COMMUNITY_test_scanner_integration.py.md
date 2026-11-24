---
type: community
members: 34
---

# test_scanner_integration.py

**Members:** 34 nodes

## Members
- [[dot-test_at_least_one()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_baseline_at_least_two()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_initial_when_not_run()_2]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_managed_when_has_criticals()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_no_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_no_wazuh_no_fluent()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_optimizing_when_clean_zero_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_three_when_both_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_three_when_semgrep_and_precommit_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_falco_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_wazuh_running()]] - code - gateway/tests/test_scanner_integration.py
- [[Score domain 11 Secure Development (0-5). 1=Trivy in build, 2=semgrep config,…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 12 Incident Response (0-5). 1=SOC exists, 2=Falco running,…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 5 Runtime Protection (0-5). 1=module exists, 2=running with…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 8 Secrets Management (0-5). 2=Docker secrets + key_vault…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 9 Logging & Monitoring (0-5). 1=SOC exists, 2=Wazuh running,…]] - rationale - gateway/security/scanner_integration.py
- [[TestScoreIncidentResponse_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreLoggingMonitoring_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreRuntimeProtection_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSecretsManagement_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSecureDevelopment_1]] - code - gateway/tests/test_scanner_integration.py
- [[Tests for gatewaysecurityscanner_integration.py — V9-T3 Scanner Aggregation.…]] - rationale - gateway/tests/test_scanner_integration.py
- [[_falco_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_score_incident_response()]] - code - gateway/security/scanner_integration.py
- [[_score_logging_monitoring()]] - code - gateway/security/scanner_integration.py
- [[_score_runtime_protection()]] - code - gateway/security/scanner_integration.py
- [[_score_secrets_management()]] - code - gateway/security/scanner_integration.py
- [[_score_secure_development()]] - code - gateway/security/scanner_integration.py
- [[_wazuh_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[path_factory()]] - code - gateway/tests/test_scanner_integration.py
- [[test_scanner_integration.py]] - code - gateway/tests/test_scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_scanner_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_scanner_integration.py]]
- 12 edges to [[_COMMUNITY_compute_scorecard]]
- 11 edges to [[_COMMUNITY_Any_1]]
- 10 edges to [[_COMMUNITY_Any]]
- 7 edges to [[_COMMUNITY__score_compliance_auditing]]
- 7 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 4 edges to [[_COMMUNITY_get_sbom]]
- 4 edges to [[_COMMUNITY__score_image_integrity]]
- 4 edges to [[_COMMUNITY_get_trivy_summary]]
- 2 edges to [[_COMMUNITY_get_falco_summary]]
- 2 edges to [[_COMMUNITY_get_wazuh_summary]]

## Top bridge nodes
- [[test_scanner_integration.py]] - degree 63, connects to 11 communities
- [[_score_incident_response()]] - degree 9, connects to 3 communities
- [[_score_logging_monitoring()]] - degree 8, connects to 3 communities
- [[_score_runtime_protection()]] - degree 8, connects to 3 communities
- [[_falco_clean()]] - degree 7, connects to 3 communities
