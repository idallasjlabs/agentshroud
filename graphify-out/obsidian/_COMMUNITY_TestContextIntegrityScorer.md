---
type: community
cohesion: 0.19
members: 14
---

# TestContextIntegrityScorer

**Cohesion:** 0.19 - loosely connected
**Members:** 14 nodes

## Members
- [[dot-test_below_alert_threshold_logs_warning()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_duplicate_hashes_detected()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_empty_context_scores_clean()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_injected_untrusted_segment_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_pristine_context_scores_high()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_tampered_system_prompt_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[A well-formed context with valid HMAC should score close to 1.0.]] - rationale - gateway/tests/test_context_integrity.py
- [[Duplicate content hashes reduce score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Empty segment list should not penalize the score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Mismatched HMAC should reduce score by at least 0.15.]] - rationale - gateway/tests/test_context_integrity.py
- [[Score below 0.6 should produce a warning log.]] - rationale - gateway/tests/test_context_integrity.py
- [[TestContextIntegrityScorer]] - code - gateway/tests/test_context_integrity.py
- [[Untrusted segment injected after system segment reduces score.]] - rationale - gateway/tests/test_context_integrity.py
- [[_make_segment()]] - code - gateway/tests/test_context_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestContextIntegrityScorer
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]

## Top bridge nodes
- [[TestContextIntegrityScorer]] - degree 12, connects to 3 communities
- [[_make_segment()]] - degree 7, connects to 1 community
