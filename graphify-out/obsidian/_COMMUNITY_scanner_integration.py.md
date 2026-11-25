---
type: community
members: 58
---

# scanner_integration.py

**Members:** 58 nodes

## Members
- [[Apply mandatory gate overrides to domain scores. Returns updated scores dict.…]] - rationale - gateway/security/scanner_integration.py
- [[Determine composite compliance level using the weakest-link rule. All 7 sub-…]] - rationale - gateway/security/scanner_integration.py
- [[Read and return the Docker daemon config from daemon.json, or {} if unavailable.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if app_state has a non-None attribute with the given name.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if running inside a Docker container (.dockerenv present).]] - rationale - gateway/security/scanner_integration.py
- [[Return True if the named Docker container is currently in 'running' state. Uses…]] - rationale - gateway/security/scanner_integration.py
- [[Return docker-compose.yml text for containerized-deployment evidence checks.]] - rationale - gateway/security/scanner_integration.py
- [[Return scriptssecurity-scan.sh text, or empty string.]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 13 Identity & Authentication (0-5). IEC 62443 FR1. 1=API token…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 14 Access Control & Authorization (0-5). IEC 62443 FR2. 1=role…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 15 Data Confidentiality & Encryption (0-5). IEC 62443 FR4. 1=TLS…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 16 Resource Availability & Limits (0-5). IEC 62443 FR7. 1=memory…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 17 Image Signing & Provenance (0-5). NIST 800-190 §3.1. 0=no…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 18 Registry Security (0-5). NIST 800-190 §3.2. 0=public registry,…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 19 Host OS Hardening (0-5). NIST 800-190 §3.5. 0=no info,…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 20 Docker Daemon Configuration (0-5). CIS Sections 2 & 3.…]] - rationale - gateway/security/scanner_integration.py
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
- [[_app_state_has()]] - code - gateway/security/scanner_integration.py
- [[_determine_compliance_level()]] - code - gateway/security/scanner_integration.py
- [[_evaluate_mandatory_gates()]] - code - gateway/security/scanner_integration.py
- [[_is_container_running()]] - code - gateway/security/scanner_integration.py
- [[_is_containerized()]] - code - gateway/security/scanner_integration.py
- [[_read_compose_text()]] - code - gateway/security/scanner_integration.py
- [[_read_docker_daemon_config()]] - code - gateway/security/scanner_integration.py
- [[_score_access_control_authorization()]] - code - gateway/security/scanner_integration.py
- [[_score_agent_behavior_integrity()]] - code - gateway/security/scanner_integration.py
- [[_score_agent_identity_nhi()]] - code - gateway/security/scanner_integration.py
- [[_score_ai_observability()]] - code - gateway/security/scanner_integration.py
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
- [[_score_tool_use_safety()]] - code - gateway/security/scanner_integration.py
- [[_security_scan_sh_text()]] - code - gateway/security/scanner_integration.py
- [[connect()_3]] - code - gateway/security/scanner_integration.py
- [[scanner_integration.py]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scanner_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_compute_scorecard]]
- 12 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 8 edges to [[_COMMUNITY_Any]]
- 4 edges to [[_COMMUNITY_get_trivy_summary]]
- 4 edges to [[_COMMUNITY_generate_summary]]
- 4 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 3 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_aggregate_results]]
- 2 edges to [[_COMMUNITY_get_wazuh_summary]]
- 2 edges to [[_COMMUNITY_test_soc_bots.py]]
- 1 edge to [[_COMMUNITY__score_secure_development]]
- 1 edge to [[_COMMUNITY_get_trivy_image_summaries]]
- 1 edge to [[_COMMUNITY_clamav_scanner.py]]
- 1 edge to [[_COMMUNITY_test_scorecard_scoring.py]]
- 1 edge to [[_COMMUNITY_test_scanner_integration_coverage.py]]

## Top bridge nodes
- [[scanner_integration.py]] - degree 71, connects to 15 communities
- [[_score_network_segmentation()]] - degree 9, connects to 2 communities
- [[_evaluate_mandatory_gates()]] - degree 6, connects to 2 communities
- [[_app_state_has()]] - degree 23, connects to 1 community
- [[_score_docker_daemon_config()]] - degree 6, connects to 1 community
