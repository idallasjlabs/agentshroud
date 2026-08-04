---
type: community
cohesion: 0.05
members: 53
---

# Module Group 76

**Cohesion:** 0.05 - loosely connected
**Members:** 53 nodes

## Members
- [[.__init__()_97]] - code - gateway/security/tool_result_injection.py
- [[._detect_encoded_injection()]] - code - gateway/security/tool_result_injection.py
- [[._detect_unicode_obfuscation()]] - code - gateway/security/tool_result_injection.py
- [[.setup_method()_33]] - code - gateway/tests/test_tool_injection_scan.py
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
- [[Detect unicode-based obfuscation techniques.]] - rationale - gateway/security/tool_result_injection.py
- [[Initialize the scanner with optional custom rules.          Args             cu]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionAction]] - code - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[InjectionSeverity]] - code - gateway/security/tool_result_injection.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Rule for detecting injection patterns in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[Set up test fixtures._2]] - rationale - gateway/tests/test_tool_injection_scan.py
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
- [[Zero-width chars are stripped by normalize_input, so injection is still caught.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[scanner()]] - code - gateway/tests/test_tool_result_injection.py
- [[test_tool_injection_scan.py]] - code - gateway/tests/test_tool_injection_scan.py
- [[test_tool_result_injection.py]] - code - gateway/tests/test_tool_result_injection.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_76
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 5 edges to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 4 edges to [[_COMMUNITY_Security Pipeline & Audit Chain]]
- 4 edges to [[_COMMUNITY_Module Group 60]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Pipeline Action & Instruction Envelope]]
- 1 edge to [[_COMMUNITY_Module Group 177]]
- 1 edge to [[_COMMUNITY_Telegram Proxy Core]]

## Top bridge nodes
- [[InjectionAction]] - degree 19, connects to 5 communities
- [[tool_result_injection.py]] - degree 8, connects to 4 communities
- [[._detect_encoded_injection()]] - degree 4, connects to 2 communities
- [[._detect_unicode_obfuscation()]] - degree 4, connects to 2 communities
- [[InjectionSeverity]] - degree 14, connects to 1 community
