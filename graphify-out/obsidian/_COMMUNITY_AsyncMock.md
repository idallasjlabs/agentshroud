---
type: community
members: 106
---

# AsyncMock

**Members:** 106 nodes

## Members
- [[dot-__call__()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-__init__()_18]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_already_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cached_corr_without_colon_falls_back_to_channel()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cached_inbound_corr_skips_history_lookup()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cant_kick_self_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_close_stops_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_close_swallows_stop_errors()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_close_with_no_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_dm_reply_recovers_inbound_via_conversations_history()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_history_error_records_outbound_without_correlation()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_keepalive_breaks_on_construction_error()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_malformed_json_body_forwards_with_empty_payload()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_missing_args_return_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_missing_args_return_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_missing_channel_or_text_skips_tracking()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_name_truncated_to_80_chars()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_network_error_returns_synthetic_failure()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_no_sanitizer_passthrough()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_no_token_returns_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_no_token_returns_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_no_token_returns_none()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_not_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_other_error_returns_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_other_error_returns_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_owner_recipient_body_preserved()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_recovery_exception_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_redaction_count_access_error_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_sanitized_with_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_sanitized_without_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_sanitizer_error_fails_open()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_send_owner_endpoint_also_bypasses_pii()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[dot-test_slack_error_returns_none()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_structured_text_serialized_for_preview()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_posts_with_bearer_token()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_returns_channel_id_with_sanitized_name()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_returns_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_returns_true()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_system_message_not_tracked()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_thread_reply_recovers_inbound_via_conversations_replies()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_tracker_exception_does_not_break_response()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_unknown_content_type_ignored()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[A dict text payload is JSON-serialized before the 80-char preview.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[AsyncMock]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Bodies with an unrecognized Content-Type are not parsed at all.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Cached correlation for the channel → no Slack history call; outbound is…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Channel name is lowercased, spacesunderscores → hyphens, symbols dropped.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Connection failure → {'ok' False, 'error' exc} (no exception leaks).]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Correlation ID with no '' separator → outbound attributed to channel id.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Coverage tests for SlackAPIProxy — tracker recovery, Slack API call layer,…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Create a SlackAPIProxy with a fake token and no real secretfile IO.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Exception during inbound recovery → swallowed; outbound still recorded.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Happy path POSTs to slack.comapimethod with injected bot token.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[History lookup returns ok=False → no inbound record; outbound still logged,…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Minimal async callable for monkeypatching.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Non-owner channel error reading info_filter_redaction_count is swallowed and…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Non-thread reply → conversations.history lookup; bot and subtype messages are…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestBodyParsing]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestCallSlackApi]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestClose]] - code - gateway/tests/test_middleware_coverage.py
- [[TestInviteChannelMember]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestKickChannelMember]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestOutboundTracking]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestOwnerEmailBypassesPii]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestProcessToolResult]] - code - gateway/tests/test_middleware_coverage.py
- [[TestProvisionGroupChannel]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestRedactionCountErrorSwallow]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[Thread reply with no cached corr → conversations.replies lookup recovers the…]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Tracker errors are non-fatal — Slack response still returned to bot.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Unknown recipient's body is PII-scrubbed before approval queue submission.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[Unparseable JSON body → warning logged, empty payload forwarded (no crash).]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[_make_proxy()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[asyncio_7]] - code
- [[boom()_1]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[chat.postMessage without channeltext → nothing recorded, no lookups.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[fake_api()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[fake_api()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[fake_api()_2]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[fake_api()_3]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[is_system=True chat.postMessage bypasses the tracker entirely.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[mock_create_subprocess()]] - code - gateway/tests/test_security_fixes.py
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
- [[test_log_audit_appends_to_audit_store()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_run_scanner_validation_and_launch()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_slack_proxy_coverage.py]] - code - gateway/tests/test_slack_proxy_coverage.py
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
- 26 edges to [[_COMMUNITY__make_proxy]]
- 25 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 9 edges to [[_COMMUNITY_app]]
- 9 edges to [[_COMMUNITY_SecurityPipeline]]
- 9 edges to [[_COMMUNITY_test_soc_bots.py]]
- 9 edges to [[_COMMUNITY_test_telegram_pipeline.py]]
- 7 edges to [[_COMMUNITY_PipelineAction]]
- 6 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 5 edges to [[_COMMUNITY_hermes_dashboard_ws_proxy]]
- 5 edges to [[_COMMUNITY_RedactionResult]]
- 4 edges to [[_COMMUNITY_dot-_make_proxy]]
- 4 edges to [[_COMMUNITY_chatbotmain.py]]
- 4 edges to [[_COMMUNITY_DNSBlocklist]]
- 4 edges to [[_COMMUNITY_DNSForwarderProtocol]]
- 4 edges to [[_COMMUNITY_test_forward_stream.py]]
- 4 edges to [[_COMMUNITY_dot-test_events_api_envelope_dispatches_handle_event]]
- 4 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 4 edges to [[_COMMUNITY_SlackAPIProxy]]
- 3 edges to [[_COMMUNITY_TestEmailSend]]
- 3 edges to [[_COMMUNITY_DataExfilVolumeGuard]]
- 3 edges to [[_COMMUNITY_test_forward_routing.py]]
- 3 edges to [[_COMMUNITY_make_proxy]]
- 3 edges to [[_COMMUNITY__audit_entry]]
- 3 edges to [[_COMMUNITY_SSHProxy]]
- 3 edges to [[_COMMUNITY_ModeRequest]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_test_middleware_coverage.py]]
- 2 edges to [[_COMMUNITY_ApprovalRequest]]
- 2 edges to [[_COMMUNITY_TestTelegramDispatch]]
- 2 edges to [[_COMMUNITY_test_image_verifier.py]]
- 2 edges to [[_COMMUNITY_StreamHead]]
- 2 edges to [[_COMMUNITY_AuditChain]]
- 2 edges to [[_COMMUNITY_RateLimitGuard]]
- 2 edges to [[_COMMUNITY_GatewayConfig]]
- 2 edges to [[_COMMUNITY_UserSessionManager]]
- 2 edges to [[_COMMUNITY_ws_soc_endpoint]]
- 2 edges to [[_COMMUNITY__mock_ws]]
- 2 edges to [[_COMMUNITY__engine]]
- 1 edge to [[_COMMUNITY_email_send]]
- 1 edge to [[_COMMUNITY_test_chat_completions_alias.py]]
- 1 edge to [[_COMMUNITY_fixture]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_test_mcp_proxy.py]]
- 1 edge to [[_COMMUNITY_TestKeyLeakDetection]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_SOCWebSocketHandler]]
- 1 edge to [[_COMMUNITY_TestMultiBotContextvarRouting]]
- 1 edge to [[_COMMUNITY_TestTelegramTokenRegistryRebuildOnMiss]]
- 1 edge to [[_COMMUNITY_test_v1_models_synthetic.py]]
- 1 edge to [[_COMMUNITY__run_disconnect_test]]
- 1 edge to [[_COMMUNITY_test_ws_pipeline_error_logs_and_recovers_to_idle]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[AsyncMock]] - degree 235, connects to 49 communities
- [[test_slack_proxy_coverage.py]] - degree 12, connects to 2 communities
- [[test_egress_approve_mode_mapping()]] - degree 3, connects to 2 communities
- [[test_log_audit_appends_to_audit_store()]] - degree 3, connects to 2 communities
- [[test_ssh_compose_success()]] - degree 3, connects to 2 communities
