---
type: community
members: 75
---

# Community 154

**Members:** 75 nodes

## Members
- [[.__init__()_123]] - code - gateway/security/tool_result_injection.py
- [[._check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[._check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[._detect_encoded_injection()]] - code - gateway/security/tool_result_injection.py
- [[._detect_unicode_obfuscation()]] - code - gateway/security/tool_result_injection.py
- [[.scan()_4]] - code - gateway/security/prompt_guard.py
- [[.scan_tool_result()_2]] - code - gateway/security/prompt_guard.py
- [[.scan_tool_result()_3]] - code - gateway/security/tool_result_injection.py
- [[.setup_method()_36]] - code - gateway/tests/test_tool_injection_scan.py
- [[.test_base64_clean_content_not_flagged()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_base64_encoded_injection()_1]] - code - gateway/tests/test_tool_injection_scan.py
- [[.test_base64_encoded_injection()_2]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_clean_content_passes_through()]] - code - gateway/tests/test_tool_injection_scan.py
- [[.test_clean_tool_output_passes()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_empty_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_high_severity_strips_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_ignore_instructions_injection_high_severity()]] - code - gateway/tests/test_tool_injection_scan.py
- [[.test_ignore_previous_instructions()_1]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_jailbreak_attempt()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_medium_severity_warns()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_new_instructions_override()_1]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_none_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_prompt_extraction()_1]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_role_reassignment()_2]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_rtl_override_detected()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_social_engineering_admin()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_system_delimiter_injection()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_xml_function_injection()]] - code - gateway/tests/test_tool_result_injection.py
- [[.test_xml_function_injection_detection()]] - code - gateway/tests/test_tool_injection_scan.py
- [[.test_zero_width_chars_dont_bypass_detection()]] - code - gateway/tests/test_tool_result_injection.py
- [[Benign base64 content should not trigger encoded injection.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[Check for base64 or hex encoded injection attempts.]] - rationale - gateway/security/tool_result_injection.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text.     Returns list of decoded st]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[Detect unicode-based obfuscation techniques.]] - rationale - gateway/security/tool_result_injection.py
- [[End-to-end scanner STRIPs a base64-encoded lower-ranked injection.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Initialize the scanner with optional custom rules.          Args             cu]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[InjectionSeverity]] - code - gateway/security/tool_result_injection.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Rule for detecting injection patterns in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[Scan input text for prompt injection patterns.          Args             text]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection.          Tool results (w]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for injection attempts.          Args             tool]] - rationale - gateway/security/tool_result_injection.py
- [[Scanner for detecting prompt injection in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[Set up test fixtures._2]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - rationale - gateway/security/input_normalizer.py
- [[Test cases for ToolResultInjectionScanner.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test detection of 'ignore previous instructions' injection.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test detection of XML function call injection.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test detection of base64 encoded injections.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test that clean content passes through unchanged.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[TestCleanContent]] - code - gateway/tests/test_tool_result_injection.py
- [[TestEncodedInjection]] - code - gateway/tests/test_tool_result_injection.py
- [[TestHighSeverity]] - code - gateway/tests/test_tool_result_injection.py
- [[TestMediumSeverity]] - code - gateway/tests/test_tool_result_injection.py
- [[TestSanitization]] - code - gateway/tests/test_tool_result_injection.py
- [[TestToolResultInjectionScanner]] - code - gateway/tests/test_tool_injection_scan.py
- [[TestUnicodeObfuscation]] - code - gateway/tests/test_tool_result_injection.py
- [[ToolResultInjectionScanner]] - code - gateway/security/tool_result_injection.py
- [[Zero-width chars are stripped by normalize_input, so injection is still caught.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[`_detect_encoded_injection` matches rules beyond the old top-6 slice.      `jail]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py
- [[hex-encoded lower-ranked injection is caught by the full ruleset.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[input_normalizer.py]] - code - gateway/security/input_normalizer.py
- [[scanner()]] - code - gateway/tests/test_tool_result_injection.py
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py
- [[test_tool_injection_encoded_check_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_injection_hex_encoded_uses_full_ruleset()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_injection_scan.py]] - code - gateway/tests/test_tool_injection_scan.py
- [[test_tool_injection_scan_blocks_encoded_lower_ranked_rule()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_result_injection.py]] - code - gateway/tests/test_tool_result_injection.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_154
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_Community 24]]
- 13 edges to [[_COMMUNITY_Community 72]]
- 11 edges to [[_COMMUNITY_Community 84]]
- 4 edges to [[_COMMUNITY_Community 14]]
- 3 edges to [[_COMMUNITY_Community 8]]
- 2 edges to [[_COMMUNITY_Community 96]]
- 2 edges to [[_COMMUNITY_Community 115]]
- 1 edge to [[_COMMUNITY_Community 223]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 162]]
- 1 edge to [[_COMMUNITY_Community 141]]
- 1 edge to [[_COMMUNITY_Community 917]]
- 1 edge to [[_COMMUNITY_Community 50]]

## Top bridge nodes
- [[ToolResultInjectionScanner]] - degree 41, connects to 5 communities
- [[tool_result_injection.py]] - degree 11, connects to 5 communities
- [[.scan()_4]] - degree 8, connects to 3 communities
- [[strip_markdown_exfil()]] - degree 7, connects to 2 communities
- [[input_normalizer.py]] - degree 4, connects to 2 communities