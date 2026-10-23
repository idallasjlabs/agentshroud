---
type: community
cohesion: 0.27
members: 6
---

# TestHeuristicClassifierDirectly

**Cohesion:** 0.27 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_classifier_flags_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_high_confidence_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier returns injection or uncertain on known bad payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[PromptGuard scans high-confidence classic payloads with non-zero score.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[TestHeuristicClassifierDirectly]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPromptGuardDirectly]] - code - gateway/tests/test_adversarial_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestHeuristicClassifierDirectly
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_soc_egress_endpoints.py]]
- 2 edges to [[_COMMUNITY_HeuristicClassifier]]
- 2 edges to [[_COMMUNITY_PromptGuard]]

## Top bridge nodes
- [[TestHeuristicClassifierDirectly]] - degree 5, connects to 3 communities
- [[TestPromptGuardDirectly]] - degree 5, connects to 3 communities
- [[dot-test_classifier_flags_payloads()]] - degree 2, connects to 1 community
- [[dot-test_high_confidence_payloads()]] - degree 2, connects to 1 community
