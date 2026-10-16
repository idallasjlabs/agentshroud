---
type: community
cohesion: 0.06
members: 76
---

# test_scanner_integration.py

**Cohesion:** 0.06 - loosely connected
**Members:** 76 nodes

## Members
- [[dot-_patch_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_baseline_at_least_two()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_baseline_three_when_openscap_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_baseline_three_without_daemon_config()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_capped_at_five()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_clean_when_installed_not_running()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_defined_when_all_passing_no_report_on_disk()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_defined_when_oscap_binary_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_five_when_openscap_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_four_when_openscap_running_with_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_four_when_sbom_and_clean_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_initial_when_not_run()_2]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_managed_when_has_criticals()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_managed_when_has_failures()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_alert_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_no_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_no_wazuh_no_fluent()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_sbom_exists()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_optimizing_when_clean_zero_findings()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_clean_when_all_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_critical_when_any_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_not_configured_when_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_warning_when_high_only()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_summary_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_scanners_dict_has_all_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_three_when_both_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_timestamp_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_totals_sum_across_scanners()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_falco_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_wazuh_running()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_no_sbom_no_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_not_run()_1]] - code - gateway/tests/test_scanner_integration.py
- [[Aggregate results from all security scanners into a unified dict.      Returns]] - rationale - gateway/security/scanner_integration.py
- [[Any_73]] - code - gateway/security/scanner_integration.py
- [[Any_74]] - code - gateway/tests/test_scanner_integration.py
- [[Return Fluent Bit log collector status.      Fluent Bit is a log shipper, not a]] - rationale - gateway/security/scanner_integration.py
- [[Return latest Wazuh alert summary from the shared alert volume.      wazuh-agent]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 10 Compliance Auditing (0-5).      0=not run, 2=has failures, 3=ze]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 12 Incident Response (0-5).      1=SOC exists, 2=Falco running, 3=]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 1 Image Integrity (0-5).      1=SBOM exists, 2=Trivy ran, 3=zero c]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 4 Container Hardening (0-5).      Baseline of 3 because docker-com]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 5 Runtime Protection (0-5).      1=module exists, 2=running with c]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 9 Logging & Monitoring (0-5).      1=SOC exists, 2=Wazuh running,]] - rationale - gateway/security/scanner_integration.py
- [[TestAggregateResults_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetWazuhSummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreComplianceAuditing_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreContainerHardening_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreImageIntegrity]] - code - gateway/tests/test_scanner_integration.py
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
- [[aggregate_results()]] - code - gateway/security/scanner_integration.py
- [[get_fluent_bit_summary()]] - code - gateway/security/scanner_integration.py
- [[get_wazuh_summary()]] - code - gateway/security/scanner_integration.py
- [[test_scanner_integration.py]] - code - gateway/tests/test_scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_scanner_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 43 edges to [[_COMMUNITY_scanner_integration.py]]
- 14 edges to [[_COMMUNITY_Path_1]]
- 13 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 9 edges to [[_COMMUNITY_get_trivy_summary]]
- 7 edges to [[_COMMUNITY__load_latest_json]]
- 4 edges to [[_COMMUNITY_get_falco_summary]]
- 2 edges to [[_COMMUNITY__score_secure_development]]
- 2 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_test_soc_bots.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[test_scanner_integration.py]] - degree 61, connects to 7 communities
- [[Any_73]] - degree 22, connects to 7 communities
- [[aggregate_results()]] - degree 19, connects to 7 communities
- [[get_wazuh_summary()]] - degree 14, connects to 3 communities
- [[_score_compliance_auditing()]] - degree 10, connects to 2 communities
