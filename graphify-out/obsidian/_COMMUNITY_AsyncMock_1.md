---
type: community
cohesion: 0.04
members: 53
---

# AsyncMock

**Cohesion:** 0.04 - loosely connected
**Members:** 53 nodes

## Members
- [[dot-__call__()_3]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-__init__()_33]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-__init__()_34]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-_passthrough_pii()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[dot-mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_close_stops_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_close_swallows_stop_errors()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_close_with_no_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_no_sanitizer_passthrough()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_owner_recipient_body_preserved()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_sanitized_with_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_sanitized_without_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_sanitizer_error_fails_open()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_send_owner_endpoint_also_bypasses_pii()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_store_error_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[AsyncMock]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Create a mock forwarder.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock security pipeline.]] - rationale - gateway/tests/test_session_isolation.py
- [[Minimal async callable for monkeypatching.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestClose]] - code - gateway/tests/test_middleware_coverage.py
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
- 30 edges to [[_COMMUNITY_AsyncMock]]
- 26 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 26 edges to [[_COMMUNITY__make_proxy]]
- 13 edges to [[_COMMUNITY_MiddlewareManager]]
- 11 edges to [[_COMMUNITY_PipelineAction]]
- 9 edges to [[_COMMUNITY_AuditChain]]
- 9 edges to [[_COMMUNITY_test_soc_bots.py]]
- 7 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 7 edges to [[_COMMUNITY_test_clamav_pipeline.py]]
- 6 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 5 edges to [[_COMMUNITY_ModeRequest]]
- 4 edges to [[_COMMUNITY__wrap_response]]
- 4 edges to [[_COMMUNITY_chatbotmain.py]]
- 4 edges to [[_COMMUNITY_DNSBlocklist]]
- 4 edges to [[_COMMUNITY_TestDNSForwarderProtocol]]
- 4 edges to [[_COMMUNITY_test_forward_stream.py_1]]
- 3 edges to [[_COMMUNITY_TestEmailSend]]
- 3 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 3 edges to [[_COMMUNITY_AgentTarget_1]]
- 3 edges to [[_COMMUNITY_StdioConnection]]
- 3 edges to [[_COMMUNITY_SlackSocketClient]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig_4]]
- 3 edges to [[_COMMUNITY__pcm_bytes]]
- 2 edges to [[_COMMUNITY_export_bot_1]]
- 2 edges to [[_COMMUNITY_AgentTarget_2]]
- 2 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 2 edges to [[_COMMUNITY__req]]
- 2 edges to [[_COMMUNITY_UserSessionManager_3]]
- 2 edges to [[_COMMUNITY_TestFabricatedSecurityNotice]]
- 2 edges to [[_COMMUNITY_test_image_verifier.py]]
- 2 edges to [[_COMMUNITY_RateLimitGuard]]
- 2 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 1 edge to [[_COMMUNITY_test_claude_via_openai_path.py]]
- 1 edge to [[_COMMUNITY_test_forward_stream.py]]
- 1 edge to [[_COMMUNITY_test_v1_models_synthetic.py]]
- 1 edge to [[_COMMUNITY_StdioConnection_1]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_RateLimiter]]
- 1 edge to [[_COMMUNITY_ConsentFramework_1]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig_2]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue_2]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_MiddlewareManager_3]]

## Top bridge nodes
- [[AsyncMock]] - degree 219, connects to 37 communities
- [[TestProcessToolResult]] - degree 9, connects to 4 communities
- [[TestClose]] - degree 8, connects to 4 communities
- [[TestOwnerEmailBypassesPii]] - degree 4, connects to 1 community
- [[dot-mock_forwarder()]] - degree 3, connects to 1 community
