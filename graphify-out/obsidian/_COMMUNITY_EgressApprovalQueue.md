---
type: community
members: 31
---

# EgressApprovalQueue

**Members:** 31 nodes

## Members
- [[dot-_append_decision()]] - code - gateway/security/egress_approval.py
- [[dot-_rule_to_dict()]] - code - gateway/security/egress_approval.py
- [[dot-_save_rules()]] - code - gateway/security/egress_approval.py
- [[dot-approve()]] - code - gateway/security/egress_approval.py
- [[dot-cleanup_expired()_1]] - code - gateway/security/egress_approval.py
- [[dot-deny()]] - code - gateway/security/egress_approval.py
- [[dot-get_all_rules()]] - code - gateway/security/egress_approval.py
- [[dot-get_decision_log()]] - code - gateway/security/egress_approval.py
- [[dot-get_emergency_status()]] - code - gateway/security/egress_approval.py
- [[dot-get_pending_requests()]] - code - gateway/security/egress_approval.py
- [[dot-log_external_decision()]] - code - gateway/security/egress_approval.py
- [[dot-remove_rule()]] - code - gateway/security/egress_approval.py
- [[dot-revoke_decision()]] - code - gateway/security/egress_approval.py
- [[dot-set_emergency_block_all()]] - code - gateway/security/egress_approval.py
- [[dot-set_event_bus()_1]] - code - gateway/security/egress_approval.py
- [[Append an entry to the capped decision audit log (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Approve a pending egress request. Args request_id ID of request to approve…]] - rationale - gateway/security/egress_approval.py
- [[Deny a pending egress request. Args request_id ID of request to deny mode…]] - rationale - gateway/security/egress_approval.py
- [[EgressApprovalQueue]] - code - gateway/security/egress_approval.py
- [[Enabledisable emergency global egress deny.]] - rationale - gateway/security/egress_approval.py
- [[Get all rules (permanent and session) with scope information.]] - rationale - gateway/security/egress_approval.py
- [[Get emergency block-all state.]] - rationale - gateway/security/egress_approval.py
- [[Get list of pending approval requests.]] - rationale - gateway/security/egress_approval.py
- [[Log an automatic allowdeny from EgressFilter.check() (non-interactive).…]] - rationale - gateway/security/egress_approval.py
- [[Remove an egress rule. Args domain Domain to remove rule for Returns True if…]] - rationale - gateway/security/egress_approval.py
- [[Remove expired session rules and timed-out requests.]] - rationale - gateway/security/egress_approval.py
- [[Return recent approvaldenial decisions (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Revoke an active rule associated with a decision log entry (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Save rules to persistent storage.]] - rationale - gateway/security/egress_approval.py
- [[Set optional event bus for approval telemetry.]] - rationale - gateway/security/egress_approval.py
- [[Thread-safe asyncio queue for managing egress approval requests. Features -…]] - rationale - gateway/security/egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressApprovalQueue
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_EgressScope]]
- 5 edges to [[_COMMUNITY_egress_approval.py]]
- 2 edges to [[_COMMUNITY_fixture]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalQueue]]
- 1 edge to [[_COMMUNITY_TestEgressApprovalAPI]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_email_send]]

## Top bridge nodes
- [[EgressApprovalQueue]] - degree 32, connects to 7 communities
- [[dot-approve()]] - degree 7, connects to 3 communities
- [[dot-deny()]] - degree 7, connects to 3 communities
- [[dot-_rule_to_dict()]] - degree 4, connects to 2 communities
- [[dot-_save_rules()]] - degree 9, connects to 1 community
