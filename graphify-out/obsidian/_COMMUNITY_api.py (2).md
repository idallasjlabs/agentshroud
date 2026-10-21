---
type: community
members: 110
---

# api.py (2)

**Members:** 110 nodes

## Members
- [[dot-__call__()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-__init__()_7]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-__init__()_107]] - code - gateway/proxy/slack_proxy.py
- [[dot-__init__()_108]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[dot-__init__()_109]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-_passthrough_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-consume_relay_token()]] - code - gateway/proxy/slack_proxy.py
- [[dot-get_stats()_14]] - code - gateway/proxy/slack_proxy.py
- [[dot-handle_event()]] - code - gateway/proxy/slack_proxy.py
- [[dot-info_filter_redaction_count()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_already_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cached_corr_without_colon_falls_back_to_channel()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cached_inbound_corr_skips_history_lookup()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_cant_kick_self_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_client_disconnect_returns_499()]] - code - gateway/tests/test_security_fixes.py
- [[dot-test_dm_reply_recovers_inbound_via_conversations_history()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_history_error_records_outbound_without_correlation()]] - code - gateway/tests/test_slack_proxy_coverage.py
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
- [[dot-test_recovery_exception_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_redaction_count_access_error_is_non_fatal()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_sanitized_with_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_sanitized_without_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_sanitizer_error_fails_open()]] - code - gateway/tests/test_middleware_coverage.py
- [[dot-test_slack_error_returns_none()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_store_error_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[dot-test_structured_text_serialized_for_preview()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_posts_with_bearer_token()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_returns_channel_id_with_sanitized_name()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_returns_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_success_returns_true()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_system_message_not_tracked()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_thread_reply_recovers_inbound_via_conversations_replies()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_tracker_exception_does_not_break_response()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[dot-test_unknown_content_type_ignored()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[A dict text payload is JSON-serialized before the 80-char preview.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[AsyncMock]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Bodies with an unrecognized Content-Type are not parsed at all.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Cached correlation for the channel → no Slack history call; outbound         is]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Channel name is lowercased, spacesunderscores → hyphens, symbols dropped.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Connection failure → {'ok' False, 'error' exc} (no exception leaks).]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Correlation ID with no '' separator → outbound attributed to channel id.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Create a SlackAPIProxy with a fake token and no real secretfile IO.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
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
- [[SlackAPIProxy]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[SlackAPIProxy_1]] - code - gateway/proxy/slack_proxy.py
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
- [[When body() raises ClientDisconnect the handler returns 499 without crashing.]] - rationale - gateway/tests/test_security_fixes.py
- [[_RaisingRedactionResult]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[_make_proxy()_1]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[chat.postMessage without channeltext → nothing recorded, no lookups.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[is_system=True chat.postMessage bypasses the tracker entirely.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[slack_proxy.py]] - code - gateway/proxy/slack_proxy.py
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
- [[test_slack_proxy_coverage.py]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[test_ssh_compose_success()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_ssh_compose_timeout_and_exception()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_bot_paths()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_gateway_paths()]] - code - gateway/tests/test_soc_router_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/apipy_2
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_AgentRegistry]]
- 26 edges to [[_COMMUNITY_ResourceGuard]]
- 9 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 9 edges to [[_COMMUNITY_Phase Review P0 — Core Pipeline Wiring]]
- 7 edges to [[_COMMUNITY_ApprovalQueueConfig (2)_1]]
- 7 edges to [[_COMMUNITY_MiddlewareManager (2)]]
- 7 edges to [[_COMMUNITY_RBACConfig (2)_1]]
- 6 edges to [[_COMMUNITY_TestPatternDetection]]
- 6 edges to [[_COMMUNITY_main.rs]]
- 5 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 5 edges to [[_COMMUNITY_Request (2)]]
- 5 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 5 edges to [[_COMMUNITY_AsyncMock]]
- 4 edges to [[_COMMUNITY_SecurityPipeline]]
- 4 edges to [[_COMMUNITY_egress_filter.py]]
- 4 edges to [[_COMMUNITY_AgentShroud Security Architecture]]
- 4 edges to [[_COMMUNITY_test_scorecard_scoring.py]]
- 4 edges to [[_COMMUNITY_UserSessionManager (2) (2)]]
- 4 edges to [[_COMMUNITY_MCPPermissionManager (2)_1]]
- 3 edges to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 3 edges to [[_COMMUNITY_test_bots_ssh_exec_wrapper.py]]
- 3 edges to [[_COMMUNITY_RBACConfig]]
- 3 edges to [[_COMMUNITY_Skill Audit Branch (AB) — Merge Regression Detection]]
- 3 edges to [[_COMMUNITY_TestSSRFDetection]]
- 3 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_MiddlewareManager (3)]]
- 2 edges to [[_COMMUNITY_TestEmailSend]]
- 2 edges to [[_COMMUNITY_climain.py]]
- 2 edges to [[_COMMUNITY_api.py (2) (2)]]
- 2 edges to [[_COMMUNITY_CICD Pipeline Advisor (SKILL)]]
- 2 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 2 edges to [[_COMMUNITY__make_cve]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_test_anthropic_openai_translator.py (2)]]
- 1 edge to [[_COMMUNITY_7. Security findings]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming) (2)]]
- 1 edge to [[_COMMUNITY__make_proxy()]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (4)]]
- 1 edge to [[_COMMUNITY_test_agent_cve_registry.py]]
- 1 edge to [[_COMMUNITY_Apple Platform Integration]]
- 1 edge to [[_COMMUNITY_export_bot]]
- 1 edge to [[_COMMUNITY_colima-health-check.sh]]
- 1 edge to [[_COMMUNITY_CrossBotTrustLedger]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]

## Top bridge nodes
- [[AsyncMock]] - degree 209, connects to 36 communities
- [[SlackAPIProxy_1]] - degree 37, connects to 6 communities
- [[TestProcessToolResult]] - degree 9, connects to 4 communities
- [[dot-test_client_disconnect_returns_499()]] - degree 4, connects to 2 communities
- [[slack_proxy.py]] - degree 3, connects to 2 communities
