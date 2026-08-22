---
source_file: "gateway/security/agent_isolation.py"
type: "code"
community: "Security Hardening"
location: "L87"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Security_Hardening
---

# IsolationVerifier

## Connections
- [[.__init__()_52]] - `method` [EXTRACTED]
- [[.generate_compose()]] - `method` [EXTRACTED]
- [[.test_capabilities_not_dropped_flagged()]] - `calls` [EXTRACTED]
- [[.test_compose_contains_all_agents()]] - `calls` [EXTRACTED]
- [[.test_compose_networks_are_internal()]] - `calls` [EXTRACTED]
- [[.test_compose_security_opts()]] - `calls` [EXTRACTED]
- [[.test_fully_isolated_agents_pass()]] - `calls` [EXTRACTED]
- [[.test_generate_compose()]] - `calls` [EXTRACTED]
- [[.test_network_isolation_ok()]] - `calls` [EXTRACTED]
- [[.test_network_isolation_violation()]] - `calls` [EXTRACTED]
- [[.test_new_privileges_allowed_flagged()]] - `calls` [EXTRACTED]
- [[.test_separate_networks_pass()]] - `calls` [EXTRACTED]
- [[.test_separate_volumes_pass()]] - `calls` [EXTRACTED]
- [[.test_shared_network_detected()]] - `calls` [EXTRACTED]
- [[.test_shared_network_flagged_in_full_check()]] - `calls` [EXTRACTED]
- [[.test_shared_nothing_ok()]] - `calls` [EXTRACTED]
- [[.test_shared_nothing_security_issue()]] - `calls` [EXTRACTED]
- [[.test_shared_volume_detected()]] - `calls` [EXTRACTED]
- [[.test_shared_volume_flagged_in_full_check()]] - `calls` [EXTRACTED]
- [[.test_single_agent_fully_secure()]] - `calls` [EXTRACTED]
- [[.test_volume_isolation_ok()]] - `calls` [EXTRACTED]
- [[.test_volume_isolation_violation()]] - `calls` [EXTRACTED]
- [[.test_writable_root_flagged()]] - `calls` [EXTRACTED]
- [[.verify_network_isolation()]] - `method` [EXTRACTED]
- [[.verify_shared_nothing()]] - `method` [EXTRACTED]
- [[.verify_volume_isolation()]] - `method` [EXTRACTED]
- [[ContainerConfig_1]] - `uses` [INFERRED]
- [[DriftDetector]] - `shares_data_with` [EXTRACTED]
- [[TestAgentIsolation]] - `uses` [INFERRED]
- [[TestAgentRegistry]] - `uses` [INFERRED]
- [[TestDriftDetector]] - `uses` [INFERRED]
- [[TestDriftDetectorHardened]] - `uses` [INFERRED]
- [[TestEgressFilter]] - `uses` [INFERRED]
- [[TestEgressSSRF]] - `uses` [INFERRED]
- [[TestEncryptedStore]] - `uses` [INFERRED]
- [[TestGenerateCompose]] - `uses` [INFERRED]
- [[TestNetworkIsolation]] - `uses` [INFERRED]
- [[TestPromptGuard_1]] - `uses` [INFERRED]
- [[TestPromptGuardEvasion]] - `uses` [INFERRED]
- [[TestSecureZero]] - `uses` [INFERRED]
- [[TestSharedNothing]] - `uses` [INFERRED]
- [[TestTrustManager]] - `uses` [INFERRED]
- [[TestTrustManagerHardened]] - `uses` [INFERRED]
- [[TestVolumeIsolation]] - `uses` [INFERRED]
- [[Verify container isolation properties.]] - `rationale_for` [EXTRACTED]
- [[agent_isolation.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_agent_isolation.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Security_Hardening