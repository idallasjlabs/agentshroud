---
type: community
cohesion: 0.07
members: 67
---

# test_mfa_guard.py

**Cohesion:** 0.07 - loosely connected
**Members:** 67 nodes

## Members
- [[.__init__()_51]] - code - gateway/security/agent_isolation.py
- [[.__init__()_52]] - code - gateway/security/agent_isolation.py
- [[.from_dict()_3]] - code - gateway/security/agent_isolation.py
- [[.register()]] - code - gateway/security/agent_isolation.py
- [[.setup_method()_31]] - code - gateway/tests/test_security_hardening.py
- [[.test_capabilities_not_dropped_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_contains_all_agents()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_networks_are_internal()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_security_opts()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_container_config_defaults()]] - code - gateway/tests/test_security_hardening.py
- [[.test_fully_isolated_agents_pass()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_generate_compose()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_missing_returns_none()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_group_agents_are_isolatable()]] - code - gateway/tests/test_group_isolation.py
- [[.test_group_and_collab_identities_coexist()]] - code - gateway/tests/test_group_isolation.py
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
- [[.to_dict()_4]] - code - gateway/security/agent_isolation.py
- [[.unregister()]] - code - gateway/security/agent_isolation.py
- [[A single properly-configured agent should have zero issues.]] - rationale - gateway/tests/test_agent_isolation.py
- [[AgentRegistry]] - code - gateway/security/agent_isolation.py
- [[ContainerConfig_1]] - code - gateway/tests/test_agent_isolation.py
- [[ContainerConfig]] - code - gateway/security/agent_isolation.py
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
TABLE source_file, type FROM #community/test_mfa_guardpy
SORT file.name ASC
```

## Connections to other communities
- 19 edges to [[_COMMUNITY_ConsentFramework]]
- 18 edges to [[_COMMUNITY_lifespan.py]]
- 11 edges to [[_COMMUNITY_TrustManager]]
- 10 edges to [[_COMMUNITY_lvgl_kawaii_face.c]]
- 8 edges to [[_COMMUNITY_test_security_audit.py]]
- 6 edges to [[_COMMUNITY__wrap_response()]]
- 4 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 3 edges to [[_COMMUNITY_A2AGovernanceProxy]]
- 3 edges to [[_COMMUNITY_Local LLM Support — Implementation Review]]
- 3 edges to [[_COMMUNITY_1Password op-proxy (POST credentialsop-proxy;]]
- 2 edges to [[_COMMUNITY_check_message()]]
- 2 edges to [[_COMMUNITY_Core Principles]]
- 2 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_TestAlertDispatcher]]
- 1 edge to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[AgentRegistry]] - degree 71, connects to 12 communities
- [[ContainerConfig]] - degree 40, connects to 11 communities
- [[IsolationVerifier]] - degree 50, connects to 8 communities
- [[TestAgentIsolation]] - degree 31, connects to 8 communities
- [[TestSharedNothing]] - degree 12, connects to 1 community