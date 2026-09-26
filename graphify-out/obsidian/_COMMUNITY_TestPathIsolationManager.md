---
type: community
cohesion: 0.04
members: 73
---

# TestPathIsolationManager

**Cohesion:** 0.04 - loosely connected
**Members:** 73 nodes

## Members
- [[._apply_outbound_model_error_rewrites()]] - code - gateway/proxy/telegram_proxy.py
- [[._build_ack_only_updates()]] - code - gateway/proxy/telegram_proxy.py
- [[._check_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[._collaborator_safe_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_critical_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_high_risk_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[._emit_quarantine_event()]] - code - gateway/proxy/telegram_proxy.py
- [[._escape_pii_placeholders()]] - code - gateway/proxy/telegram_proxy.py
- [[._extract_embedded_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[._filter_outbound()_1]] - code - gateway/proxy/telegram_proxy.py
- [[._filter_outbound_multipart()]] - code - gateway/proxy/telegram_proxy.py
- [[._forward_file_download()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_outbound_tool_calls()]] - code - gateway/proxy/telegram_proxy.py
- [[._html_tags_balanced()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_owner_chat()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_suppressed_outbound_payload()]] - code - gateway/proxy/telegram_proxy.py
- [[._multipart_boundary()]] - code - gateway/proxy/telegram_proxy.py
- [[._multipart_get_field()]] - code - gateway/proxy/telegram_proxy.py
- [[._multipart_replace_field()]] - code - gateway/proxy/telegram_proxy.py
- [[._notify_user_blocked()]] - code - gateway/proxy/telegram_proxy.py
- [[._parse_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[._proxy_request_impl()]] - code - gateway/proxy/telegram_proxy.py
- [[._quarantine_outbound_block()]] - code - gateway/proxy/telegram_proxy.py
- [[._redact_owner_ids()]] - code - gateway/proxy/telegram_proxy.py
- [[._resolve_text_field()]] - code - gateway/proxy/telegram_proxy.py
- [[._rewrite_known_runtime_errors()]] - code - gateway/proxy/telegram_proxy.py
- [[._sanitize_reason()]] - code - gateway/proxy/telegram_proxy.py
- [[._scan_outbound_text()]] - code - gateway/proxy/telegram_proxy.py
- [[._set_outbound_block_cascade()]] - code - gateway/proxy/telegram_proxy.py
- [[._strip_collaborator_html_markup()]] - code - gateway/proxy/telegram_proxy.py
- [[._strip_json_fence()]] - code - gateway/proxy/telegram_proxy.py
- [[._suppress_duplicate_system_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._trigger_web_search_log()]] - code - gateway/proxy/telegram_proxy.py
- [[._username_for_bot()]] - code - gateway/proxy/telegram_proxy.py
- [[.proxy_request()]] - code - gateway/proxy/telegram_proxy.py
- [[Activate per-chat cascade window to prevent streaming-fragment leak-through.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Any_21]] - code - gateway/proxy/telegram_proxy.py
- [[Best-effort async event emission for quarantine actions.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Concise collaborator-safe reason text without internal leakage.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Core outbound security scan shared by JSON, form, and multipart branches.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect leakage patterns blocked for local_onlyproject_scoped collaborators.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect patterns that must redact for ALL non-owner chats, including full_access.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract a non-file text field value from a multipartform-data body.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract the boundary token from a multipart Content-Type header.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter multipartform-data outbound bodies (sendPhotosendDocument).          Te]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter outbound bot messages (sendMessage, etc.).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Find first embedded tool-call JSON object inside arbitrary text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Forward a Telegram file download and return a raw-binary sentinel dict.]] - rationale - gateway/proxy/telegram_proxy.py
- [[HTML-escape PII redaction placeholders so they render as literal         text in]] - rationale - gateway/proxy/telegram_proxy.py
- [[Intercept leaked raw tool-call JSON in outbound text.          Shared by the JSO]] - rationale - gateway/proxy/telegram_proxy.py
- [[Log a web_search egress event with user attribution when raw JSON leaks.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Map recurring runtimeprovider failures to deterministic operator guidance.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Parse leaked model tool-call JSON blobs (e.g. {'name' 'NO_REPLY', ...}).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Persist blocked outbound messages for admin review.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Proxy a single Telegram API request.          For getUpdates responses scan eac]] - rationale - gateway/proxy/telegram_proxy.py
- [[Redact the owner's Telegram user ID from collaborator-bound text.          Strip]] - rationale - gateway/proxy/telegram_proxy.py
- [[Remove Telegram HTML formatting tags from collaborator outbound text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Replace a non-file text field value in a multipartform-data body.          Only]] - rationale - gateway/proxy/telegram_proxy.py
- [[Result of the shared outbound text security scan.      processed a scan path (c]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return (field_name, text_value) for Telegram-style outbound payloads.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True only when every Telegram-supported HTML open tag has a matching clos]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True when chat_id belongs to the configured owner.          Handles both]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return a safe-notice replacement when protected content would leak.          Cri]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return minimal getUpdates payload entries containing only update_id.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return the @username (without @) for the given bot_id.          Looks up ``_bot_]] - rationale - gateway/proxy/telegram_proxy.py
- [[Rewrite raw modelruntime error texts to actionable user-facing messages.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send a user-friendly notification when a message is blocked.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip internal paths and module names from block reasons before user display.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip optional markdown json fences around model output.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Suppress repeated startupshutdown system notices in short windows.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Thin wrapper sets per-request bot identity in contextvars so local replies]] - rationale - gateway/proxy/telegram_proxy.py
- [[True when filtered payload should be dropped instead of forwarded.]] - rationale - gateway/proxy/telegram_proxy.py
- [[_OutboundScan]] - code - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPathIsolationManager
SORT file.name ASC
```

## Connections to other communities
- 58 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY_test_a2a_proxy.py]]
- 2 edges to [[_COMMUNITY_StdioConnection]]
- 2 edges to [[_COMMUNITY_make_event()]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_IntelReportStore]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_ToolACLEnforcer]]
- 2 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]

## Top bridge nodes
- [[Any_21]] - degree 17, connects to 7 communities
- [[_OutboundScan]] - degree 9, connects to 7 communities
- [[._proxy_request_impl()]] - degree 15, connects to 3 communities
- [[._filter_outbound()_1]] - degree 19, connects to 2 communities
- [[._filter_outbound_multipart()]] - degree 12, connects to 2 communities