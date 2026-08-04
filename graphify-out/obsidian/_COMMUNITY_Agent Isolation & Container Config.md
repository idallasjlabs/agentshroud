---
type: community
cohesion: 0.07
members: 73
---

# Agent Isolation & Container Config

**Cohesion:** 0.07 - loosely connected
**Members:** 73 nodes

## Members
- [[.__init__()_40]] - code - gateway/security/agent_isolation.py
- [[.__init__()_41]] - code - gateway/security/agent_isolation.py
- [[.from_dict()_2]] - code - gateway/security/agent_isolation.py
- [[.generate_compose()]] - code - gateway/security/agent_isolation.py
- [[.get()_2]] - code - gateway/security/agent_isolation.py
- [[.list_agents()]] - code - gateway/security/agent_isolation.py
- [[.register()]] - code - gateway/security/agent_isolation.py
- [[.setup_method()_28]] - code - gateway/tests/test_security_hardening.py
- [[.test_capabilities_not_dropped_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_contains_all_agents()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_networks_are_internal()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_compose_security_opts()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_container_config_defaults()]] - code - gateway/tests/test_security_hardening.py
- [[.test_fully_isolated_agents_pass()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_generate_compose()]] - code - gateway/tests/test_security_hardening.py
- [[.test_get_missing_returns_none()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_list_agents()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_list_agents()_1]] - code - gateway/tests/test_security_hardening.py
- [[.test_network_isolation_ok()]] - code - gateway/tests/test_security_hardening.py
- [[.test_network_isolation_violation()]] - code - gateway/tests/test_security_hardening.py
- [[.test_new_privileges_allowed_flagged()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_register_and_get()]] - code - gateway/tests/test_agent_isolation.py
- [[.test_register_and_get()_1]] - code - gateway/tests/test_security_hardening.py
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
- [[.to_dict()_3]] - code - gateway/security/agent_isolation.py
- [[.unregister()]] - code - gateway/security/agent_isolation.py
- [[.verify_network_isolation()]] - code - gateway/security/agent_isolation.py
- [[.verify_shared_nothing()]] - code - gateway/security/agent_isolation.py
- [[.verify_volume_isolation()]] - code - gateway/security/agent_isolation.py
- [[A single properly-configured agent should have zero issues.]] - rationale - gateway/tests/test_agent_isolation.py
- [[AgentRegistry]] - code - gateway/security/agent_isolation.py
- [[ContainerConfig_1]] - code - gateway/tests/test_agent_isolation.py
- [[ContainerConfig]] - code - gateway/security/agent_isolation.py
- [[Deserialize registry from dict.]] - rationale - gateway/security/agent_isolation.py
- [[Full shared-nothing verification network + volume + security settings.]] - rationale - gateway/security/agent_isolation.py
- [[Generate Docker Compose config for all registered agents.]] - rationale - gateway/security/agent_isolation.py
- [[Get container config for an agent.]] - rationale - gateway/security/agent_isolation.py
- [[Helper to create a ContainerConfig with sensible defaults.]] - rationale - gateway/tests/test_agent_isolation.py
- [[IsolationCheck]] - code - gateway/security/agent_isolation.py
- [[IsolationVerifier]] - code - gateway/security/agent_isolation.py
- [[List all registered agent IDs.]] - rationale - gateway/security/agent_isolation.py
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
- [[Verify container isolation properties.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own network namespace.]] - rationale - gateway/security/agent_isolation.py
- [[Verify that each agent has its own volume (no shared filesystems).]] - rationale - gateway/security/agent_isolation.py
- [[_make_config()]] - code - gateway/tests/test_agent_isolation.py
- [[agent_isolation.py]] - code - gateway/security/agent_isolation.py
- [[test_agent_isolation.py]] - code - gateway/tests/test_agent_isolation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agent_Isolation__Container_Config
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_Module Group 79]]
- 10 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 9 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 7 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 5 edges to [[_COMMUNITY_Alert Dispatcher]]
- 4 edges to [[_COMMUNITY_Module Group 88]]
- 4 edges to [[_COMMUNITY_Module Group 66]]
- 3 edges to [[_COMMUNITY_Module Group 323]]
- 3 edges to [[_COMMUNITY_Module Group 285]]
- 3 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 1 edge to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 1 edge to [[_COMMUNITY_Egress Filter & Approval]]
- 1 edge to [[_COMMUNITY_Module Group 71]]
- 1 edge to [[_COMMUNITY_Context Guard & Integrity]]

## Top bridge nodes
- [[TestAgentIsolation]] - degree 31, connects to 9 communities
- [[AgentRegistry]] - degree 62, connects to 8 communities
- [[IsolationVerifier]] - degree 49, connects to 7 communities
- [[ContainerConfig]] - degree 32, connects to 7 communities
- [[agent_isolation.py]] - degree 7, connects to 3 communities
