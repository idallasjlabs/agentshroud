---
type: community
members: 63
---

# ._filter_outbound

**Members:** 63 nodes

## Members
- [[dot-_apply_outbound_model_error_rewrites()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_build_ack_only_updates()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_check_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_collaborator_safe_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_escape_pii_placeholders()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_extract_embedded_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_filter_outbound()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_filter_outbound_multipart()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_handle_outbound_tool_calls()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_html_tags_balanced()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_multipart_boundary()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_multipart_get_field()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_multipart_replace_field()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_parse_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_quarantine_outbound_block()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_redact_owner_ids()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_resolve_text_field()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_scan_outbound_text()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_set_outbound_block_cascade()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_strip_collaborator_html_markup()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_strip_json_fence()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_suppress_duplicate_system_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_trigger_web_fetch_approval()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_trigger_web_search_log()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-test_collaborator_safe_notice_maps_internal_network_probe_to_egress_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_safe_notice_maps_metadata_probe_to_secret_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_safe_notice_maps_obfuscated_probe_to_scope_notice()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_safe_notice_uses_canonical_header_with_blank_line()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_resolve_text_field_falls_back_to_first_string_when_all_empty()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_resolve_text_field_prefers_first_non_empty_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Activate per-chat cascade window to prevent streaming-fragment leak-through.…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Any_18]] - code
- [[Collaborator-safe notices must use the canonical protected header format.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Concise collaborator-safe reason text without internal leakage.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Core outbound security scan shared by JSON, form, and multipart branches. Runs…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract a non-file text field value from a multipartform-data body.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract the boundary token from a multipart Content-Type header.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter multipartform-data outbound bodies (sendPhotosendDocument). Text parts…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter outbound bot messages (sendMessage, etc.).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Find first embedded tool-call JSON object inside arbitrary text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[HTML-escape PII redaction placeholders so they render as literal text instead…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Intercept leaked raw tool-call JSON in outbound text. Shared by the JSON and…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Log a web_search egress event with user attribution when raw JSON leaks.…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Parse leaked model tool-call JSON blobs (e.g. {'name' 'NO_REPLY', ...}).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Persist blocked outbound messages for admin review.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Queue an interactive egress approval when raw web_fetch JSON leaks.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Redact the owner's Telegram user ID from collaborator-bound text. Strips the ID…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Remove Telegram HTML formatting tags from collaborator outbound text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Replace a non-file text field value in a multipartform-data body. Only the…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Result of the shared outbound text security scan. processed a scan path…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return (field_name, text_value) for Telegram-style outbound payloads.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True only when every Telegram-supported HTML open tag has a matching…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return a safe-notice replacement when protected content would leak. Critical…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return minimal getUpdates payload entries containing only update_id.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Rewrite raw modelruntime error texts to actionable user-facing messages. Pure…]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip optional markdown json fences around model output.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip potentially malicious markdown from tool results. Removes - Markdown…]] - rationale - gateway/security/input_normalizer.py
- [[Suppress repeated startupshutdown system notices in short windows.]] - rationale - gateway/proxy/telegram_proxy.py
- [[TestOutboundTextFieldResolution]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unit tests for outbound text field resolution helper behavior.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_OutboundScan]] - code - gateway/proxy/telegram_proxy.py
- [[_canonical_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_filter_outbound
SORT file.name ASC
```

## Connections to other communities
- 38 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 8 edges to [[_COMMUNITY_normalize_input]]
- 6 edges to [[_COMMUNITY_TestOutboundClassifierHelpers]]
- 4 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 3 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py]]
- 2 edges to [[_COMMUNITY_ToolResultInjectionScanner]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_dot-_rewrite_known_runtime_errors]]
- 1 edge to [[_COMMUNITY_SlackAPIProxy]]
- 1 edge to [[_COMMUNITY_dot-_is_valid_domain_name]]

## Top bridge nodes
- [[dot-_trigger_web_fetch_approval()]] - degree 9, connects to 5 communities
- [[dot-_filter_outbound()]] - degree 19, connects to 3 communities
- [[dot-_collaborator_safe_notice()]] - degree 18, connects to 3 communities
- [[strip_markdown_exfil()]] - degree 7, connects to 3 communities
- [[dot-_trigger_web_search_log()]] - degree 6, connects to 3 communities
