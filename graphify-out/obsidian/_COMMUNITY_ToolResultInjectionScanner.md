---
type: community
members: 41
---

# ToolResultInjectionScanner

**Members:** 41 nodes

## Members
- [[dot-_detect_encoded_injection()]] - code - gateway/security/tool_result_injection.py
- [[dot-_detect_unicode_obfuscation()]] - code - gateway/security/tool_result_injection.py
- [[dot-scan_tool_result()_2]] - code - gateway/security/tool_result_injection.py
- [[dot-setup_method()_11]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_base64_encoded_injection()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_high_severity_strips_content()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_ignore_instructions_injection_high_severity()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_medium_severity_warns()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_rtl_override_detected()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_xml_function_injection_detection()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_zero_width_chars_dont_bypass_detection()]] - code - gateway/tests/test_tool_result_injection.py
- [[Check for base64 or hex encoded injection attempts.]] - rationale - gateway/security/tool_result_injection.py
- [[Detect unicode-based obfuscation techniques.]] - rationale - gateway/security/tool_result_injection.py
- [[End-to-end scanner STRIPs a base64-encoded lower-ranked injection.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Enum_17]] - code
- [[InjectionAction]] - code - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[InjectionSeverity]] - code - gateway/security/tool_result_injection.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Scan tool result content for injection attempts. Args tool_name Name of the…]] - rationale - gateway/security/tool_result_injection.py
- [[Scanner for detecting prompt injection in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[Set up test fixtures._1]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test cases for ToolResultInjectionScanner.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test detection of 'ignore previous instructions' injection.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test detection of XML function call injection.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Test detection of base64 encoded injections.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[TestSanitization]] - code - gateway/tests/test_tool_result_injection.py
- [[TestToolResultInjectionScanner]] - code - gateway/tests/test_tool_injection_scan.py
- [[TestUnicodeObfuscation]] - code - gateway/tests/test_tool_result_injection.py
- [[Tests for ToolResultInjectionScanner.]] - rationale - gateway/tests/test_tool_injection_scan.py
- [[Tests for gatewaysecuritytool_result_injection.py — detect injections in tool…]] - rationale - gateway/tests/test_tool_result_injection.py
- [[Tool Result Injection Scanner — detect and neutralize prompt injection attempts…]] - rationale - gateway/security/tool_result_injection.py
- [[ToolResultInjectionScanner]] - code - gateway/security/tool_result_injection.py
- [[Zero-width chars are stripped by normalize_input, so injection is still caught.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[fixture_44]] - code
- [[scanner()]] - code - gateway/tests/test_tool_result_injection.py
- [[str_11]] - code
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
- 3 edges to [[_COMMUNITY_TestHighSeverity]]
- 3 edges to [[_COMMUNITY_normalize_input]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_SecurityPipeline]]
- 2 edges to [[_COMMUNITY_TestCleanContent]]
- 2 edges to [[_COMMUNITY_TestMediumSeverity]]
- 2 edges to [[_COMMUNITY_run]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_InjectionRule]]
- 2 edges to [[_COMMUNITY_dot-_filter_outbound]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY_dot-test_clean_content_passes_through]]
- 1 edge to [[_COMMUNITY_TestEncodedInjection]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[ToolResultInjectionScanner]] - degree 23, connects to 7 communities
- [[tool_result_injection.py]] - degree 14, connects to 5 communities
- [[InjectionAction]] - degree 14, connects to 4 communities
- [[test_tool_result_injection.py]] - degree 12, connects to 4 communities
- [[InjectionSeverity]] - degree 13, connects to 3 communities
