---
source_file: "gateway/soc/services.py"
type: "code"
community: "ServiceManager"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ServiceManager
---

# services.py

## Connections
- [[HealthStatus_1]] - `imports` [EXTRACTED]
- [[ServiceDescriptor_1]] - `imports` [EXTRACTED]
- [[ServiceManager]] - `references` [EXTRACTED]
- [[ServiceStatus_1]] - `imports` [EXTRACTED]
- [[_INTERNAL_SERVICE_ATTRS (internal gateway service table)]] - `references` [EXTRACTED]
- [[_check_clamd()]] - `references` [EXTRACTED]
- [[_check_fluent_bit()]] - `references` [EXTRACTED]
- [[_check_openscap()]] - `contains` [EXTRACTED]
- [[_check_wazuh_agent()]] - `references` [EXTRACTED]
- [[_engine_health_to_health()]] - `contains` [EXTRACTED]
- [[_engine_status_to_service_status()]] - `contains` [EXTRACTED]
- [[_inspect_via_socket()]] - `contains` [EXTRACTED]
- [[_known_services()]] - `references` [EXTRACTED]
- [[agent_cve_registry.py]] - `conceptually_related_to` [INFERRED]
- [[load_config()]] - `imports` [EXTRACTED]
- [[socmodels.py]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ServiceManager
