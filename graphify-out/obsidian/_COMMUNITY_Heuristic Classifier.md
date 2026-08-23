---
type: community
cohesion: 0.12
members: 16
---

# Heuristic Classifier

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_backward_compat_alias()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_benign_text_low_score()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_clear_injection_high_score()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_cyrillic_homoglyph()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_empty_text()_1]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_encoding_evasion()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_exfiltration_attempt()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_long_benign_text()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_model_not_loaded_by_default()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_multi_signal_increases_confidence()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_roleplay_attack()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_separator_injection()]] - code - gateway/tests/test_heuristic_classifier.py
- [[.test_unicode_anomaly()]] - code - gateway/tests/test_heuristic_classifier.py
- [[InjectionClassifier alias should still work.]] - rationale - gateway/tests/test_heuristic_classifier.py
- [[Test the heuristic injection classifier.]] - rationale - gateway/tests/test_heuristic_classifier.py
- [[TestHeuristicClassifier]] - code - gateway/tests/test_heuristic_classifier.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Heuristic_Classifier
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Heuristic Classifier (security)]]

## Top bridge nodes
- [[TestHeuristicClassifier]] - degree 19, connects to 1 community