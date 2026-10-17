---
type: community
members: 44
---

# test_scanner_integration.py

**Members:** 44 nodes

## Members
- [[dot-test_at_least_one()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_baseline_at_least_two()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_capped_at_five()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_clean_tools_improve_score()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_four_when_sbom_and_clean_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_initial_when_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_managed_when_has_criticals()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_no_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_no_wazuh_no_fluent()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_sbom_exists()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_optimizing_when_clean_zero_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_clean_when_all_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_three_when_both_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_three_when_semgrep_and_precommit_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_falco_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_wazuh_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_no_sbom_no_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[Any_19]] - code - gateway/tests/test_scanner_integration.py
- [[Score domain 11 Secure Development (0-5).      1=Trivy in build, 2=semgrep conf]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 12 Incident Response (0-5).      1=SOC exists, 2=Falco running, 3=]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 1 Image Integrity (0-5).      1=SBOM exists, 2=Trivy ran, 3=zero c]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 5 Runtime Protection (0-5).      1=module exists, 2=running with c]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 9 Logging & Monitoring (0-5).      1=SOC exists, 2=Wazuh running,]] - rationale - gateway/security/scanner_integration.py
- [[TestScoreImageIntegrity]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreIncidentResponse_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreLoggingMonitoring]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreRuntimeProtection_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSecretsManagement]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSecureDevelopment]] - code - gateway/tests/test_scanner_integration.py
- [[_clamav_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[_falco_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_openscap_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_score_image_integrity()]] - code - gateway/security/scanner_integration.py
- [[_score_incident_response()]] - code - gateway/security/scanner_integration.py
- [[_score_logging_monitoring()]] - code - gateway/security/scanner_integration.py
- [[_score_runtime_protection()]] - code - gateway/security/scanner_integration.py
- [[_score_secure_development()]] - code - gateway/security/scanner_integration.py
- [[_trivy_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_trivy_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[test_scanner_integration.py]] - code - gateway/tests/test_scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_scanner_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_test_collaborator_greeter.py (2)]]
- 14 edges to [[_COMMUNITY_AgentTarget (4)]]
- 14 edges to [[_COMMUNITY_scanner_integration.py]]
- 12 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 10 edges to [[_COMMUNITY_test_scanner_integration.py (2)]]
- 8 edges to [[_COMMUNITY_Path (3)]]
- 6 edges to [[_COMMUNITY_get_trivy_summary]]
- 4 edges to [[_COMMUNITY__load_latest_json]]

## Top bridge nodes
- [[test_scanner_integration.py]] - degree 61, connects to 8 communities
- [[_score_image_integrity()]] - degree 10, connects to 4 communities
- [[Any_19]] - degree 16, connects to 3 communities
- [[_score_incident_response()]] - degree 10, connects to 3 communities
- [[_score_logging_monitoring()]] - degree 9, connects to 3 communities
