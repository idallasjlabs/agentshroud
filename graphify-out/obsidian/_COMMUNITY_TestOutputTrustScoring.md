---
type: community
cohesion: 0.29
members: 7
---

# TestOutputTrustScoring

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_api_key_detected()_1]] - code - gateway/tests/test_subagent_governance.py
- [[.test_clean_output_high_score()_1]] - code - gateway/tests/test_subagent_governance.py
- [[.test_exfil_pattern_detected()_1]] - code - gateway/tests/test_subagent_governance.py
- [[.test_injection_detected()_1]] - code - gateway/tests/test_subagent_governance.py
- [[.test_low_agent_trust_penalty()_1]] - code - gateway/tests/test_subagent_governance.py
- [[.test_pii_detected_lowers_score()_1]] - code - gateway/tests/test_subagent_governance.py
- [[TestOutputTrustScoring_1]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutputTrustScoring
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[TestOutputTrustScoring_1]] - degree 7, connects to 1 community