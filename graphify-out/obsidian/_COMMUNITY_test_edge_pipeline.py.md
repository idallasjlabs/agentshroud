---
type: community
members: 107
---

# test_edge_pipeline.py

**Members:** 107 nodes

## Members
- [[dot-__call__()_7]] - code - gateway/tests/test_edge_pipeline.py
- [[dot-__init__()_123]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-__init__()_124]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-__init__()_125]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-__init__()_126]] - code - gateway/tests/test_edge_pipeline.py
- [[dot-__init__()_127]] - code - gateway/tests/test_edge_pipeline.py
- [[dot-_alert()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_authenticate()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_card()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-_check_limits()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_count_denial()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_idem_key()]] - code - gateway/inbound_edge/approvals.py
- [[dot-_p0()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_record()_1]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_scrub()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_status()]] - code - gateway/inbound_edge/approvals.py
- [[dot-_strike()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-_visible_tools()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-call_tool()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-enforcing()]] - code - gateway/inbound_edge/profiles.py
- [[dot-handle_callback()]] - code - gateway/inbound_edge/approvals.py
- [[dot-hit()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-list_tools()]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-principal_id()]] - code - gateway/inbound_edge/edge_jwt.py
- [[dot-redeem()]] - code - gateway/inbound_edge/approvals.py
- [[dot-request()_1]] - code - gateway/inbound_edge/approvals.py
- [[dot-run()_4]] - code - gateway/inbound_edge/call_pipeline.py
- [[dot-run()_5]] - code - gateway/tests/test_edge_pipeline.py
- [[dot-test_after_use_a_new_request_needs_a_new_approval()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_approved_executes_exactly_once()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_card_has_no_field_for_agent_prose()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_card_snapshot()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_changed_args_are_denied()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_concurrent_redeem_executes_once()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_expired_is_denied()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_first_call_returns_pending_ticket_and_notifies()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_large_args_truncated_with_full_hash()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_markup_cannot_break_out_of_the_card()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_non_owner_button_ignored()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_one_approval_cannot_run_twice_via_two_tickets()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_other_client_cannot_use_ticket()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_other_tool_cannot_use_ticket()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_owner_button_approves()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_queue_timeout_is_deny()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_rejected_is_denied()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_repeat_request_reuses_the_pending_approval()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_ticket_is_excluded_from_args_hash()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_unapproved_ticket_is_pending_not_executed()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_unknown_request_and_garbage()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-test_unknown_ticket()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-tool_access()]] - code - gateway/inbound_edge/profiles.py
- [[Any_49]] - code
- [[Any_50]] - code
- [[ApprovalContext]] - code - gateway/inbound_edge/approvals.py
- [[ApprovalDenied]] - code - gateway/inbound_edge/approvals.py
- [[ApprovalPending]] - code - gateway/inbound_edge/approvals.py
- [[Authorise exactly one execution, or raise. Never returns on a bad ticket.]] - rationale - gateway/inbound_edge/approvals.py
- [[CallContext]] - code - gateway/inbound_edge/call_pipeline.py
- [[Clock]] - code - gateway/tests/test_edge_pipeline.py
- [[EdgeApprovals]] - code - gateway/inbound_edge/approvals.py
- [[EdgeCallPipeline]] - code - gateway/inbound_edge/call_pipeline.py
- [[EdgeDeps]] - code - gateway/inbound_edge/call_pipeline.py
- [[EdgePrincipal]] - code - gateway/inbound_edge/edge_jwt.py
- [[Exception_12]] - code
- [[Exception_13]] - code
- [[Facade]] - code - gateway/inbound_edge/call_pipeline.py
- [[FakeFacade]] - code - gateway/tests/test_edge_pipeline.py
- [[Hash of the canonical arguments, excluding the ticket itself.]] - rationale - gateway/inbound_edge/approvals.py
- [[Namespaced identity used by every downstream module. Never an owner ID.]] - rationale - gateway/inbound_edge/edge_jwt.py
- [[PendingApproval]] - code - gateway/inbound_edge/approvals.py
- [[Plain-text card (no parse mode, so nothing in the args can format it).]] - rationale - gateway/inbound_edge/approvals.py
- [[Protocol_1]] - code
- [[Queue (or re-use) the approval for this exact call and issue a ticket.]] - rationale - gateway/inbound_edge/approvals.py
- [[Sliding one-minute window counter keyed by principal or vendor.]] - rationale - gateway/inbound_edge/call_pipeline.py
- [[T5 the owner sees raw arguments and their hash — never agent-written prose.]] - rationale - gateway/tests/test_edge_approvals.py
- [[Telegram inline-button handler. Returns the toast text to show.]] - rationale - gateway/inbound_edge/approvals.py
- [[TestApprovalCard]] - code - gateway/tests/test_edge_approvals.py
- [[TestCallback]] - code - gateway/tests/test_edge_approvals.py
- [[TestIdempotency]] - code - gateway/tests/test_edge_approvals.py
- [[TestNoApprovalNoExecution]] - code - gateway/tests/test_edge_approvals.py
- [[TestTicketBinding]] - code - gateway/tests/test_edge_approvals.py
- [[The MCP ``Tool`` view of a descriptor (internal fields stripped).]] - rationale - gateway/inbound_edge/descriptors.py
- [[The owner has not decided yet. Not an error for the caller — try again later.]] - rationale - gateway/inbound_edge/approvals.py
- [[The ticket cannot authorise this call. ``str(exc)`` is safe to return.]] - rationale - gateway/inbound_edge/approvals.py
- [[There is no summaryjustification input to render_card at all.]] - rationale - gateway/tests/test_edge_approvals.py
- [[VendorProfile]] - code - gateway/inbound_edge/profiles.py
- [[_Denied]] - code - gateway/inbound_edge/call_pipeline.py
- [[_Window]] - code - gateway/inbound_edge/call_pipeline.py
- [[_ctx()]] - code - gateway/tests/test_edge_approvals.py
- [[_iso()]] - code - gateway/inbound_edge/approvals.py
- [[_principal()]] - code - gateway/tests/test_edge_approvals.py
- [[_rank()]] - code - gateway/inbound_edge/call_pipeline.py
- [[_result()]] - code - gateway/inbound_edge/call_pipeline.py
- [[_string_leaves()]] - code - gateway/inbound_edge/call_pipeline.py
- [[``read````write`` when the vendor may call ``tool``, else ``None``.]] - rationale - gateway/inbound_edge/profiles.py
- [[approvals.py]] - code - gateway/inbound_edge/approvals.py
- [[args_sha256()]] - code - gateway/inbound_edge/approvals.py
- [[call_pipeline.py]] - code - gateway/inbound_edge/call_pipeline.py
- [[edge()]] - code - gateway/tests/test_edge_pipeline.py
- [[edge_jwt.py]] - code - gateway/inbound_edge/edge_jwt.py
- [[emit()_6]] - code - gateway/tests/test_edge_pipeline.py
- [[fixture_95]] - code
- [[inbound_edgestore.py]] - code - gateway/inbound_edge/store.py
- [[mcp_tool()]] - code - gateway/inbound_edge/descriptors.py
- [[render_card()]] - code - gateway/inbound_edge/approvals.py
- [[test_edge_approvals.py]] - code - gateway/tests/test_edge_approvals.py
- [[test_edge_pipeline.py]] - code - gateway/tests/test_edge_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_edge_pipelinepy
SORT file.name ASC
```

## Connections to other communities
- 30 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 26 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 16 edges to [[_COMMUNITY__token]]
- 13 edges to [[_COMMUNITY_test_soc_edge.py]]
- 11 edges to [[_COMMUNITY_EdgeStore]]
- 8 edges to [[_COMMUNITY_service.py]]
- 7 edges to [[_COMMUNITY_descriptors.py]]
- 6 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 6 edges to [[_COMMUNITY_test_edge_service_routes.py]]
- 6 edges to [[_COMMUNITY_LockdownLevel]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_ApprovalRequest]]
- 3 edges to [[_COMMUNITY_CanaryTripwire]]
- 3 edges to [[_COMMUNITY_PIIConfig]]
- 3 edges to [[_COMMUNITY_EdgeOAuthService]]
- 3 edges to [[_COMMUNITY_test_edge_oauth.py]]
- 3 edges to [[_COMMUNITY_PromptGuard]]
- 3 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 3 edges to [[_COMMUNITY_secrets.py]]
- 2 edges to [[_COMMUNITY_PIISanitizer]]
- 2 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 2 edges to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_TestTelegramDispatch]]
- 1 edge to [[_COMMUNITY_aiosqlite]]
- 1 edge to [[_COMMUNITY_ToolResultInjectionScanner]]
- 1 edge to [[_COMMUNITY_test_audit_export.py]]
- 1 edge to [[_COMMUNITY_AgentTarget]]

## Top bridge nodes
- [[test_edge_pipeline.py]] - degree 50, connects to 15 communities
- [[edge()]] - degree 25, connects to 12 communities
- [[call_pipeline.py]] - degree 36, connects to 9 communities
- [[approvals.py]] - degree 26, connects to 9 communities
- [[EdgeApprovals]] - degree 22, connects to 7 communities
