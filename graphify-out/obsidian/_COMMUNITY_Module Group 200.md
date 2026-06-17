---
type: community
cohesion: 0.09
members: 24
---

# Module Group 200

**Cohesion:** 0.09 - loosely connected
**Members:** 24 nodes

## Members
- [[.mock_auth()]] - code - gateway/tests/test_egress_approval.py
- [[.test_add_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[.test_approve_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[.test_cleanup_expired_requests()]] - code - gateway/tests/test_egress_approval.py
- [[.test_deny_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[.test_get_egress_rules_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[.test_pending_requests_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[.test_remove_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[EgressRequest]] - code - gateway/security/egress_approval.py
- [[Mock authentication dependency.]] - rationale - gateway/tests/test_egress_approval.py
- [[Represents a pending egress approval request.]] - rationale - gateway/security/egress_approval.py
- [[Risk assessment levels for egress requests.]] - rationale - gateway/security/egress_approval.py
- [[RiskLevel]] - code - gateway/security/egress_approval.py
- [[Test DELETE manageegressrules{domain} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test GET manageegresspending endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test GET manageegressrules endpoint.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressapprove{request_id} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressdeny{request_id} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressrules endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test cleanup of expired pending requests.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test suite for egress approval API endpoints.]] - rationale - gateway/tests/test_egress_approval.py
- [[TestEgressApprovalAPI]] - code - gateway/tests/test_egress_approval.py
- [[egress_approval.py]] - code - gateway/security/egress_approval.py
- [[test_egress_approval.py]] - code - gateway/tests/test_egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_200
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 252]]
- 4 edges to [[_COMMUNITY_Module Group 117]]
- 3 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 3 edges to [[_COMMUNITY_Egress Filter & Approval]]
- 2 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 2 edges to [[_COMMUNITY_Module Group 522]]
- 1 edge to [[_COMMUNITY_Dashboard Routes & WebSocket]]
- 1 edge to [[_COMMUNITY_Module Group 334]]
- 1 edge to [[_COMMUNITY_Module Group 231]]
- 1 edge to [[_COMMUNITY_Module Group 240]]
- 1 edge to [[_COMMUNITY_Module Group 74]]

## Top bridge nodes
- [[egress_approval.py]] - degree 10, connects to 8 communities
- [[test_egress_approval.py]] - degree 7, connects to 4 communities
- [[TestEgressApprovalAPI]] - degree 15, connects to 3 communities
- [[RiskLevel]] - degree 7, connects to 3 communities
- [[EgressRequest]] - degree 7, connects to 2 communities