---
type: community
cohesion: 0.17
members: 19
---

# ContextSegment

**Cohesion:** 0.17 - loosely connected
**Members:** 19 nodes

## Members
- [[dot-__init__()_149]] - code - gateway/security/context_integrity.py
- [[dot-get_segment_provenance()]] - code - gateway/security/context_guard.py
- [[dot-score_context()]] - code - gateway/security/context_integrity.py
- [[dot-test_empty_context_scores_clean()]] - code - gateway/tests/test_context_integrity.py
- [[Any_57]] - code - gateway/security/context_integrity.py
- [[Compute a 0.0–1.0 integrity score for the given context segments.          Args]] - rationale - gateway/security/context_integrity.py
- [[ContextIntegrityScorer]] - code - gateway/security/context_integrity.py
- [[ContextSegment]] - code - gateway/security/context_guard.py
- [[Empty segment list should not penalize the score.]] - rationale - gateway/tests/test_context_integrity.py
- [[IntegrityScore]] - code - gateway/security/context_integrity.py
- [[Return ordered list of provenance records for the session.]] - rationale - gateway/security/context_guard.py
- [[Rolling context integrity score for a session.]] - rationale - gateway/security/context_integrity.py
- [[Scores the integrity of a session's context.      Usage          scorer = Cont]] - rationale - gateway/security/context_integrity.py
- [[Tagged provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[TestContextIntegrityScorer]] - code - gateway/tests/test_context_integrity.py
- [[context_integrity.py]] - code - gateway/security/context_integrity.py
- [[guard()_4]] - code - gateway/tests/test_context_integrity.py
- [[scorer()]] - code - gateway/tests/test_context_integrity.py
- [[test_context_integrity.py]] - code - gateway/tests/test_context_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContextSegment
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_PIIConfig]]
- 7 edges to [[_COMMUNITY_ContextSegment_1]]
- 4 edges to [[_COMMUNITY_test_prompt_guard.py]]
- 2 edges to [[_COMMUNITY_ContextSegment_2]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL_4]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_5]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL_6]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]

## Top bridge nodes
- [[ContextSegment]] - degree 15, connects to 5 communities
- [[ContextIntegrityScorer]] - degree 13, connects to 3 communities
- [[TestContextIntegrityScorer]] - degree 12, connects to 3 communities
- [[IntegrityScore]] - degree 9, connects to 2 communities
- [[test_context_integrity.py]] - degree 8, connects to 2 communities
