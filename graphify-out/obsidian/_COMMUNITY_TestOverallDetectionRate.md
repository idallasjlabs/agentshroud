---
type: community
cohesion: 0.29
members: 7
---

# TestOverallDetectionRate

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_detection_breakdown_by_category()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_overall_detection_rate_meets_threshold()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_payload_count_meets_minimum()]] - code - gateway/tests/test_adversarial_injection.py
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
- 4 edges to [[_COMMUNITY__any_detector_fires()]]
- 3 edges to [[_COMMUNITY_test_adversarial_injection.py]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]

## Top bridge nodes
- [[TestOverallDetectionRate]] - degree 8, connects to 4 communities
- [[.test_detection_breakdown_by_category()]] - degree 6, connects to 3 communities
- [[.test_overall_detection_rate_meets_threshold()]] - degree 5, connects to 3 communities