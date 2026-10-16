---
type: community
cohesion: 0.04
members: 49
---

# TestEgressApprovalQueue

**Cohesion:** 0.04 - loosely connected
**Members:** 49 nodes

## Members
- [[dot-approval_queue()]] - code - gateway/tests/test_egress_approval.py
- [[dot-temp_rules_file()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_allowlist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approval_flow_once()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approval_flow_permanent()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_approval_flow_session()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_cleanup_expired_requests()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_denial_flow()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_denylist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_emergency_block_all_denies_requests()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_existing_rule_bypass()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_basic()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_cap()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_different_agent_same_domain()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_throttle_same_agent_domain()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_risk_assessment_green()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_risk_assessment_red()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_risk_assessment_yellow()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_rule_management()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_session_rules_not_persisted()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_timeout_behavior()]] - code - gateway/tests/test_egress_approval.py
- [[Create EgressApprovalQueue instance for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[Create temporary rules file for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[Decision log is capped at 500 entries.]] - rationale - gateway/tests/test_egress_approval.py
- [[Different agent_ids for the same domain each produce their own log entry.]] - rationale - gateway/tests/test_egress_approval.py
- [[EgressRequest]] - code - gateway/security/egress_approval.py
- [[Emergency block-all should deny all new approval requests.]] - rationale - gateway/tests/test_egress_approval.py
- [[Represents a pending egress approval request.]] - rationale - gateway/security/egress_approval.py
- [[Risk assessment levels for egress requests.]] - rationale - gateway/security/egress_approval.py
- [[RiskLevel]] - code - gateway/security/egress_approval.py
- [[Second call within 1 hour for the same (agent_id, domain) is suppressed.]] - rationale - gateway/tests/test_egress_approval.py
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
- [[Test that allowlist rules are persisted to disk.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that denylist rules are persisted to disk.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that existing rules bypass the approval queue.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that session rules are not persisted to disk.]] - rationale - gateway/tests/test_egress_approval.py
- [[TestEgressApprovalQueue]] - code - gateway/tests/test_egress_approval.py
- [[log_external_decision appends an entry to the decision log.]] - rationale - gateway/tests/test_egress_approval.py
- [[test_egress_approval.py]] - code - gateway/tests/test_egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEgressApprovalQueue
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_TestEgressApprovalQueue]]
- 3 edges to [[_COMMUNITY_TestEgressApprovalQueue_2]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig_1]]
- 1 edge to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[RiskLevel]] - degree 7, connects to 3 communities
- [[test_egress_approval.py]] - degree 7, connects to 3 communities
- [[TestEgressApprovalQueue]] - degree 29, connects to 2 communities
- [[EgressRequest]] - degree 7, connects to 2 communities
- [[dot-approval_queue()]] - degree 3, connects to 1 community
