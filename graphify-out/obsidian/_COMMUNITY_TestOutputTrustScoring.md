---
type: community
cohesion: 0.29
members: 7
---

# TestOutputTrustScoring

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[dot-test_api_key_detected()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_clean_output_high_score()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_exfil_pattern_detected()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_injection_detected()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_low_agent_trust_penalty()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_pii_detected_lowers_score()]] - code - gateway/tests/test_subagent_governance.py
- [[TestOutputTrustScoring]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutputTrustScoring
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_SubagentGovernance]]
- 2 edges to [[_COMMUNITY_GovernanceAction]]
- 1 edge to [[_COMMUNITY_dot-_check_budget]]

## Top bridge nodes
- [[TestOutputTrustScoring]] - degree 12, connects to 3 communities
