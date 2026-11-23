---
type: community
members: 7
---

# TestOverallDetectionRate

**Members:** 7 nodes

## Members
- [[dot-test_detection_breakdown_by_category()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_overall_detection_rate_meets_threshold()]] - code - gateway/tests/test_adversarial_injection.py
- [[dot-test_payload_count_meets_minimum()]] - code - gateway/tests/test_adversarial_injection.py
- [[End-to-end all 110+ payloads against combined defense layer.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Ensure the payload library stays above 100 entries (CI regression gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Report per-category detection rates for observability (not a gate).]] - rationale - gateway/tests/test_adversarial_injection.py
- [[TestOverallDetectionRate]] - code - gateway/tests/test_adversarial_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOverallDetectionRate
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_adversarial_injection.py]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]

## Top bridge nodes
- [[TestOverallDetectionRate]] - degree 7, connects to 3 communities
- [[dot-test_detection_breakdown_by_category()]] - degree 4, connects to 2 communities
- [[dot-test_overall_detection_rate_meets_threshold()]] - degree 3, connects to 2 communities
