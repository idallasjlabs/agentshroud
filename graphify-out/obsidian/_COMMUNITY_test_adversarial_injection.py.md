---
type: community
cohesion: 0.16
members: 16
---

# test_adversarial_injection.py

**Cohesion:** 0.16 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_classifier_flags_payloads()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_context_injection_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_multilingual_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[.test_persona_hijack_detection_rate()]] - code - gateway/tests/test_adversarial_injection.py
- [[Context  document retrieval poisoning payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier]] - code - gateway/tests/test_adversarial_injection.py
- [[HeuristicClassifier returns injection or uncertain on known bad payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Multilingual injection variants.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Persona hijack  DAN-style payloads.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[Return True if HeuristicClassifier flags as injection or uncertain.]] - rationale - gateway/tests/test_adversarial_injection.py
- [[TestContextInjection]] - code - gateway/tests/test_adversarial_injection.py
- [[TestHeuristicClassifierDirectly]] - code - gateway/tests/test_adversarial_injection.py
- [[TestMultilingual]] - code - gateway/tests/test_adversarial_injection.py
- [[TestPersonaHijack]] - code - gateway/tests/test_adversarial_injection.py
- [[_heuristic_detects()]] - code - gateway/tests/test_adversarial_injection.py
- [[test_adversarial_injection.py]] - code - gateway/tests/test_adversarial_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_adversarial_injectionpy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY__any_detector_fires()]]
- 6 edges to [[_COMMUNITY_TrustManager]]
- 6 edges to [[_COMMUNITY_HeuristicClassifier]]
- 3 edges to [[_COMMUNITY_TestOverallDetectionRate]]
- 2 edges to [[_COMMUNITY_TestPromptExtraction]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_TestPromptGuardDirectly]]

## Top bridge nodes
- [[test_adversarial_injection.py]] - degree 16, connects to 7 communities
- [[HeuristicClassifier]] - degree 15, connects to 5 communities
- [[TestContextInjection]] - degree 5, connects to 2 communities
- [[TestHeuristicClassifierDirectly]] - degree 5, connects to 2 communities
- [[TestMultilingual]] - degree 5, connects to 2 communities