---
type: community
members: 53
---

# Community 96

**Members:** 53 nodes

## Members
- [[._apply_outbound_model_error_rewrites()]] - code - gateway/proxy/telegram_proxy.py
- [[._build_ack_only_updates()]] - code - gateway/proxy/telegram_proxy.py
- [[._escape_pii_placeholders()]] - code - gateway/proxy/telegram_proxy.py
- [[._extract_embedded_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[._filter_outbound()_1]] - code - gateway/proxy/telegram_proxy.py
- [[._filter_outbound_multipart()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_outbound_tool_calls()]] - code - gateway/proxy/telegram_proxy.py
- [[._html_tags_balanced()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_owner_chat()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_valid_domain_name()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_filename_reference()]] - code - gateway/proxy/telegram_proxy.py
- [[._multipart_boundary()]] - code - gateway/proxy/telegram_proxy.py
- [[._multipart_get_field()]] - code - gateway/proxy/telegram_proxy.py
- [[._multipart_replace_field()]] - code - gateway/proxy/telegram_proxy.py
- [[._parse_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[._quarantine_outbound_block()]] - code - gateway/proxy/telegram_proxy.py
- [[._redact_owner_ids()]] - code - gateway/proxy/telegram_proxy.py
- [[._resolve_text_field()]] - code - gateway/proxy/telegram_proxy.py
- [[._rewrite_known_runtime_errors()]] - code - gateway/proxy/telegram_proxy.py
- [[._scan_outbound_text()]] - code - gateway/proxy/telegram_proxy.py
- [[._set_outbound_block_cascade()]] - code - gateway/proxy/telegram_proxy.py
- [[._strip_collaborator_html_markup()]] - code - gateway/proxy/telegram_proxy.py
- [[._strip_json_fence()]] - code - gateway/proxy/telegram_proxy.py
- [[._suppress_duplicate_system_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._trigger_web_fetch_approval()]] - code - gateway/proxy/telegram_proxy.py
- [[._trigger_web_search_log()]] - code - gateway/proxy/telegram_proxy.py
- [[Activate per-chat cascade window to prevent streaming-fragment leak-through.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Any_21]] - code - gateway/proxy/telegram_proxy.py
- [[Best-effort check to avoid treating local file names as egress domains.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Core outbound security scan shared by JSON, form, and multipart branches.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract a non-file text field value from a multipartform-data body.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract the boundary token from a multipart Content-Type header.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter multipartform-data outbound bodies (sendPhotosendDocument).          Te]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter outbound bot messages (sendMessage, etc.).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Find first embedded tool-call JSON object inside arbitrary text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[HTML-escape PII redaction placeholders so they render as literal         text in]] - rationale - gateway/proxy/telegram_proxy.py
- [[Intercept leaked raw tool-call JSON in outbound text.          Shared by the JSO]] - rationale - gateway/proxy/telegram_proxy.py
- [[Log a web_search egress event with user attribution when raw JSON leaks.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Map recurring runtimeprovider failures to deterministic operator guidance.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Parse leaked model tool-call JSON blobs (e.g. {'name' 'NO_REPLY', ...}).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Persist blocked outbound messages for admin review.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Queue an interactive egress approval when raw web_fetch JSON leaks.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Redact the owner's Telegram user ID from collaborator-bound text.          Strip]] - rationale - gateway/proxy/telegram_proxy.py
- [[Remove Telegram HTML formatting tags from collaborator outbound text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Replace a non-file text field value in a multipartform-data body.          Only]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return (field_name, text_value) for Telegram-style outbound payloads.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True only when every Telegram-supported HTML open tag has a matching clos]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True when chat_id belongs to the configured owner.          Handles both]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return minimal getUpdates payload entries containing only update_id.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Rewrite raw modelruntime error texts to actionable user-facing messages.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip optional markdown json fences around model output.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Suppress repeated startupshutdown system notices in short windows.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Validate normalized domain labels to avoid malformed allowlist entries.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_96
SORT file.name ASC
```

## Connections to other communities
- 42 edges to [[_COMMUNITY_Community 14]]
- 11 edges to [[_COMMUNITY_Community 344]]
- 3 edges to [[_COMMUNITY_Community 61]]
- 1 edge to [[_COMMUNITY_Community 138]]
- 1 edge to [[_COMMUNITY_Community 89]]
- 1 edge to [[_COMMUNITY_Community 23]]
- 1 edge to [[_COMMUNITY_Community 75]]

## Top bridge nodes
- [[Any_21]] - degree 17, connects to 7 communities
- [[._filter_outbound()_1]] - degree 19, connects to 2 communities
- [[._filter_outbound_multipart()]] - degree 12, connects to 2 communities
- [[._scan_outbound_text()]] - degree 8, connects to 2 communities
- [[._trigger_web_fetch_approval()]] - degree 8, connects to 2 communities