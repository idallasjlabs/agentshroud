---
source_file: "gateway/soc/services.py"
type: "code"
community: "test_soc_realtime_coverage.py"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_soc_realtime_coveragepy
---

# services.py

## Connections
- [[HealthStatus]] - `imports` [EXTRACTED]
- [[SOC Service Manager — wraps container runtime engine to produce…]] - `rationale_for` [EXTRACTED]
- [[ServiceDescriptor]] - `imports` [EXTRACTED]
- [[ServiceManager]] - `contains` [EXTRACTED]
- [[ServiceStatus]] - `imports` [EXTRACTED]
- [[_check_clamd()]] - `indirect_call` [INFERRED]
- [[_check_fluent_bit()]] - `indirect_call` [INFERRED]
- [[_check_openscap()]] - `indirect_call` [INFERRED]
- [[_check_wazuh_agent()]] - `indirect_call` [INFERRED]
- [[_engine_health_to_health()]] - `contains` [EXTRACTED]
- [[_engine_status_to_service_status()]] - `contains` [EXTRACTED]
- [[_inspect_via_socket()]] - `contains` [EXTRACTED]
- [[_known_services()]] - `contains` [EXTRACTED]
- [[load_config()]] - `imports` [EXTRACTED]
- [[socmodels.py]] - `imports_from` [EXTRACTED]
- [[test_soc_services_coverage.py]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_soc_realtime_coveragepy
