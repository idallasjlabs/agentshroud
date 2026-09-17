---
type: community
cohesion: 0.05
members: 57
---

# EgressApprovalQueue

**Cohesion:** 0.05 - loosely connected
**Members:** 57 nodes

## Members
- [[.__init__()_191]] - code - gateway/security/egress_approval.py
- [[._append_decision()]] - code - gateway/security/egress_approval.py
- [[._assess_risk()]] - code - gateway/security/egress_approval.py
- [[._check_existing_rule()]] - code - gateway/security/egress_approval.py
- [[._load_rules()]] - code - gateway/security/egress_approval.py
- [[._rule_to_dict()]] - code - gateway/security/egress_approval.py
- [[._save_rules()]] - code - gateway/security/egress_approval.py
- [[.add_rule()]] - code - gateway/security/egress_approval.py
- [[.approve()]] - code - gateway/security/egress_approval.py
- [[.cleanup_expired()_3]] - code - gateway/security/egress_approval.py
- [[.deny()]] - code - gateway/security/egress_approval.py
- [[.from_dict()_8]] - code - gateway/security/egress_approval.py
- [[.get_all_rules()]] - code - gateway/security/egress_approval.py
- [[.get_decision_log()]] - code - gateway/security/egress_approval.py
- [[.get_emergency_status()]] - code - gateway/security/egress_approval.py
- [[.get_pending_requests()]] - code - gateway/security/egress_approval.py
- [[.get_rules_for_user()]] - code - gateway/security/egress_approval.py
- [[.log_external_decision()]] - code - gateway/security/egress_approval.py
- [[.matches()]] - code - gateway/security/egress_approval.py
- [[.preload_permanent_rules()]] - code - gateway/security/egress_approval.py
- [[.remove_rule()]] - code - gateway/security/egress_approval.py
- [[.request_approval()]] - code - gateway/security/egress_approval.py
- [[.revoke_decision()]] - code - gateway/security/egress_approval.py
- [[.set_emergency_block_all()]] - code - gateway/security/egress_approval.py
- [[.set_event_bus()_2]] - code - gateway/security/egress_approval.py
- [[.to_dict()_16]] - code - gateway/security/egress_approval.py
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
- [[egress_approval.py]] - code - gateway/security/egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressApprovalQueue
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 5 edges to [[_COMMUNITY_ingest_apimain.py]]
- 4 edges to [[_COMMUNITY_make_event()]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 1 edge to [[_COMMUNITY_cls]]
- 1 edge to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]

## Top bridge nodes
- [[egress_approval.py]] - degree 11, connects to 7 communities
- [[EgressApprovalQueue]] - degree 35, connects to 4 communities
- [[.request_approval()]] - degree 7, connects to 3 communities
- [[.approve()]] - degree 7, connects to 2 communities
- [[.deny()]] - degree 7, connects to 2 communities