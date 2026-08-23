---
type: community
cohesion: 0.02
members: 125
---

# Egress Approval (security)

**Cohesion:** 0.02 - loosely connected
**Members:** 125 nodes

## Members
- [[.__init__()_74]] - code - gateway/security/egress_approval.py
- [[._append_decision()]] - code - gateway/security/egress_approval.py
- [[._assess_risk()]] - code - gateway/security/egress_approval.py
- [[._check_existing_rule()]] - code - gateway/security/egress_approval.py
- [[._load_rules()]] - code - gateway/security/egress_approval.py
- [[._rule_to_dict()]] - code - gateway/security/egress_approval.py
- [[._save_rules()]] - code - gateway/security/egress_approval.py
- [[.add_rule()]] - code - gateway/security/egress_approval.py
- [[.approval_queue()]] - code - gateway/tests/test_egress_approval.py
- [[.approve()]] - code - gateway/security/egress_approval.py
- [[.cleanup_expired()_2]] - code - gateway/security/egress_approval.py
- [[.deny()]] - code - gateway/security/egress_approval.py
- [[.from_dict()_6]] - code - gateway/security/egress_approval.py
- [[.get_all_rules()]] - code - gateway/security/egress_approval.py
- [[.get_decision_log()]] - code - gateway/security/egress_approval.py
- [[.get_emergency_status()]] - code - gateway/security/egress_approval.py
- [[.get_pending_requests()]] - code - gateway/security/egress_approval.py
- [[.get_rules_for_user()]] - code - gateway/security/egress_approval.py
- [[.log_external_decision()]] - code - gateway/security/egress_approval.py
- [[.matches()]] - code - gateway/security/egress_approval.py
- [[.mock_app_state()]] - code - gateway/tests/test_egress_approval.py
- [[.mock_auth()]] - code - gateway/tests/test_egress_approval.py
- [[.preload_permanent_rules()]] - code - gateway/security/egress_approval.py
- [[.remove_rule()]] - code - gateway/security/egress_approval.py
- [[.request_approval()]] - code - gateway/security/egress_approval.py
- [[.revoke_decision()]] - code - gateway/security/egress_approval.py
- [[.set_emergency_block_all()]] - code - gateway/security/egress_approval.py
- [[.set_event_bus()_1]] - code - gateway/security/egress_approval.py
- [[.temp_rules_file()]] - code - gateway/tests/test_egress_approval.py
- [[.test_add_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[.test_allowlist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[.test_approval_flow_once()]] - code - gateway/tests/test_egress_approval.py
- [[.test_approval_flow_permanent()]] - code - gateway/tests/test_egress_approval.py
- [[.test_approval_flow_session()]] - code - gateway/tests/test_egress_approval.py
- [[.test_approve_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[.test_cleanup_expired_requests()]] - code - gateway/tests/test_egress_approval.py
- [[.test_denial_flow()]] - code - gateway/tests/test_egress_approval.py
- [[.test_deny_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[.test_denylist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[.test_emergency_block_all_denies_requests()]] - code - gateway/tests/test_egress_approval.py
- [[.test_existing_rule_bypass()]] - code - gateway/tests/test_egress_approval.py
- [[.test_get_egress_rules_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[.test_log_external_decision_basic()]] - code - gateway/tests/test_egress_approval.py
- [[.test_log_external_decision_cap()]] - code - gateway/tests/test_egress_approval.py
- [[.test_log_external_decision_different_agent_same_domain()]] - code - gateway/tests/test_egress_approval.py
- [[.test_log_external_decision_throttle_same_agent_domain()]] - code - gateway/tests/test_egress_approval.py
- [[.test_pending_requests_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[.test_remove_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[.test_risk_assessment_green()]] - code - gateway/tests/test_egress_approval.py
- [[.test_risk_assessment_red()]] - code - gateway/tests/test_egress_approval.py
- [[.test_risk_assessment_yellow()]] - code - gateway/tests/test_egress_approval.py
- [[.test_rule_management()]] - code - gateway/tests/test_egress_approval.py
- [[.test_session_rules_not_persisted()]] - code - gateway/tests/test_egress_approval.py
- [[.test_timeout_behavior()]] - code - gateway/tests/test_egress_approval.py
- [[.to_dict()_9]] - code - gateway/security/egress_approval.py
- [[Add or modify an egress rule.          Args             domain Target domain]] - rationale - gateway/security/egress_approval.py
- [[Append an entry to the capped decision audit log (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Approval modes for rules.]] - rationale - gateway/security/egress_approval.py
- [[ApprovalMode]] - code - gateway/security/egress_approval.py
- [[Approve a pending egress request.          Args             request_id ID of r]] - rationale - gateway/security/egress_approval.py
- [[Assess risk level for a domainport combination.          Returns             R]] - rationale - gateway/security/egress_approval.py
- [[Check if domain matches an existing rule.]] - rationale - gateway/security/egress_approval.py
- [[Create EgressApprovalQueue instance for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[Create temporary rules file for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[Decision log is capped at 500 entries.]] - rationale - gateway/tests/test_egress_approval.py
- [[Defines who an egress rule applies to.      kind values       all   — applies]] - rationale - gateway/security/egress_approval.py
- [[Deny a pending egress request.          Args             request_id ID of requ]] - rationale - gateway/security/egress_approval.py
- [[Different agent_ids for the same domain each produce their own log entry.]] - rationale - gateway/tests/test_egress_approval.py
- [[EgressApprovalQueue]] - code - gateway/security/egress_approval.py
- [[EgressRequest]] - code - gateway/security/egress_approval.py
- [[EgressRule]] - code - gateway/security/egress_approval.py
- [[EgressScope]] - code - gateway/security/egress_approval.py
- [[Emergency block-all should deny all new approval requests.]] - rationale - gateway/tests/test_egress_approval.py
- [[Enabledisable emergency global egress deny.]] - rationale - gateway/security/egress_approval.py
- [[Get all rules (permanent and session) with scope information.]] - rationale - gateway/security/egress_approval.py
- [[Get emergency block-all state.]] - rationale - gateway/security/egress_approval.py
- [[Get list of pending approval requests.]] - rationale - gateway/security/egress_approval.py
- [[Initialize the approval queue.          Args             rules_file Path to pe]] - rationale - gateway/security/egress_approval.py
- [[Load rules from persistent storage.]] - rationale - gateway/security/egress_approval.py
- [[Log an automatic allowdeny from EgressFilter.check() (non-interactive).]] - rationale - gateway/security/egress_approval.py
- [[Mock app_state with egress approval queue.]] - rationale - gateway/tests/test_egress_approval.py
- [[Mock authentication dependency.]] - rationale - gateway/tests/test_egress_approval.py
- [[Pre-approve known service domains at startup without interactive prompts.]] - rationale - gateway/security/egress_approval.py
- [[Public risk assessment helper for managementAPI surfaces.]] - rationale - gateway/security/egress_approval.py
- [[Remove an egress rule.          Args             domain Domain to remove rule]] - rationale - gateway/security/egress_approval.py
- [[Remove expired session rules and timed-out requests.]] - rationale - gateway/security/egress_approval.py
- [[Represents a pending egress approval request.]] - rationale - gateway/security/egress_approval.py
- [[Represents an egress allowdeny rule.]] - rationale - gateway/security/egress_approval.py
- [[Request approval for egress to a domainport.          Args             domain]] - rationale - gateway/security/egress_approval.py
- [[Return True if this scope applies to the given user context.]] - rationale - gateway/security/egress_approval.py
- [[Return all rules whose scope matches the given user context (synchronous, lock-f]] - rationale - gateway/security/egress_approval.py
- [[Return recent approvaldenial decisions (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Revoke an active rule associated with a decision log entry (CC-40).]] - rationale - gateway/security/egress_approval.py
- [[Risk assessment levels for egress requests.]] - rationale - gateway/security/egress_approval.py
- [[RiskLevel_3]] - code - gateway/security/egress_approval.py
- [[Save rules to persistent storage.]] - rationale - gateway/security/egress_approval.py
- [[Second call within 1 hour for the same (agent_id, domain) is suppressed.]] - rationale - gateway/tests/test_egress_approval.py
- [[Set optional event bus for approval telemetry.]] - rationale - gateway/security/egress_approval.py
- [[Test DELETE manageegressrules{domain} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test GET manageegresspending endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test GET manageegressrules endpoint.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressapprove{request_id} endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test POST manageegressrules endpoint logic.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test adding and removing rules.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test approval flow with one-time approval.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test approval flow with permanent rule creation.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test approval flow with session rule creation.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test cleanup of expired pending requests.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test denial flow with rule creation.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test request timeout behavior.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test risk assessment for high-risk targets.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test risk assessment for known-safe domains.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test risk assessment for unknown domains on standard ports.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test suite for EgressApprovalQueue functionality.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test suite for egress approval API endpoints.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that allowlist rules are persisted to disk.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that denylist rules are persisted to disk.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that existing rules bypass the approval queue.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that session rules are not persisted to disk.]] - rationale - gateway/tests/test_egress_approval.py
- [[TestEgressApprovalAPI]] - code - gateway/tests/test_egress_approval.py
- [[TestEgressApprovalQueue]] - code - gateway/tests/test_egress_approval.py
- [[Thread-safe asyncio queue for managing egress approval requests.      Features]] - rationale - gateway/security/egress_approval.py
- [[egress_approval.py]] - code - gateway/security/egress_approval.py
- [[log_external_decision appends an entry to the decision log.]] - rationale - gateway/tests/test_egress_approval.py
- [[test_egress_approval.py]] - code - gateway/tests/test_egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Egress_Approval_security
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Ingest API Main & Models]]
- 6 edges to [[_COMMUNITY_Egress Filter]]
- 5 edges to [[_COMMUNITY_SOC Router Coverage]]
- 4 edges to [[_COMMUNITY_Soc Egress Endpoints]]
- 3 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 3 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 3 edges to [[_COMMUNITY_SOC Router (Collaborator Mgmt)]]
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 1 edge to [[_COMMUNITY_Manifest (skills)]]
- 1 edge to [[_COMMUNITY_Main Simple]]
- 1 edge to [[_COMMUNITY_Aiosqlite (05 - Dependencies)]]
- 1 edge to [[_COMMUNITY_Group Config & Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Progressive Lockdown]]
- 1 edge to [[_COMMUNITY_Delegation]]
- 1 edge to [[_COMMUNITY_Iec 62443 Matrix (compliance)]]
- 1 edge to [[_COMMUNITY_Egress Filter]]
- 1 edge to [[_COMMUNITY_Slack Proxy Coverage]]

## Top bridge nodes
- [[ApprovalMode]] - degree 30, connects to 9 communities
- [[egress_approval.py]] - degree 11, connects to 4 communities
- [[EgressApprovalQueue]] - degree 35, connects to 3 communities
- [[TestEgressApprovalQueue]] - degree 29, connects to 2 communities
- [[.request_approval()]] - degree 7, connects to 2 communities