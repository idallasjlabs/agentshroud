---
source_file: "gateway/security/agent_isolation.py"
type: "code"
community: "Agent Isolation & Container Config"
location: "L52"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Agent_Isolation__Container_Config
---

# AgentRegistry

## Connections
- [[.__init__()_8]] - `calls` [EXTRACTED]
- [[.__init__()_40]] - `method` [EXTRACTED]
- [[.__init__()_41]] - `references` [EXTRACTED]
- [[.from_dict()_2]] - `method` [EXTRACTED]
- [[.get()_2]] - `method` [EXTRACTED]
- [[.list_agents()]] - `method` [EXTRACTED]
- [[.register()]] - `method` [EXTRACTED]
- [[.setup_method()_28]] - `calls` [EXTRACTED]
- [[.test_capabilities_not_dropped_flagged()]] - `calls` [EXTRACTED]
- [[.test_compose_contains_all_agents()]] - `calls` [EXTRACTED]
- [[.test_compose_networks_are_internal()]] - `calls` [EXTRACTED]
- [[.test_compose_security_opts()]] - `calls` [EXTRACTED]
- [[.test_fully_isolated_agents_pass()]] - `calls` [EXTRACTED]
- [[.test_get_missing_returns_none()]] - `calls` [EXTRACTED]
- [[.test_list_agents()]] - `calls` [EXTRACTED]
- [[.test_new_privileges_allowed_flagged()]] - `calls` [EXTRACTED]
- [[.test_register_and_get()]] - `calls` [EXTRACTED]
- [[.test_separate_networks_pass()]] - `calls` [EXTRACTED]
- [[.test_separate_volumes_pass()]] - `calls` [EXTRACTED]
- [[.test_serialization_roundtrip()]] - `calls` [EXTRACTED]
- [[.test_shared_network_detected()]] - `calls` [EXTRACTED]
- [[.test_shared_network_flagged_in_full_check()]] - `calls` [EXTRACTED]
- [[.test_shared_volume_detected()]] - `calls` [EXTRACTED]
- [[.test_shared_volume_flagged_in_full_check()]] - `calls` [EXTRACTED]
- [[.test_single_agent_fully_secure()]] - `calls` [EXTRACTED]
- [[.test_unregister_missing_returns_none()]] - `calls` [EXTRACTED]
- [[.test_unregister_removes_agent()]] - `calls` [EXTRACTED]
- [[.test_writable_root_flagged()]] - `calls` [EXTRACTED]
- [[.to_dict()_3]] - `method` [EXTRACTED]
- [[.unregister()]] - `method` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any_6]] - `uses` [INFERRED]
- [[ContainerConfig_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Registry mapping agent IDs to container configurations.]] - `rationale_for` [EXTRACTED]
- [[Resource]] - `uses` [INFERRED]
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
- [[ToolTier]] - `uses` [INFERRED]
- [[agent_isolation.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[test_agent_isolation.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Agent_Isolation__Container_Config
