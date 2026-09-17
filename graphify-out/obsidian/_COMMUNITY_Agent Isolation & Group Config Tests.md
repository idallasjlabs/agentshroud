---
type: community
cohesion: 0.04
members: 104
---

# Agent Isolation & Group Config Tests

**Cohesion:** 0.04 - loosely connected
**Members:** 104 nodes

## Members
- [[dot-__init__()_126]] - code - gateway/security/agent_isolation.py
- [[dot-__init__()_127]] - code - gateway/security/agent_isolation.py
- [[dot-from_dict()_3]] - code - gateway/security/agent_isolation.py
- [[dot-generate_compose()]] - code - gateway/security/agent_isolation.py
- [[dot-get()_1]] - code - gateway/security/agent_isolation.py
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
- [[dot-test_get_missing_returns_none()]] - code - gateway/tests/test_agent_isolation.py
- [[dot-test_group_a_write_invisible_from_group_b()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_agents_are_isolatable()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_and_collab_identities_coexist()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_b_write_invisible_from_group_a()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_id_uses_group_prefix_namespace()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_memory_physically_isolated()]] - code - gateway/tests/test_group_isolation.py
- [[dot-test_group_writes_are_independent_namespaces()]] - code - gateway/tests/test_group_isolation.py
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
- [[dot-to_dict()_9]] - code - gateway/security/agent_isolation.py
- [[dot-unregister()]] - code - gateway/security/agent_isolation.py
- [[dot-verify_network_isolation()]] - code - gateway/security/agent_isolation.py
- [[dot-verify_shared_nothing()]] - code - gateway/security/agent_isolation.py
- [[dot-verify_volume_isolation()]] - code - gateway/security/agent_isolation.py
- [[A single properly-configured agent should have zero issues.]] - rationale - gateway/tests/test_agent_isolation.py
- [[AgentRegistry]] - code - gateway/security/agent_isolation.py
- [[AgentRegistry must accept group-{chat_id} agent IDs with chat_type metadata.]] - rationale - gateway/tests/test_group_isolation.py
- [[Both groups store separate content with no cross-contamination.]] - rationale - gateway/tests/test_group_isolation.py
- [[ContainerConfig]] - code - gateway/tests/test_agent_isolation.py
- [[ContainerConfig_1]] - code - gateway/security/agent_isolation.py
- [[Content appended to group-A memory must not appear in group-B memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Content appended to group-B must not appear in group-A memory.]] - rationale - gateway/tests/test_group_isolation.py
- [[Deserialize registry from dict.]] - rationale - gateway/security/agent_isolation.py
- [[Full shared-nothing verification network + volume + security settings.]] - rationale - gateway/security/agent_isolation.py
- [[Generate Docker Compose config for all registered agents.]] - rationale - gateway/security/agent_isolation.py
- [[Get container config for an agent.]] - rationale - gateway/security/agent_isolation.py
- [[Helper to create a ContainerConfig with sensible defaults.]] - rationale - gateway/tests/test_agent_isolation.py
- [[IsolationCheck]] - code - gateway/security/agent_isolation.py
- [[IsolationStatus]] - code - gateway/security/agent_isolation.py
- [[IsolationVerifier]] - code - gateway/security/agent_isolation.py
- [[List all registered agent IDs.]] - rationale - gateway/security/agent_isolation.py
- [[Register a group-{chat_id} identity in AgentRegistry.]] - rationale - gateway/tests/test_group_isolation.py
- [[Register a supergroup-type agent identity.]] - rationale - gateway/tests/test_group_isolation.py
- [[Register an agent with its container configuration.]] - rationale - gateway/security/agent_isolation.py
- [[Registry mapping agent IDs to container configurations.]] - rationale - gateway/security/agent_isolation.py
- [[Remove an agent from the registry.]] - rationale - gateway/security/agent_isolation.py
- [[Serialize registry to dict.]] - rationale - gateway/security/agent_isolation.py
- [[Test Group Config]] - code - gateway/tests/test_group_config.py
- [[TestAgentIsolation]] - code - gateway/tests/test_security_hardening.py
- [[TestAgentRegistry]] - code - gateway/tests/test_agent_isolation.py
- [[TestAgentRegistryGroupIdentity]] - code - gateway/tests/test_group_isolation.py
- [[TestGenerateCompose]] - code - gateway/tests/test_agent_isolation.py
- [[TestGroupMemoryNamespaceIsolation]] - code - gateway/tests/test_group_isolation.py
- [[TestNetworkIsolation]] - code - gateway/tests/test_agent_isolation.py
- [[TestSharedNothing]] - code - gateway/tests/test_agent_isolation.py
- [[TestVolumeIsolation]] - code - gateway/tests/test_agent_isolation.py
- [[Two group identities should each have distinct volumes.]] - rationale - gateway/tests/test_group_isolation.py
- [[Verify container isolation properties.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own network namespace.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own volume (no shared filesystems).]] - rationale - gateway/security/agent_isolation.py
- [[Writes in group-A must not be readable from group-B.]] - rationale - gateway/tests/test_group_isolation.py
- [[_make_config()]] - code - gateway/tests/test_agent_isolation.py
- [[agent_isolation.py]] - code - gateway/security/agent_isolation.py
- [[agent_isolation.py (AgentRegistry)]] - code - gateway/security/agent_isolation.py
- [[group-A and group-B memory files must be in separate directories.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-{chat_id} and collab-{uid} identities can coexist in the same registry.]] - rationale - gateway/tests/test_group_isolation.py
- [[group-{chat_id} sessions must live under the 'groups' subdirectory.]] - rationale - gateway/tests/test_group_isolation.py
- [[rbac()_1]] - code - gateway/tests/test_group_isolation.py
- [[session_manager()]] - code - gateway/tests/test_group_isolation.py
- [[shared_memory()]] - code - gateway/tests/test_group_isolation.py
- [[teams()_2]] - code - gateway/tests/test_group_isolation.py
- [[test_agent_isolation.py]] - code - gateway/tests/test_agent_isolation.py
- [[test_group_isolation.py]] - code - gateway/tests/test_group_isolation.py
- [[tmp_workspace()]] - code - gateway/tests/test_group_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agent_Isolation__Group_Config_Tests
SORT file.name ASC
```

## Connections to other communities
- 40 edges to [[_COMMUNITY_Encrypted Store & Drift Detector]]
- 15 edges to [[_COMMUNITY_Alert Dispatcher & RBAC Reliability]]
- 9 edges to [[_COMMUNITY_P3 Infrastructure Security Modules]]
- 7 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 5 edges to [[_COMMUNITY_Community 182]]
- 5 edges to [[_COMMUNITY_Prompt Guard & Context Integrity]]
- 5 edges to [[_COMMUNITY_Ingest Middleware & File Sandbox]]
- 5 edges to [[_COMMUNITY_Community 41]]
- 4 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 4 edges to [[_COMMUNITY_TeamsGroup Collaborator Responses]]
- 3 edges to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 3 edges to [[_COMMUNITY_Voice Gateway STT & Browser Security]]
- 3 edges to [[_COMMUNITY_Community 909]]
- 2 edges to [[_COMMUNITY_Community 611]]
- 1 edge to [[_COMMUNITY_Community 52]]
- 1 edge to [[_COMMUNITY_BlueRed Team Security Auditor Skills]]
- 1 edge to [[_COMMUNITY_Signed Instruction Envelopes & Security Pipeline]]
- 1 edge to [[_COMMUNITY_Community 167]]
- 1 edge to [[_COMMUNITY_Community 185]]
- 1 edge to [[_COMMUNITY_Community 56]]
- 1 edge to [[_COMMUNITY_Community 565]]
- 1 edge to [[_COMMUNITY_Community 475]]
- 1 edge to [[_COMMUNITY_File Sandbox & Privilege Separation Tests]]
- 1 edge to [[_COMMUNITY_Community 48]]
- 1 edge to [[_COMMUNITY_Session Manager & PIIContext Guard]]

## Top bridge nodes
- [[TestAgentIsolation]] - degree 31, connects to 9 communities
- [[IsolationStatus]] - degree 35, connects to 8 communities
- [[AgentRegistry]] - degree 71, connects to 7 communities
- [[agent_isolation.py]] - degree 13, connects to 7 communities
- [[test_group_isolation.py]] - degree 18, connects to 6 communities