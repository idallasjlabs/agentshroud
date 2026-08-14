---
type: community
members: 101
---

# Audit Export Pipeline

**Members:** 101 nodes

## Members
- [[--- new instructions patterns should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[.__init__()_63]] - code - gateway/security/context_integrity.py
- [[._check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[._check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[._get_hmac_key()]] - code - gateway/security/prompt_guard.py
- [[.get_segment_provenance()]] - code - gateway/security/context_guard.py
- [[.guard()_2]] - code - gateway/tests/test_performance.py
- [[.guard()_3]] - code - gateway/tests/test_prompt_guard.py
- [[.guard()_4]] - code - gateway/tests/test_prompt_guard.py
- [[.guard()_5]] - code - gateway/tests/test_security_audit.py
- [[.pg()_1]] - code - gateway/tests/test_prompt_guard.py
- [[.reanchor_delimiters()]] - code - gateway/security/prompt_guard.py
- [[.record_segment()]] - code - gateway/security/context_guard.py
- [[.register_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[.scan()_4]] - code - gateway/security/prompt_guard.py
- [[.scan_tool_result()_2]] - code - gateway/security/prompt_guard.py
- [[.score_context()]] - code - gateway/security/context_integrity.py
- [[.tag_segment()]] - code - gateway/security/context_guard.py
- [[.test_below_alert_threshold_logs_warning()]] - code - gateway/tests/test_context_integrity.py
- [[.test_benign_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_direct_injection_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_duplicate_hashes_detected()]] - code - gateway/tests/test_context_integrity.py
- [[.test_empty_context_scores_clean()]] - code - gateway/tests/test_context_integrity.py
- [[.test_empty_prompt()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_empty_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_explicit_key_used()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_injected_untrusted_segment_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[.test_lower_threshold_than_direct_scan()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_preserves_legitimate_markdown()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_pristine_context_scores_high()]] - code - gateway/tests/test_context_integrity.py
- [[.test_prompt_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[.test_prompt_guard_large_input()]] - code - gateway/tests/test_security_audit.py
- [[.test_register_and_verify()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_role_override_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_strips_fake_system_tags()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_strips_separator_overrides()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_tamper_detected()]] - code - gateway/tests/test_prompt_guard.py
- [[.test_tampered_system_prompt_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[.test_write_baseline_json()]] - code - gateway/tests/test_performance.py
- [[.verify_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[system style fake tags should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[A well-formed context with valid HMAC should score close to 1.0.]] - rationale - gateway/tests/test_context_integrity.py
- [[Any_36]] - code - gateway/security/context_integrity.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Compute a 0.0–1.0 integrity score for the given context segments.          Args]] - rationale - gateway/security/context_integrity.py
- [[Compute and return an HMAC-SHA256 fingerprint for the system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[ContextIntegrityScorer]] - code - gateway/security/context_integrity.py
- [[ContextSegment]] - code - gateway/security/context_guard.py
- [[Create a PromptGuard instance for testing]] - rationale - gateway/tests/test_prompt_guard.py
- [[Create a provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Detect and block prompt injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text.     Returns list of decoded st]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[Duplicate content hashes reduce score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Empty prompt should still register and verify cleanly.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Empty segment list should not penalize the score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Explicit ignore-instructions payload embedded in a tool result.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Explicit key parameter should override session key.]] - rationale - gateway/tests/test_prompt_guard.py
- [[HMAC-SHA256 fingerprint for a registered system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[IntegrityScore]] - code - gateway/security/context_integrity.py
- [[Large inputs shouldn't crash prompt guard.]] - rationale - gateway/tests/test_security_audit.py
- [[Mismatched HMAC should reduce score by at least 0.15.]] - rationale - gateway/tests/test_context_integrity.py
- [[Normal markdown headers ( Title) should not be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[PromptGuard]] - code - gateway/security/prompt_guard.py
- [[Return HMAC key env var preferred, session-scoped random fallback.]] - rationale - gateway/security/prompt_guard.py
- [[Return True if prompt_text matches the stored HMAC fingerprint.]] - rationale - gateway/security/prompt_guard.py
- [[Return ordered list of provenance records for the session.]] - rationale - gateway/security/context_guard.py
- [[Rolling context integrity score for a session.]] - rationale - gateway/security/context_integrity.py
- [[Run standard benchmarks and write results to .benchmarksbaseline-v1.0.0.json.]] - rationale - gateway/tests/test_performance.py
- [[Scan input text for prompt injection patterns.          Args             text]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection.          Tool results (w]] - rationale - gateway/security/prompt_guard.py
- [[Score below 0.6 should produce a warning log.]] - rationale - gateway/tests/test_context_integrity.py
- [[Scores the integrity of a session's context.      Usage          scorer = Cont]] - rationale - gateway/security/context_integrity.py
- [[Strip injected fake delimiters and return sanitized message.          Called whe]] - rationale - gateway/security/prompt_guard.py
- [[SystemPromptFingerprint]] - code - gateway/security/prompt_guard.py
- [[Tag a segment and append it to the session's provenance log.]] - rationale - gateway/security/context_guard.py
- [[Tagged provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Test PromptGuard initialization]] - rationale - gateway/tests/test_prompt_guard.py
- [[Test that normal messages pass through]] - rationale - gateway/tests/test_prompt_guard.py
- [[TestContextIntegrityScorer]] - code - gateway/tests/test_context_integrity.py
- [[TestReanchorDelimiters]] - code - gateway/tests/test_prompt_guard.py
- [[TestSystemPromptHMAC]] - code - gateway/tests/test_prompt_guard.py
- [[TestToolResultScan]] - code - gateway/tests/test_prompt_guard.py
- [[Tests for indirect prompt injection detection in tool results.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Tool result scan blocks at score ≥ 0.6 vs direct scan threshold of 0.8.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Untrusted segment injected after system segment reduces score.]] - rationale - gateway/tests/test_context_integrity.py
- [[Verifying a tampered prompt should return False.]] - rationale - gateway/tests/test_prompt_guard.py
- [[_make_segment()]] - code - gateway/tests/test_context_integrity.py
- [[context_integrity.py]] - code - gateway/security/context_integrity.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py
- [[guard()_1]] - code - gateway/tests/test_context_integrity.py
- [[prompt_guard()_1]] - code - gateway/tests/test_prompt_guard.py
- [[prompt_guard()_2]] - code - gateway/tests/test_security_integration.py
- [[prompt_guard.py]] - code - gateway/security/prompt_guard.py
- [[register_system_prompt + verify_system_prompt should succeed.]] - rationale - gateway/tests/test_prompt_guard.py
- [[scorer()]] - code - gateway/tests/test_context_integrity.py
- [[test_benign_message()]] - code - gateway/tests/test_prompt_guard.py
- [[test_context_integrity.py]] - code - gateway/tests/test_context_integrity.py
- [[test_multilingual_injection.py]] - code - gateway/tests/test_multilingual_injection.py
- [[test_prompt_guard.py]] - code - gateway/tests/test_prompt_guard.py
- [[test_prompt_guard_init()]] - code - gateway/tests/test_prompt_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Audit_Export_Pipeline
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_SOC RBAC & Auth]]
- 14 edges to [[_COMMUNITY_Telegram Proxy Test Suite]]
- 12 edges to [[_COMMUNITY_Gateway Test Suite]]
- 11 edges to [[_COMMUNITY_Egress & RBAC Security Core]]
- 11 edges to [[_COMMUNITY_Gateway Test Suite]]
- 11 edges to [[_COMMUNITY_Auth & Exception Types]]
- 8 edges to [[_COMMUNITY_MCP Proxy Config]]
- 7 edges to [[_COMMUNITY_Slack API Proxy]]
- 7 edges to [[_COMMUNITY_Security Module Middleware]]
- 6 edges to [[_COMMUNITY_Gateway Security Module]]
- 6 edges to [[_COMMUNITY_SOC Collaborator Lifecycle]]
- 4 edges to [[_COMMUNITY_Gateway Test Suite]]
- 4 edges to [[_COMMUNITY_Gateway Test Suite]]
- 3 edges to [[_COMMUNITY_gatewayREADME]]
- 3 edges to [[_COMMUNITY_Web Control Center]]
- 3 edges to [[_COMMUNITY_Collaborator Response Templates]]
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 2 edges to [[_COMMUNITY_PII Sanitizer Pipeline]]
- 2 edges to [[_COMMUNITY_Cross-Bot Trust Ledger]]
- 2 edges to [[_COMMUNITY_Bot Skill Config]]
- 2 edges to [[_COMMUNITY_Gateway Test Suite]]
- 2 edges to [[_COMMUNITY_Planning Docs]]
- 2 edges to [[_COMMUNITY_MCP Policy Engine]]
- 1 edge to [[_COMMUNITY_Planning Docs]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_docstesting]]
- 1 edge to [[_COMMUNITY_ESP32 Firmware]]
- 1 edge to [[_COMMUNITY_docsreference]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Gateway Test Suite]]
- 1 edge to [[_COMMUNITY_Security Docs]]
- 1 edge to [[_COMMUNITY_Bot Skill Config]]

## Top bridge nodes
- [[PromptGuard]] - degree 146, connects to 27 communities
- [[prompt_guard.py]] - degree 13, connects to 6 communities
- [[ContextSegment]] - degree 15, connects to 2 communities
- [[test_prompt_guard.py]] - degree 10, connects to 2 communities
- [[.scan()_4]] - degree 8, connects to 2 communities