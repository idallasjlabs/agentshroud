---
type: community
cohesion: 0.06
members: 66
---

# Security Scanner Integration

**Cohesion:** 0.06 - loosely connected
**Members:** 66 nodes

## Members
- [[Apply mandatory gate overrides to domain scores.      Returns updated scores dic]] - rationale - gateway/security/scanner_integration.py
- [[Path_15]] - code - gateway/security/scanner_integration.py
- [[Read and return the Docker daemon config from daemon.json, or {} if unavailable.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if a non-zombie falco process is running inside this container.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if app_state has a non-None attribute with the given name.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if fluent-bit pidfile tmpfluent-bit.pid exists with a live PID.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if running inside a Docker container (.dockerenv present).]] - rationale - gateway/security/scanner_integration.py
- [[Return True if the named Docker container is currently in 'running' state.]] - rationale - gateway/security/scanner_integration.py
- [[Return True if wazuh-agentd is running as a local process inside this container.]] - rationale - gateway/security/scanner_integration.py
- [[Return docker-compose.yml text for containerized-deployment evidence checks.]] - rationale - gateway/security/scanner_integration.py
- [[Return scriptssecurity-scan.sh text, or empty string.]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 13 Identity & Authentication (0-5). IEC 62443 FR1.      1=API toke]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 14 Access Control & Authorization (0-5). IEC 62443 FR2.      1=rol]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 15 Data Confidentiality & Encryption (0-5). IEC 62443 FR4.      1=]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 16 Resource Availability & Limits (0-5). IEC 62443 FR7.      1=mem]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 17 Image Signing & Provenance (0-5). NIST 800-190 §3.1.      0=no]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 18 Registry Security (0-5). NIST 800-190 §3.2.      0=public regis]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 19 Host OS Hardening (0-5). NIST 800-190 §3.5.      0=no info, 1=k]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 20 Docker Daemon Configuration (0-5). CIS Sections 2 & 3.      0=d]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 21 Container Runtime Isolation (0-5). CIS Section 5.      0=privil]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 22 Prompt Injection Defense (0-5). OWASP ASI-07, MITRE AML.T0051.]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 23 Agent Goal & Behavior Integrity (0-5). OWASP ASI-01, NIST AI RM]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 24 Tool Use Safety & Validation (0-5). OWASP ASI-02, CSA MAESTRO.]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 25 Least Agency Enforcement (0-5). OWASP ASI-05, NIST AI Agent Sta]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 26 Agent Identity & NHI (0-5). OWASP ASI-09, NIST AI Agent Standar]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 27 Memory Integrity (0-5). OWASP ASI-08, MITRE ATLAS.      1=memor]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 28 Inter-Agent Trust & Orchestration Security (0-5). OWASP ASI-03]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 30 AI Observability & Audit Trail (0-5). NIST AI RMF MEASURE, IEC]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 31 Human-in-the-Loop Controls (0-5). NIST AI RMF MANAGE, ISO 42001]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 32 Rogue Agent Containment & Killswitch (0-5). OWASP ASI-03, CSA M]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 33 Data Exfiltration Prevention (0-5). OWASP ASI-06, MITRE ATLAS,]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 7 Network Segmentation (0-5).      3=Docker network architecture b]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 8 Secrets Management (0-5).      2=Docker secrets + key_vault base]] - rationale - gateway/security/scanner_integration.py
- [[_app_state_has()]] - code - gateway/security/scanner_integration.py
- [[_evaluate_mandatory_gates()]] - code - gateway/security/scanner_integration.py
- [[_is_container_running()]] - code - gateway/security/scanner_integration.py
- [[_is_containerized()]] - code - gateway/security/scanner_integration.py
- [[_is_falco_running()]] - code - gateway/security/scanner_integration.py
- [[_is_fluent_bit_running()]] - code - gateway/security/scanner_integration.py
- [[_is_wazuh_agent_running()]] - code - gateway/security/scanner_integration.py
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
- [[scanner_integration.py]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Security_Scanner_Integration
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_Module Group 134]]
- 16 edges to [[_COMMUNITY_Scanner Integration Tests]]
- 9 edges to [[_COMMUNITY_Module Group 228]]
- 5 edges to [[_COMMUNITY_Module Group 163]]
- 5 edges to [[_COMMUNITY_Module Group 381]]
- 5 edges to [[_COMMUNITY_Module Group 122]]
- 3 edges to [[_COMMUNITY_Module Group 437]]
- 3 edges to [[_COMMUNITY_Module Group 269]]
- 2 edges to [[_COMMUNITY_Module Group 141]]
- 2 edges to [[_COMMUNITY_Module Group 335]]
- 1 edge to [[_COMMUNITY_Module Group 155]]
- 1 edge to [[_COMMUNITY_Module Group 213]]
- 1 edge to [[_COMMUNITY_Module Group 210]]
- 1 edge to [[_COMMUNITY_Module Group 176]]
- 1 edge to [[_COMMUNITY_Module Group 294]]

## Top bridge nodes
- [[scanner_integration.py]] - degree 67, connects to 15 communities
- [[Path_15]] - degree 34, connects to 6 communities
- [[_score_network_segmentation()]] - degree 9, connects to 2 communities
- [[_evaluate_mandatory_gates()]] - degree 7, connects to 2 communities
- [[_score_host_os_hardening()]] - degree 7, connects to 2 communities
