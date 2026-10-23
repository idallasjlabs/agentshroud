---
type: community
cohesion: 0.06
members: 87
---

# test_a2a_policy.py

**Cohesion:** 0.06 - loosely connected
**Members:** 87 nodes

## Members
- [[dot-__init__()_159]] - code - gateway/security/agent_isolation.py
- [[dot-__init__()_160]] - code - gateway/security/agent_isolation.py
- [[dot-from_dict()_7]] - code - gateway/security/agent_isolation.py
- [[dot-generate_compose()]] - code - gateway/security/agent_isolation.py
- [[dot-get()_4]] - code - gateway/security/agent_isolation.py
- [[dot-list_agents()]] - code - gateway/security/agent_isolation.py
- [[dot-register()]] - code - gateway/security/agent_isolation.py
- [[dot-setup_method()_28]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_capabilities_not_dropped_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_compose_contains_all_agents()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_compose_networks_are_internal()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_compose_security_opts()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_container_config_defaults()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_fully_isolated_agents_pass()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_generate_compose()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_get_missing_returns_none()_1]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_group_agents_are_isolatable()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_and_collab_identities_coexist()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_list_agents()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_list_agents()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_network_isolation_ok()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_network_isolation_violation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_new_privileges_allowed_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_register_and_get()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_register_and_get()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_group_agent_identity()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_register_group_agent_with_chat_type_supergroup()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_separate_networks_pass()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_separate_volumes_pass()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_serialization()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_serialization_roundtrip()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_shared_network_detected()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_shared_network_flagged_in_full_check()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_shared_nothing_ok()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_shared_nothing_security_issue()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_shared_volume_detected()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_shared_volume_flagged_in_full_check()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_single_agent_fully_secure()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_unregister()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_unregister_missing_returns_none()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_unregister_removes_agent()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_volume_isolation_ok()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_volume_isolation_violation()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_writable_root_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-to_dict()_10]] - code - gateway/security/agent_isolation.py
- [[dot-unregister()]] - code - gateway/security/agent_isolation.py
- [[dot-verify_network_isolation()]] - code - gateway/security/agent_isolation.py
- [[dot-verify_shared_nothing()]] - code - gateway/security/agent_isolation.py
- [[dot-verify_volume_isolation()]] - code - gateway/security/agent_isolation.py
- [[A single properly-configured agent should have zero issues.]] - rationale - gateway/tests/test_agent_isolation.py
- [[Agent Isolation Module Badge Icon]] - image - branding/icons/modules/agent-isolation-256x256.png
- [[AgentRegistry]] - code - gateway/security/agent_isolation.py
- [[AgentRegistry must accept group-{chat_id} agent IDs with chat_type metadata.]] - rationale - gateway/tests/test_group_isolation.py
- [[ContainerConfig]] - code - gateway/tests/test_agent_isolation.py
- [[ContainerConfig_1]] - code - gateway/security/agent_isolation.py
- [[Deserialize registry from dict.]] - rationale - gateway/security/agent_isolation.py
- [[Full shared-nothing verification network + volume + security settings.]] - rationale - gateway/security/agent_isolation.py
- [[Generate Docker Compose config for all registered agents.]] - rationale - gateway/security/agent_isolation.py
- [[Get container config for an agent.]] - rationale - gateway/security/agent_isolation.py
- [[Helper to create a ContainerConfig with sensible defaults.]] - rationale - gateway/tests/test_agent_isolation.py
- [[IsolationCheck]] - code - gateway/security/agent_isolation.py
- [[IsolationStatus]] - code - gateway/security/agent_isolation.py
- [[IsolationVerifier]] - code - gateway/security/agent_isolation.py
- [[List all registered agent IDs.]] - rationale - gateway/security/agent_isolation.py
- [[OPENCLAW_DISABLE_HOST_FILESYSTEM_1]] - document - docs/vault/04 - Environment Variables/OPENCLAW_DISABLE_HOST_FILESYSTEM.md
- [[OPENCLAW_SANDBOX_MODE_1]] - document - docs/vault/04 - Environment Variables/OPENCLAW_SANDBOX_MODE.md
- [[Register a group-{chat_id} identity in AgentRegistry.]] - rationale - gateway/tests/test_group_isolation.py
- [[Register a supergroup-type agent identity.]] - rationale - gateway/tests/test_group_isolation.py
- [[Register an agent with its container configuration.]] - rationale - gateway/security/agent_isolation.py
- [[Registry mapping agent IDs to container configurations.]] - rationale - gateway/security/agent_isolation.py
- [[Remove an agent from the registry.]] - rationale - gateway/security/agent_isolation.py
- [[Serialize registry to dict.]] - rationale - gateway/security/agent_isolation.py
- [[TestAgentIsolation]] - code - gateway/tests/test_security_hardening.py
- [[TestAgentRegistry]] - code - gateway/tests/test_agent_isolation.py
- [[TestAgentRegistryGroupIdentity]] - code - gateway/tests/test_group_isolation.py
- [[TestGenerateCompose]] - code - gateway/tests/test_agent_isolation.py
- [[TestNetworkIsolation]] - code - gateway/tests/test_agent_isolation.py
- [[TestSharedNothing]] - code - gateway/tests/test_agent_isolation.py
- [[TestVolumeIsolation]] - code - gateway/tests/test_agent_isolation.py
- [[Two group identities should each have distinct volumes.]] - rationale - gateway/tests/test_group_isolation.py
- [[Verify container isolation properties.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own network namespace.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own volume (no shared filesystems).]] - rationale - gateway/security/agent_isolation.py
- [[_make_config()]] - code - gateway/tests/test_agent_isolation.py
- [[agent_isolation.py]] - code - gateway/security/agent_isolation.py
- [[group-{chat_id} and collab-{uid} identities can coexist in the same registry.]] - rationale - gateway/tests/test_group_isolation.py
- [[test_agent_isolation.py]] - code - gateway/tests/test_agent_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_a2a_policypy
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 19 edges to [[_COMMUNITY_ContextGuard]]
- 9 edges to [[_COMMUNITY_Any]]
- 7 edges to [[_COMMUNITY_KillSwitchMonitor (5)]]
- 5 edges to [[_COMMUNITY_PromptGuard]]
- 4 edges to [[_COMMUNITY_TestEncryptedStore]]
- 4 edges to [[_COMMUNITY_TestPromptGuardEvasion]]
- 4 edges to [[_COMMUNITY_socrouter.py (2)]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_Enum]]
- 2 edges to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_KeyRotationManager (2)]]
- 1 edge to [[_COMMUNITY_OPENCLAW_DISABLE_HOST_FILESYSTEM]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 1 edge to [[_COMMUNITY_KeyVaultConfig]]
- 1 edge to [[_COMMUNITY_check_command]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy()]]
- 1 edge to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (2)]]
- 1 edge to [[_COMMUNITY_SharedMemoryManager]]
- 1 edge to [[_COMMUNITY_DelegationManager]]

## Top bridge nodes
- [[AgentRegistry]] - degree 69, connects to 9 communities
- [[IsolationStatus]] - degree 35, connects to 9 communities
- [[ContainerConfig_1]] - degree 38, connects to 7 communities
- [[IsolationVerifier]] - degree 48, connects to 6 communities
- [[TestAgentIsolation]] - degree 31, connects to 6 communities
