---
type: community
cohesion: 0.04
members: 54
---

# Module Group 74

**Cohesion:** 0.04 - loosely connected
**Members:** 54 nodes

## Members
- [[.__call__()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.__init__()_126]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.__init__()_142]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.test_client_disconnect_returns_499()]] - code - gateway/tests/test_security_fixes.py
- [[.test_close_stops_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_close_swallows_stop_errors()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_close_with_no_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_no_sanitizer_passthrough()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_owner_recipient_body_preserved()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[.test_sanitized_with_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_sanitized_without_redactions()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_sanitizer_error_fails_open()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_send_owner_endpoint_also_bypasses_pii()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[.test_store_error_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[AsyncMock]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Minimal async callable for monkeypatching.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[Test WebSocket client connection]] - rationale - gateway/tests/test_approval_queue.py
- [[Test broadcast handles failed client sends]] - rationale - gateway/tests/test_approval_queue.py
- [[TestClose]] - code - gateway/tests/test_middleware_coverage.py
- [[TestOwnerEmailBypassesPii]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[TestProcessToolResult]] - code - gateway/tests/test_middleware_coverage.py
- [[Unknown recipient's body is PII-scrubbed before approval queue submission.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[When body() raises ClientDisconnect the handler returns 499 without crashing.]] - rationale - gateway/tests/test_security_fixes.py
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
- [[test_ssh_compose_success()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_ssh_compose_timeout_and_exception()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_bot_paths()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_upgrade_gateway_paths()]] - code - gateway/tests/test_soc_router_coverage.py
- [[test_websocket_connect()]] - code - gateway/tests/test_approval_queue.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_74
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_Slack Proxy]]
- 26 edges to [[_COMMUNITY_Slack Proxy Tests]]
- 26 edges to [[_COMMUNITY_SOC Router Tests]]
- 10 edges to [[_COMMUNITY_Agent Routing & Request Models]]
- 9 edges to [[_COMMUNITY_SOC Bots & CVE Management]]
- 9 edges to [[_COMMUNITY_Module Group 177]]
- 7 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 7 edges to [[_COMMUNITY_Module Group 184]]
- 7 edges to [[_COMMUNITY_Module Group 207]]
- 5 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 4 edges to [[_COMMUNITY_Module Group 100]]
- 4 edges to [[_COMMUNITY_Module Group 291]]
- 4 edges to [[_COMMUNITY_Pipeline Action & Instruction Envelope]]
- 3 edges to [[_COMMUNITY_Module Group 221]]
- 3 edges to [[_COMMUNITY_Module Group 124]]
- 3 edges to [[_COMMUNITY_Module Group 109]]
- 3 edges to [[_COMMUNITY_Module Group 296]]
- 3 edges to [[_COMMUNITY_Module Group 94]]
- 3 edges to [[_COMMUNITY_Module Group 69]]
- 3 edges to [[_COMMUNITY_Module Group 126]]
- 2 edges to [[_COMMUNITY_Authentication & Rate Limiting]]
- 2 edges to [[_COMMUNITY_Session Manager & Webhook]]
- 2 edges to [[_COMMUNITY_Approval Queue Core]]
- 2 edges to [[_COMMUNITY_Module Group 253]]
- 2 edges to [[_COMMUNITY_Middleware Coverage Tests]]
- 2 edges to [[_COMMUNITY_Webhook Receiver]]
- 2 edges to [[_COMMUNITY_SOC Authentication]]
- 2 edges to [[_COMMUNITY_Module Group 70]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]
- 1 edge to [[_COMMUNITY_Module Group 465]]
- 1 edge to [[_COMMUNITY_Module Group 200]]
- 1 edge to [[_COMMUNITY_Module Group 195]]
- 1 edge to [[_COMMUNITY_Module Group 242]]
- 1 edge to [[_COMMUNITY_Module Group 73]]
- 1 edge to [[_COMMUNITY_MCP Config & Proxy]]
- 1 edge to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 1 edge to [[_COMMUNITY_Module Group 72]]
- 1 edge to [[_COMMUNITY_Module Group 132]]
- 1 edge to [[_COMMUNITY_Module Group 498]]

## Top bridge nodes
- [[AsyncMock]] - degree 196, connects to 32 communities
- [[TestProcessToolResult]] - degree 9, connects to 4 communities
- [[TestClose]] - degree 8, connects to 4 communities
- [[.test_client_disconnect_returns_499()]] - degree 4, connects to 2 communities
- [[TestOwnerEmailBypassesPii]] - degree 4, connects to 1 community
