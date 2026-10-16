---
type: community
cohesion: 0.18
members: 13
---

# GovernanceAction

**Cohesion:** 0.18 - loosely connected
**Members:** 13 nodes

## Members
- [[dot-_log_event()_1]] - code - gateway/security/subagent_governance.py
- [[dot-authorize_spawn()]] - code - gateway/security/subagent_governance.py
- [[dot-get_governance_events()]] - code - gateway/security/subagent_governance.py
- [[dot-test_deregister_cleans_up()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_deregister_returns_usage()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_summary()_1]] - code - gateway/tests/test_subagent_governance.py
- [[Action to take when a governance limit is hit.]] - rationale - gateway/security/subagent_governance.py
- [[Authorize a subagent spawn. Returns (allowed, reason).]] - rationale - gateway/security/subagent_governance.py
- [[GovernanceAction]] - code - gateway/security/subagent_governance.py
- [[GovernanceEvent]] - code - gateway/security/subagent_governance.py
- [[GovernanceEventType]] - code - gateway/security/subagent_governance.py
- [[Retrieve governance events with optional filters.]] - rationale - gateway/security/a2a_governance.py
- [[TestLifecycle_1]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GovernanceAction
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_SubagentGovernance]]
- 3 edges to [[_COMMUNITY_subagent_governance.py]]
- 3 edges to [[_COMMUNITY_TestPatternDetection]]
- 2 edges to [[_COMMUNITY_TestOutputTrustScoring]]
- 2 edges to [[_COMMUNITY_TestSpawnAuthorization]]
- 2 edges to [[_COMMUNITY_TestToolAuthorization]]
- 2 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_Action]]
- 2 edges to [[_COMMUNITY_dot-_check_budget]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]
- 1 edge to [[_COMMUNITY_ResourceUsage]]

## Top bridge nodes
- [[GovernanceAction]] - degree 12, connects to 8 communities
- [[GovernanceEventType]] - degree 12, connects to 8 communities
- [[dot-_log_event()_1]] - degree 8, connects to 3 communities
- [[dot-authorize_spawn()]] - degree 4, connects to 2 communities
- [[TestLifecycle_1]] - degree 9, connects to 1 community
