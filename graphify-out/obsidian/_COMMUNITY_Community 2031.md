---
type: community
members: 7
---

# Community 2031

**Members:** 7 nodes

## Members
- [[.test_api_key_detected()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_clean_output_high_score()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_exfil_pattern_detected()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_injection_detected()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_low_agent_trust_penalty()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_pii_detected_lowers_score()]] - code - gateway/tests/test_subagent_governance.py
- [[TestOutputTrustScoring]] - code - gateway/tests/test_subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2031
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 1209]]
- 2 edges to [[_COMMUNITY_Community 1269]]
- 1 edge to [[_COMMUNITY_Community 1343]]

## Top bridge nodes
- [[TestOutputTrustScoring]] - degree 12, connects to 3 communities