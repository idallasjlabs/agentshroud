---
type: community
members: 73
---

# AsyncMock

**Members:** 73 nodes

## Members
- [[dot-__call__()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-__init__()_7]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-__init__()_181]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-_passthrough_pii()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[dot-mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[dot-test_cached_corr_without_colon_falls_back_to_channel()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cached_inbound_corr_skips_history_lookup()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_close_stops_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_close_swallows_stop_errors()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_close_with_no_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_dm_reply_recovers_inbound_via_conversations_history()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_history_error_records_outbound_without_correlation()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_missing_channel_or_text_skips_tracking()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_no_sanitizer_passthrough()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_owner_recipient_body_preserved()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_recovery_exception_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_sanitized_with_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_sanitized_without_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_sanitizer_error_fails_open()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_send_owner_endpoint_also_bypasses_pii()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_structured_text_serialized_for_preview()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_system_message_not_tracked()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_thread_reply_recovers_inbound_via_conversations_replies()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_tracker_exception_does_not_break_response()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[A dict text payload is JSON-serialized before the 80-char preview.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[AsyncMock]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Cached correlation for the channel → no Slack history call; outbound         is]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Correlation ID with no '' separator → outbound attributed to channel id.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Create a mock forwarder.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock security pipeline.]] - rationale - gateway/tests/test_session_isolation.py
- [[Exception during inbound recovery → swallowed; outbound still recorded.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[History lookup returns ok=False → no inbound record; outbound still         logg]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Minimal async callable for monkeypatching.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Non-thread reply → conversations.history lookup; bot and subtype         message]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestClose]] - code - gateway/tests/test_middleware_coverage.py
- [[TestOutboundTracking]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestOwnerEmailBypassesPii]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestProcessToolResult]] - code - gateway/tests/test_middleware_coverage.py
- [[Thread reply with no cached corr → conversations.replies lookup recovers]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Tracker errors are non-fatal — Slack response still returned to bot.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Unknown recipient's body is PII-scrubbed before approval queue submission.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[chat.postMessage without channeltext → nothing recorded, no lookups.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[is_system=True chat.postMessage bypasses the tracker entirely.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
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
- 32 edges to [[_COMMUNITY_AsyncMock (2)]]
- 26 edges to [[_COMMUNITY__make_proxy]]
- 26 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 13 edges to [[_COMMUNITY_SecurityPipeline]]
- 9 edges to [[_COMMUNITY_test_soc_bots.py]]
- 9 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 9 edges to [[_COMMUNITY_PipelineAction (2)]]
- 6 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 5 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 5 edges to [[_COMMUNITY_ModeRequest]]
- 4 edges to [[_COMMUNITY_chatbotmain.py]]
- 4 edges to [[_COMMUNITY_DNSBlocklist]]
- 4 edges to [[_COMMUNITY_TestDNSForwarderProtocol]]
- 4 edges to [[_COMMUNITY_test_forward_stream.py]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 3 edges to [[_COMMUNITY_TestEmailSend]]
- 3 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 3 edges to [[_COMMUNITY_StdioConnection (2)]]
- 3 edges to [[_COMMUNITY_SlackSocketClient]]
- 3 edges to [[_COMMUNITY_export_bot]]
- 3 edges to [[_COMMUNITY_ApprovalQueueConfig (6)]]
- 3 edges to [[_COMMUNITY__pcm_bytes]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig (5)]]
- 2 edges to [[_COMMUNITY_AgentTarget (3)]]
- 2 edges to [[_COMMUNITY_test_image_verifier.py]]
- 2 edges to [[_COMMUNITY_RateLimitGuard]]
- 2 edges to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_UserSessionManager]]
- 2 edges to [[_COMMUNITY_TestFabricatedSecurityNotice]]
- 2 edges to [[_COMMUNITY__req (2)]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 1 edge to [[_COMMUNITY_test_claude_via_openai_path.py]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue (3)]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_AgentTarget]]
- 1 edge to [[_COMMUNITY_MiddlewareManager (3)]]
- 1 edge to [[_COMMUNITY_test_v1_models_synthetic.py]]
- 1 edge to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY_test_forward_stream.py (2)]]

## Top bridge nodes
- [[AsyncMock]] - degree 209, connects to 33 communities
- [[TestProcessToolResult]] - degree 9, connects to 4 communities
- [[TestClose]] - degree 8, connects to 4 communities
- [[TestOutboundTracking]] - degree 12, connects to 1 community
- [[TestOwnerEmailBypassesPii]] - degree 4, connects to 1 community
