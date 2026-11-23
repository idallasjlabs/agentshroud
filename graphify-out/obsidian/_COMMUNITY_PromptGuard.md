---
type: community
members: 106
---

# PromptGuard

**Members:** 106 nodes

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
- [[dot-setup_method()_24]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_1000_messages_under_5s()]] - code - gateway/tests/test_performance.py
- [[dot-test_benign_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_binary_data_in_text_fields()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_context_guard_session_isolation_under_load()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_context_guard_tool_manipulation()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_crlf_in_prompt_guard()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_deeply_nested_json()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_detection_accuracy_at_scale()]] - code - gateway/tests/test_performance.py
- [[dot-test_direct_injection_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_double_base64_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_empty_prompt()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_empty_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_explicit_key_used()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_fullwidth_detection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_homoglyph_detection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_lower_threshold_than_direct_scan()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_mcp_proxy_module_exists()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_mixed_case_still_caught()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_null_byte_in_prompt()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_polyglot_payload()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_preserves_legitimate_markdown()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_prompt_guard_catches_tool_injection()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_prompt_guard_concurrent_scans()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_prompt_guard_no_early_exit_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_rapid_fire_scans()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_register_and_verify()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_role_override_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_rtl_override_detection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_strips_fake_system_tags()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_strips_separator_overrides()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_tamper_detected()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_very_long_message()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_xml_entity_expansion()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_zero_width_evasion()]] - code - gateway/tests/test_security_hardening.py
- [[dot-verify_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[system style fake tags should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Binary data in text fields shouldn't crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[CRLF injection in prompt shouldn't bypass detection.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Compute and return an HMAC-SHA256 fingerprint for the system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[Concurrent prompt scans shouldn't interfere with each other.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Context guard should detect tool result manipulation.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Create a PromptGuard instance for testing]] - rationale - gateway/tests/test_prompt_guard.py
- [[Deeply nested JSON shouldn't cause stack overflow.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Detect and block prompt injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text. Returns list of decoded…]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[Double-encoded base64 injection should be caught.]] - rationale - gateway/tests/test_security_hardening.py
- [[Empty prompt should still register and verify cleanly.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Explicit ignore-instructions payload embedded in a tool result.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Explicit key parameter should override session key.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Fullwidth chars NFKC-normalized — injection defeated.]] - rationale - gateway/tests/test_security_hardening.py
- [[Injection attempts should be detected even under load.]] - rationale - gateway/tests/test_performance.py
- [[MCP proxy module should be importable.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Mix of Latin and Cyrillic should trigger homoglyph detection.]] - rationale - gateway/tests/test_security_hardening.py
- [[Normal markdown headers ( Title) should not be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Null bytes shouldn't bypass prompt guard.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Polyglot (valid as multiple formats) shouldn't bypass checks.]] - rationale - gateway/tests/test_security_audit_advanced.py
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
- [[Sessions shouldn't leak data under concurrent access.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Strip injected fake delimiters and return sanitized message. Called when…]] - rationale - gateway/security/prompt_guard.py
- [[Test MCP tool proxy security controls.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test thread safety and race conditions in security modules.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestConcurrency_1]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestMCPSecurity]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestPromptGuardEvasion]] - code - gateway/tests/test_security_hardening.py
- [[TestPromptGuardPerformance]] - code - gateway/tests/test_performance.py
- [[TestReanchorDelimiters]] - code - gateway/tests/test_prompt_guard.py
- [[TestSystemPromptHMAC]] - code - gateway/tests/test_prompt_guard.py
- [[TestToolResultScan]] - code - gateway/tests/test_prompt_guard.py
- [[Tests for indirect prompt injection detection in tool results.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Tests for prompt guard evasion techniques.]] - rationale - gateway/tests/test_security_hardening.py
- [[Tool result scan blocks at score ≥ 0.6 vs direct scan threshold of 0.8.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Verifying a tampered prompt should return False.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Very long messages should be handled without crash.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[XXE-style payloads shouldn't crash processing.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Zero-width chars between letters should not bypass detection.]] - rationale - gateway/tests/test_security_hardening.py
- [[analyze()]] - code - gateway/tests/test_security_audit_advanced.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py
- [[fixture_96]] - code
- [[prompt_guard()_1]] - code - gateway/tests/test_prompt_guard.py
- [[register_system_prompt + verify_system_prompt should succeed.]] - rationale - gateway/tests/test_prompt_guard.py
- [[scan()_3]] - code - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PromptGuard
SORT file.name ASC
```

## Connections to other communities
- 25 edges to [[_COMMUNITY_PIIConfig]]
- 16 edges to [[_COMMUNITY_prompt_guard.py]]
- 8 edges to [[_COMMUNITY_ContextGuard]]
- 6 edges to [[_COMMUNITY_test_adversarial_injection.py]]
- 5 edges to [[_COMMUNITY_SecurityPipeline]]
- 5 edges to [[_COMMUNITY_middleware.py]]
- 5 edges to [[_COMMUNITY_EnhancedApprovalQueue]]
- 4 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 3 edges to [[_COMMUNITY_test_all_modules_enforce.py]]
- 3 edges to [[_COMMUNITY_ContainerSnapshot]]
- 3 edges to [[_COMMUNITY_TestMultilingualInjection]]
- 3 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_TestClassicOverride]]
- 2 edges to [[_COMMUNITY_asyncio_1]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_test_redteam_probes.py]]
- 2 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 2 edges to [[_COMMUNITY_test_e2e_watchtower.py]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_test_security_integration.py]]
- 2 edges to [[_COMMUNITY_TestNewPatternsV080]]
- 2 edges to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_TestOverallDetectionRate]]
- 1 edge to [[_COMMUNITY_TestPromptExtraction]]
- 1 edge to [[_COMMUNITY_test_edge_service_routes.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]
- 1 edge to [[_COMMUNITY_ToolResultInjectionScanner]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]

## Top bridge nodes
- [[PromptGuard]] - degree 113, connects to 27 communities
- [[TestConcurrency_1]] - degree 13, connects to 5 communities
- [[TestMCPSecurity]] - degree 12, connects to 4 communities
- [[dot-scan()_3]] - degree 8, connects to 2 communities
- [[detect_base64_payloads()]] - degree 4, connects to 2 communities
