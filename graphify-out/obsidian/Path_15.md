---
source_file: "gateway/security/scanner_integration.py"
type: "code"
community: "Security Scanner Integration"
location: "L321"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Security_Scanner_Integration
---

# Path

## Connections
- [[_evaluate_mandatory_gates()]] - `calls` [EXTRACTED]
- [[_is_containerized()]] - `calls` [EXTRACTED]
- [[_is_falco_running()]] - `calls` [EXTRACTED]
- [[_is_fluent_bit_running()]] - `calls` [EXTRACTED]
- [[_is_fresh()]] - `references` [EXTRACTED]
- [[_is_wazuh_agent_running()]] - `calls` [EXTRACTED]
- [[_load_latest_json()]] - `references` [EXTRACTED]
- [[_read_compose_text()]] - `calls` [EXTRACTED]
- [[_read_docker_daemon_config()]] - `calls` [EXTRACTED]
- [[_score_access_control_authorization()]] - `calls` [EXTRACTED]
- [[_score_ai_model_supply_chain()]] - `calls` [EXTRACTED]
- [[_score_ai_observability()]] - `calls` [EXTRACTED]
- [[_score_container_runtime_isolation()]] - `calls` [EXTRACTED]
- [[_score_data_confidentiality_encryption()]] - `calls` [EXTRACTED]
- [[_score_data_exfiltration_prevention()]] - `calls` [EXTRACTED]
- [[_score_host_os_hardening()]] - `calls` [EXTRACTED]
- [[_score_identity_authentication()]] - `calls` [EXTRACTED]
- [[_score_image_signing_provenance()]] - `calls` [EXTRACTED]
- [[_score_incident_response()]] - `calls` [EXTRACTED]
- [[_score_least_agency()]] - `calls` [EXTRACTED]
- [[_score_logging_monitoring()]] - `calls` [EXTRACTED]
- [[_score_memory_integrity()]] - `calls` [EXTRACTED]
- [[_score_prompt_injection_defense()]] - `calls` [EXTRACTED]
- [[_score_registry_security()]] - `calls` [EXTRACTED]
- [[_score_resource_availability()]] - `calls` [EXTRACTED]
- [[_score_rogue_agent_containment()]] - `calls` [EXTRACTED]
- [[_score_secrets_management()]] - `calls` [EXTRACTED]
- [[_score_secure_development()]] - `calls` [EXTRACTED]
- [[_score_tool_use_safety()]] - `calls` [EXTRACTED]
- [[_security_scan_sh_text()]] - `calls` [EXTRACTED]
- [[get_clamav_summary()]] - `calls` [EXTRACTED]
- [[get_falco_summary()]] - `calls` [EXTRACTED]
- [[get_fluent_bit_summary()]] - `calls` [EXTRACTED]
- [[get_wazuh_summary()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Security_Scanner_Integration
