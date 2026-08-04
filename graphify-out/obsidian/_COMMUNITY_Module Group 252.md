---
type: community
cohesion: 0.11
members: 18
---

# Module Group 252

**Cohesion:** 0.11 - loosely connected
**Members:** 18 nodes

## Members
- [[.approval_queue()]] - code - gateway/tests/test_egress_approval.py
- [[.get_decision_log()]] - code - gateway/security/egress_approval.py
- [[.get_emergency_status()]] - code - gateway/security/egress_approval.py
- [[.get_pending_requests()]] - code - gateway/security/egress_approval.py
- [[.log_external_decision()]] - code - gateway/security/egress_approval.py
- [[.mock_app_state()]] - code - gateway/tests/test_egress_approval.py
- [[.set_emergency_block_all()]] - code - gateway/security/egress_approval.py
- [[.set_event_bus()_1]] - code - gateway/security/egress_approval.py
- [[Create EgressApprovalQueue instance for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[EgressApprovalQueue]] - code - gateway/security/egress_approval.py
- [[Enabledisable emergency global egress deny.]] - rationale - gateway/security/egress_approval.py
- [[Get emergency block-all state.]] - rationale - gateway/security/egress_approval.py
- [[Get list of pending approval requests.]] - rationale - gateway/security/egress_approval.py
- [[Log an automatic allowdeny from EgressFilter.check() (non-interactive).]] - rationale - gateway/security/egress_approval.py
- [[Mock app_state with egress approval queue.]] - rationale - gateway/tests/test_egress_approval.py
- [[Return recent approvaldenial decisions (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Set optional event bus for approval telemetry.]] - rationale - gateway/security/egress_approval.py
- [[Thread-safe asyncio queue for managing egress approval requests.      Features]] - rationale - gateway/security/egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_252
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Module Group 231]]
- 5 edges to [[_COMMUNITY_Module Group 334]]
- 4 edges to [[_COMMUNITY_Module Group 200]]
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]
- 2 edges to [[_COMMUNITY_Module Group 522]]
- 2 edges to [[_COMMUNITY_Module Group 523]]
- 2 edges to [[_COMMUNITY_Module Group 117]]

## Top bridge nodes
- [[EgressApprovalQueue]] - degree 32, connects to 7 communities
- [[.mock_app_state()]] - degree 3, connects to 1 community
- [[.approval_queue()]] - degree 3, connects to 1 community
