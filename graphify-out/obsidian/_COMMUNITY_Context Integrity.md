---
type: community
cohesion: 0.10
members: 32
---

# Context Integrity

**Cohesion:** 0.10 - loosely connected
**Members:** 32 nodes

## Members
- [[.__init__()_66]] - code - gateway/security/context_integrity.py
- [[.get_segment_provenance()]] - code - gateway/security/context_guard.py
- [[.score_context()]] - code - gateway/security/context_integrity.py
- [[.test_below_alert_threshold_logs_warning()]] - code - gateway/tests/test_context_integrity.py
- [[.test_duplicate_hashes_detected()]] - code - gateway/tests/test_context_integrity.py
- [[.test_empty_context_scores_clean()]] - code - gateway/tests/test_context_integrity.py
- [[.test_injected_untrusted_segment_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[.test_pristine_context_scores_high()]] - code - gateway/tests/test_context_integrity.py
- [[.test_tampered_system_prompt_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[A well-formed context with valid HMAC should score close to 1.0.]] - rationale - gateway/tests/test_context_integrity.py
- [[Any_36]] - code - gateway/security/context_integrity.py
- [[Compute a 0.0–1.0 integrity score for the given context segments.          Args]] - rationale - gateway/security/context_integrity.py
- [[ContextIntegrityScorer]] - code - gateway/security/context_integrity.py
- [[ContextSegment]] - code - gateway/security/context_guard.py
- [[Duplicate content hashes reduce score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Empty segment list should not penalize the score.]] - rationale - gateway/tests/test_context_integrity.py
- [[HMAC-SHA256 fingerprint for a registered system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[IntegrityScore]] - code - gateway/security/context_integrity.py
- [[Mismatched HMAC should reduce score by at least 0.15.]] - rationale - gateway/tests/test_context_integrity.py
- [[Return ordered list of provenance records for the session.]] - rationale - gateway/security/context_guard.py
- [[Rolling context integrity score for a session.]] - rationale - gateway/security/context_integrity.py
- [[Score below 0.6 should produce a warning log.]] - rationale - gateway/tests/test_context_integrity.py
- [[Scores the integrity of a session's context.      Usage          scorer = Cont]] - rationale - gateway/security/context_integrity.py
- [[SystemPromptFingerprint]] - code - gateway/security/prompt_guard.py
- [[Tagged provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[TestContextIntegrityScorer]] - code - gateway/tests/test_context_integrity.py
- [[Untrusted segment injected after system segment reduces score.]] - rationale - gateway/tests/test_context_integrity.py
- [[_make_segment()]] - code - gateway/tests/test_context_integrity.py
- [[context_integrity.py]] - code - gateway/security/context_integrity.py
- [[guard()_1]] - code - gateway/tests/test_context_integrity.py
- [[scorer()]] - code - gateway/tests/test_context_integrity.py
- [[test_context_integrity.py]] - code - gateway/tests/test_context_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Context_Integrity
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 3 edges to [[_COMMUNITY_Context Guard]]
- 2 edges to [[_COMMUNITY_Context Guard (security)]]
- 2 edges to [[_COMMUNITY_Prompt Guard (security)]]
- 2 edges to [[_COMMUNITY_Prompt Guard]]
- 1 edge to [[_COMMUNITY_Context Guard]]
- 1 edge to [[_COMMUNITY_Prompt Guard]]
- 1 edge to [[_COMMUNITY_Prompt Guard]]
- 1 edge to [[_COMMUNITY_Prompt Guard]]
- 1 edge to [[_COMMUNITY_Adversarial Injection]]

## Top bridge nodes
- [[SystemPromptFingerprint]] - degree 13, connects to 6 communities
- [[ContextSegment]] - degree 15, connects to 3 communities
- [[TestContextIntegrityScorer]] - degree 12, connects to 2 communities
- [[ContextIntegrityScorer]] - degree 13, connects to 1 community
- [[IntegrityScore]] - degree 9, connects to 1 community