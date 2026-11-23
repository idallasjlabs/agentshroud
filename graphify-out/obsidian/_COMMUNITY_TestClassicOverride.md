---
type: community
members: 11
---

# TestClassicOverride

**Members:** 11 nodes

## Members
- [[dot-test_classic_override_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_classic_payloads_individually()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_classifier_flags_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_high_confidence_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[Classic instruction-override payloads — should have near-100% detection.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier returns injection or uncertain on known bad payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[PromptGuard scans high-confidence classic payloads with non-zero score.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[TestClassicOverride]] - code - gateway/tests/test_adversarial_injection.py
- [[TestHeuristicClassifierDirectly]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPromptGuardDirectly]] - code - gateway/tests/test_adversarial_injection.py
- [[parametrize_6]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestClassicOverride
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_adversarial_injection.py]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 2 edges to [[_COMMUNITY_HeuristicClassifier]]

## Top bridge nodes
- [[TestClassicOverride]] - degree 6, connects to 3 communities
- [[TestHeuristicClassifierDirectly]] - degree 4, connects to 2 communities
- [[TestPromptGuardDirectly]] - degree 4, connects to 2 communities
- [[dot-test_classic_payloads_individually()]] - degree 3, connects to 1 community
- [[dot-test_classic_override_detection_rate()]] - degree 2, connects to 1 community
