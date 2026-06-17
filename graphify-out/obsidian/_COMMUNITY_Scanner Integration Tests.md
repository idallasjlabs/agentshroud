---
type: community
cohesion: 0.06
members: 61
---

# Scanner Integration Tests

**Cohesion:** 0.06 - loosely connected
**Members:** 61 nodes

## Members
- [[.test_at_least_one()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_baseline_at_least_two()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_baseline_three_when_openscap_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_baseline_three_without_daemon_config()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_capped_at_five()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_defined_when_all_passing_no_report_on_disk()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_defined_when_oscap_binary_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_five_when_openscap_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_four_when_openscap_running_with_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_four_when_sbom_and_clean_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_initial_when_not_run()_1]] - code - gateway/tests/test_scanner_integration.py
- [[.test_managed_when_has_criticals()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_managed_when_has_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_one_when_no_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_one_when_no_wazuh_no_fluent()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_one_when_sbom_exists()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_optimizing_when_clean_zero_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_three_when_both_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_three_when_semgrep_and_precommit_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_two_when_falco_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_two_when_wazuh_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_zero_when_no_sbom_no_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_zero_when_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[Any_63]] - code - gateway/tests/test_scanner_integration.py
- [[Score domain 10 Compliance Auditing (0-5).      0=not run, 2=has failures, 3=ze]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 11 Secure Development (0-5).      1=Trivy in build, 2=semgrep conf]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 12 Incident Response (0-5).      1=SOC exists, 2=Falco running, 3=]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 1 Image Integrity (0-5).      1=SBOM exists, 2=Trivy ran, 3=zero c]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 4 Container Hardening (0-5).      Baseline of 3 because docker-com]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 5 Runtime Protection (0-5).      1=module exists, 2=running with c]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 9 Logging & Monitoring (0-5).      1=SOC exists, 2=Wazuh running,]] - rationale - gateway/security/scanner_integration.py
- [[TestScoreComplianceAuditing]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreContainerHardening]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreImageIntegrity]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreIncidentResponse]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreLoggingMonitoring]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreNetworkSegmentation]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreRuntimeProtection]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSecretsManagement]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSecureDevelopment]] - code - gateway/tests/test_scanner_integration.py
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
- [[_score_image_integrity()]] - code - gateway/security/scanner_integration.py
- [[_score_incident_response()]] - code - gateway/security/scanner_integration.py
- [[_score_logging_monitoring()]] - code - gateway/security/scanner_integration.py
- [[_score_runtime_protection()]] - code - gateway/security/scanner_integration.py
- [[_score_secure_development()]] - code - gateway/security/scanner_integration.py
- [[_trivy_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_trivy_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[_trivy_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[test_scanner_integration.py]] - code - gateway/tests/test_scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Scanner_Integration_Tests
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_Module Group 228]]
- 19 edges to [[_COMMUNITY_Module Group 134]]
- 16 edges to [[_COMMUNITY_Security Scanner Integration]]
- 9 edges to [[_COMMUNITY_Module Group 122]]
- 8 edges to [[_COMMUNITY_Module Group 210]]
- 4 edges to [[_COMMUNITY_Module Group 381]]
- 4 edges to [[_COMMUNITY_Module Group 269]]
- 4 edges to [[_COMMUNITY_Module Group 335]]
- 2 edges to [[_COMMUNITY_Module Group 437]]
- 2 edges to [[_COMMUNITY_Module Group 163]]

## Top bridge nodes
- [[test_scanner_integration.py]] - degree 61, connects to 10 communities
- [[_score_compliance_auditing()]] - degree 10, connects to 4 communities
- [[_score_image_integrity()]] - degree 10, connects to 4 communities
- [[_score_incident_response()]] - degree 10, connects to 3 communities
- [[_score_logging_monitoring()]] - degree 9, connects to 3 communities