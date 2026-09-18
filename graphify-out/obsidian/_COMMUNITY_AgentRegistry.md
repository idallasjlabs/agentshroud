---
type: community
cohesion: 0.05
members: 87
---

# AgentRegistry

**Cohesion:** 0.05 - loosely connected
**Members:** 87 nodes

## Members
- [[.__init__()_126]] - code - gateway/security/agent_isolation.py
- [[.__init__()_127]] - code - gateway/security/agent_isolation.py
- [[.from_dict()_3]] - code - gateway/security/agent_isolation.py
- [[.generate_compose()]] - code - gateway/security/agent_isolation.py
- [[.get()_1]] - code - gateway/security/agent_isolation.py
- [[.list_agents()]] - code - gateway/security/agent_isolation.py
- [[.register()]] - code - gateway/security/agent_isolation.py
- [[.setup_method()_28]] - code - gateway/tests/test_security_hardening.py
- [[.test_capabilities_not_dropped_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_contains_all_agents()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_networks_are_internal()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_security_opts()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_container_config_defaults()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[.test_fully_isolated_agents_pass()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_generate_compose()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_missing_returns_none()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_group_agents_are_isolatable()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_and_collab_identities_coexist()]] - code - gateway/tests/test_group_isolation.py
- [[.test_key_rotation_with_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[.test_list_agents()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_list_agents()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_network_isolation_ok()]] - code - gateway/tests/test_security_hardening.py
- [[.test_network_isolation_violation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_new_privileges_allowed_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_register_and_get()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_register_and_get()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_register_group_agent_identity()]] - code - gateway/tests/test_group_isolation.py
- [[.test_register_group_agent_with_chat_type_supergroup()]] - code - gateway/tests/test_group_isolation.py
- [[.test_separate_networks_pass()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_separate_volumes_pass()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_serialization()]] - code - gateway/tests/test_security_hardening.py
- [[.test_serialization_roundtrip()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_shared_network_detected()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_shared_network_flagged_in_full_check()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_shared_nothing_ok()]] - code - gateway/tests/test_security_hardening.py
- [[.test_shared_nothing_security_issue()]] - code - gateway/tests/test_security_hardening.py
- [[.test_shared_volume_detected()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_shared_volume_flagged_in_full_check()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_single_agent_fully_secure()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_unregister()]] - code - gateway/tests/test_security_hardening.py
- [[.test_unregister_missing_returns_none()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_unregister_removes_agent()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_volume_isolation_ok()]] - code - gateway/tests/test_security_hardening.py
- [[.test_volume_isolation_violation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_writable_root_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[.to_dict()_9]] - code - gateway/security/agent_isolation.py
- [[.unregister()]] - code - gateway/security/agent_isolation.py
- [[.verify_network_isolation()]] - code - gateway/security/agent_isolation.py
- [[.verify_shared_nothing()]] - code - gateway/security/agent_isolation.py
- [[.verify_volume_isolation()]] - code - gateway/security/agent_isolation.py
- [[A single properly-configured agent should have zero issues.]] - rationale - gateway/tests/test_agent_isolation.py
- [[AgentRegistry]] - code - gateway/security/agent_isolation.py
- [[AgentRegistry must accept group-{chat_id} agent IDs with chat_type metadata.]] - rationale - gateway/tests/test_group_isolation.py
- [[ContainerConfig]] - code - gateway/tests/test_agent_isolation.py
- [[ContainerConfig_1]] - code - gateway/security/agent_isolation.py
- [[Deserialize registry from dict.]] - rationale - gateway/security/agent_isolation.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[Full shared-nothing verification network + volume + security settings.]] - rationale - gateway/security/agent_isolation.py
- [[Generate Docker Compose config for all registered agents.]] - rationale - gateway/security/agent_isolation.py
- [[Get container config for an agent.]] - rationale - gateway/security/agent_isolation.py
- [[Helper to create a ContainerConfig with sensible defaults.]] - rationale - gateway/tests/test_agent_isolation.py
- [[IsolationCheck]] - code - gateway/security/agent_isolation.py
- [[IsolationVerifier]] - code - gateway/security/agent_isolation.py
- [[List all registered agent IDs.]] - rationale - gateway/security/agent_isolation.py
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
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[TestSharedNothing]] - code - gateway/tests/test_agent_isolation.py
- [[TestVolumeIsolation]] - code - gateway/tests/test_agent_isolation.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[Two group identities should each have distinct volumes.]] - rationale - gateway/tests/test_group_isolation.py
- [[Verify container isolation properties.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own network namespace.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own volume (no shared filesystems).]] - rationale - gateway/security/agent_isolation.py
- [[_make_config()]] - code - gateway/tests/test_agent_isolation.py
- [[group-{chat_id} and collab-{uid} identities can coexist in the same registry.]] - rationale - gateway/tests/test_group_isolation.py
- [[test_agent_isolation.py]] - code - gateway/tests/test_agent_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentRegistry
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_EgressAction]]
- 27 edges to [[_COMMUNITY_EncryptedStore]]
- 19 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_RBACConfig]]
- 5 edges to [[_COMMUNITY_EgressFilter]]
- 4 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_TrustLevel]]
- 2 edges to [[_COMMUNITY_KeyVaultConfig]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestGroupMemoryInvisibleFromDM]]
- 2 edges to [[_COMMUNITY_TestGroupMemoryNamespaceIsolation]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_cls]]

## Top bridge nodes
- [[TestAgentIsolation]] - degree 31, connects to 10 communities
- [[TestSecureZero]] - degree 23, connects to 10 communities
- [[AgentRegistry]] - degree 71, connects to 8 communities
- [[ContainerConfig_1]] - degree 40, connects to 7 communities
- [[IsolationVerifier]] - degree 50, connects to 4 communities