---
type: community
cohesion: 0.14
members: 22
---

# ContextSegment

**Cohesion:** 0.14 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-__init__()_57]] - code - gateway/security/context_integrity.py
- [[dot-get_segment_provenance()]] - code - gateway/security/context_guard.py
- [[dot-record_segment()]] - code - gateway/security/context_guard.py
- [[dot-score_context()]] - code - gateway/security/context_integrity.py
- [[dot-tag_segment()]] - code - gateway/security/context_guard.py
- [[Any_24]] - code - gateway/security/context_integrity.py
- [[Compute a 0.0–1.0 integrity score for the given context segments.          Args]] - rationale - gateway/security/context_integrity.py
- [[ContextIntegrityScorer]] - code - gateway/security/context_integrity.py
- [[ContextSegment]] - code - gateway/security/context_guard.py
- [[Create a provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[HMAC-SHA256 fingerprint for a registered system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[IntegrityScore]] - code - gateway/security/context_integrity.py
- [[Return ordered list of provenance records for the session.]] - rationale - gateway/security/context_guard.py
- [[Rolling context integrity score for a session.]] - rationale - gateway/security/context_integrity.py
- [[Scores the integrity of a session's context.      Usage          scorer = Cont]] - rationale - gateway/security/context_integrity.py
- [[SystemPromptFingerprint]] - code - gateway/security/prompt_guard.py
- [[Tag a segment and append it to the session's provenance log.]] - rationale - gateway/security/context_guard.py
- [[Tagged provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[context_integrity.py]] - code - gateway/security/context_integrity.py
- [[guard()_1]] - code - gateway/tests/test_context_integrity.py
- [[scorer()]] - code - gateway/tests/test_context_integrity.py
- [[test_context_integrity.py]] - code - gateway/tests/test_context_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContextSegment
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_PIIConfig]]
- 6 edges to [[_COMMUNITY_TestContextIntegrityScorer]]
- 3 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_dot-_get_hmac_key]]
- 2 edges to [[_COMMUNITY_check_message]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_TestSourceTagging]]
- 1 edge to [[_COMMUNITY_dot-analyze_message]]
- 1 edge to [[_COMMUNITY_TestNewPatternsV080]]

## Top bridge nodes
- [[ContextSegment]] - degree 15, connects to 4 communities
- [[SystemPromptFingerprint]] - degree 13, connects to 4 communities
- [[ContextIntegrityScorer]] - degree 13, connects to 3 communities
- [[IntegrityScore]] - degree 9, connects to 2 communities
- [[test_context_integrity.py]] - degree 8, connects to 2 communities
