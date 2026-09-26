---
type: community
cohesion: 0.08
members: 54
---

# A2AMethod

**Cohesion:** 0.08 - loosely connected
**Members:** 54 nodes

## Members
- [[.test_baseline_three_when_openscap_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_capped_at_five()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_clean_tools_improve_score()]] - code - gateway/tests/test_scanner_integration.py
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
- [[.test_overall_clean_when_all_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_three_when_both_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_two_when_falco_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_two_when_wazuh_running()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_zero_when_no_sbom_no_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_zero_when_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[Any_70]] - code - gateway/tests/test_scanner_integration.py
- [[Score domain 10 Compliance Auditing (0-5).      0=not run, 2=has failures, 3=ze]] - rationale - gateway/security/scanner_integration.py
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
- [[TestScoreRuntimeProtection]] - code - gateway/tests/test_scanner_integration.py
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
- [[_trivy_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_trivy_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[_trivy_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_wazuh_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[test_scanner_integration.py]] - code - gateway/tests/test_scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/A2AMethod
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_Canvas Skill]]
- 16 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 16 edges to [[_COMMUNITY_MCPAuditTrail]]
- 10 edges to [[_COMMUNITY_Step-by-Step Installation]]
- 9 edges to [[_COMMUNITY_AgentShroud Dev Environment — Raspberry Pi 4 (8G]]
- 4 edges to [[_COMMUNITY_agentshroud-bot]]
- 4 edges to [[_COMMUNITY_🟢 INFO (nice to have)]]
- 2 edges to [[_COMMUNITY_LLMProxy]]
- 2 edges to [[_COMMUNITY_iCloud Data Manager (ICLOUD)]]

## Top bridge nodes
- [[test_scanner_integration.py]] - degree 61, connects to 9 communities
- [[_score_compliance_auditing()]] - degree 10, connects to 3 communities
- [[_score_image_integrity()]] - degree 10, connects to 3 communities
- [[_score_incident_response()]] - degree 10, connects to 3 communities
- [[_score_logging_monitoring()]] - degree 9, connects to 3 communities