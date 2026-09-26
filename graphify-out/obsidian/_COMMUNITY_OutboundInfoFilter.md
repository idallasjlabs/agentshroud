---
type: community
cohesion: 0.03
members: 128
---

# OutboundInfoFilter

**Cohesion:** 0.03 - loosely connected
**Members:** 128 nodes

## Members
- [[.__call__()_10]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.__init__()_35]] - code - gateway/proxy/slack_proxy.py
- [[.__init__()_173]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.__init__()_180]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.__init__()_191]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[._call_slack_api()]] - code - gateway/proxy/slack_proxy.py
- [[._intercept_connections_open()]] - code - gateway/proxy/slack_proxy.py
- [[._is_owner_channel()]] - code - gateway/proxy/slack_proxy.py
- [[._passthrough_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[.consume_relay_token()]] - code - gateway/proxy/slack_proxy.py
- [[.get_stats()_8]] - code - gateway/proxy/slack_proxy.py
- [[.handle_event()]] - code - gateway/proxy/slack_proxy.py
- [[.info_filter_redaction_count()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.invite_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[.kick_channel_member()]] - code - gateway/proxy/slack_proxy.py
- [[.provision_group_channel()]] - code - gateway/proxy/slack_proxy.py
- [[.proxy_outbound()]] - code - gateway/proxy/slack_proxy.py
- [[.test_already_in_channel_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_bots_inventory_matches_the_real_container_name()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_cached_corr_without_colon_falls_back_to_channel()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_cached_inbound_corr_skips_history_lookup()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_cant_kick_self_is_idempotent_true()]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[.test_close_stops_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_close_swallows_stop_errors()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_close_with_no_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
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
- [[.test_store_error_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
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
- [[Create a Slack channel for a group. Returns channel_id or None on failure.]] - rationale - gateway/proxy/slack_proxy.py
- [[Create a SlackAPIProxy with a fake token and no real secretfile IO.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Exception during inbound recovery → swallowed; outbound still recorded.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Handle an inbound Slack event payload received via Socket Mode.          Called]] - rationale - gateway/proxy/slack_proxy.py
- [[Happy path POSTs to slack.comapimethod with injected bot token.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[History lookup returns ok=False → no inbound record; outbound still         logg]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Intercept apps.connections.open rewrite the returned WSS URL to route         t]] - rationale - gateway/proxy/slack_proxy.py
- [[Invite a Slack user to a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[Minimal async callable for monkeypatching.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Non-owner channel error reading info_filter_redaction_count is swallowed]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Non-thread reply → conversations.history lookup; bot and subtype         message]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[POST to httpsslack.comapimethod with the bot token.]] - rationale - gateway/proxy/slack_proxy.py
- [[Pipeline result whose redaction-count attribute raises on access.]] - rationale - gateway/tests/test_slack_proxy_coverage.py
- [[Pop and return the real WSS URL for a relay token (one-time use).          Retur]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxies bot Slack Web API calls through SecurityPipeline.      Outbound flow (bo]] - rationale - gateway/proxy/slack_proxy.py
- [[Proxy a bot Slack Web API call through the security pipeline.          For messa]] - rationale - gateway/proxy/slack_proxy.py
- [[Remove a Slack user from a channel. Returns True on success.]] - rationale - gateway/proxy/slack_proxy.py
- [[Return True if channel is a DM with the configured owner.          In Slack, DM]] - rationale - gateway/proxy/slack_proxy.py
- [[SlackAPIProxy_2]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[SlackAPIProxy]] - code - gateway/proxy/slack_proxy.py
- [[TestBodyParsing]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestCallSlackApi]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[TestClose]] - code - gateway/tests/test_middleware_coverage.py
- [[TestHealthCheckDetailBotsInventory]] - code - gateway/tests/test_main_endpoints.py
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
- [[health_check_detail's per-bot inventory must key the Docker lookup by     each b]] - rationale - gateway/tests/test_main_endpoints.py
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
- [[test_slack_proxy_coverage.py]] - code - gateway/tests/test_slack_proxy_coverage.py
- [[test_ssh_compose_success()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_ssh_compose_timeout_and_exception()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_bot_paths()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_gateway_paths()]] - code - gateway/tests/test_soc_router_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OutboundInfoFilter
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_test_agent_cve_registry.py]]
- 26 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 14 edges to [[_COMMUNITY_RBACConfig]]
- 12 edges to [[_COMMUNITY_MiddlewareManager]]
- 9 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 9 edges to [[_COMMUNITY_falco_monitor.py]]
- 7 edges to [[_COMMUNITY_AgentShroud™ — Trademark Prior Use Record]]
- 6 edges to [[_COMMUNITY_TrustManager]]
- 6 edges to [[_COMMUNITY_CollaboratorActivityTracker]]
- 5 edges to [[_COMMUNITY_.proxy_messages()]]
- 5 edges to [[_COMMUNITY_version_routes.py]]
- 4 edges to [[_COMMUNITY_server.py]]
- 4 edges to [[_COMMUNITY_DNSBlocklist]]
- 4 edges to [[_COMMUNITY_AgentShroud Development Roadmap — 2026 Gantt Cha]]
- 4 edges to [[_COMMUNITY_TestMultiTurnTracker]]
- 4 edges to [[_COMMUNITY_test_voice_gateway.py]]
- 4 edges to [[_COMMUNITY_test_soc_bots.py]]
- 3 edges to [[_COMMUNITY_FileSandbox]]
- 3 edges to [[_COMMUNITY_Skill MCP AWS Profile Configuration (MCPM-AWS-P]]
- 3 edges to [[_COMMUNITY_AgentShroud Access Control Matrix]]
- 3 edges to [[_COMMUNITY_Atlas — Curriculum Architect (SKILL)]]
- 3 edges to [[_COMMUNITY_ApprovalRequest]]
- 3 edges to [[_COMMUNITY_Common Queries]]
- 3 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 3 edges to [[_COMMUNITY_system-requirements]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_input_normalizer.py]]
- 2 edges to [[_COMMUNITY_KeyVaultConfig]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_MultiHostResult]]
- 2 edges to [[_COMMUNITY_InjectionSeverity]]
- 2 edges to [[_COMMUNITY_Skill Technical Writer (TW)]]
- 2 edges to [[_COMMUNITY_TestCollaboratorAccess]]
- 2 edges to [[_COMMUNITY_DELIVERABLE 3 — v0.8.0 Implementation Items]]
- 2 edges to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]
- 2 edges to [[_COMMUNITY_RateLimitGuard]]
- 2 edges to [[_COMMUNITY_gateway service (prod, sole egress point, 75-mod]]
- 2 edges to [[_COMMUNITY_GitHub Copilot CLI Setup Guide]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_test_a2a_proxy.py]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Hardening Plan]]
- 1 edge to [[_COMMUNITY_Path]]
- 1 edge to [[_COMMUNITY_Phase 3 MITIGATE (Rollback First!)]]
- 1 edge to [[_COMMUNITY_soc.js]]
- 1 edge to [[_COMMUNITY_Hermes — Podcast Production Orchestrator]]
- 1 edge to [[_COMMUNITY_macOS System Administrator (MAC)]]
- 1 edge to [[_COMMUNITY_test_approval_queue.py]]
- 1 edge to [[_COMMUNITY_OPENCLAW_SANDBOX_MODE]]

## Top bridge nodes
- [[AsyncMock]] - degree 230, connects to 43 communities
- [[SlackAPIProxy]] - degree 38, connects to 7 communities
- [[TestProcessToolResult]] - degree 9, connects to 4 communities
- [[TestClose]] - degree 8, connects to 4 communities
- [[TestHealthCheckDetailBotsInventory]] - degree 4, connects to 2 communities