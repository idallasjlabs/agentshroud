---
type: community
members: 14
---

# TestEgressApprovalAPI

**Members:** 14 nodes

## Members
- [[dot-test_add_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approve_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_deny_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_get_egress_rules_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_pending_requests_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_remove_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[Test DELETE manageegressrules{domain} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test GET manageegresspending endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test GET manageegressrules endpoint.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressapprove{request_id} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressdeny{request_id} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressrules endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test suite for egress approval API endpoints.]] - rationale - gateway/tests/test_egress_approval.py
- [[TestEgressApprovalAPI]] - code - gateway/tests/test_egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEgressApprovalAPI
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 2 edges to [[_COMMUNITY_egress_approval.py]]
- 2 edges to [[_COMMUNITY_fixture]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_app]]

## Top bridge nodes
- [[TestEgressApprovalAPI]] - degree 13, connects to 4 communities
- [[dot-test_get_egress_rules_endpoint()]] - degree 4, connects to 2 communities
- [[dot-test_add_egress_rule_endpoint()]] - degree 3, connects to 1 community
- [[dot-test_approve_endpoint_logic()]] - degree 3, connects to 1 community
- [[dot-test_deny_endpoint_logic()]] - degree 3, connects to 1 community
