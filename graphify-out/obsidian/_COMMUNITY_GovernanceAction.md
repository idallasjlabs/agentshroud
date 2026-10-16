---
type: community
cohesion: 0.14
members: 18
---

# GovernanceAction

**Cohesion:** 0.14 - loosely connected
**Members:** 18 nodes

## Members
- [[dot-_log_event()_1]] - code - gateway/security/subagent_governance.py
- [[dot-acceptable()]] - code - gateway/security/subagent_governance.py
- [[dot-get_governance_events()]] - code - gateway/security/subagent_governance.py
- [[dot-test_deregister_cleans_up()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_deregister_returns_usage()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_summary()_1]] - code - gateway/tests/test_subagent_governance.py
- [[Action to take when a governance limit is hit.]] - rationale - gateway/security/subagent_governance.py
- [[Configuration for subagent output trust scoring.]] - rationale - gateway/security/subagent_governance.py
- [[GovernanceAction]] - code - gateway/security/subagent_governance.py
- [[GovernanceEvent]] - code - gateway/security/subagent_governance.py
- [[GovernanceEventType]] - code - gateway/security/subagent_governance.py
- [[OutputScore]] - code - gateway/security/subagent_governance.py
- [[OutputTrustConfig]] - code - gateway/security/subagent_governance.py
- [[Privilege escalation prevention policy.]] - rationale - gateway/security/subagent_governance.py
- [[PrivilegePolicy]] - code - gateway/security/subagent_governance.py
- [[Result of scoring a subagent's output.]] - rationale - gateway/security/subagent_governance.py
- [[TestLifecycle_1]] - code - gateway/tests/test_subagent_governance.py
- [[subagent_governance.py]] - code - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GovernanceAction
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_SubagentGovernance]]
- 7 edges to [[_COMMUNITY_TestPatternDetection]]
- 6 edges to [[_COMMUNITY_dot-_check_budget]]
- 5 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 2 edges to [[_COMMUNITY_TestOutputTrustScoring]]
- 2 edges to [[_COMMUNITY_TestSpawnAuthorization]]
- 2 edges to [[_COMMUNITY_TestToolAuthorization]]
- 2 edges to [[_COMMUNITY_ResourceUsage]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]

## Top bridge nodes
- [[subagent_governance.py]] - degree 15, connects to 6 communities
- [[GovernanceAction]] - degree 12, connects to 6 communities
- [[GovernanceEventType]] - degree 12, connects to 6 communities
- [[dot-_log_event()_1]] - degree 8, connects to 3 communities
- [[TestLifecycle_1]] - degree 9, connects to 2 communities
