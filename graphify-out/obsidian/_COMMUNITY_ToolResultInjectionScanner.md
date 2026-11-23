---
type: community
members: 113
---

# ToolResultInjectionScanner

**Members:** 113 nodes

## Members
- [[dot-__init__()_32]] - code - gateway/security/tool_result_injection.py
- [[dot-_apply_outbound_model_error_rewrites()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_apply_outbound_status_notices()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_check_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_collaborator_safe_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_detect_encoded_injection()]] - code - gateway/security/tool_result_injection.py
- [[dot-_detect_unicode_obfuscation()]] - code - gateway/security/tool_result_injection.py
- [[dot-_escape_pii_placeholders()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_extract_embedded_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_filter_outbound()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_filter_outbound_multipart()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_handle_outbound_tool_calls()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_html_tags_balanced()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_is_owner_chat()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_multipart_boundary()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_multipart_get_field()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_multipart_replace_field()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_quarantine_outbound_block()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_redact_owner_ids()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_scan_outbound_text()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_set_outbound_block_cascade()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_strip_collaborator_html_markup()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_trigger_web_search_log()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-scan_tool_result()_1]] - code - gateway/security/tool_result_injection.py
- [[dot-setup_method()_8]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_base64_clean_content_not_flagged()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_base64_encoded_injection()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_base64_encoded_injection()_1]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_clean_content_passes_through()]] - code - gateway/tests/test_tool_injection_scan.py
- [[dot-test_clean_tool_output_passes()]] - code - gateway/tests/test_tool_result_injection.py
- [[dot-test_collaborator_safe_notice_uses_canonical_header_with_blank_line()]] - code - gateway/tests/test_telegram_proxy_inbound.py
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
- [[Activate per-chat cascade window to prevent streaming-fragment leak-through.…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Any_12]] - code
- [[Benign base64 content should not trigger encoded injection.]] - rationale - gateway/tests/test_tool_result_injection.py
- [[Check for base64 or hex encoded injection attempts.]] - rationale - gateway/security/tool_result_injection.py
- [[Collaborator-safe notices must use the canonical protected header format.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Concise collaborator-safe reason text without internal leakage.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Core outbound security scan shared by JSON, form, and multipart branches. Runs…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect unicode-based obfuscation techniques.]] - rationale - gateway/security/tool_result_injection.py
- [[End-to-end scanner STRIPs a base64-encoded lower-ranked injection.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[Enum_14]] - code
- [[Extract a non-file text field value from a multipartform-data body.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract the boundary token from a multipart Content-Type header.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter multipartform-data outbound bodies (sendPhotosendDocument). Text parts…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter outbound bot messages (sendMessage, etc.).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Find first embedded tool-call JSON object inside arbitrary text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[HTML-escape PII redaction placeholders so they render as literal text instead…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Initialize the scanner with optional custom rules. Args custom_rules…]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionAction]] - code - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[InjectionSeverity]] - code - gateway/security/tool_result_injection.py
- [[Input Normalization — pre-process text before security scanning. Strips…]] - rationale - gateway/security/input_normalizer.py
- [[Intercept leaked raw tool-call JSON in outbound text. Shared by the JSON and…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Log a web_search egress event with user attribution when raw JSON leaks.…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Map internal statuspolicy texts to user-safe replacement notices. Pure helper…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Persist blocked outbound messages for admin review.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Redact the owner's Telegram user ID from collaborator-bound text. Strips the ID…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Remove Telegram HTML formatting tags from collaborator outbound text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Replace a non-file text field value in a multipartform-data body. Only the…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Return True only when every Telegram-supported HTML open tag has a matching…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True when chat_id belongs to the configured owner. Handles both real…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return a safe-notice replacement when protected content would leak. Critical…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Rewrite raw modelruntime error texts to actionable user-facing messages. Pure…]] - rationale - gateway/proxy/telegram_proxy.py
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
- [[fixture_23]] - code
- [[input_normalizer.py_2]] - code - gateway/security/input_normalizer.py
- [[norm_ws()]] - code - gateway/tests/test_tool_injection_scan.py
- [[scanner()]] - code - gateway/tests/test_tool_result_injection.py
- [[str_9]] - code
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
- 47 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 7 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 6 edges to [[_COMMUNITY_middleware.py]]
- 5 edges to [[_COMMUNITY_dot-_extract_first_egress_target]]
- 3 edges to [[_COMMUNITY_telegram_proxy.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_asyncio_1]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_SecurityPipeline]]
- 1 edge to [[_COMMUNITY_lifespan]]
- 1 edge to [[_COMMUNITY__make_proxy]]
- 1 edge to [[_COMMUNITY_dot-_rewrite_known_runtime_errors]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_PromptGuard]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_prompt_guard.py]]
- 1 edge to [[_COMMUNITY_test_adversarial_injection.py]]

## Top bridge nodes
- [[input_normalizer.py_2]] - degree 11, connects to 8 communities
- [[ToolResultInjectionScanner]] - degree 23, connects to 5 communities
- [[InjectionAction]] - degree 14, connects to 4 communities
- [[tool_result_injection.py]] - degree 14, connects to 3 communities
- [[dot-_scan_outbound_text()]] - degree 9, connects to 3 communities
