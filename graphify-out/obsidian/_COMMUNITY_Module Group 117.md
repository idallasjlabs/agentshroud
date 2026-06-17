---
type: community
cohesion: 0.05
members: 40
---

# Module Group 117

**Cohesion:** 0.05 - loosely connected
**Members:** 40 nodes

## Members
- [[.temp_rules_file()]] - code - gateway/tests/test_egress_approval.py
- [[.test_allowlist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[.test_approval_flow_once()]] - code - gateway/tests/test_egress_approval.py
- [[.test_approval_flow_permanent()]] - code - gateway/tests/test_egress_approval.py
- [[.test_approval_flow_session()]] - code - gateway/tests/test_egress_approval.py
- [[.test_denial_flow()]] - code - gateway/tests/test_egress_approval.py
- [[.test_denylist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[.test_emergency_block_all_denies_requests()]] - code - gateway/tests/test_egress_approval.py
- [[.test_existing_rule_bypass()]] - code - gateway/tests/test_egress_approval.py
- [[.test_log_external_decision_basic()]] - code - gateway/tests/test_egress_approval.py
- [[.test_log_external_decision_cap()]] - code - gateway/tests/test_egress_approval.py
- [[.test_log_external_decision_different_agent_same_domain()]] - code - gateway/tests/test_egress_approval.py
- [[.test_log_external_decision_throttle_same_agent_domain()]] - code - gateway/tests/test_egress_approval.py
- [[.test_risk_assessment_green()]] - code - gateway/tests/test_egress_approval.py
- [[.test_risk_assessment_red()]] - code - gateway/tests/test_egress_approval.py
- [[.test_risk_assessment_yellow()]] - code - gateway/tests/test_egress_approval.py
- [[.test_rule_management()]] - code - gateway/tests/test_egress_approval.py
- [[.test_session_rules_not_persisted()]] - code - gateway/tests/test_egress_approval.py
- [[.test_timeout_behavior()]] - code - gateway/tests/test_egress_approval.py
- [[Create temporary rules file for testing.]] - rationale - gateway/tests/test_egress_approval.py
- [[Decision log is capped at 500 entries.]] - rationale - gateway/tests/test_egress_approval.py
- [[Different agent_ids for the same domain each produce their own log entry.]] - rationale - gateway/tests/test_egress_approval.py
- [[Emergency block-all should deny all new approval requests.]] - rationale - gateway/tests/test_egress_approval.py
- [[Second call within 1 hour for the same (agent_id, domain) is suppressed.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test adding and removing rules.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test approval flow with one-time approval.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test approval flow with permanent rule creation.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test approval flow with session rule creation.]] - rationale - gateway/tests/test_egress_approval.py
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

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_117
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 200]]
- 2 edges to [[_COMMUNITY_Module Group 252]]
- 1 edge to [[_COMMUNITY_Egress Filter & Approval]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]

## Top bridge nodes
- [[TestEgressApprovalQueue]] - degree 28, connects to 4 communities