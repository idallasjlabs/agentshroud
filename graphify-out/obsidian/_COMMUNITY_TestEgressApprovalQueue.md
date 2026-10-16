---
type: community
cohesion: 0.03
members: 69
---

# TestEgressApprovalQueue

**Cohesion:** 0.03 - loosely connected
**Members:** 69 nodes

## Members
- [[dot-approval_queue()]] - code - gateway/tests/test_egress_approval.py
- [[dot-mock_app_state()]] - code - gateway/tests/test_egress_approval.py
- [[dot-mock_auth()]] - code - gateway/tests/test_egress_approval.py
- [[dot-temp_rules_file()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_add_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_allowlist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approval_flow_once()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approval_flow_permanent()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approval_flow_session()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approve_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_cleanup_expired_requests()_1]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_denial_flow()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_deny_endpoint_logic()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_denylist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_emergency_block_all_denies_requests()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_existing_rule_bypass()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_get_egress_rules_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_basic()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_cap()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_different_agent_same_domain()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_throttle_same_agent_domain()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_pending_requests_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_remove_egress_rule_endpoint()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_risk_assessment_green()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_risk_assessment_red()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_risk_assessment_yellow()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_rule_management()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_session_rules_not_persisted()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_timeout_behavior()]] - code - gateway/tests/test_egress_approval.py
- [[Approval modes for rules.]] - rationale - gateway/security/egress_approval.py
- [[ApprovalMode]] - code - gateway/security/egress_approval.py
- [[Create EgressApprovalQueue instance for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[Create temporary rules file for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[Decision log is capped at 500 entries.]] - rationale - gateway/tests/test_egress_approval.py
- [[Different agent_ids for the same domain each produce their own log entry.]] - rationale - gateway/tests/test_egress_approval.py
- [[EgressRequest_1]] - code - gateway/security/egress_approval.py
- [[Emergency block-all should deny all new approval requests.]] - rationale - gateway/tests/test_egress_approval.py
- [[Mock app_state with egress approval queue.]] - rationale - gateway/tests/test_egress_approval.py
- [[Mock authentication dependency.]] - rationale - gateway/tests/test_egress_approval.py
- [[Represents a pending egress approval request.]] - rationale - gateway/security/egress_approval.py
- [[Risk assessment levels for egress requests.]] - rationale - gateway/security/egress_approval.py
- [[RiskLevel_6]] - code - gateway/security/egress_approval.py
- [[Second call within 1 hour for the same (agent_id, domain) is suppressed.]] - rationale - gateway/tests/test_egress_approval.py
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
- [[egress_approval.py]] - code - gateway/security/egress_approval.py
- [[log_external_decision appends an entry to the decision log.]] - rationale - gateway/tests/test_egress_approval.py
- [[test_egress_approval.py]] - code - gateway/tests/test_egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEgressApprovalQueue
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 5 edges to [[_COMMUNITY__make_filter]]
- 5 edges to [[_COMMUNITY_test_soc_router_coverage.py]]
- 3 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_1]]
- 1 edge to [[_COMMUNITY_RBACConfig]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_dot-_filter_outbound]]

## Top bridge nodes
- [[ApprovalMode]] - degree 20, connects to 8 communities
- [[egress_approval.py]] - degree 11, connects to 6 communities
- [[TestEgressApprovalQueue]] - degree 29, connects to 2 communities
- [[TestEgressApprovalAPI]] - degree 15, connects to 2 communities
- [[RiskLevel_6]] - degree 7, connects to 2 communities
