---
type: community
cohesion: 0.67
members: 3
---

# Adversarial Injection

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[.test_classifier_flags_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier returns injection or uncertain on known bad payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[TestHeuristicClassifierDirectly]] - code - gateway/tests/test_adversarial_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Adversarial_Injection
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Adversarial Injection]]
- 1 edge to [[_COMMUNITY_Heuristic Classifier (security)]]
- 1 edge to [[_COMMUNITY_Security Audit & Watchtower Tests]]

## Top bridge nodes
- [[TestHeuristicClassifierDirectly]] - degree 5, connects to 3 communities
- [[.test_classifier_flags_payloads()]] - degree 2, connects to 1 community