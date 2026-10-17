---
type: community
members: 61
---

# agentshroud-blueteam/SKILL.md (3)

**Members:** 61 nodes

## Members
- [[NOTE Gateway-side Slack Socket Mode listener removed.]] - rationale - gateway/ingest_api/lifespan.py
- [[dot-__init__()_25]] - code - gateway/security/prompt_protection.py
- [[dot-_calculate_similarity()]] - code - gateway/security/prompt_protection.py
- [[dot-_compile_detection_patterns()]] - code - gateway/security/prompt_protection.py
- [[dot-_load_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_fuzzy_match()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_match()]] - code - gateway/security/prompt_protection.py
- [[dot-add_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-get_protection_stats()]] - code - gateway/security/prompt_protection.py
- [[dot-register_bot_hostnames()]] - code - gateway/security/prompt_protection.py
- [[dot-scan_response()_1]] - code - gateway/security/prompt_protection.py
- [[dot-test_everything_else_fails_closed_to_enforce()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[dot-test_monitor_token_resolves_monitor()]] - code - gateway/tests/test_progressive_trust_integration.py
- [[A piece of content that should be protected from disclosure.]] - rationale - gateway/security/prompt_protection.py
- [[Add bot container hostnames to the infrastructure detection patterns.          C]] - rationale - gateway/security/prompt_protection.py
- [[Add content to the protected registry.          Args             name Identifi]] - rationale - gateway/security/prompt_protection.py
- [[Any_6]] - code - gateway/security/prompt_protection.py
- [[Attach BufferHandler to the root agentshroud logger.]] - rationale - gateway/web/dashboard_endpoints.py
- [[Calculate similarity between text and protected content.]] - rationale - gateway/security/prompt_protection.py
- [[Compile regex patterns for detecting disclosure attempts.]] - rationale - gateway/security/prompt_protection.py
- [[Create a PromptProtection instance for testing.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Fail-closed resolver for the enforcement-mode env var (SCRUM-78).      Returns]] - rationale - gateway/security/progressive_trust_config.py
- [[FastAPI lifespan - startup and shutdown]] - rationale - gateway/ingest_api/lifespan.py
- [[Get statistics about the protection system.]] - rationale - gateway/security/prompt_protection.py
- [[Hermes API forwarder must include an HTTP-method peek to drop non-HTTP connectio]] - rationale - gateway/tests/test_telegram_executor.py
- [[Initialize prompt protection system.          Args             config Configur]] - rationale - gateway/security/prompt_protection.py
- [[Install warning filter once for uvicorn logger.]] - rationale - gateway/ingest_api/lifespan.py
- [[Load protected content from configured sources.]] - rationale - gateway/security/prompt_protection.py
- [[Log warnings for any core modules running in monitor mode.]] - rationale - gateway/ingest_api/config.py
- [[Main system prompt protection engine.      Maintains fingerprints of sensitive c]] - rationale - gateway/security/prompt_protection.py
- [[Match]] - code - gateway/security/prompt_protection.py
- [[Non-HTTP bytes (e.g. TLS ClientHello) must be dropped without proxying.]] - rationale - gateway/tests/test_telegram_executor.py
- [[PromptProtection]] - code - gateway/security/prompt_protection.py
- [[ProtectedContent]] - code - gateway/security/prompt_protection.py
- [[Redact text that fuzzy matches protected content.]] - rationale - gateway/security/prompt_protection.py
- [[RedactionResult_3]] - code - gateway/security/prompt_protection.py
- [[Replace a regex match with a redaction placeholder.]] - rationale - gateway/security/prompt_protection.py
- [[Resolve each configured bot's OWN Telegram token, distinct from the default.]] - rationale - gateway/ingest_api/lifespan.py
- [[Result of scanning and redacting content.]] - rationale - gateway/security/prompt_protection.py
- [[Return module mode, respecting the global permissive override.]] - rationale - gateway/ingest_api/config.py
- [[Sample protected content for testing.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Scan text for protected content and return redacted version.          Args]] - rationale - gateway/security/prompt_protection.py
- [[System Prompt Protection Tests]] - code - gateway/tests/test_prompt_protection.py
- [[_build_bridge() — test-local reimplementation of the ResourceGuard→AlertDispatcher bridge closure]] - code - gateway/tests/test_resource_guard_wiring.py
- [[_build_per_bot_telegram_tokens()]] - code - gateway/ingest_api/lifespan.py
- [[_install_uvicorn_warning_filter()]] - code - gateway/ingest_api/lifespan.py
- [[check_monitor_mode_warnings()]] - code - gateway/ingest_api/config.py
- [[get_module_mode()]] - code - gateway/ingest_api/config.py
- [[install_log_handler()]] - code - gateway/web/dashboard_endpoints.py
- [[lifespan startup must install ThreadPoolExecutor(max_workers=64).]] - rationale - gateway/tests/test_telegram_executor.py
- [[lifespan()]] - code - gateway/ingest_api/lifespan.py
- [[lifespan.py]] - code - gateway/ingest_api/lifespan.py
- [[prompt_protection()]] - code - gateway/tests/test_prompt_protection.py
- [[prompt_protection.py]] - code - gateway/security/prompt_protection.py
- [[resolve_enforcement_mode()]] - code - gateway/security/progressive_trust_config.py
- [[sample_protected_content()]] - code - gateway/tests/test_prompt_protection.py
- [[test_hermes_forwarder_drops_non_http()]] - code - gateway/tests/test_telegram_executor.py
- [[test_lifespan_hermes_forwarder_has_http_peek()]] - code - gateway/tests/test_telegram_executor.py
- [[test_lifespan_installs_64_worker_executor()]] - code - gateway/tests/test_telegram_executor.py
- [[test_prompt_protection.py]] - code - gateway/tests/test_prompt_protection.py
- [[test_telegram_executor.py]] - code - gateway/tests/test_telegram_executor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/SKILLmd_3
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_AlertDispatcher]]
- 13 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 11 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 10 edges to [[_COMMUNITY_TrustConfig]]
- 8 edges to [[_COMMUNITY_MiddlewareManager (5)]]
- 7 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 6 edges to [[_COMMUNITY_AgentRegistry]]
- 6 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 6 edges to [[_COMMUNITY_AlertDispatcher (2) (4)]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 5 edges to [[_COMMUNITY_ContextSegment]]
- 5 edges to [[_COMMUNITY_AuditChain]]
- 5 edges to [[_COMMUNITY_test_collaborator_tracker.py (3)]]
- 4 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_WebProxyConfig]]
- 4 edges to [[_COMMUNITY_DNSForwarderProtocol]]
- 4 edges to [[_COMMUNITY_TestOutboundInfoFilter]]
- 4 edges to [[_COMMUNITY_RateLimitGuard]]
- 4 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 4 edges to [[_COMMUNITY_TestPromptProtection]]
- 4 edges to [[_COMMUNITY_test_daily_cve_report.py]]
- 3 edges to [[_COMMUNITY_AlertDispatcher (2) (2)]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 3 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 3 edges to [[_COMMUNITY_make_event]]
- 3 edges to [[_COMMUNITY_ReportStore]]
- 3 edges to [[_COMMUNITY_RBACConfig (3)_1]]
- 3 edges to [[_COMMUNITY_dashboard_endpoints.py]]
- 2 edges to [[_COMMUNITY_WebProxy]]
- 2 edges to [[_COMMUNITY_test_llm_proxy_local_parity.py (2)_1]]
- 2 edges to [[_COMMUNITY_ConfigIntegrityMonitor]]
- 2 edges to [[_COMMUNITY_StdioConnection]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (2)_1]]
- 2 edges to [[_COMMUNITY_AlertTelegramRelay]]
- 2 edges to [[_COMMUNITY_CronStateMonitor]]
- 2 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 2 edges to [[_COMMUNITY_DNSBlocklist]]
- 2 edges to [[_COMMUNITY_AgentTarget (2)_1]]
- 2 edges to [[_COMMUNITY_HeuristicClassifier]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 2 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 2 edges to [[_COMMUNITY_EgressTelegramNotifier]]
- 2 edges to [[_COMMUNITY_AuditStore]]
- 2 edges to [[_COMMUNITY_PipelineAction]]
- 2 edges to [[_COMMUNITY_PipelineAction (2)]]
- 2 edges to [[_COMMUNITY_OutputSchemaEnforcer]]
- 2 edges to [[_COMMUNITY_DifferentialPIIDetector]]
- 2 edges to [[_COMMUNITY_DelegationManager]]
- 2 edges to [[_COMMUNITY_RBACConfig (2)]]
- 2 edges to [[_COMMUNITY_EgressFilterConfig (3)]]
- 2 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 2 edges to [[_COMMUNITY_MCPPermissionManager (2)]]
- 2 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor (3)]]
- 1 edge to [[_COMMUNITY_test_prompt_guard.py]]
- 1 edge to [[_COMMUNITY_main.py_1]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]
- 1 edge to [[_COMMUNITY_test_image_verifier.py]]
- 1 edge to [[_COMMUNITY_test_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_canvas_proxy_app]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger]]
- 1 edge to [[_COMMUNITY_test_clamav_pipeline.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_ProxyAction]]
- 1 edge to [[_COMMUNITY_AgentRegistry (2)]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (3)]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_iMessage Integration Fix - Using imsg + imessage-exporter]]

## Top bridge nodes
- [[lifespan.py]] - degree 134, connects to 69 communities
- [[lifespan()]] - degree 83, connects to 50 communities
- [[get_module_mode()]] - degree 14, connects to 6 communities
- [[PromptProtection]] - degree 23, connects to 3 communities
- [[check_monitor_mode_warnings()]] - degree 9, connects to 3 communities
