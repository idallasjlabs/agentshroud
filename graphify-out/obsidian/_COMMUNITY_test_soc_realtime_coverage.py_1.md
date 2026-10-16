---
type: community
cohesion: 0.05
members: 70
---

# test_soc_realtime_coverage.py

**Cohesion:** 0.05 - loosely connected
**Members:** 70 nodes

## Members
- [[dot-__init__()_172]] - code - gateway/soc/services.py
- [[dot-_describe_service()]] - code - gateway/soc/services.py
- [[dot-get_service()]] - code - gateway/soc/services.py
- [[dot-list_services()]] - code - gateway/soc/services.py
- [[dot-test_approved_status()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_confirmation_required()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_construction()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_construction()_1]] - code - gateway/tests/test_soc_models.py
- [[dot-test_construction()_2]] - code - gateway/tests/test_soc_models.py
- [[dot-test_defaults()_1]] - code - gateway/tests/test_soc_models.py
- [[dot-test_destructive_requires_confirmation()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_error_model()]] - code - gateway/tests/test_soc_models.py
- [[dot-test_pending_status_default()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_permission_denied_error()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_red_risk_high_threat()]] - code - gateway/tests/test_soc_egress.py
- [[dot-test_running_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_standby_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_stopped_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_unhealthy_service()]] - code - gateway/tests/test_soc_services.py
- [[dot-test_with_resource_usage()]] - code - gateway/tests/test_soc_models.py
- [[Alarm]] - code - gateway/soc/models.py
- [[Any_67]] - code - gateway/soc/services.py
- [[ContributorRecord_1]] - code - gateway/soc/models.py
- [[EgressRequest]] - code - gateway/soc/models.py
- [[EgressStatus]] - code - gateway/soc/models.py
- [[HealthStatus]] - code - gateway/soc/services.py
- [[HealthStatus_1]] - code - gateway/soc/models.py
- [[Platform]] - code - gateway/soc/models.py
- [[Query Docker daemon directly via Unix socket — no CLI needed.]] - rationale - gateway/soc/services.py
- [[ResourceUsage_1]] - code - gateway/soc/models.py
- [[Return 'running', 'stopped', or 'not_installed' for clamd (CC-01).]] - rationale - gateway/soc/services.py
- [[Return 'running', 'stopped', or 'not_installed' for fluent-bit (CC-01).]] - rationale - gateway/soc/services.py
- [[Return ServiceDescriptor for each known container plus internal gateway services]] - rationale - gateway/soc/services.py
- [[Return the gateway's own container plus each configured bot's real     container]] - rationale - gateway/soc/services.py
- [[RiskLevel_5]] - code - gateway/soc/models.py
- [[SCLError]] - code - gateway/soc/models.py
- [[STANDBY = binary installed but cannot run in this environment; should be healthy]] - rationale - gateway/tests/test_soc_services.py
- [[ServiceDescriptor]] - code - gateway/soc/services.py
- [[ServiceDescriptor_1]] - code - gateway/soc/models.py
- [[ServiceStatus]] - code - gateway/soc/services.py
- [[ServiceStatus_1]] - code - gateway/soc/models.py
- [[TestConfirmationModel]] - code - gateway/tests/test_soc_egress.py
- [[TestContributorRecord]] - code - gateway/tests/test_soc_models.py
- [[TestEgressRequest]] - code - gateway/tests/test_soc_models.py
- [[TestEgressRequestModel]] - code - gateway/tests/test_soc_egress.py
- [[TestSCLError]] - code - gateway/tests/test_soc_models.py
- [[TestServiceDescriptor]] - code - gateway/tests/test_soc_models.py
- [[TestServiceDescriptorDefaults]] - code - gateway/tests/test_soc_services.py
- [[TestWSEvent]] - code - gateway/tests/test_soc_models.py
- [[UserRole]] - code - gateway/soc/models.py
- [[UserRole_1]] - code - gateway/soc/contributors.py
- [[Validate ServiceDescriptor model defaults — no real container calls.]] - rationale - gateway/tests/test_soc_services.py
- [[_INTERNAL_SERVICE_ATTRS (internal gateway service table)]] - code - gateway/soc/services.py
- [[_check_clamd()]] - code - gateway/soc/services.py
- [[_check_fluent_bit()]] - code - gateway/soc/services.py
- [[_check_openscap()]] - code - gateway/soc/services.py
- [[_check_wazuh_agent()]] - code - gateway/soc/services.py
- [[_engine_health_to_health()]] - code - gateway/soc/services.py
- [[_engine_status_to_service_status()]] - code - gateway/soc/services.py
- [[_inspect_via_socket()]] - code - gateway/soc/services.py
- [[_known_services()]] - code - gateway/soc/services.py
- [[_new_uuid()]] - code - gateway/soc/models.py
- [[_now_iso()]] - code - gateway/soc/models.py
- [[_role_enum()]] - code - gateway/soc/contributors.py
- [[contributors.py]] - code - gateway/soc/contributors.py
- [[services.py]] - code - gateway/soc/services.py
- [[socmodels.py]] - code - gateway/soc/models.py
- [[test_soc_egress.py]] - code - gateway/tests/test_soc_egress.py
- [[test_soc_models.py]] - code - gateway/tests/test_soc_models.py
- [[test_soc_services.py]] - code - gateway/tests/test_soc_services.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_realtime_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_ServiceManager]]
- 15 edges to [[_COMMUNITY_socrouter.py]]
- 14 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 8 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 8 edges to [[_COMMUNITY__FakeRBAC]]
- 4 edges to [[_COMMUNITY_test_soc_bots.py_1]]
- 4 edges to [[_COMMUNITY_test_soc_bots.py]]
- 3 edges to [[_COMMUNITY_soc.js]]
- 2 edges to [[_COMMUNITY_start-agentshroud.sh]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig_2]]
- 1 edge to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py_1]]

## Top bridge nodes
- [[socmodels.py]] - degree 29, connects to 4 communities
- [[ServiceDescriptor_1]] - degree 20, connects to 4 communities
- [[ContributorRecord_1]] - degree 10, connects to 4 communities
- [[test_soc_models.py]] - degree 22, connects to 3 communities
- [[services.py]] - degree 16, connects to 3 communities
