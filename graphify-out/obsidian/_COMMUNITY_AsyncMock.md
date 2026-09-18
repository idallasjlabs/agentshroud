---
type: community
cohesion: 0.03
members: 62
---

# AsyncMock

**Cohesion:** 0.03 - loosely connected
**Members:** 62 nodes

## Members
- [[.__call__()_5]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.__init__()_110]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.__init__()_112]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[._passthrough_pii()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[.mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[.mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[.test_approval_decision()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_approval_queue_list()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_close_stops_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_close_swallows_stop_errors()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_google_proxy_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_google_proxy_non_json_body_passthrough()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_mcp_proxy_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_no_sanitizer_passthrough()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_owner_recipient_body_preserved()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[.test_sanitized_with_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_sanitized_without_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_sanitizer_error_fails_open()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_send_owner_endpoint_also_bypasses_pii()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[.test_status_endpoint()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[AsyncMock]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Create a mock forwarder.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock security pipeline.]] - rationale - gateway/tests/test_session_isolation.py
- [[JSON upstream responses must stay JSON.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Minimal async callable for monkeypatching.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[Plain-text upstream errors must not turn into gateway 500s.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test MCP proxy endpoint basic functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test basic status endpoint functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test listing pending approvals.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test making approval decisions.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestOwnerEmailBypassesPii]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestProcessToolResult]] - code - gateway/tests/test_middleware_coverage.py
- [[Unknown recipient's body is PII-scrubbed before approval queue submission.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[test_approvals_approve_and_deny()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_approvals_approve_raises()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_audit_export_cef()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_audit_export_exporter_raises()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_audit_export_json_dict_payload()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_cve_report_queued()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_approve_missing_or_raises()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_approve_mode_mapping()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_history_revoke()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_history_with_bot_filter()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_pending_non_list_and_missing()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_pending_queue_raises()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_pending_with_bot_filter()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_rule_override_scoped()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_rule_remove()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_rules_fallback_empty()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_egress_rules_source_tagging()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_launch_scan_background_exec_failure()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_launch_scan_background_success()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_log_audit_appends_to_audit_store()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_rollback_gateway_paths()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_run_scanner_validation_and_launch()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_ssh_compose_success()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_ssh_compose_timeout_and_exception()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_bot_paths()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_gateway_paths()]] - code - gateway/tests/test_soc_router_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AsyncMock
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_SlackAPIProxy]]
- 26 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 26 edges to [[_COMMUNITY__make_proxy()]]
- 10 edges to [[_COMMUNITY_KeyVaultConfig]]
- 9 edges to [[_COMMUNITY_PipelineAction]]
- 9 edges to [[_COMMUNITY_test_soc_bots.py]]
- 8 edges to [[_COMMUNITY_ingest_apimain.py]]
- 7 edges to [[_COMMUNITY_SOCWebSocketHandler]]
- 7 edges to [[_COMMUNITY_MiddlewareManager]]
- 7 edges to [[_COMMUNITY_test_clamav_pipeline.py]]
- 5 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 5 edges to [[_COMMUNITY_ModeRequest]]
- 4 edges to [[_COMMUNITY__make_stream_app_state()]]
- 4 edges to [[_COMMUNITY_DNSBlocklist]]
- 4 edges to [[_COMMUNITY_chatbotmain.py]]
- 4 edges to [[_COMMUNITY_TestDNSForwarderProtocol]]
- 4 edges to [[_COMMUNITY__wrap_response()]]
- 3 edges to [[_COMMUNITY_TestFromAuditChainEntry]]
- 3 edges to [[_COMMUNITY_AgentTarget]]
- 3 edges to [[_COMMUNITY_StdioConnection]]
- 3 edges to [[_COMMUNITY_SlackSocketClient]]
- 3 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 3 edges to [[_COMMUNITY_TestEmailSend]]
- 3 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TestForwardEndpoint]]
- 2 edges to [[_COMMUNITY_AuditChain]]
- 2 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_BotConfig]]
- 2 edges to [[_COMMUNITY_RateLimitGuard]]
- 2 edges to [[_COMMUNITY_test_approval_queue.py]]
- 2 edges to [[_COMMUNITY_test_image_verifier.py]]
- 1 edge to [[_COMMUNITY_FakeProcess]]
- 1 edge to [[_COMMUNITY_test_v1_models_synthetic.py]]
- 1 edge to [[_COMMUNITY_forward.py]]
- 1 edge to [[_COMMUNITY_RateLimiter]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_test_claude_via_openai_path.py]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_falco_monitor.py]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[AsyncMock]] - degree 220, connects to 38 communities
- [[TestProcessToolResult]] - degree 9, connects to 3 communities
- [[TestOwnerEmailBypassesPii]] - degree 4, connects to 1 community
- [[.test_approval_decision()]] - degree 3, connects to 1 community
- [[.test_approval_queue_list()]] - degree 3, connects to 1 community