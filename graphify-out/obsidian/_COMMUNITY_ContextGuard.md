---
type: community
members: 87
---

# ContextGuard

**Members:** 87 nodes

## Members
- [[dot-__init__()_72]] - code - gateway/security/context_guard.py
- [[dot-__init__()_73]] - code - gateway/security/context_integrity.py
- [[dot-_detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[dot-_detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[dot-_detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[dot-_detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[dot-analyze_message()]] - code - gateway/security/context_guard.py
- [[dot-get_segment_provenance()]] - code - gateway/security/context_guard.py
- [[dot-get_session_risk_level()]] - code - gateway/security/context_guard.py
- [[dot-guard()]] - code - gateway/tests/test_context_guard.py
- [[dot-record_segment()]] - code - gateway/security/context_guard.py
- [[dot-score_context()]] - code - gateway/security/context_integrity.py
- [[dot-tag_segment()]] - code - gateway/security/context_guard.py
- [[dot-test_below_alert_threshold_logs_warning()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_deeply_nested_context_attacks()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_duplicate_hashes_detected()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_empty_context_scores_clean()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_empty_inputs_everywhere()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_empty_provenance_for_unknown_session()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_few_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_injected_untrusted_segment_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_json_injection_in_context()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_normal_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_normal_sized_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_oversized_json_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_oversized_message_blocked()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_pristine_context_scores_high()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_repeated_pattern_flagged()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_hash_integrity()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_provenance_ordering()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_segment_tagging_basic()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_separate_sessions_isolated()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_short_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[dot-test_tampered_system_prompt_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[A well-formed context with valid HMAC should score close to 1.0.]] - rationale - gateway/tests/test_context_integrity.py
- [[Analyze a message for context poisoning attempts. Args session_id Session…]] - rationale - gateway/security/context_guard.py
- [[Any_27]] - code
- [[Check if message should be allowed, with detailed findings. Args text Message…]] - rationale - gateway/security/context_guard.py
- [[Compute a 0.0–1.0 integrity score for the given context segments. Args…]] - rationale - gateway/security/context_integrity.py
- [[Context Integrity Scoring — C21 Computes a rolling 0.0–1.0 integrity score for…]] - rationale - gateway/security/context_integrity.py
- [[Context Window Poisoning Defense - Security Hardening Module Detect attempts to…]] - rationale - gateway/security/context_guard.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[ContextGuard]] - code - gateway/security/context_guard.py
- [[ContextIntegrityScorer]] - code - gateway/security/context_integrity.py
- [[ContextSegment]] - code - gateway/security/context_guard.py
- [[Create a provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Duplicate content hashes reduce score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Empty segment list should not penalize the score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Empty strings shouldn't crash any module.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Get risk level for a session based on detected attacks.]] - rationale - gateway/security/context_guard.py
- [[Get the global context guard instance.]] - rationale - gateway/security/context_guard.py
- [[Guard against context window poisoning attacks.]] - rationale - gateway/security/context_guard.py
- [[IntegrityScore]] - code - gateway/security/context_integrity.py
- [[JSON injection in message shouldn't manipulate context.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Mismatched HMAC should reduce score by at least 0.15.]] - rationale - gateway/tests/test_context_integrity.py
- [[Nested context attacks shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Return ordered list of provenance records for the session.]] - rationale - gateway/security/context_guard.py
- [[Rolling context integrity score for a session.]] - rationale - gateway/security/context_integrity.py
- [[Score below 0.6 should produce a warning log.]] - rationale - gateway/tests/test_context_integrity.py
- [[Scores the integrity of a session's context. Usage scorer =…]] - rationale - gateway/security/context_integrity.py
- [[SessionContext_1]] - code - gateway/security/context_guard.py
- [[Tag a segment and append it to the session's provenance log.]] - rationale - gateway/security/context_guard.py
- [[Tagged provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Test Context Window Poisoning Defense.]] - rationale - gateway/tests/test_context_guard.py
- [[TestCheckMessage]] - code - gateway/tests/test_context_guard.py
- [[TestContextIntegrityScorer]] - code - gateway/tests/test_context_integrity.py
- [[TestSourceTagging]] - code - gateway/tests/test_context_guard.py
- [[Tests for ContextIntegrityScorer (C21).]] - rationale - gateway/tests/test_context_integrity.py
- [[Untrusted segment injected after system segment reduces score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Very large JSON shouldn't crash the parser.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[_make_segment()]] - code - gateway/tests/test_context_integrity.py
- [[check_message()]] - code - gateway/security/context_guard.py
- [[context_guard.py]] - code - gateway/security/context_guard.py
- [[context_integrity.py]] - code - gateway/security/context_integrity.py
- [[fixture_46]] - code
- [[fixture_47]] - code
- [[get_context_guard()]] - code - gateway/security/context_guard.py
- [[guard()]] - code - gateway/tests/test_context_integrity.py
- [[scorer()]] - code - gateway/tests/test_context_integrity.py
- [[test_context_guard.py]] - code - gateway/tests/test_context_guard.py
- [[test_context_integrity.py]] - code - gateway/tests/test_context_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ContextGuard
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_PromptGuard]]
- 6 edges to [[_COMMUNITY_PIIConfig]]
- 5 edges to [[_COMMUNITY_middleware.py]]
- 4 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 3 edges to [[_COMMUNITY_deep_security_test]]
- 3 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 3 edges to [[_COMMUNITY_test_security_audit.py]]
- 3 edges to [[_COMMUNITY_test_e2e_watchtower.py]]
- 3 edges to [[_COMMUNITY_prompt_guard.py]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_ToolResultInjectionScanner]]

## Top bridge nodes
- [[ContextGuard]] - degree 44, connects to 10 communities
- [[context_guard.py]] - degree 16, connects to 6 communities
- [[dot-test_empty_inputs_everywhere()]] - degree 5, connects to 3 communities
- [[test_context_integrity.py]] - degree 12, connects to 2 communities
- [[context_integrity.py]] - degree 9, connects to 2 communities
