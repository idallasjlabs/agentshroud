---
type: community
members: 101
---

# Community 52

**Members:** 101 nodes

## Members
- [[.__init__()_51]] - code - gateway/security/agent_isolation.py
- [[.__init__()_52]] - code - gateway/security/agent_isolation.py
- [[.__init__()_109]] - code - gateway/security/prompt_guard.py
- [[.from_dict()_3]] - code - gateway/security/agent_isolation.py
- [[.generate_compose()]] - code - gateway/security/agent_isolation.py
- [[.get()_3]] - code - gateway/security/agent_isolation.py
- [[.list_agents()]] - code - gateway/security/agent_isolation.py
- [[.register()]] - code - gateway/security/agent_isolation.py
- [[.setup_method()_31]] - code - gateway/tests/test_security_hardening.py
- [[.test_capabilities_not_dropped_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_contains_all_agents()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_networks_are_internal()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_security_opts()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_container_config_defaults()]] - code - gateway/tests/test_security_hardening.py
- [[.test_encrypt_decrypt_still_works_after_zeroing()]] - code - gateway/tests/test_security_hardening.py
- [[.test_event_type_validation()]] - code - gateway/tests/test_security_hardening.py
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
- [[.test_rate_limiting_prevents_rapid_escalation()]] - code - gateway/tests/test_security_hardening.py
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
- [[.to_dict()_4]] - code - gateway/security/agent_isolation.py
- [[.unregister()]] - code - gateway/security/agent_isolation.py
- [[.verify_network_isolation()]] - code - gateway/security/agent_isolation.py
- [[.verify_shared_nothing()]] - code - gateway/security/agent_isolation.py
- [[.verify_volume_isolation()]] - code - gateway/security/agent_isolation.py
- [[A single properly-configured agent should have zero issues.]] - rationale - gateway/tests/test_agent_isolation.py
- [[AgentRegistry]] - code - gateway/security/agent_isolation.py
- [[AgentRegistry must accept group-{chat_id} agent IDs with chat_type metadata.]] - rationale - gateway/tests/test_group_isolation.py
- [[Args             block_threshold Score at or above which input is blocked.]] - rationale - gateway/security/prompt_guard.py
- [[ContainerConfig]] - code - gateway/security/agent_isolation.py
- [[ContainerConfig_1]] - code - gateway/tests/test_agent_isolation.py
- [[Deserialize registry from dict.]] - rationale - gateway/security/agent_isolation.py
- [[Ensure zeroing doesn't break normal encryptdecrypt flow.]] - rationale - gateway/tests/test_security_hardening.py
- [[Full shared-nothing verification network + volume + security settings.]] - rationale - gateway/security/agent_isolation.py
- [[Generate Docker Compose config for all registered agents.]] - rationale - gateway/security/agent_isolation.py
- [[Get container config for an agent.]] - rationale - gateway/security/agent_isolation.py
- [[Helper to create a ContainerConfig with sensible defaults.]] - rationale - gateway/tests/test_agent_isolation.py
- [[IsolationCheck]] - code - gateway/security/agent_isolation.py
- [[IsolationStatus]] - code - gateway/security/agent_isolation.py
- [[IsolationVerifier]] - code - gateway/security/agent_isolation.py
- [[List all registered agent IDs.]] - rationale - gateway/security/agent_isolation.py
- [[PatternRule]] - code - gateway/security/prompt_guard.py
- [[Rapid successes should be capped by rate limiting.]] - rationale - gateway/tests/test_security_hardening.py
- [[Register a group-{chat_id} identity in AgentRegistry.]] - rationale - gateway/tests/test_group_isolation.py
- [[Register a supergroup-type agent identity.]] - rationale - gateway/tests/test_group_isolation.py
- [[Register an agent with its container configuration.]] - rationale - gateway/security/agent_isolation.py
- [[Registry mapping agent IDs to container configurations.]] - rationale - gateway/security/agent_isolation.py
- [[Remove an agent from the registry.]] - rationale - gateway/security/agent_isolation.py
- [[Serialize registry to dict.]] - rationale - gateway/security/agent_isolation.py
- [[TestAgentIsolation]] - code - gateway/tests/test_security_hardening.py
- [[TestAgentRegistry]] - code - gateway/tests/test_agent_isolation.py
- [[TestAgentRegistryGroupIdentity]] - code - gateway/tests/test_group_isolation.py
- [[TestDriftDetectorHardened]] - code - gateway/tests/test_security_hardening.py
- [[TestGenerateCompose]] - code - gateway/tests/test_agent_isolation.py
- [[TestNetworkIsolation]] - code - gateway/tests/test_agent_isolation.py
- [[TestSecureZero]] - code - gateway/tests/test_security_hardening.py
- [[TestSharedNothing]] - code - gateway/tests/test_agent_isolation.py
- [[TestTrustManagerHardened]] - code - gateway/tests/test_security_hardening.py
- [[TestVolumeIsolation]] - code - gateway/tests/test_agent_isolation.py
- [[Tests for drift detector hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for key material zeroing (C2 fix).]] - rationale - gateway/tests/test_security_hardening.py
- [[Tests for trust manager hardening.]] - rationale - gateway/tests/test_security_hardening.py
- [[Two group identities should each have distinct volumes.]] - rationale - gateway/tests/test_group_isolation.py
- [[Unknown event types should not inject SQL.]] - rationale - gateway/tests/test_security_hardening.py
- [[Verify container isolation properties.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own network namespace.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own volume (no shared filesystems).]] - rationale - gateway/security/agent_isolation.py
- [[_make_config()]] - code - gateway/tests/test_agent_isolation.py
- [[agent_isolation.py]] - code - gateway/security/agent_isolation.py
- [[group-{chat_id} and collab-{uid} identities can coexist in the same registry.]] - rationale - gateway/tests/test_group_isolation.py
- [[test_agent_isolation.py]] - code - gateway/tests/test_agent_isolation.py
- [[test_security_hardening.py]] - code - gateway/tests/test_security_hardening.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_52
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Community 11]]
- 16 edges to [[_COMMUNITY_Community 477]]
- 15 edges to [[_COMMUNITY_Community 0]]
- 13 edges to [[_COMMUNITY_Community 146]]
- 11 edges to [[_COMMUNITY_Community 93]]
- 10 edges to [[_COMMUNITY_Community 72]]
- 10 edges to [[_COMMUNITY_Community 17]]
- 8 edges to [[_COMMUNITY_Community 60]]
- 8 edges to [[_COMMUNITY_Community 22]]
- 7 edges to [[_COMMUNITY_Community 104]]
- 7 edges to [[_COMMUNITY_Community 888]]
- 6 edges to [[_COMMUNITY_Community 162]]
- 6 edges to [[_COMMUNITY_Community 1119]]
- 6 edges to [[_COMMUNITY_Community 792]]
- 6 edges to [[_COMMUNITY_Community 947]]
- 5 edges to [[_COMMUNITY_Community 24]]
- 3 edges to [[_COMMUNITY_Community 8]]
- 2 edges to [[_COMMUNITY_Community 516]]
- 2 edges to [[_COMMUNITY_Community 61]]
- 1 edge to [[_COMMUNITY_Community 489]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 684]]
- 1 edge to [[_COMMUNITY_Community 196]]
- 1 edge to [[_COMMUNITY_Community 41]]
- 1 edge to [[_COMMUNITY_Community 509]]
- 1 edge to [[_COMMUNITY_Community 431]]
- 1 edge to [[_COMMUNITY_Community 79]]

## Top bridge nodes
- [[IsolationStatus]] - degree 35, connects to 13 communities
- [[test_security_hardening.py]] - degree 30, connects to 13 communities
- [[AgentRegistry]] - degree 71, connects to 11 communities
- [[IsolationVerifier]] - degree 50, connects to 9 communities
- [[ContainerConfig]] - degree 40, connects to 9 communities