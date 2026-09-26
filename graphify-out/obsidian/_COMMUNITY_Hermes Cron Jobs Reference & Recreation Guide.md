---
type: community
cohesion: 0.06
members: 46
---

# Hermes Cron Jobs Reference & Recreation Guide

**Cohesion:** 0.06 - loosely connected
**Members:** 46 nodes

## Members
- [[.__init__()_131]] - code - gateway/soc/services.py
- [[._describe_service()]] - code - gateway/soc/services.py
- [[.get_service()]] - code - gateway/soc/services.py
- [[.list_services()]] - code - gateway/soc/services.py
- [[.mgr_with_engine()]] - code - gateway/tests/test_soc_services.py
- [[.test_defaults()_2]] - code - gateway/tests/test_soc_models.py
- [[.test_get_logs_module_filter_case_insensitive()]] - code - gateway/tests/test_soc_services.py
- [[.test_get_logs_module_filter_empty_returns_all()]] - code - gateway/tests/test_soc_services.py
- [[.test_get_logs_module_filter_excludes_non_matching()]] - code - gateway/tests/test_soc_services.py
- [[.test_get_logs_module_filter_keeps_matching_lines()]] - code - gateway/tests/test_soc_services.py
- [[.test_get_logs_no_engine_returns_empty()]] - code - gateway/tests/test_soc_services.py
- [[.test_get_logs_no_filter_returns_tail()]] - code - gateway/tests/test_soc_services.py
- [[.test_import()]] - code - gateway/tests/test_soc_services.py
- [[.test_instantiate_without_engine()]] - code - gateway/tests/test_soc_services.py
- [[.test_running_service()]] - code - gateway/tests/test_soc_services.py
- [[.test_standby_service()]] - code - gateway/tests/test_soc_services.py
- [[.test_stopped_service()]] - code - gateway/tests/test_soc_services.py
- [[.test_unhealthy_service()]] - code - gateway/tests/test_soc_services.py
- [[.test_with_resource_usage()]] - code - gateway/tests/test_soc_models.py
- [[Any_68]] - code - gateway/soc/services.py
- [[Query Docker daemon directly via Unix socket — no CLI needed.]] - rationale - gateway/soc/services.py
- [[Return 'running', 'stopped', or 'not_installed' for clamd (CC-01).]] - rationale - gateway/soc/services.py
- [[Return 'running', 'stopped', or 'not_installed' for fluent-bit (CC-01).]] - rationale - gateway/soc/services.py
- [[Return ServiceDescriptor for each known container plus internal gateway services]] - rationale - gateway/soc/services.py
- [[Return the gateway's own container plus each configured bot's real     container]] - rationale - gateway/soc/services.py
- [[STANDBY = binary installed but cannot run in this environment; should be healthy]] - rationale - gateway/tests/test_soc_services.py
- [[ServiceDescriptor_1]] - code - gateway/soc/services.py
- [[ServiceDescriptor]] - code - gateway/soc/models.py
- [[TestServiceDescriptor]] - code - gateway/tests/test_soc_models.py
- [[TestServiceDescriptorDefaults]] - code - gateway/tests/test_soc_services.py
- [[TestServiceManagerGetLogs]] - code - gateway/tests/test_soc_services.py
- [[TestServiceManagerImport]] - code - gateway/tests/test_soc_services.py
- [[Unit tests for ServiceManager.get_logs — including module_filter behaviour.]] - rationale - gateway/tests/test_soc_services.py
- [[Validate ServiceDescriptor model defaults — no real container calls.]] - rationale - gateway/tests/test_soc_services.py
- [[Verify ServiceManager can be imported without a running container engine.]] - rationale - gateway/tests/test_soc_services.py
- [[_INTERNAL_SERVICE_ATTRS (internal gateway service table)]] - code - gateway/soc/services.py
- [[_check_clamd()]] - code - gateway/soc/services.py
- [[_check_fluent_bit()]] - code - gateway/soc/services.py
- [[_check_openscap()]] - code - gateway/soc/services.py
- [[_check_wazuh_agent()]] - code - gateway/soc/services.py
- [[_engine_health_to_health()]] - code - gateway/soc/services.py
- [[_engine_status_to_service_status()]] - code - gateway/soc/services.py
- [[_inspect_via_socket()]] - code - gateway/soc/services.py
- [[_known_services()]] - code - gateway/soc/services.py
- [[services.py]] - code - gateway/soc/services.py
- [[test_soc_services.py]] - code - gateway/tests/test_soc_services.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Hermes_Cron_Jobs_Reference__Recreation_Guide
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_main.rs]]
- 17 edges to [[_COMMUNITY_EncryptedStore]]
- 3 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_What You Must Do When Invoked]]
- 2 edges to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_RuntimeConfig]]

## Top bridge nodes
- [[ServiceDescriptor]] - degree 20, connects to 4 communities
- [[services.py]] - degree 16, connects to 4 communities
- [[.list_services()]] - degree 8, connects to 2 communities
- [[Any_68]] - degree 7, connects to 2 communities
- [[test_soc_services.py]] - degree 7, connects to 2 communities