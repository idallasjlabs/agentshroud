---
type: community
members: 113
---

# Community 37

**Members:** 113 nodes

## Members
- [[.__call__()_10]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.__init__()_35]] - code - gateway/proxy/slack_proxy.py
- [[.__init__()_177]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.__init__()_184]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.__init__()_195]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[._passthrough_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[.consume_relay_token()]] - code - gateway/proxy/slack_proxy.py
- [[.get_stats()_8]] - code - gateway/proxy/slack_proxy.py
- [[.handle_event()]] - code - gateway/proxy/slack_proxy.py
- [[.info_filter_redaction_count()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.mock_forwarder()]] - code - gateway/tests/test_session_isolation.py
- [[.mock_pipeline()]] - code - gateway/tests/test_session_isolation.py
- [[.test_already_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_cached_corr_without_colon_falls_back_to_channel()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_cached_inbound_corr_skips_history_lookup()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_cant_kick_self_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_close_stops_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_dm_reply_recovers_inbound_via_conversations_history()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_history_error_records_outbound_without_correlation()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_malformed_json_body_forwards_with_empty_payload()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_missing_args_return_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_missing_args_return_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_missing_channel_or_text_skips_tracking()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_name_truncated_to_80_chars()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_network_error_returns_synthetic_failure()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_no_sanitizer_passthrough()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_no_token_returns_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_no_token_returns_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_no_token_returns_none()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_not_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_other_error_returns_false()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_other_error_returns_false()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_recovery_exception_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_redaction_count_access_error_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_sanitized_with_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_sanitized_without_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_sanitizer_error_fails_open()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_slack_error_returns_none()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_structured_text_serialized_for_preview()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_success_posts_with_bearer_token()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_success_returns_channel_id_with_sanitized_name()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_success_returns_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_success_returns_true()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_system_message_not_tracked()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_thread_reply_recovers_inbound_via_conversations_replies()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_tracker_exception_does_not_break_response()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_unknown_content_type_ignored()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[A dict text payload is JSON-serialized before the 80-char preview.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[AsyncMock]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Bodies with an unrecognized Content-Type are not parsed at all.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Cached correlation for the channel → no Slack history call; outbound         is]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Channel name is lowercased, spacesunderscores → hyphens, symbols dropped.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Connection failure → {'ok' False, 'error' exc} (no exception leaks).]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Correlation ID with no '' separator → outbound attributed to channel id.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Create a SlackAPIProxy with a fake token and no real secretfile IO.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Create a mock forwarder.]] - rationale - gateway/tests/test_session_isolation.py
- [[Create a mock security pipeline.]] - rationale - gateway/tests/test_session_isolation.py
- [[Exception during inbound recovery → swallowed; outbound still recorded.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Handle an inbound Slack event payload received via Socket Mode.          Called]] - rationale - gateway/proxy/slack_proxy.py
- [[Happy path POSTs to slack.comapimethod with injected bot token.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[History lookup returns ok=False → no inbound record; outbound still         logg]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Minimal async callable for monkeypatching.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Non-owner channel error reading info_filter_redaction_count is swallowed]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Non-thread reply → conversations.history lookup; bot and subtype         message]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Pipeline result whose redaction-count attribute raises on access.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Pop and return the real WSS URL for a relay token (one-time use).          Retur]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxies bot Slack Web API calls through SecurityPipeline.      Outbound flow (bo]] - rationale - gateway/proxy/slack_proxy.py
- [[SlackAPIProxy]] - code - gateway/proxy/slack_proxy.py
- [[SlackAPIProxy_2]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[Test broadcast handles failed client sends]] - rationale - gateway/tests/test_approval_queue.py
- [[TestBodyParsing]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestCallSlackApi]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestInviteChannelMember]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestKickChannelMember]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestOutboundTracking]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestProcessToolResult]] - code - gateway/tests/test_middleware_coverage.py
- [[TestProvisionGroupChannel]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestRedactionCountErrorSwallow]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[Thread reply with no cached corr → conversations.replies lookup recovers]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Tracker errors are non-fatal — Slack response still returned to bot.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Unparseable JSON body → warning logged, empty payload forwarded (no crash).]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[_RaisingRedactionResult]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[_make_proxy()_3]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[chat.postMessage without channeltext → nothing recorded, no lookups.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[is_system=True chat.postMessage bypasses the tracker entirely.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[test_approvals_approve_and_deny()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_approvals_approve_raises()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_audit_export_cef()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_audit_export_exporter_raises()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_audit_export_json_dict_payload()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_broadcast_with_failed_client()]] - code - gateway/tests/test_approval_queue.py
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
- [[test_slack_proxy_coverage.py]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[test_ssh_compose_success()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_ssh_compose_timeout_and_exception()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_bot_paths()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_gateway_paths()]] - code - gateway/tests/test_soc_router_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_37
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_Community 100]]
- 26 edges to [[_COMMUNITY_Community 19]]
- 14 edges to [[_COMMUNITY_Community 24]]
- 12 edges to [[_COMMUNITY_Community 53]]
- 11 edges to [[_COMMUNITY_Community 6]]
- 9 edges to [[_COMMUNITY_Community 2030]]
- 9 edges to [[_COMMUNITY_Community 51]]
- 9 edges to [[_COMMUNITY_Community 63]]
- 7 edges to [[_COMMUNITY_Community 1070]]
- 7 edges to [[_COMMUNITY_Community 220]]
- 6 edges to [[_COMMUNITY_Community 46]]
- 5 edges to [[_COMMUNITY_Community 1]]
- 5 edges to [[_COMMUNITY_Community 176]]
- 5 edges to [[_COMMUNITY_Community 28]]
- 5 edges to [[_COMMUNITY_Community 40]]
- 4 edges to [[_COMMUNITY_Community 95]]
- 4 edges to [[_COMMUNITY_Community 158]]
- 4 edges to [[_COMMUNITY_Community 683]]
- 4 edges to [[_COMMUNITY_Community 47]]
- 4 edges to [[_COMMUNITY_Community 132]]
- 4 edges to [[_COMMUNITY_Community 12]]
- 3 edges to [[_COMMUNITY_Community 14]]
- 3 edges to [[_COMMUNITY_Community 512]]
- 3 edges to [[_COMMUNITY_Community 205]]
- 3 edges to [[_COMMUNITY_Community 1127]]
- 3 edges to [[_COMMUNITY_Community 1658]]
- 3 edges to [[_COMMUNITY_Community 25]]
- 3 edges to [[_COMMUNITY_Community 101]]
- 2 edges to [[_COMMUNITY_Community 72]]
- 2 edges to [[_COMMUNITY_Community 660]]
- 2 edges to [[_COMMUNITY_Community 30]]
- 2 edges to [[_COMMUNITY_Community 368]]
- 2 edges to [[_COMMUNITY_Community 507]]
- 2 edges to [[_COMMUNITY_Community 206]]
- 2 edges to [[_COMMUNITY_Community 105]]
- 1 edge to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 138]]
- 1 edge to [[_COMMUNITY_Community 7]]
- 1 edge to [[_COMMUNITY_Community 978]]
- 1 edge to [[_COMMUNITY_Community 18]]
- 1 edge to [[_COMMUNITY_Community 79]]
- 1 edge to [[_COMMUNITY_Community 890]]
- 1 edge to [[_COMMUNITY_Community 23]]
- 1 edge to [[_COMMUNITY_Community 531]]
- 1 edge to [[_COMMUNITY_Community 325]]
- 1 edge to [[_COMMUNITY_Community 1278]]
- 1 edge to [[_COMMUNITY_Community 123]]
- 1 edge to [[_COMMUNITY_Community 1112]]

## Top bridge nodes
- [[AsyncMock]] - degree 235, connects to 39 communities
- [[SlackAPIProxy]] - degree 38, connects to 8 communities
- [[TestProcessToolResult]] - degree 9, connects to 4 communities
- [[test_broadcast_with_failed_client()]] - degree 4, connects to 2 communities
- [[test_audit_export_exporter_raises()]] - degree 3, connects to 2 communities