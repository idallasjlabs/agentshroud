---
type: community
members: 90
---

# PromptGuard

**Members:** 90 nodes

## Members
- [[--- new instructions patterns should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[dot-_check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[dot-_check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[dot-_get_hmac_key()]] - code - gateway/security/prompt_guard.py
- [[dot-guard()_2]] - code - gateway/tests/test_performance.py
- [[dot-guard()_3]] - code - gateway/tests/test_prompt_guard.py
- [[dot-guard()_4]] - code - gateway/tests/test_prompt_guard.py
- [[dot-pg()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-pg()_1]] - code - gateway/tests/test_prompt_guard.py
- [[dot-reanchor_delimiters()]] - code - gateway/security/prompt_guard.py
- [[dot-register_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[dot-scan()_3]] - code - gateway/security/prompt_guard.py
- [[dot-scan_tool_result()_2]] - code - gateway/security/prompt_guard.py
- [[dot-test_1000_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[dot-test_binary_data_in_text_fields()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_crlf_in_prompt_guard()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_deeply_nested_json()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_detection_accuracy_at_scale()]] - code - gateway/tests/test_performance.py
- [[dot-test_empty_prompt()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_explicit_key_used()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_null_byte_in_prompt()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_polyglot_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_preserves_legitimate_markdown()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_prompt_guard_catches_tool_injection()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_prompt_guard_instantiates()]] - code - gateway/tests/test_all_modules_enforce.py
- [[dot-test_prompt_guard_no_early_exit_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_rapid_fire_scans()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_register_and_verify()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_strips_fake_system_tags()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_strips_separator_overrides()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_tamper_detected()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_very_long_message()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_xml_entity_expansion()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-verify_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[system style fake tags should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Binary data in text fields shouldn't crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[CRLF injection in prompt shouldn't bypass detection.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Compute and return an HMAC-SHA256 fingerprint for the system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[Create a PromptGuard instance for testing]] - rationale - gateway/tests/test_prompt_guard.py
- [[Deeply nested JSON shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Detect and block prompt injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text. Returns list of decoded…]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[Double-base64 encoded lower-ranked injection is caught (was top-5 only).]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Empty prompt should still register and verify cleanly.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Enum_33]] - code
- [[Explicit key parameter should override session key.]] - rationale - gateway/tests/test_prompt_guard.py
- [[HMAC-SHA256 fingerprint for a registered system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[Injection attempts should be detected even under load.]] - rationale - gateway/tests/test_performance.py
- [[Normal markdown headers ( Title) should not be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Null bytes shouldn't bypass prompt guard.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Polyglot (valid as multiple formats) shouldn't bypass checks.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Prompt Injection Defense — detect and block prompt injection attempts. Scoring…]] - rationale - gateway/security/prompt_guard.py
- [[Prompt guard should catch tool-call injection attempts.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Prompt guard should scan full input, not short-circuit on first match.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Prompt guard 1000 messages in  5s.]] - rationale - gateway/tests/test_performance.py
- [[PromptGuard]] - code - gateway/security/prompt_guard.py
- [[Rapid scanning shouldn't degrade or crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Return HMAC key env var preferred, session-scoped random fallback.]] - rationale - gateway/security/prompt_guard.py
- [[Return True if prompt_text matches the stored HMAC fingerprint.]] - rationale - gateway/security/prompt_guard.py
- [[Scan 1000 messages in under 5 seconds.]] - rationale - gateway/tests/test_performance.py
- [[Scan input text for prompt injection patterns. Args text The user input to…]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection. Tool results (web…]] - rationale - gateway/security/prompt_guard.py
- [[Strip injected fake delimiters and return sanitized message. Called when…]] - rationale - gateway/security/prompt_guard.py
- [[SystemPromptFingerprint]] - code - gateway/security/prompt_guard.py
- [[Test PromptGuard initialization]] - rationale - gateway/tests/test_prompt_guard.py
- [[Test that normal messages pass through]] - rationale - gateway/tests/test_prompt_guard.py
- [[TestPromptGuardPerformance]] - code - gateway/tests/test_performance.py
- [[TestReanchorDelimiters]] - code - gateway/tests/test_prompt_guard.py
- [[TestSystemPromptHMAC]] - code - gateway/tests/test_prompt_guard.py
- [[Tests for PromptGuard security component]] - rationale - gateway/tests/test_prompt_guard.py
- [[Tests for multilingual prompt injection detection.]] - rationale - gateway/tests/test_multilingual_injection.py
- [[ThreatAction]] - code - gateway/security/prompt_guard.py
- [[Verifying a tampered prompt should return False.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Very long messages should be handled without crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[XXE-style payloads shouldn't crash processing.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[`_check_encoded_content` now matches rules beyond the old top-5 slice. Failing-…]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py
- [[fixture_101]] - code
- [[prompt_guard()_2]] - code - gateway/tests/test_prompt_guard.py
- [[prompt_guard.py_2]] - code - gateway/security/prompt_guard.py
- [[register_system_prompt + verify_system_prompt should succeed.]] - rationale - gateway/tests/test_prompt_guard.py
- [[str_16]] - code
- [[test_benign_message()]] - code - gateway/tests/test_prompt_guard.py
- [[test_multilingual_injection.py]] - code - gateway/tests/test_multilingual_injection.py
- [[test_prompt_guard.py]] - code - gateway/tests/test_prompt_guard.py
- [[test_prompt_guard_double_encoded_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_prompt_guard_encoded_check_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_prompt_guard_init()]] - code - gateway/tests/test_prompt_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PromptGuard
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_PIISanitizer]]
- 12 edges to [[_COMMUNITY_HeuristicClassifier]]
- 8 edges to [[_COMMUNITY_TestHTTPSecurity]]
- 7 edges to [[_COMMUNITY_TestPromptGuard]]
- 6 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 6 edges to [[_COMMUNITY_context_guard.py]]
- 5 edges to [[_COMMUNITY_asyncio_2]]
- 5 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 3 edges to [[_COMMUNITY_TestToolResultScan]]
- 3 edges to [[_COMMUNITY_TestMultilingualInjection]]
- 3 edges to [[_COMMUNITY_deep_security_test]]
- 3 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 3 edges to [[_COMMUNITY_test_canary.py]]
- 3 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 3 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 3 edges to [[_COMMUNITY_test_edge_pipeline.py]]
- 3 edges to [[_COMMUNITY_AgentRegistry]]
- 3 edges to [[_COMMUNITY_TestNewPatternsV080]]
- 2 edges to [[_COMMUNITY_TestPromptGuardEvasion]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_TestModuleInstantiationInEnforceMode]]
- 2 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 2 edges to [[_COMMUNITY_TestConcurrency]]
- 2 edges to [[_COMMUNITY_ToolResultInjectionScanner]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_test_edge_service_routes.py]]
- 1 edge to [[_COMMUNITY_TestFileSandbox]]
- 1 edge to [[_COMMUNITY_service.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_TestPromptGuard_1]]
- 1 edge to [[_COMMUNITY_secrets.py]]

## Top bridge nodes
- [[PromptGuard]] - degree 113, connects to 32 communities
- [[prompt_guard.py_2]] - degree 30, connects to 19 communities
- [[ThreatAction]] - degree 9, connects to 3 communities
- [[test_prompt_guard.py]] - degree 12, connects to 2 communities
- [[dot-scan()_3]] - degree 8, connects to 2 communities
