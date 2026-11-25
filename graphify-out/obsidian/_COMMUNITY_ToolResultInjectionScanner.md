---
type: community
members: 70
---

# ToolResultInjectionScanner

**Members:** 70 nodes

## Members
- [[dot-__init__()_59]] - code - gateway/security/tool_result_injection.py
- [[dot-_detect_encoded_injection()]] - code - gateway/security/tool_result_injection.py
- [[dot-_detect_unicode_obfuscation()]] - code - gateway/security/tool_result_injection.py
- [[dot-scan_tool_result()_1]] - code - gateway/security/tool_result_injection.py
- [[dot-setup_method()_12]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_base64_clean_content_not_flagged()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_base64_encoded_injection()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_base64_encoded_injection()_1]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_clean_content_passes_through()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_clean_tool_output_passes()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_empty_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_high_severity_strips_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_ignore_instructions_injection_high_severity()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_ignore_previous_instructions()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_jailbreak_attempt()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_medium_severity_warns()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_new_instructions_override()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_none_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_prompt_extraction()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_role_reassignment()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_rtl_override_detected()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_social_engineering_admin()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_system_delimiter_injection()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_xml_function_injection()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_xml_function_injection_detection()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_zero_width_chars_dont_bypass_detection()]] - code - gateway/tests/test_tool_result_injection.py
- [[Benign base64 content should not trigger encoded injection.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[Check for base64 or hex encoded injection attempts.]] - rationale - gateway/security/tool_result_injection.py
- [[Detect unicode-based obfuscation techniques.]] - rationale - gateway/security/tool_result_injection.py
- [[End-to-end scanner STRIPs a base64-encoded lower-ranked injection.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Enum_17]] - code
- [[Initialize the scanner with optional custom rules. Args custom_rules…]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionAction]] - code - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[InjectionSeverity]] - code - gateway/security/tool_result_injection.py
- [[Input Normalization — pre-process text before security scanning. Strips…]] - rationale - gateway/security/input_normalizer.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Rule for detecting injection patterns in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[Scan tool result content for injection attempts. Args tool_name Name of the…]] - rationale - gateway/security/tool_result_injection.py
- [[Scanner for detecting prompt injection in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[Set up test fixtures._1]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Strip potentially malicious markdown from tool results. Removes - Markdown…]] - rationale - gateway/security/input_normalizer.py
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
- [[Tests for ToolResultInjectionScanner.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Tests for gatewaysecuritytool_result_injection.py — detect injections in tool…]] - rationale - gateway/tests/test_tool_result_injection.py
- [[Tool Result Injection Scanner — detect and neutralize prompt injection attempts…]] - rationale - gateway/security/tool_result_injection.py
- [[ToolResultInjectionScanner]] - code - gateway/security/tool_result_injection.py
- [[Zero-width chars are stripped by normalize_input, so injection is still caught.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[fixture_48]] - code
- [[input_normalizer.py_2]] - code - gateway/security/input_normalizer.py
- [[norm_ws()]] - code - gateway/tests/test_tool_injection_scan.py
- [[scanner()]] - code - gateway/tests/test_tool_result_injection.py
- [[str_8]] - code
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py
- [[test_tool_injection_scan.py]] - code - gateway/tests/test_tool_injection_scan.py
- [[test_tool_injection_scan_blocks_encoded_lower_ranked_rule()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_tool_result_injection.py]] - code - gateway/tests/test_tool_result_injection.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ToolResultInjectionScanner
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_asyncio_2]]
- 2 edges to [[_COMMUNITY_TeamsConfig]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_PIISanitizer]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_test_edge_pipeline.py]]
- 1 edge to [[_COMMUNITY_context_guard.py]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]

## Top bridge nodes
- [[input_normalizer.py_2]] - degree 11, connects to 7 communities
- [[ToolResultInjectionScanner]] - degree 23, connects to 6 communities
- [[InjectionAction]] - degree 14, connects to 4 communities
- [[tool_result_injection.py]] - degree 14, connects to 3 communities
- [[strip_markdown_exfil()]] - degree 7, connects to 2 communities
