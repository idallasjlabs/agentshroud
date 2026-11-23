---
type: community
members: 95
---

# scanner_integration.py

**Members:** 95 nodes

## Members
- [[dot-_all_not_run_patches()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_all_domains_have_required_fields()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_compliance_new_keys_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_compute_weighted_subscore_full_score()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_compute_weighted_subscore_zero_for_empty_map()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_disa_stig_domain_map_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_eu_ai_act_domain_map_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_iso_42001_domain_map_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_maturity_labels_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_network_segmentation_baseline_three()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_nist_csf_domain_map_valid()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_maturity_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_thirty_three_domains()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_scorecard_domain_ids_are_sequential()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_secrets_management_baseline_two()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_standard_basis_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_timestamp_present()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_totals_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_version_is_v090()]] - code - gateway/tests/test_scanner_integration.py
- [[Apply mandatory gate overrides to domain scores. Returns updated scores dict.…]] - rationale - gateway/security/scanner_integration.py
- [[Compute the 33-domain Security Scorecard. Domains 1–21 Container…]] - rationale - gateway/security/scanner_integration.py
- [[DISA STIG domain map references only valid domain IDs.]] - rationale - gateway/tests/test_scanner_integration.py
- [[Determine composite compliance level using the weakest-link rule. All 7 sub-…]] - rationale - gateway/security/scanner_integration.py
- [[Determine the highest achieved IEC 62443 Security Level. SL 1 All IEC-mapped…]] - rationale - gateway/security/scanner_integration.py
- [[EU AI Act domain map references only valid domain IDs.]] - rationale - gateway/tests/test_scanner_integration.py
- [[ISO 42001 domain map references only valid domain IDs.]] - rationale - gateway/tests/test_scanner_integration.py
- [[NIST CSF domain map references only valid domain IDs.]] - rationale - gateway/tests/test_scanner_integration.py
- [[New compliance sub-scores (EU AI Act, ISO 42001, NIST CSF, DISA STIG) appear in…]] - rationale - gateway/tests/test_scanner_integration.py
- [[Read and return the Docker daemon config from daemon.json, or {} if unavailable.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if app_state has a non-None attribute with the given name.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if running inside a Docker container (.dockerenv present).]] - rationale - gateway/security/scanner_integration.py
- [[Return True if the named Docker container is currently in 'running' state. Uses…]] - rationale - gateway/security/scanner_integration.py
- [[Return docker-compose.yml text for containerized-deployment evidence checks.]] - rationale - gateway/security/scanner_integration.py
- [[Return scriptssecurity-scan.sh text, or empty string.]] - rationale - gateway/security/scanner_integration.py
- [[Return weighted sub-score as 0.0–100.0 percentage.]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 13 Identity & Authentication (0-5). IEC 62443 FR1. 1=API token…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 14 Access Control & Authorization (0-5). IEC 62443 FR2. 1=role…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 15 Data Confidentiality & Encryption (0-5). IEC 62443 FR4. 1=TLS…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 16 Resource Availability & Limits (0-5). IEC 62443 FR7. 1=memory…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 17 Image Signing & Provenance (0-5). NIST 800-190 §3.1. 0=no…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 18 Registry Security (0-5). NIST 800-190 §3.2. 0=public registry,…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 19 Host OS Hardening (0-5). NIST 800-190 §3.5. 0=no info,…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 20 Docker Daemon Configuration (0-5). CIS Sections 2 & 3.…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 21 Container Runtime Isolation (0-5). CIS Section 5. 0=privileged…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 22 Prompt Injection Defense (0-5). OWASP ASI-07, MITRE AML.T0051.…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 23 Agent Goal & Behavior Integrity (0-5). OWASP ASI-01, NIST AI…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 24 Tool Use Safety & Validation (0-5). OWASP ASI-02, CSA MAESTRO.…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 25 Least Agency Enforcement (0-5). OWASP ASI-05, NIST AI Agent…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 26 Agent Identity & NHI (0-5). OWASP ASI-09, NIST AI Agent…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 27 Memory Integrity (0-5). OWASP ASI-08, MITRE ATLAS.…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 28 Inter-Agent Trust & Orchestration Security (0-5). OWASP…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 30 AI Observability & Audit Trail (0-5). NIST AI RMF MEASURE, IEC…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 31 Human-in-the-Loop Controls (0-5). NIST AI RMF MANAGE, ISO…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 32 Rogue Agent Containment & Killswitch (0-5). OWASP ASI-03, CSA…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 33 Data Exfiltration Prevention (0-5). OWASP ASI-06, MITRE ATLAS,…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 7 Network Segmentation (0-5). 3=Docker network architecture…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 8 Secrets Management (0-5). 2=Docker secrets + key_vault…]] - rationale - gateway/security/scanner_integration.py
- [[TestComputeScorecard_1]] - code - gateway/tests/test_scanner_integration.py
- [[_app_state_has()]] - code - gateway/security/scanner_integration.py
- [[_compute_weighted_subscore returns 0.0 for an empty domain map.]] - rationale - gateway/tests/test_scanner_integration.py
- [[_compute_weighted_subscore returns 100.0 when all domains score 5.]] - rationale - gateway/tests/test_scanner_integration.py
- [[_compute_weighted_subscore()]] - code - gateway/security/scanner_integration.py
- [[_determine_compliance_level()]] - code - gateway/security/scanner_integration.py
- [[_determine_iec_sl()]] - code - gateway/security/scanner_integration.py
- [[_evaluate_mandatory_gates()]] - code - gateway/security/scanner_integration.py
- [[_is_container_running()]] - code - gateway/security/scanner_integration.py
- [[_is_containerized()]] - code - gateway/security/scanner_integration.py
- [[_read_compose_text()]] - code - gateway/security/scanner_integration.py
- [[_read_docker_daemon_config()]] - code - gateway/security/scanner_integration.py
- [[_score_access_control_authorization()]] - code - gateway/security/scanner_integration.py
- [[_score_agent_behavior_integrity()]] - code - gateway/security/scanner_integration.py
- [[_score_agent_identity_nhi()]] - code - gateway/security/scanner_integration.py
- [[_score_ai_observability()]] - code - gateway/security/scanner_integration.py
- [[_score_container_runtime_isolation()]] - code - gateway/security/scanner_integration.py
- [[_score_data_confidentiality_encryption()]] - code - gateway/security/scanner_integration.py
- [[_score_data_exfiltration_prevention()]] - code - gateway/security/scanner_integration.py
- [[_score_docker_daemon_config()]] - code - gateway/security/scanner_integration.py
- [[_score_host_os_hardening()]] - code - gateway/security/scanner_integration.py
- [[_score_human_in_the_loop()]] - code - gateway/security/scanner_integration.py
- [[_score_identity_authentication()]] - code - gateway/security/scanner_integration.py
- [[_score_image_signing_provenance()]] - code - gateway/security/scanner_integration.py
- [[_score_inter_agent_trust()]] - code - gateway/security/scanner_integration.py
- [[_score_least_agency()]] - code - gateway/security/scanner_integration.py
- [[_score_memory_integrity()]] - code - gateway/security/scanner_integration.py
- [[_score_network_segmentation()]] - code - gateway/security/scanner_integration.py
- [[_score_prompt_injection_defense()]] - code - gateway/security/scanner_integration.py
- [[_score_registry_security()]] - code - gateway/security/scanner_integration.py
- [[_score_resource_availability()]] - code - gateway/security/scanner_integration.py
- [[_score_rogue_agent_containment()]] - code - gateway/security/scanner_integration.py
- [[_score_secrets_management()]] - code - gateway/security/scanner_integration.py
- [[_score_tool_use_safety()]] - code - gateway/security/scanner_integration.py
- [[_security_scan_sh_text()]] - code - gateway/security/scanner_integration.py
- [[compute_scorecard()]] - code - gateway/security/scanner_integration.py
- [[connect()_6]] - code - gateway/security/scanner_integration.py
- [[scanner_integration.py]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scanner_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 11 edges to [[_COMMUNITY_Any]]
- 8 edges to [[_COMMUNITY_get_wazuh_summary]]
- 6 edges to [[_COMMUNITY_get_trivy_summary]]
- 5 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 3 edges to [[_COMMUNITY_get_sbom]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 2 edges to [[_COMMUNITY__score_secure_development]]
- 2 edges to [[_COMMUNITY_test_soc_bots.py]]
- 1 edge to [[_COMMUNITY_parse_trivy_output]]
- 1 edge to [[_COMMUNITY_test_clamav_pipeline.py]]
- 1 edge to [[_COMMUNITY_get_trivy_image_summaries]]
- 1 edge to [[_COMMUNITY_test_scorecard_scoring.py]]
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]

## Top bridge nodes
- [[scanner_integration.py]] - degree 71, connects to 14 communities
- [[compute_scorecard()]] - degree 61, connects to 8 communities
- [[_app_state_has()]] - degree 23, connects to 1 community
- [[TestComputeScorecard_1]] - degree 21, connects to 1 community
- [[dot-_all_not_run_patches()]] - degree 18, connects to 1 community
