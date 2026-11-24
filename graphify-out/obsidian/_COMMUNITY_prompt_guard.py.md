---
type: community
members: 82
---

# prompt_guard.py

**Members:** 82 nodes

## Members
- [[--- new instructions patterns should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[dot-__init__()_136]] - code - gateway/security/prompt_guard.py
- [[dot-_check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[dot-_check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[dot-_get_hmac_key()]] - code - gateway/security/prompt_guard.py
- [[dot-guard()_6]] - code - gateway/tests/test_prompt_guard.py
- [[dot-register_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[dot-scan()_3]] - code - gateway/security/prompt_guard.py
- [[dot-scan_tool_result()_3]] - code - gateway/security/prompt_guard.py
- [[dot-setup_method()_23]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_base64_encoded_injection()_2]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_benign_base64()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_benign_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_clean_input()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_combined_attack_high_score()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_custom_pattern()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_dan_jailbreak()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_delimiter_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_direct_injection_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_empty_input()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_empty_prompt()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_empty_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_explicit_key_used()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_forget_everything()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_ignore_instructions()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_indirect_injection()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_lower_threshold_than_direct_scan()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_new_instructions_override()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_none_input()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_preserves_legitimate_markdown()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_prompt_extraction()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_prompt_leak_question()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_register_and_verify()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_role_override_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_role_reassignment()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_rtl_override()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_sanitized_output()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_strips_fake_system_tags()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_strips_separator_overrides()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_tamper_detected()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_unicode_zero_width()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_warn_threshold()]] - code - gateway/tests/test_security_hardening.py
- [[dot-test_xml_tag_injection()_1]] - code - gateway/tests/test_security_hardening.py
- [[dot-verify_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[system style fake tags should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Args block_threshold Score at or above which input is blocked.…]] - rationale - gateway/security/prompt_guard.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Compute and return an HMAC-SHA256 fingerprint for the system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text. Returns list of decoded…]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[Empty prompt should still register and verify cleanly.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Enum_34]] - code
- [[Explicit ignore-instructions payload embedded in a tool result.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Explicit key parameter should override session key.]] - rationale - gateway/tests/test_prompt_guard.py
- [[HMAC-SHA256 fingerprint for a registered system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[Normal markdown headers ( Title) should not be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[PatternRule]] - code - gateway/security/prompt_guard.py
- [[Prompt Injection Defense — detect and block prompt injection attempts. Scoring…]] - rationale - gateway/security/prompt_guard.py
- [[Return HMAC key env var preferred, session-scoped random fallback.]] - rationale - gateway/security/prompt_guard.py
- [[Return True if prompt_text matches the stored HMAC fingerprint.]] - rationale - gateway/security/prompt_guard.py
- [[Scan input text for prompt injection patterns. Args text The user input to…]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection. Tool results (web…]] - rationale - gateway/security/prompt_guard.py
- [[ScanResult]] - code - gateway/security/prompt_guard.py
- [[SystemPromptFingerprint]] - code - gateway/security/prompt_guard.py
- [[Test PromptGuard initialization]] - rationale - gateway/tests/test_prompt_guard.py
- [[Test that normal messages pass through]] - rationale - gateway/tests/test_prompt_guard.py
- [[TestPromptGuard]] - code - gateway/tests/test_security_hardening.py
- [[TestReanchorDelimiters]] - code - gateway/tests/test_prompt_guard.py
- [[TestSystemPromptHMAC]] - code - gateway/tests/test_prompt_guard.py
- [[TestToolResultScan]] - code - gateway/tests/test_prompt_guard.py
- [[Tests for PromptGuard security component]] - rationale - gateway/tests/test_prompt_guard.py
- [[Tests for indirect prompt injection detection in tool results.]] - rationale - gateway/tests/test_prompt_guard.py
- [[ThreatAction]] - code - gateway/security/prompt_guard.py
- [[Tool result scan blocks at score ≥ 0.6 vs direct scan threshold of 0.8.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Verifying a tampered prompt should return False.]] - rationale - gateway/tests/test_prompt_guard.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py
- [[prompt_guard.py_2]] - code - gateway/security/prompt_guard.py
- [[register_system_prompt + verify_system_prompt should succeed.]] - rationale - gateway/tests/test_prompt_guard.py
- [[str_19]] - code
- [[test_benign_message()]] - code - gateway/tests/test_prompt_guard.py
- [[test_prompt_guard.py]] - code - gateway/tests/test_prompt_guard.py
- [[test_prompt_guard_init()]] - code - gateway/tests/test_prompt_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/prompt_guardpy
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_normalize_input]]
- 4 edges to [[_COMMUNITY_AgentRegistry]]
- 3 edges to [[_COMMUNITY_SecurityPipeline]]
- 3 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 3 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 1 edge to [[_COMMUNITY_TestNewPatternsV080]]
- 1 edge to [[_COMMUNITY_test_e2e_watchtower.py]]
- 1 edge to [[_COMMUNITY_TestMultilingualInjection]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_security_integration.py]]
- 1 edge to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]

## Top bridge nodes
- [[prompt_guard.py_2]] - degree 30, connects to 12 communities
- [[ThreatAction]] - degree 9, connects to 3 communities
- [[TestPromptGuard]] - degree 26, connects to 2 communities
- [[test_prompt_guard.py]] - degree 12, connects to 2 communities
- [[dot-scan()_3]] - degree 8, connects to 2 communities
