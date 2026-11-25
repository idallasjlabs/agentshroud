---
type: community
members: 26
---

# TestEgressApprovalQueue

**Members:** 26 nodes

## Members
- [[dot-test_cleanup_expired_requests()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_denylist_persistence()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_emergency_block_all_denies_requests()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_basic()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_cap()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_different_agent_same_domain()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_log_external_decision_throttle_same_agent_domain()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_risk_assessment_green()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_risk_assessment_red()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_risk_assessment_yellow()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_session_rules_not_persisted()]] - code - gateway/tests/test_egress_approval.py
- [[dot-test_timeout_behavior()]] - code - gateway/tests/test_egress_approval.py
- [[Decision log is capped at 500 entries.]] - rationale - gateway/tests/test_egress_approval.py
- [[Different agent_ids for the same domain each produce their own log entry.]] - rationale - gateway/tests/test_egress_approval.py
- [[Emergency block-all should deny all new approval requests.]] - rationale - gateway/tests/test_egress_approval.py
- [[Second call within 1 hour for the same (agent_id, domain) is suppressed.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test cleanup of expired pending requests.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test request timeout behavior.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test risk assessment for high-risk targets.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test risk assessment for known-safe domains.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test risk assessment for unknown domains on standard ports.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test suite for EgressApprovalQueue functionality.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that denylist rules are persisted to disk.]] - rationale - gateway/tests/test_egress_approval.py
- [[Test that session rules are not persisted to disk.]] - rationale - gateway/tests/test_egress_approval.py
- [[TestEgressApprovalQueue]] - code - gateway/tests/test_egress_approval.py
- [[log_external_decision appends an entry to the decision log.]] - rationale - gateway/tests/test_egress_approval.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestEgressApprovalQueue
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_asyncio_7]]
- 6 edges to [[_COMMUNITY_ApprovalMode]]
- 2 edges to [[_COMMUNITY_fixture]]
- 1 edge to [[_COMMUNITY_EgressApprovalQueue]]

## Top bridge nodes
- [[TestEgressApprovalQueue]] - degree 28, connects to 4 communities
- [[dot-test_cleanup_expired_requests()]] - degree 4, connects to 2 communities
- [[dot-test_denylist_persistence()]] - degree 3, connects to 1 community
- [[dot-test_emergency_block_all_denies_requests()]] - degree 3, connects to 1 community
- [[dot-test_session_rules_not_persisted()]] - degree 3, connects to 1 community
