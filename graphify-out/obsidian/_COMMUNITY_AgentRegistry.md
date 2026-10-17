---
type: community
members: 69
---

# AgentRegistry

**Members:** 69 nodes

## Members
- [[dot-__init__()_191]] - code - gateway/security/agent_isolation.py
- [[dot-__init__()_192]] - code - gateway/security/agent_isolation.py
- [[dot-from_dict()_8]] - code - gateway/security/agent_isolation.py
- [[dot-register()]] - code - gateway/security/agent_isolation.py
- [[dot-setup_method()_38]] - code - gateway/tests/test_security_hardening.py
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
- [[dot-to_dict()_13]] - code - gateway/security/agent_isolation.py
- [[dot-unregister()]] - code - gateway/security/agent_isolation.py
- [[A single properly-configured agent should have zero issues.]] - rationale - gateway/tests/test_agent_isolation.py
- [[AgentRegistry]] - code - gateway/security/agent_isolation.py
- [[AgentRegistry must accept group-{chat_id} agent IDs with chat_type metadata.]] - rationale - gateway/tests/test_group_isolation.py
- [[ContainerConfig]] - code - gateway/tests/test_agent_isolation.py
- [[ContainerConfig_1]] - code - gateway/security/agent_isolation.py
- [[Deserialize registry from dict.]] - rationale - gateway/security/agent_isolation.py
- [[Helper to create a ContainerConfig with sensible defaults.]] - rationale - gateway/tests/test_agent_isolation.py
- [[IsolationVerifier]] - code - gateway/security/agent_isolation.py
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
- [[_make_config()]] - code - gateway/tests/test_agent_isolation.py
- [[group-{chat_id} and collab-{uid} identities can coexist in the same registry.]] - rationale - gateway/tests/test_group_isolation.py
- [[test_agent_isolation.py]] - code - gateway/tests/test_agent_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentRegistry
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_EgressFilterConfig (3)]]
- 18 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 10 edges to [[_COMMUNITY_AgentRegistry (2)]]
- 8 edges to [[_COMMUNITY_AlertDispatcher]]
- 8 edges to [[_COMMUNITY_RBACConfig]]
- 6 edges to [[_COMMUNITY_agentshroud-blueteamSKILL.md (3)]]
- 6 edges to [[_COMMUNITY_TrustConfig]]
- 4 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 3 edges to [[_COMMUNITY_ContextSegment (2)]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig (4)]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig]]
- 2 edges to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_RBACConfig (3)]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig (2)]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_Path (4)]]

## Top bridge nodes
- [[AgentRegistry]] - degree 71, connects to 10 communities
- [[ContainerConfig_1]] - degree 40, connects to 8 communities
- [[IsolationVerifier]] - degree 50, connects to 7 communities
- [[TestAgentIsolation]] - degree 31, connects to 6 communities
- [[TestAgentRegistryGroupIdentity]] - degree 12, connects to 4 communities
