---
type: community
cohesion: 0.29
members: 7
---

# Hermes — Reference Verifier

**Cohesion:** 0.29 - loosely connected
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
TABLE source_file, type FROM #community/Hermes__Reference_Verifier
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Quick Reference — AgentShroud]]
- 2 edges to [[_COMMUNITY_TestCanvasAuthHelpers]]

## Top bridge nodes
- [[TestOutputTrustScoring]] - degree 12, connects to 2 communities