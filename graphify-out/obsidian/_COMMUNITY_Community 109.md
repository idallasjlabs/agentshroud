---
type: community
members: 61
---

# Community 109

**Members:** 61 nodes

## Members
- [[.__call__()_10]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[.__init__()_173]] - code - gateway/tests/test_mcp_proxy_coverage.py
- [[.__init__()_191]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[._passthrough_pii()]] - code - gateway/tests/test_pipeline_unit.py
- [[.test_approval_decision()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_approval_queue_list()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_close_stops_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_close_swallows_stop_errors()]] - code - gateway/tests/test_middleware_coverage.py
- [[.test_close_with_no_resource_guard()]] - code - gateway/tests/test_middleware_coverage.py
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
- [[.test_store_error_returns_empty()]] - code - gateway/tests/test_soc_realtime_coverage.py
- [[.test_unknown_recipient_body_still_scrubbed()]] - code - gateway/tests/test_email_owner_bypasses_pii.py
- [[emailsend-owner delegates to email_send and also skips PII for the owner.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[AsyncMock]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[JSON upstream responses must stay JSON.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Minimal async callable for monkeypatching.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Owner-allowlisted recipient receives body verbatim; pii_redacted=False.]] - rationale - gateway/tests/test_email_owner_bypasses_pii.py
- [[Plain-text upstream errors must not turn into gateway 500s.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test MCP proxy endpoint basic functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test basic status endpoint functionality.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test listing pending approvals.]] - rationale - gateway/tests/test_main_endpoints.py
- [[Test making approval decisions.]] - rationale - gateway/tests/test_main_endpoints.py
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
TABLE source_file, type FROM #community/Community_109
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_Community 25]]
- 26 edges to [[_COMMUNITY_Community 72]]
- 26 edges to [[_COMMUNITY_Community 17]]
- 13 edges to [[_COMMUNITY_Community 22]]
- 10 edges to [[_COMMUNITY_Community 9]]
- 9 edges to [[_COMMUNITY_Community 39]]
- 9 edges to [[_COMMUNITY_Community 86]]
- 7 edges to [[_COMMUNITY_Community 331]]
- 7 edges to [[_COMMUNITY_Community 15]]
- 7 edges to [[_COMMUNITY_Community 37]]
- 5 edges to [[_COMMUNITY_Community 6]]
- 5 edges to [[_COMMUNITY_Community 513]]
- 5 edges to [[_COMMUNITY_Community 115]]
- 5 edges to [[_COMMUNITY_Community 31]]
- 4 edges to [[_COMMUNITY_Community 83]]
- 4 edges to [[_COMMUNITY_Community 141]]
- 4 edges to [[_COMMUNITY_Community 651]]
- 4 edges to [[_COMMUNITY_Community 76]]
- 4 edges to [[_COMMUNITY_Community 32]]
- 3 edges to [[_COMMUNITY_Community 222]]
- 3 edges to [[_COMMUNITY_Community 176]]
- 3 edges to [[_COMMUNITY_Community 1339]]
- 3 edges to [[_COMMUNITY_Community 157]]
- 3 edges to [[_COMMUNITY_Community 12]]
- 3 edges to [[_COMMUNITY_Community 101]]
- 2 edges to [[_COMMUNITY_Community 1]]
- 2 edges to [[_COMMUNITY_Community 174]]
- 2 edges to [[_COMMUNITY_Community 43]]
- 2 edges to [[_COMMUNITY_Community 477]]
- 2 edges to [[_COMMUNITY_Community 426]]
- 2 edges to [[_COMMUNITY_Community 177]]
- 2 edges to [[_COMMUNITY_Community 273]]
- 2 edges to [[_COMMUNITY_Community 1137]]
- 2 edges to [[_COMMUNITY_Community 780]]
- 2 edges to [[_COMMUNITY_Community 127]]
- 1 edge to [[_COMMUNITY_Community 124]]
- 1 edge to [[_COMMUNITY_Community 4]]
- 1 edge to [[_COMMUNITY_Community 117]]
- 1 edge to [[_COMMUNITY_Community 21]]
- 1 edge to [[_COMMUNITY_Community 63]]
- 1 edge to [[_COMMUNITY_Community 1131]]
- 1 edge to [[_COMMUNITY_Community 167]]
- 1 edge to [[_COMMUNITY_Community 38]]
- 1 edge to [[_COMMUNITY_Community 500]]
- 1 edge to [[_COMMUNITY_Community 79]]
- 1 edge to [[_COMMUNITY_Community 1540]]
- 1 edge to [[_COMMUNITY_Community 66]]
- 1 edge to [[_COMMUNITY_Community 1054]]
- 1 edge to [[_COMMUNITY_Community 1065]]

## Top bridge nodes
- [[AsyncMock]] - degree 236, connects to 43 communities
- [[TestProcessToolResult]] - degree 9, connects to 4 communities
- [[TestClose]] - degree 8, connects to 4 communities
- [[TestOwnerEmailBypassesPii]] - degree 4, connects to 1 community
- [[.test_status_endpoint()]] - degree 3, connects to 1 community