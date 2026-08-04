---
type: community
cohesion: 0.06
members: 64
---

# SOC Services & Health Status

**Cohesion:** 0.06 - loosely connected
**Members:** 64 nodes

## Members
- [[.__init__()_105]] - code - gateway/soc/services.py
- [[._build_record()]] - code - gateway/soc/contributors.py
- [[._describe_service()]] - code - gateway/soc/services.py
- [[._ensure_rbac()]] - code - gateway/soc/contributors.py
- [[._ensure_teams()]] - code - gateway/soc/contributors.py
- [[.get_contributor()]] - code - gateway/soc/contributors.py
- [[.get_service()]] - code - gateway/soc/services.py
- [[.list_contributors()]] - code - gateway/soc/contributors.py
- [[.list_services()]] - code - gateway/soc/services.py
- [[.test_construction()_1]] - code - gateway/tests/test_soc_models.py
- [[.test_construction()_2]] - code - gateway/tests/test_soc_models.py
- [[.test_defaults()_2]] - code - gateway/tests/test_soc_models.py
- [[.test_import()]] - code - gateway/tests/test_soc_services.py
- [[.test_instantiate_without_engine()]] - code - gateway/tests/test_soc_services.py
- [[.test_running_service()]] - code - gateway/tests/test_soc_services.py
- [[.test_standby_service()]] - code - gateway/tests/test_soc_services.py
- [[.test_stopped_service()]] - code - gateway/tests/test_soc_services.py
- [[.test_unhealthy_service()]] - code - gateway/tests/test_soc_services.py
- [[.test_with_resource_usage()]] - code - gateway/tests/test_soc_models.py
- [[Alarm]] - code - gateway/soc/models.py
- [[Any_61]] - code - gateway/soc/services.py
- [[ContributorRecord]] - code - gateway/soc/contributors.py
- [[ContributorRecord_1]] - code - gateway/soc/models.py
- [[HealthStatus_1]] - code - gateway/soc/services.py
- [[HealthStatus]] - code - gateway/soc/models.py
- [[Platform]] - code - gateway/soc/models.py
- [[Query Docker daemon directly via Unix socket — no CLI needed.]] - rationale - gateway/soc/services.py
- [[ResourceUsage_1]] - code - gateway/soc/models.py
- [[Return 'running', 'stopped', or 'not_installed' for clamd (CC-01).]] - rationale - gateway/soc/services.py
- [[Return 'running', 'stopped', or 'not_installed' for fluent-bit (CC-01).]] - rationale - gateway/soc/services.py
- [[Return 'running', 'stopped', or 'not_installed' for openscap (CC-01).]] - rationale - gateway/soc/services.py
- [[Return 'running', 'stopped', or 'not_installed' for wazuh-agentd (CC-01).]] - rationale - gateway/soc/services.py
- [[Return ServiceDescriptor for each known container plus internal gateway services]] - rationale - gateway/soc/services.py
- [[STANDBY = binary installed but cannot run in this environment; should be healthy]] - rationale - gateway/tests/test_soc_services.py
- [[ServiceDescriptor_1]] - code - gateway/soc/services.py
- [[ServiceDescriptor]] - code - gateway/soc/models.py
- [[ServiceStatus_1]] - code - gateway/soc/services.py
- [[ServiceStatus]] - code - gateway/soc/models.py
- [[TestContributorRecord]] - code - gateway/tests/test_soc_models.py
- [[TestServiceDescriptor]] - code - gateway/tests/test_soc_models.py
- [[TestServiceDescriptorDefaults]] - code - gateway/tests/test_soc_services.py
- [[TestServiceManagerImport]] - code - gateway/tests/test_soc_services.py
- [[TestWSEvent]] - code - gateway/tests/test_soc_models.py
- [[UserRole_1]] - code - gateway/soc/models.py
- [[UserRole]] - code - gateway/soc/contributors.py
- [[Validate ServiceDescriptor model defaults — no real container calls.]] - rationale - gateway/tests/test_soc_services.py
- [[Verify ServiceManager can be imported without a running container engine.]] - rationale - gateway/tests/test_soc_services.py
- [[WSEvent]] - code - gateway/soc/models.py
- [[_check_clamd()]] - code - gateway/soc/services.py
- [[_check_fluent_bit()]] - code - gateway/soc/services.py
- [[_check_openscap()]] - code - gateway/soc/services.py
- [[_check_wazuh_agent()]] - code - gateway/soc/services.py
- [[_engine_health_to_health()]] - code - gateway/soc/services.py
- [[_engine_status_to_service_status()]] - code - gateway/soc/services.py
- [[_inspect_via_socket()]] - code - gateway/soc/services.py
- [[_new_uuid()]] - code - gateway/soc/models.py
- [[_now_iso()]] - code - gateway/soc/models.py
- [[_role_enum()]] - code - gateway/soc/contributors.py
- [[contributors.py]] - code - gateway/soc/contributors.py
- [[models.py_1]] - code - gateway/soc/models.py
- [[services.py]] - code - gateway/soc/services.py
- [[test_soc_models.py]] - code - gateway/tests/test_soc_models.py
- [[test_soc_services.py]] - code - gateway/tests/test_soc_services.py
- [[websocket.py]] - code - gateway/soc/websocket.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SOC_Services__Health_Status
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_Module Group 83]]
- 19 edges to [[_COMMUNITY_SOC Services]]
- 17 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 4 edges to [[_COMMUNITY_SOC Authentication]]
- 4 edges to [[_COMMUNITY_Module Group 206]]
- 4 edges to [[_COMMUNITY_SOC Bots & CVE Management]]
- 3 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 3 edges to [[_COMMUNITY_Module Group 270]]
- 2 edges to [[_COMMUNITY_Module Group 120]]
- 2 edges to [[_COMMUNITY_Module Group 207]]
- 1 edge to [[_COMMUNITY_RBAC Configuration]]
- 1 edge to [[_COMMUNITY_SOC Router & Correlation]]

## Top bridge nodes
- [[websocket.py]] - degree 11, connects to 6 communities
- [[WSEvent]] - degree 13, connects to 5 communities
- [[models.py_1]] - degree 29, connects to 4 communities
- [[test_soc_models.py]] - degree 22, connects to 3 communities
- [[ServiceDescriptor]] - degree 19, connects to 3 communities
