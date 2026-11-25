---
type: community
members: 27
---

# asyncio

**Members:** 27 nodes

## Members
- [[dot-test_add_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_allowlist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approval_flow_once()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approval_flow_permanent()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approval_flow_session()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approve_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_denial_flow()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_deny_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_existing_rule_bypass()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_get_egress_rules_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_pending_requests_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_remove_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_rule_management()]] - code - gateway/tests/test_egress_approval.py
- [[Test DELETE manageegressrules{domain} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test GET manageegresspending endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test GET manageegressrules endpoint.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressapprove{request_id} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressdeny{request_id} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressrules endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test adding and removing rules.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test approval flow with one-time approval.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test approval flow with permanent rule creation.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test approval flow with session rule creation.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test denial flow with rule creation.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that allowlist rules are persisted to disk.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that existing rules bypass the approval queue.]] - rationale - gateway/tests/test_egress_approval.py
- [[asyncio_22]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asyncio
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 7 edges to [[_COMMUNITY_ApprovalMode]]
- 1 edge to [[_COMMUNITY_app]]

## Top bridge nodes
- [[asyncio_22]] - degree 19, connects to 2 communities
- [[dot-test_get_egress_rules_endpoint()]] - degree 4, connects to 2 communities
- [[dot-test_add_egress_rule_endpoint()]] - degree 3, connects to 1 community
- [[dot-test_approve_endpoint_logic()]] - degree 3, connects to 1 community
- [[dot-test_deny_endpoint_logic()]] - degree 3, connects to 1 community
