---
type: community
members: 34
---

# lifespan

**Members:** 34 nodes

## Members
- [[dot-filter()]] - code - gateway/ingest_api/lifespan.py
- [[dot-test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise()]] - code - gateway/tests/test_config_validation.py
- [[FastAPI_4]] - code
- [[FastAPI lifespan - startup and shutdown]] - rationale - gateway/ingest_api/lifespan.py
- [[Install warning filter once for uvicorn logger.]] - rationale - gateway/ingest_api/lifespan.py
- [[Lifespan filter should suppress repeated malformed HTTP warning noise.]] - rationale - gateway/tests/test_config_validation.py
- [[LogRecord]] - code
- [[Resolve each configured bot's OWN Telegram token, distinct from the default.…]] - rationale - gateway/ingest_api/lifespan.py
- [[Suppress noisy uvicorn warning spam for malformed probe traffic.]] - rationale - gateway/ingest_api/lifespan.py
- [[_DropInvalidHTTPRequestFilter]] - code - gateway/ingest_api/lifespan.py
- [[_alert_sanitize()]] - code - gateway/ingest_api/lifespan.py
- [[_audit_chain_heartbeat()]] - code - gateway/ingest_api/lifespan.py
- [[_build_per_bot_telegram_tokens()]] - code - gateway/ingest_api/lifespan.py
- [[_check_trivy_report()]] - code - gateway/ingest_api/lifespan.py
- [[_handle()_1]] - code - gateway/ingest_api/lifespan.py
- [[_handle()_2]] - code - gateway/ingest_api/lifespan.py
- [[_install_uvicorn_warning_filter()]] - code - gateway/ingest_api/lifespan.py
- [[_on_config_reload()]] - code - gateway/ingest_api/lifespan.py
- [[_op_authenticate()]] - code - gateway/ingest_api/lifespan.py
- [[_pipe()]] - code - gateway/ingest_api/lifespan.py
- [[_pipe()_1]] - code - gateway/ingest_api/lifespan.py
- [[_prewarm_op()]] - code - gateway/ingest_api/lifespan.py
- [[_report_sanitize()]] - code - gateway/ingest_api/lifespan.py
- [[_resource_alert_bridge()_1]] - code - gateway/ingest_api/lifespan.py
- [[_run_canvas_proxy()]] - code - gateway/ingest_api/lifespan.py
- [[_run_hermes_api_forwarder()]] - code - gateway/ingest_api/lifespan.py
- [[_run_hermes_dashboard_forwarder()]] - code - gateway/ingest_api/lifespan.py
- [[_run_initial_scan_if_needed()]] - code - gateway/ingest_api/lifespan.py
- [[_run_security_scheduler()]] - code - gateway/ingest_api/lifespan.py
- [[_verify_bot_image()]] - code - gateway/ingest_api/lifespan.py
- [[_wazuh_periodic()]] - code - gateway/ingest_api/lifespan.py
- [[client()_12]] - code - gateway/tests/test_mcp_proxy_endpoint.py
- [[fixture_61]] - code
- [[lifespan()]] - code - gateway/ingest_api/lifespan.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/lifespan
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 4 edges to [[_COMMUNITY_app]]
- 3 edges to [[_COMMUNITY_PrivacyPolicyEnforcer]]
- 3 edges to [[_COMMUNITY_KeyVault]]
- 3 edges to [[_COMMUNITY_test_mcp_proxy.py]]
- 3 edges to [[_COMMUNITY_TrustLevel]]
- 3 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_PIISanitizer]]
- 2 edges to [[_COMMUNITY_RateLimitGuard]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_SecurityConfig]]
- 2 edges to [[_COMMUNITY_test_edge_service_routes.py]]
- 2 edges to [[_COMMUNITY_test_dashboard_endpoints.py]]
- 1 edge to [[_COMMUNITY_EventBus]]
- 1 edge to [[_COMMUNITY_DelegationPrivilege]]
- 1 edge to [[_COMMUNITY_ReportStore]]
- 1 edge to [[_COMMUNITY_CronStateMonitor]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_MemoryLifecycleConfig]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_LLMProxy]]
- 1 edge to [[_COMMUNITY_ToolResultInjectionScanner]]
- 1 edge to [[_COMMUNITY_context_guard.py]]
- 1 edge to [[_COMMUNITY_TestParanoidConfig]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_ConfigIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_CanaryTripwire]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_ProgressiveLockdown]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]
- 1 edge to [[_COMMUNITY_OutputSchemaEnforcer]]
- 1 edge to [[_COMMUNITY_GroupRegistry]]
- 1 edge to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_MemoryLifecycleManager]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_CollaboratorActivityTracker]]
- 1 edge to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 1 edge to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_test_memory_lifecycle.py]]
- 1 edge to [[_COMMUNITY_TestConfigValidation]]
- 1 edge to [[_COMMUNITY_AlertTelegramRelay]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_DriftDetector]]
- 1 edge to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_DNSBlocklist]]
- 1 edge to [[_COMMUNITY_NetworkValidator]]
- 1 edge to [[_COMMUNITY_EgressTelegramNotifier]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]
- 1 edge to [[_COMMUNITY_DifferentialPIIDetector]]
- 1 edge to [[_COMMUNITY_service.py]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_HTTPConnectProxy]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_setup_resource_guard]]
- 1 edge to [[_COMMUNITY_test_config_hot_reload.py]]
- 1 edge to [[_COMMUNITY_secrets.py]]
- 1 edge to [[_COMMUNITY_test_dns_canvas_coverage.py]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY__t]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_canary.py]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 1 edge to [[_COMMUNITY_ProxyResult]]

## Top bridge nodes
- [[lifespan()]] - degree 119, connects to 70 communities
- [[_DropInvalidHTTPRequestFilter]] - degree 6, connects to 2 communities
- [[_build_per_bot_telegram_tokens()]] - degree 4, connects to 2 communities
- [[client()_12]] - degree 4, connects to 2 communities
- [[_install_uvicorn_warning_filter()]] - degree 4, connects to 1 community
