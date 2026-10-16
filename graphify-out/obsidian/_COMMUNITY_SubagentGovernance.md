---
type: community
cohesion: 0.22
members: 20
---

# SubagentGovernance

**Cohesion:** 0.22 - loosely connected
**Members:** 20 nodes

## Members
- [[dot-__init__()_150]] - code - gateway/security/subagent_governance.py
- [[dot-test_api_calls_exceed()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_no_tracking_returns_ok()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_tokens_exceed_budget()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_tokens_within_budget()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_tool_calls_budget_blocks_authorize_tool()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_warning_at_80_percent()]] - code - gateway/tests/test_subagent_governance.py
- [[Default governance instance in enforce mode.]] - rationale - gateway/tests/test_subagent_governance.py
- [[Governance in monitor mode (log but don't block).]] - rationale - gateway/tests/test_subagent_governance.py
- [[GovernanceConfig]] - code - gateway/security/subagent_governance.py
- [[Per-subagent resource limits.]] - rationale - gateway/security/subagent_governance.py
- [[ResourceBudget]] - code - gateway/security/subagent_governance.py
- [[SubagentGovernance]] - code - gateway/security/subagent_governance.py
- [[TestResourceBudgets]] - code - gateway/tests/test_subagent_governance.py
- [[Top-level governance configuration.]] - rationale - gateway/security/subagent_governance.py
- [[Unified governance layer for subagent lifecycle.      Wraps SubagentMonitor with]] - rationale - gateway/security/subagent_governance.py
- [[disabled_gov()]] - code - gateway/tests/test_subagent_governance.py
- [[gov()]] - code - gateway/tests/test_subagent_governance.py
- [[monitor_gov()]] - code - gateway/tests/test_subagent_governance.py
- [[test_subagent_governance.py]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SubagentGovernance
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_GovernanceAction]]
- 8 edges to [[_COMMUNITY_TestPatternDetection]]
- 6 edges to [[_COMMUNITY_dot-_check_budget]]
- 4 edges to [[_COMMUNITY_TestOutputTrustScoring]]
- 4 edges to [[_COMMUNITY_TestSpawnAuthorization]]
- 4 edges to [[_COMMUNITY_TestToolAuthorization]]
- 3 edges to [[_COMMUNITY_subagent_governance.py]]
- 3 edges to [[_COMMUNITY_ResourceUsage]]

## Top bridge nodes
- [[SubagentGovernance]] - degree 30, connects to 8 communities
- [[GovernanceConfig]] - degree 17, connects to 6 communities
- [[ResourceBudget]] - degree 13, connects to 6 communities
- [[test_subagent_governance.py]] - degree 17, connects to 5 communities
- [[TestResourceBudgets]] - degree 12, connects to 1 community
