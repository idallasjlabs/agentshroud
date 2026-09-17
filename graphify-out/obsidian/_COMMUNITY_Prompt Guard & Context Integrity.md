---
type: community
cohesion: 0.02
members: 122
---

# Prompt Guard & Context Integrity

**Cohesion:** 0.02 - loosely connected
**Members:** 122 nodes

## Members
- [[--- new instructions patterns should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[dot-__init__()_102]] - code - gateway/security/context_integrity.py
- [[dot-_check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[dot-_check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[dot-_get_hmac_key()]] - code - gateway/security/prompt_guard.py
- [[dot-guard()_3]] - code - gateway/tests/test_performance.py
- [[dot-guard()_4]] - code - gateway/tests/test_prompt_guard.py
- [[dot-guard()_5]] - code - gateway/tests/test_prompt_guard.py
- [[dot-pg()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-pg()_1]] - code - gateway/tests/test_prompt_guard.py
- [[dot-pipeline()]] - code - gateway/tests/test_performance.py
- [[dot-pipeline()_1]] - code - gateway/tests/test_performance.py
- [[dot-reanchor_delimiters()]] - code - gateway/security/prompt_guard.py
- [[dot-register_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[dot-scan()_2]] - code - gateway/security/prompt_guard.py
- [[dot-scan_tool_result()]] - code - gateway/security/prompt_guard.py
- [[dot-score_context()]] - code - gateway/security/context_integrity.py
- [[dot-setup_method()_25]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_base64_encoded_injection()_2]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_below_alert_threshold_logs_warning()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_benign_base64()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_benign_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_clean_input()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_combined_attack_high_score()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_custom_pattern()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_dan_jailbreak()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_delimiter_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_direct_injection_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_duplicate_hashes_detected()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_empty_context_scores_clean()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_empty_input()_3]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_empty_prompt()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_empty_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_explicit_key_used()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_forget_everything()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_ignore_instructions()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_indirect_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_injected_untrusted_segment_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_lower_threshold_than_direct_scan()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_new_instructions_override()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_none_input()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_preserves_legitimate_markdown()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_pristine_context_scores_high()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_prompt_extraction()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_prompt_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_prompt_guard_large_input()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_prompt_leak_question()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_and_verify()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_role_override_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_role_reassignment()_2]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_rtl_override()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_sanitized_output()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_strips_fake_system_tags()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_strips_separator_overrides()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_tamper_detected()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_tampered_system_prompt_lowers_score()]] - code - gateway/tests/test_context_integrity.py
- [[dot-test_unicode_zero_width()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_warn_threshold()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_write_baseline_json()]] - code - gateway/tests/test_performance.py
- [[dot-test_xml_tag_injection()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-verify_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[system style fake tags should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[A well-formed context with valid HMAC should score close to 1.0.]] - rationale - gateway/tests/test_context_integrity.py
- [[Any_38]] - code - gateway/security/context_integrity.py
- [[CVE-2026-31045 — indirect prompt injection via tool results]] - concept - gateway/tests/test_prompt_guard.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Compute a 0.0–1.0 integrity score for the given context segments.          Args]] - rationale - gateway/security/context_integrity.py
- [[Compute and return an HMAC-SHA256 fingerprint for the system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[ContextIntegrityScorer]] - code - gateway/security/context_integrity.py
- [[ContextSegment]] - code - gateway/security/context_guard.py
- [[Create a PromptGuard instance for testing]] - rationale - gateway/tests/test_prompt_guard.py
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
- [[Prompt Guard Module Badge Icon]] - image - branding/icons/modules/prompt-guard-256x256.png
- [[PromptGuard]] - code - gateway/security/prompt_guard.py
- [[Return HMAC key env var preferred, session-scoped random fallback.]] - rationale - gateway/security/prompt_guard.py
- [[Return True if prompt_text matches the stored HMAC fingerprint.]] - rationale - gateway/security/prompt_guard.py
- [[Rolling context integrity score for a session.]] - rationale - gateway/security/context_integrity.py
- [[Run standard benchmarks and write results to .benchmarksbaseline-v1.0.0.json.]] - rationale - gateway/tests/test_performance.py
- [[Scan input text for prompt injection patterns.          Args             text]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection.          Tool results (w]] - rationale - gateway/security/prompt_guard.py
- [[Score below 0.6 should produce a warning log.]] - rationale - gateway/tests/test_context_integrity.py
- [[Scores the integrity of a session's context.      Usage          scorer = Cont]] - rationale - gateway/security/context_integrity.py
- [[Strip injected fake delimiters and return sanitized message.          Called whe]] - rationale - gateway/security/prompt_guard.py
- [[SystemPromptFingerprint]] - code - gateway/security/prompt_guard.py
- [[Tagged provenance record for a context segment.]] - rationale - gateway/security/context_guard.py
- [[Test PromptGuard initialization]] - rationale - gateway/tests/test_prompt_guard.py
- [[Test that normal messages pass through]] - rationale - gateway/tests/test_prompt_guard.py
- [[TestContextIntegrityScorer]] - code - gateway/tests/test_context_integrity.py
- [[TestPromptGuard_1]] - code - gateway/tests/test_security_hardening.py
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
- [[guard()_3]] - code - gateway/tests/test_context_integrity.py
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
TABLE source_file, type FROM #community/Prompt_Guard__Context_Integrity
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Encrypted Store & Drift Detector]]
- 17 edges to [[_COMMUNITY_Session Manager & PIIContext Guard]]
- 16 edges to [[_COMMUNITY_Canary Tripwire]]
- 16 edges to [[_COMMUNITY_Community 43]]
- 13 edges to [[_COMMUNITY_Gateway Config & PII Sanitizer]]
- 12 edges to [[_COMMUNITY_Signed Instruction Envelopes & Security Pipeline]]
- 11 edges to [[_COMMUNITY_P3 Infrastructure Security Modules]]
- 9 edges to [[_COMMUNITY_Proxy Sidecar & Forwarder]]
- 8 edges to [[_COMMUNITY_Cross-Bot Trust & A2A Governance]]
- 8 edges to [[_COMMUNITY_Alert Dispatcher & RBAC Reliability]]
- 7 edges to [[_COMMUNITY_Approval Routing & Event Bus]]
- 5 edges to [[_COMMUNITY_Agent Isolation & Group Config Tests]]
- 4 edges to [[_COMMUNITY_Community 152]]
- 4 edges to [[_COMMUNITY_Community 286]]
- 3 edges to [[_COMMUNITY_Tool Result Sanitizer & XML Injection Filtering]]
- 3 edges to [[_COMMUNITY_Community 208]]
- 3 edges to [[_COMMUNITY_File Sandbox & Privilege Separation Tests]]
- 3 edges to [[_COMMUNITY_Community 92]]
- 3 edges to [[_COMMUNITY_Community 322]]
- 3 edges to [[_COMMUNITY_Community 253]]
- 2 edges to [[_COMMUNITY_Ingest API & RBAC Core]]
- 2 edges to [[_COMMUNITY_Community 182]]
- 2 edges to [[_COMMUNITY_Community 86]]
- 2 edges to [[_COMMUNITY_PII Sanitizer & Redaction]]
- 1 edge to [[_COMMUNITY_Community 52]]
- 1 edge to [[_COMMUNITY_Community 157]]
- 1 edge to [[_COMMUNITY_Community 167]]
- 1 edge to [[_COMMUNITY_Community 185]]
- 1 edge to [[_COMMUNITY_Voice Gateway STT & Browser Security]]
- 1 edge to [[_COMMUNITY_Community 731]]
- 1 edge to [[_COMMUNITY_Community 254]]
- 1 edge to [[_COMMUNITY_BlueRed Team Security Auditor Skills]]
- 1 edge to [[_COMMUNITY_Community 48]]
- 1 edge to [[_COMMUNITY_Community 598]]
- 1 edge to [[_COMMUNITY_Community 565]]

## Top bridge nodes
- [[PromptGuard]] - degree 151, connects to 24 communities
- [[prompt_guard.py]] - degree 18, connects to 10 communities
- [[TestPromptGuard_1]] - degree 40, connects to 9 communities
- [[test_prompt_guard.py]] - degree 14, connects to 5 communities
- [[dot-pipeline()]] - degree 6, connects to 5 communities