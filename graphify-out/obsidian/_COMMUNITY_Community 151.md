---
type: community
members: 65
---

# Community 151

**Members:** 65 nodes

## Members
- [[NOTE Gateway-side Slack Socket Mode listener removed.]] - rationale - gateway/ingest_api/lifespan.py
- [[.__init__()_27]] - code - gateway/ingest_api/event_bus.py
- [[.filter()]] - code - gateway/ingest_api/lifespan.py
- [[.subscribe()]] - code - gateway/ingest_api/event_bus.py
- [[.test_get_module_mode_enforce_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_no_env_override()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_get_module_mode_no_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_get_module_mode_with_override()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_global_monitor_override_downgrades_all()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_monitor_mode_warning_message_format()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_monitor_mode_warnings_all_modules()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_monitor_mode_warnings_no_warnings_in_enforce()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_pii_sanitizer_default_action()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_security_config_all_defaults_enforce()]] - code - gateway/tests/test_enforce_defaults.py
- [[.test_security_config_dns_filter_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_egress_filter_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_egress_monitor_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_killswitch_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_mcp_proxy_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_pii_sanitizer_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_prompt_guard_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_security_config_subagent_monitor_enforce()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.unsubscribe()]] - code - gateway/ingest_api/event_bus.py
- [[3+ auth failures within 5 minutes escalates event severity to critical]] - concept - gateway/tests/test_event_bus.py
- [[AGENTSHROUD_MODE=monitor must downgrade ALL modules to monitor.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[Attach BufferHandler to the root agentshroud logger.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Complete security configuration]] - rationale - gateway/ingest_api/config.py
- [[EventBus]] - code - gateway/ingest_api/event_bus.py
- [[FastAPI_1]] - code - gateway/ingest_api/lifespan.py
- [[FastAPI lifespan - startup and shutdown]] - rationale - gateway/ingest_api/lifespan.py
- [[Hermes API forwarder must include an HTTP-method peek to drop non-HTTP connectio]] - rationale - gateway/tests/test_telegram_executor.py
- [[Install warning filter once for uvicorn logger.]] - rationale - gateway/ingest_api/lifespan.py
- [[Log warnings for any core modules running in monitor mode.]] - rationale - gateway/ingest_api/config.py
- [[LogRecord]] - code - gateway/ingest_api/lifespan.py
- [[Non-HTTP bytes (e.g. TLS ClientHello) must be dropped without proxying.]] - rationale - gateway/tests/test_telegram_executor.py
- [[Resolve each configured bot's OWN Telegram token, distinct from the default.]] - rationale - gateway/ingest_api/lifespan.py
- [[Return module mode, respecting the global permissive override.]] - rationale - gateway/ingest_api/config.py
- [[SecurityConfig_3]] - code - gateway/ingest_api/config.py
- [[Simple in-process event bus with async support]] - rationale - gateway/ingest_api/event_bus.py
- [[Subscribe to all events]] - rationale - gateway/ingest_api/event_bus.py
- [[Suppress noisy uvicorn warning spam for malformed probe traffic.]] - rationale - gateway/ingest_api/lifespan.py
- [[Test get_module_mode returns enforce when explicitly set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns enforce when no override set.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test get_module_mode returns monitor when AGENTSHROUD_MODE=monitor.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that PII sanitizer defaults to redact action.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that all core modules default to enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that monitor mode warnings contain required information.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that no warnings are logged when all modules are in enforce mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[Test that warnings are logged for all core modules in monitor mode.]] - rationale - gateway/tests/test_enforce_defaults.py
- [[TestSecurityConfigDefaults]] - code - gateway/tests/test_all_modules_enforce.py
- [[Unsubscribe from events]] - rationale - gateway/ingest_api/event_bus.py
- [[Verify SecurityConfig and SecurityModuleConfig default to enforce.]] - rationale - gateway/tests/test_all_modules_enforce.py
- [[_DropInvalidHTTPRequestFilter]] - code - gateway/ingest_api/lifespan.py
- [[_build_per_bot_telegram_tokens()]] - code - gateway/ingest_api/lifespan.py
- [[_install_uvicorn_warning_filter()]] - code - gateway/ingest_api/lifespan.py
- [[check_monitor_mode_warnings()]] - code - gateway/ingest_api/config.py
- [[get_module_mode()]] - code - gateway/ingest_api/config.py
- [[install_log_handler()]] - code - gateway/web/dashboard_endpoints.py
- [[lifespan startup must install ThreadPoolExecutor(max_workers=64).]] - rationale - gateway/tests/test_telegram_executor.py
- [[lifespan()_1]] - code - gateway/ingest_api/lifespan.py
- [[lifespan.py]] - code - gateway/ingest_api/lifespan.py
- [[test_hermes_forwarder_drops_non_http()]] - code - gateway/tests/test_telegram_executor.py
- [[test_lifespan_hermes_forwarder_has_http_peek()]] - code - gateway/tests/test_telegram_executor.py
- [[test_lifespan_installs_64_worker_executor()]] - code - gateway/tests/test_telegram_executor.py
- [[test_telegram_executor.py]] - code - gateway/tests/test_telegram_executor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_151
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_Community 7]]
- 27 edges to [[_COMMUNITY_Community 84]]
- 17 edges to [[_COMMUNITY_Community 72]]
- 11 edges to [[_COMMUNITY_Community 52]]
- 10 edges to [[_COMMUNITY_Community 75]]
- 9 edges to [[_COMMUNITY_Community 229]]
- 9 edges to [[_COMMUNITY_Community 85]]
- 8 edges to [[_COMMUNITY_Community 32]]
- 7 edges to [[_COMMUNITY_Community 194]]
- 6 edges to [[_COMMUNITY_Community 11]]
- 5 edges to [[_COMMUNITY_Community 30]]
- 5 edges to [[_COMMUNITY_Community 9]]
- 5 edges to [[_COMMUNITY_Community 1]]
- 5 edges to [[_COMMUNITY_Community 1066]]
- 5 edges to [[_COMMUNITY_Community 1305]]
- 4 edges to [[_COMMUNITY_Community 590]]
- 4 edges to [[_COMMUNITY_Community 27]]
- 4 edges to [[_COMMUNITY_Community 54]]
- 4 edges to [[_COMMUNITY_Community 205]]
- 4 edges to [[_COMMUNITY_Community 684]]
- 4 edges to [[_COMMUNITY_Community 477]]
- 4 edges to [[_COMMUNITY_Community 16]]
- 4 edges to [[_COMMUNITY_Community 206]]
- 3 edges to [[_COMMUNITY_Community 220]]
- 3 edges to [[_COMMUNITY_Community 22]]
- 3 edges to [[_COMMUNITY_Community 17]]
- 3 edges to [[_COMMUNITY_Community 35]]
- 3 edges to [[_COMMUNITY_Community 98]]
- 3 edges to [[_COMMUNITY_Community 97]]
- 3 edges to [[_COMMUNITY_Community 110]]
- 3 edges to [[_COMMUNITY_Community 575]]
- 2 edges to [[_COMMUNITY_Community 41]]
- 2 edges to [[_COMMUNITY_Community 104]]
- 2 edges to [[_COMMUNITY_Community 158]]
- 2 edges to [[_COMMUNITY_Community 81]]
- 2 edges to [[_COMMUNITY_Community 1278]]
- 2 edges to [[_COMMUNITY_Community 64]]
- 2 edges to [[_COMMUNITY_Community 383]]
- 2 edges to [[_COMMUNITY_Community 120]]
- 2 edges to [[_COMMUNITY_Community 557]]
- 2 edges to [[_COMMUNITY_Community 329]]
- 2 edges to [[_COMMUNITY_Community 241]]
- 2 edges to [[_COMMUNITY_Community 113]]
- 2 edges to [[_COMMUNITY_Community 368]]
- 2 edges to [[_COMMUNITY_Community 89]]
- 2 edges to [[_COMMUNITY_Community 56]]
- 2 edges to [[_COMMUNITY_Community 23]]
- 2 edges to [[_COMMUNITY_Community 21]]
- 2 edges to [[_COMMUNITY_Community 187]]
- 2 edges to [[_COMMUNITY_Community 80]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 2 edges to [[_COMMUNITY_Community 71]]
- 2 edges to [[_COMMUNITY_Community 262]]
- 2 edges to [[_COMMUNITY_Community 141]]
- 2 edges to [[_COMMUNITY_Community 532]]
- 2 edges to [[_COMMUNITY_Community 943]]
- 2 edges to [[_COMMUNITY_Community 154]]
- 2 edges to [[_COMMUNITY_Community 431]]
- 2 edges to [[_COMMUNITY_Community 978]]
- 2 edges to [[_COMMUNITY_Community 26]]
- 1 edge to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 1002]]
- 1 edge to [[_COMMUNITY_Community 309]]
- 1 edge to [[_COMMUNITY_Community 794]]
- 1 edge to [[_COMMUNITY_Community 169]]
- 1 edge to [[_COMMUNITY_Community 707]]
- 1 edge to [[_COMMUNITY_Community 595]]
- 1 edge to [[_COMMUNITY_Community 63]]
- 1 edge to [[_COMMUNITY_Community 43]]
- 1 edge to [[_COMMUNITY_Community 1070]]
- 1 edge to [[_COMMUNITY_Community 88]]
- 1 edge to [[_COMMUNITY_Community 127]]
- 1 edge to [[_COMMUNITY_Community 166]]
- 1 edge to [[_COMMUNITY_Community 73]]
- 1 edge to [[_COMMUNITY_Community 102]]
- 1 edge to [[_COMMUNITY_Community 185]]
- 1 edge to [[_COMMUNITY_Community 507]]
- 1 edge to [[_COMMUNITY_Community 311]]
- 1 edge to [[_COMMUNITY_Community 2071]]
- 1 edge to [[_COMMUNITY_Community 131]]
- 1 edge to [[_COMMUNITY_Community 36]]
- 1 edge to [[_COMMUNITY_Community 78]]
- 1 edge to [[_COMMUNITY_Community 31]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 233]]
- 1 edge to [[_COMMUNITY_Community 146]]

## Top bridge nodes
- [[lifespan.py]] - degree 133, connects to 74 communities
- [[lifespan()_1]] - degree 84, connects to 52 communities
- [[TestSecurityConfigDefaults]] - degree 30, connects to 10 communities
- [[_DropInvalidHTTPRequestFilter]] - degree 15, connects to 9 communities
- [[EventBus]] - degree 35, connects to 7 communities