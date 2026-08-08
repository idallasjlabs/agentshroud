---
source_file: "gateway/tests/test_security_hardening.py"
type: "code"
community: "Gateway Test Suite"
location: "L646"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Gateway_Test_Suite
---

# TestAgentIsolation

## Connections
- [[.setup_method()_31]] - `method` [EXTRACTED]
- [[.test_container_config_defaults()]] - `method` [EXTRACTED]
- [[.test_generate_compose()]] - `method` [EXTRACTED]
- [[.test_list_agents()_1]] - `method` [EXTRACTED]
- [[.test_network_isolation_ok()]] - `method` [EXTRACTED]
- [[.test_network_isolation_violation()]] - `method` [EXTRACTED]
- [[.test_register_and_get()_1]] - `method` [EXTRACTED]
- [[.test_serialization()]] - `method` [EXTRACTED]
- [[.test_shared_nothing_ok()]] - `method` [EXTRACTED]
- [[.test_shared_nothing_security_issue()]] - `method` [EXTRACTED]
- [[.test_unregister()]] - `method` [EXTRACTED]
- [[.test_volume_isolation_ok()]] - `method` [EXTRACTED]
- [[.test_volume_isolation_violation()]] - `method` [EXTRACTED]
- [[AgentRegistry]] - `uses` [INFERRED]
- [[ContainerConfig]] - `uses` [INFERRED]
- [[ContainerSnapshot]] - `uses` [INFERRED]
- [[DriftDetector]] - `uses` [INFERRED]
- [[EgressAction]] - `uses` [INFERRED]
- [[EgressFilter_1]] - `uses` [INFERRED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EgressPolicy]] - `uses` [INFERRED]
- [[EncryptedStore]] - `uses` [INFERRED]
- [[IsolationStatus]] - `uses` [INFERRED]
- [[IsolationVerifier]] - `uses` [INFERRED]
- [[PatternRule]] - `uses` [INFERRED]
- [[PromptGuard]] - `uses` [INFERRED]
- [[ThreatAction]] - `uses` [INFERRED]
- [[TrustConfig]] - `uses` [INFERRED]
- [[TrustLevel_1]] - `uses` [INFERRED]
- [[TrustManager_1]] - `uses` [INFERRED]
- [[test_security_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Gateway_Test_Suite