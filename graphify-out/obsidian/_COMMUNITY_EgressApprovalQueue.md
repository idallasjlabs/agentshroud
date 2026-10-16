---
type: community
cohesion: 0.05
members: 56
---

# EgressApprovalQueue

**Cohesion:** 0.05 - loosely connected
**Members:** 56 nodes

## Members
- [[dot-__init__()_14]] - code - gateway/security/egress_approval.py
- [[dot-_append_decision()]] - code - gateway/security/egress_approval.py
- [[dot-_assess_risk()]] - code - gateway/security/egress_approval.py
- [[dot-_check_existing_rule()]] - code - gateway/security/egress_approval.py
- [[dot-_load_rules()]] - code - gateway/security/egress_approval.py
- [[dot-_rule_to_dict()]] - code - gateway/security/egress_approval.py
- [[dot-_save_rules()]] - code - gateway/security/egress_approval.py
- [[dot-add_rule()]] - code - gateway/security/egress_approval.py
- [[dot-approve()]] - code - gateway/security/egress_approval.py
- [[dot-cleanup_expired()]] - code - gateway/security/egress_approval.py
- [[dot-deny()]] - code - gateway/security/egress_approval.py
- [[dot-from_dict()]] - code - gateway/security/egress_approval.py
- [[dot-get_all_rules()]] - code - gateway/security/egress_approval.py
- [[dot-get_decision_log()]] - code - gateway/security/egress_approval.py
- [[dot-get_emergency_status()]] - code - gateway/security/egress_approval.py
- [[dot-get_pending_requests()]] - code - gateway/security/egress_approval.py
- [[dot-get_rules_for_user()]] - code - gateway/security/egress_approval.py
- [[dot-log_external_decision()]] - code - gateway/security/egress_approval.py
- [[dot-matches()]] - code - gateway/security/egress_approval.py
- [[dot-preload_permanent_rules()]] - code - gateway/security/egress_approval.py
- [[dot-remove_rule()]] - code - gateway/security/egress_approval.py
- [[dot-request_approval()]] - code - gateway/security/egress_approval.py
- [[dot-revoke_decision()]] - code - gateway/security/egress_approval.py
- [[dot-set_emergency_block_all()]] - code - gateway/security/egress_approval.py
- [[dot-set_event_bus()]] - code - gateway/security/egress_approval.py
- [[dot-to_dict()_1]] - code - gateway/security/egress_approval.py
- [[Add or modify an egress rule.          Args             domain Target domain]] - rationale - gateway/security/egress_approval.py
- [[Append an entry to the capped decision audit log (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Approve a pending egress request.          Args             request_id ID of r]] - rationale - gateway/security/egress_approval.py
- [[Assess risk level for a domainport combination.          Returns             R]] - rationale - gateway/security/egress_approval.py
- [[Check if domain matches an existing rule.]] - rationale - gateway/security/egress_approval.py
- [[Defines who an egress rule applies to.      kind values       all   — applies]] - rationale - gateway/security/egress_approval.py
- [[Deny a pending egress request.          Args             request_id ID of requ]] - rationale - gateway/security/egress_approval.py
- [[EgressApprovalQueue]] - code - gateway/security/egress_approval.py
- [[EgressRule]] - code - gateway/security/egress_approval.py
- [[EgressScope]] - code - gateway/security/egress_approval.py
- [[Enabledisable emergency global egress deny.]] - rationale - gateway/security/egress_approval.py
- [[Get all rules (permanent and session) with scope information.]] - rationale - gateway/security/egress_approval.py
- [[Get emergency block-all state.]] - rationale - gateway/security/egress_approval.py
- [[Get list of pending approval requests.]] - rationale - gateway/security/egress_approval.py
- [[Initialize the approval queue.          Args             rules_file Path to pe]] - rationale - gateway/security/egress_approval.py
- [[Load rules from persistent storage.]] - rationale - gateway/security/egress_approval.py
- [[Log an automatic allowdeny from EgressFilter.check() (non-interactive).]] - rationale - gateway/security/egress_approval.py
- [[Pre-approve known service domains at startup without interactive prompts.]] - rationale - gateway/security/egress_approval.py
- [[Public risk assessment helper for managementAPI surfaces.]] - rationale - gateway/security/egress_approval.py
- [[Remove an egress rule.          Args             domain Domain to remove rule]] - rationale - gateway/security/egress_approval.py
- [[Remove expired session rules and timed-out requests.]] - rationale - gateway/security/egress_approval.py
- [[Represents an egress allowdeny rule.]] - rationale - gateway/security/egress_approval.py
- [[Request approval for egress to a domainport.          Args             domain]] - rationale - gateway/security/egress_approval.py
- [[Return True if this scope applies to the given user context.]] - rationale - gateway/security/egress_approval.py
- [[Return all rules whose scope matches the given user context (synchronous, lock-f]] - rationale - gateway/security/egress_approval.py
- [[Return recent approvaldenial decisions (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Revoke an active rule associated with a decision log entry (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Save rules to persistent storage.]] - rationale - gateway/security/egress_approval.py
- [[Set optional event bus for approval telemetry.]] - rationale - gateway/security/egress_approval.py
- [[Thread-safe asyncio queue for managing egress approval requests.      Features]] - rationale - gateway/security/egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressApprovalQueue
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 3 edges to [[_COMMUNITY_make_event]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_1]]
- 1 edge to [[_COMMUNITY__make_filter]]
- 1 edge to [[_COMMUNITY_Path]]

## Top bridge nodes
- [[EgressApprovalQueue]] - degree 35, connects to 4 communities
- [[dot-request_approval()]] - degree 7, connects to 3 communities
- [[EgressScope]] - degree 12, connects to 2 communities
- [[dot-approve()]] - degree 7, connects to 2 communities
- [[dot-deny()]] - degree 7, connects to 2 communities
