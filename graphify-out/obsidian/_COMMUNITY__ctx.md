---
type: community
members: 35
---

# _ctx

**Members:** 35 nodes

## Members
- [[dot-_card()]] - code - gateway/tests/test_edge_approvals.py
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
- [[Any_50]] - code
- [[Hash of the canonical arguments, excluding the ticket itself.]] - rationale - gateway/inbound_edge/approvals.py
- [[T5 the owner sees raw arguments and their hash — never agent-written prose.]] - rationale - gateway/tests/test_edge_approvals.py
- [[TestApprovalCard]] - code - gateway/tests/test_edge_approvals.py
- [[TestCallback]] - code - gateway/tests/test_edge_approvals.py
- [[TestIdempotency]] - code - gateway/tests/test_edge_approvals.py
- [[TestNoApprovalNoExecution]] - code - gateway/tests/test_edge_approvals.py
- [[TestTicketBinding]] - code - gateway/tests/test_edge_approvals.py
- [[There is no summaryjustification input to render_card at all.]] - rationale - gateway/tests/test_edge_approvals.py
- [[_ctx()]] - code - gateway/tests/test_edge_approvals.py
- [[_principal()]] - code - gateway/tests/test_edge_approvals.py
- [[args_sha256()]] - code - gateway/inbound_edge/approvals.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_ctx
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 1 edge to [[_COMMUNITY_test_edge_service_routes.py]]

## Top bridge nodes
- [[args_sha256()]] - degree 12, connects to 2 communities
- [[_ctx()]] - degree 20, connects to 1 community
- [[TestNoApprovalNoExecution]] - degree 10, connects to 1 community
- [[TestApprovalCard]] - degree 8, connects to 1 community
- [[TestTicketBinding]] - degree 7, connects to 1 community
