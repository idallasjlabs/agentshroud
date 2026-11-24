---
type: community
members: 56
---

# test_edge_approvals.py

**Members:** 56 nodes

## Members
- [[dot-_card()]] - code - gateway/tests/test_edge_approvals.py
- [[dot-_idem_key()]] - code - gateway/inbound_edge/approvals.py
- [[dot-_status()]] - code - gateway/inbound_edge/approvals.py
- [[dot-handle_callback()]] - code - gateway/inbound_edge/approvals.py
- [[dot-redeem()]] - code - gateway/inbound_edge/approvals.py
- [[dot-request()_1]] - code - gateway/inbound_edge/approvals.py
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
- [[Any_48]] - code
- [[ApprovalContext]] - code - gateway/inbound_edge/approvals.py
- [[ApprovalDenied]] - code - gateway/inbound_edge/approvals.py
- [[ApprovalPending]] - code - gateway/inbound_edge/approvals.py
- [[Authorise exactly one execution, or raise. Never returns on a bad ticket.]] - rationale - gateway/inbound_edge/approvals.py
- [[EdgeApprovals]] - code - gateway/inbound_edge/approvals.py
- [[Exception_13]] - code
- [[Hash of the canonical arguments, excluding the ticket itself.]] - rationale - gateway/inbound_edge/approvals.py
- [[PendingApproval]] - code - gateway/inbound_edge/approvals.py
- [[Plain-text card (no parse mode, so nothing in the args can format it).]] - rationale - gateway/inbound_edge/approvals.py
- [[Queue (or re-use) the approval for this exact call and issue a ticket.]] - rationale - gateway/inbound_edge/approvals.py
- [[T5 the owner sees raw arguments and their hash — never agent-written prose.]] - rationale - gateway/tests/test_edge_approvals.py
- [[Telegram inline-button handler. Returns the toast text to show.]] - rationale - gateway/inbound_edge/approvals.py
- [[TestApprovalCard]] - code - gateway/tests/test_edge_approvals.py
- [[TestCallback]] - code - gateway/tests/test_edge_approvals.py
- [[TestIdempotency]] - code - gateway/tests/test_edge_approvals.py
- [[TestNoApprovalNoExecution]] - code - gateway/tests/test_edge_approvals.py
- [[TestTicketBinding]] - code - gateway/tests/test_edge_approvals.py
- [[The owner has not decided yet. Not an error for the caller — try again later.]] - rationale - gateway/inbound_edge/approvals.py
- [[The ticket cannot authorise this call. ``str(exc)`` is safe to return.]] - rationale - gateway/inbound_edge/approvals.py
- [[There is no summaryjustification input to render_card at all.]] - rationale - gateway/tests/test_edge_approvals.py
- [[_ctx()]] - code - gateway/tests/test_edge_approvals.py
- [[_iso()]] - code - gateway/inbound_edge/approvals.py
- [[_principal()]] - code - gateway/tests/test_edge_approvals.py
- [[approvals.py]] - code - gateway/inbound_edge/approvals.py
- [[args_sha256()]] - code - gateway/inbound_edge/approvals.py
- [[render_card()]] - code - gateway/inbound_edge/approvals.py
- [[test_edge_approvals.py]] - code - gateway/tests/test_edge_approvals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_edge_approvalspy
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 15 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 13 edges to [[_COMMUNITY_make_event]]
- 4 edges to [[_COMMUNITY_test_edge_service_routes.py]]
- 4 edges to [[_COMMUNITY_EdgeStore]]
- 3 edges to [[_COMMUNITY_ApprovalRequest]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TestTelegramDispatch]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_GatewayBackedProvider]]
- 1 edge to [[_COMMUNITY_GatewayConfig]]

## Top bridge nodes
- [[approvals.py]] - degree 26, connects to 8 communities
- [[test_edge_approvals.py]] - degree 30, connects to 7 communities
- [[EdgeApprovals]] - degree 22, connects to 6 communities
- [[dot-request()_1]] - degree 12, connects to 3 communities
- [[ApprovalContext]] - degree 12, connects to 1 community
