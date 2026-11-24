---
type: community
members: 75
---

# run

**Members:** 75 nodes

## Members
- [[dot-__init__()_3]] - code - gateway/security/prompt_protection.py
- [[dot-__init__()_4]] - code - gateway/security/xml_leak_filter.py
- [[dot-_calculate_similarity()]] - code - gateway/security/prompt_protection.py
- [[dot-_compile_detection_patterns()]] - code - gateway/security/prompt_protection.py
- [[dot-_load_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-_redact_fuzzy_match()]] - code - gateway/security/prompt_protection.py
- [[dot-add_protected_content()]] - code - gateway/security/prompt_protection.py
- [[dot-filter_function_calls_only()]] - code - gateway/security/xml_leak_filter.py
- [[dot-filter_response()]] - code - gateway/security/xml_leak_filter.py
- [[dot-get_protection_stats()]] - code - gateway/security/prompt_protection.py
- [[dot-register_bot_hostnames()]] - code - gateway/security/prompt_protection.py
- [[dot-scan_command_injection()]] - code - gateway/security/xml_leak_filter.py
- [[dot-scan_response()]] - code - gateway/security/prompt_protection.py
- [[dot-setup_method()_2]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_clean_response_passes_through()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_clean_text_passes()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_empty_text_returns_clean()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_file_path_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_function_calls_xml_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_python_eval_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_quick_function_calls_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_shell_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-test_sql_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[dot-xml_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[A piece of content that should be protected from disclosure.]] - rationale - gateway/security/prompt_protection.py
- [[Add bot container hostnames to the infrastructure detection patterns. Called at…]] - rationale - gateway/security/prompt_protection.py
- [[Add content to the protected registry. Args name Identifier for this content…]] - rationale - gateway/security/prompt_protection.py
- [[Any_3]] - code
- [[Calculate similarity between text and protected content.]] - rationale - gateway/security/prompt_protection.py
- [[Compile regex patterns for detecting disclosure attempts.]] - rationale - gateway/security/prompt_protection.py
- [[Create a PromptProtection instance for testing.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Filter outbound response content to remove sensitive information. Args…]] - rationale - gateway/security/xml_leak_filter.py
- [[Filter to remove sensitive XML and path information from outbound responses.]] - rationale - gateway/security/xml_leak_filter.py
- [[FilterResult]] - code - gateway/security/xml_leak_filter.py
- [[Get statistics about the protection system.]] - rationale - gateway/security/prompt_protection.py
- [[Initialize prompt protection system. Args config Configuration dictionary…]] - rationale - gateway/security/prompt_protection.py
- [[Initialize the filter with predefined patterns.]] - rationale - gateway/security/xml_leak_filter.py
- [[Load protected content from configured sources.]] - rationale - gateway/security/prompt_protection.py
- [[Main system prompt protection engine. Maintains fingerprints of sensitive…]] - rationale - gateway/security/prompt_protection.py
- [[PromptProtection]] - code - gateway/security/prompt_protection.py
- [[ProtectedContent]] - code - gateway/security/prompt_protection.py
- [[Quick filter that only removes function call XML (for performance). Args…]] - rationale - gateway/security/xml_leak_filter.py
- [[Redact text that fuzzy matches protected content.]] - rationale - gateway/security/prompt_protection.py
- [[RedactionResult]] - code - gateway/security/prompt_protection.py
- [[Result from XML leak filtering.]] - rationale - gateway/security/xml_leak_filter.py
- [[Result of scanning and redacting content.]] - rationale - gateway/security/prompt_protection.py
- [[Sample protected content for testing.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Scan outbound text for command  code injection patterns. Does NOT modify the…]] - rationale - gateway/security/xml_leak_filter.py
- [[Scan text for protected content and return redacted version. Args text The…]] - rationale - gateway/security/prompt_protection.py
- [[Set up test fixtures.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[System Prompt Protection for AgentShroud Gateway Prevents extraction of system…]] - rationale - gateway/security/prompt_protection.py
- [[Test cases for XMLLeakFilter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of file paths from responses.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of function call XML blocks.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test that clean responses pass through unchanged.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test the performance-optimized function calls only filter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[TestCommandInjectionScan]] - code - gateway/tests/test_xml_leak_filter.py
- [[TestXMLLeakFilter]] - code - gateway/tests/test_xml_leak_filter.py
- [[Tests for System Prompt Protection module.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Tests for XMLLeakFilter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[XML Leak Filter — prevent sensitive XML and path information from leaking in…]] - rationale - gateway/security/xml_leak_filter.py
- [[XMLLeakFilter]] - code - gateway/security/xml_leak_filter.py
- [[enforcement-audit-script.py]] - code - docs/planning/reviews/enforcement-audit-script.py
- [[fail()]] - code - docs/planning/reviews/enforcement-audit-script.py
- [[fixture]] - code
- [[fixture_1]] - code
- [[ok()]] - code - docs/planning/reviews/enforcement-audit-script.py
- [[prompt_protection()]] - code - gateway/tests/test_prompt_protection.py
- [[prompt_protection.py]] - code - gateway/security/prompt_protection.py
- [[run()]] - code - docs/planning/reviews/enforcement-audit-script.py
- [[sample_protected_content()]] - code - gateway/tests/test_prompt_protection.py
- [[test_prompt_protection.py]] - code - gateway/tests/test_prompt_protection.py
- [[test_xml_leak_filter.py]] - code - gateway/tests/test_xml_leak_filter.py
- [[warn()]] - code - docs/planning/reviews/enforcement-audit-script.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/run
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_socrouter.py]]
- 7 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_EgressFilter]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_TestPromptProtection]]
- 4 edges to [[_COMMUNITY_FileSandbox]]
- 4 edges to [[_COMMUNITY_PathIsolationManager]]
- 4 edges to [[_COMMUNITY_TestApprovalHardening]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_lifespan]]
- 2 edges to [[_COMMUNITY_ToolResultInjectionScanner]]
- 2 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_SecurityPipeline]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_CanaryTripwire]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_EncodingDetector]]
- 2 edges to [[_COMMUNITY_AuditStore]]
- 2 edges to [[_COMMUNITY_UserSessionManager]]
- 1 edge to [[_COMMUNITY_GatewayConfig]]
- 1 edge to [[_COMMUNITY_KeyLeakDetector]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_KeyRotationManager]]

## Top bridge nodes
- [[run()]] - degree 36, connects to 18 communities
- [[enforcement-audit-script.py]] - degree 33, connects to 18 communities
- [[XMLLeakFilter]] - degree 18, connects to 4 communities
- [[PromptProtection]] - degree 20, connects to 3 communities
- [[test_prompt_protection.py]] - degree 6, connects to 1 community
