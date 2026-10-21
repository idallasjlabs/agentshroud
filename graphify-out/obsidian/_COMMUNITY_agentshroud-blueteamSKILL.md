---
type: community
members: 45
---

# agentshroud-blueteam/SKILL.md

**Members:** 45 nodes

## Members
- [[NOTE Gateway-side Slack Socket Mode listener removed.]] - rationale - gateway/ingest_api/lifespan.py
- [[dot-filter()]] - code - gateway/ingest_api/lifespan.py
- [[dot-test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise()]] - code - gateway/tests/test_config_validation.py
- [[Application lifespan management for the AgentShroud Gateway]] - rationale - gateway/ingest_api/lifespan.py
- [[FastAPI]] - code
- [[FastAPI lifespan - startup and shutdown]] - rationale - gateway/ingest_api/lifespan.py
- [[Hermes API forwarder must include an HTTP-method peek to drop non-HTTP connectio]] - rationale - gateway/tests/test_telegram_executor.py
- [[Install warning filter once for uvicorn logger.]] - rationale - gateway/ingest_api/lifespan.py
- [[Lifespan filter should suppress repeated malformed HTTP warning noise.]] - rationale - gateway/tests/test_config_validation.py
- [[LogRecord_1]] - code
- [[Non-HTTP bytes (e.g. TLS ClientHello) must be dropped without proxying.]] - rationale - gateway/tests/test_telegram_executor.py
- [[Resolve each configured bot's OWN Telegram token, distinct from the default.…]] - rationale - gateway/ingest_api/lifespan.py
- [[Suppress noisy uvicorn warning spam for malformed probe traffic.]] - rationale - gateway/ingest_api/lifespan.py
- [[_DropInvalidHTTPRequestFilter]] - code - gateway/ingest_api/lifespan.py
- [[_alert_sanitize()]] - code - gateway/ingest_api/lifespan.py
- [[_audit_chain_heartbeat()]] - code - gateway/ingest_api/lifespan.py
- [[_build_bridge() — test-local reimplementation of the ResourceGuard→AlertDispatcher bridge closure]] - code - gateway/tests/test_resource_guard_wiring.py
- [[_build_per_bot_telegram_tokens()]] - code - gateway/ingest_api/lifespan.py
- [[_check_trivy_report()]] - code - gateway/ingest_api/lifespan.py
- [[_handle()]] - code - gateway/ingest_api/lifespan.py
- [[_handle()_1]] - code - gateway/ingest_api/lifespan.py
- [[_install_uvicorn_warning_filter()]] - code - gateway/ingest_api/lifespan.py
- [[_on_config_reload()]] - code - gateway/ingest_api/lifespan.py
- [[_op_authenticate()]] - code - gateway/ingest_api/lifespan.py
- [[_pipe()]] - code - gateway/ingest_api/lifespan.py
- [[_pipe()_1]] - code - gateway/ingest_api/lifespan.py
- [[_prewarm_op()]] - code - gateway/ingest_api/lifespan.py
- [[_report_sanitize()]] - code - gateway/ingest_api/lifespan.py
- [[_resource_alert_bridge()]] - code - gateway/ingest_api/lifespan.py
- [[_run_canvas_proxy()]] - code - gateway/ingest_api/lifespan.py
- [[_run_hermes_api_forwarder()]] - code - gateway/ingest_api/lifespan.py
- [[_run_hermes_dashboard_forwarder()]] - code - gateway/ingest_api/lifespan.py
- [[_run_initial_scan_if_needed()]] - code - gateway/ingest_api/lifespan.py
- [[_run_security_scheduler()]] - code - gateway/ingest_api/lifespan.py
- [[_startup_scanner()]] - code - gateway/ingest_api/lifespan.py
- [[_store_result()]] - code - gateway/ingest_api/lifespan.py
- [[_verify_bot_image()]] - code - gateway/ingest_api/lifespan.py
- [[_wazuh_periodic()]] - code - gateway/ingest_api/lifespan.py
- [[lifespan startup must install ThreadPoolExecutor(max_workers=64).]] - rationale - gateway/tests/test_telegram_executor.py
- [[lifespan()]] - code - gateway/ingest_api/lifespan.py
- [[lifespan.py]] - code - gateway/ingest_api/lifespan.py
- [[test_hermes_forwarder_drops_non_http()]] - code - gateway/tests/test_telegram_executor.py
- [[test_lifespan_hermes_forwarder_has_http_peek()]] - code - gateway/tests/test_telegram_executor.py
- [[test_lifespan_installs_64_worker_executor()]] - code - gateway/tests/test_telegram_executor.py
- [[test_telegram_executor.py]] - code - gateway/tests/test_telegram_executor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_climain.py]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 2 edges to [[_COMMUNITY_Browser — Secure Browser Automation (SKILL)]]
- 1 edge to [[_COMMUNITY_hermesskillsi-crSKILL]]
- 1 edge to [[_COMMUNITY_MCPPermissionManager]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (4)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (2) (2)]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_dot-_make_proxy()]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]

## Top bridge nodes
- [[lifespan.py]] - degree 20, connects to 9 communities
- [[lifespan()]] - degree 28, connects to 7 communities
- [[_DropInvalidHTTPRequestFilter]] - degree 6, connects to 1 community
- [[FastAPI]] - degree 3, connects to 1 community
- [[dot-test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise()]] - degree 3, connects to 1 community
