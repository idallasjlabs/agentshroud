---
type: community
members: 9
---

# fixture

**Members:** 9 nodes

## Members
- [[dot-approval_queue()]] - code - gateway/tests/test_egress_approval.py
- [[dot-mock_app_state()]] - code - gateway/tests/test_egress_approval.py
- [[dot-mock_auth()]] - code - gateway/tests/test_egress_approval.py
- [[dot-temp_rules_file()]] - code - gateway/tests/test_egress_approval.py
- [[Create EgressApprovalQueue instance for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[Create temporary rules file for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[Mock app_state with egress approval queue.]] - rationale - gateway/tests/test_egress_approval.py
- [[Mock authentication dependency.]] - rationale - gateway/tests/test_egress_approval.py
- [[fixture_52]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/fixture
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 2 edges to [[_COMMUNITY_TestEgressApprovalAPI]]
- 2 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[dot-mock_app_state()]] - degree 4, connects to 2 communities
- [[dot-mock_auth()]] - degree 4, connects to 2 communities
- [[dot-approval_queue()]] - degree 4, connects to 2 communities
- [[dot-temp_rules_file()]] - degree 3, connects to 1 community
