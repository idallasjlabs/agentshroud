---
type: community
members: 56
---

# ._filter_outbound

**Members:** 56 nodes

## Members
- [[dot-_apply_outbound_model_error_rewrites()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_check_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_collaborator_safe_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_escape_pii_placeholders()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_extract_embedded_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_filter_outbound()_1]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_filter_outbound_multipart()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_handle_outbound_tool_calls()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_html_tags_balanced()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_is_owner_chat()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_is_valid_domain_name()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_multipart_boundary()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_multipart_get_field()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_multipart_replace_field()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_notify_user_blocked()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_parse_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_quarantine_outbound_block()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_redact_owner_ids()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_rewrite_known_runtime_errors()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_sanitize_reason()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_scan_outbound_text()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_set_outbound_block_cascade()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_strip_collaborator_html_markup()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_trigger_web_fetch_approval()]] - code - gateway/proxy/telegram_proxy.py
- [[dot-_trigger_web_search_log()]] - code - gateway/proxy/telegram_proxy.py
- [[Activate per-chat cascade window to prevent streaming-fragment leak-through.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Any_4]] - code - gateway/proxy/telegram_proxy.py
- [[Concise collaborator-safe reason text without internal leakage.]] - rationale - gateway/proxy/telegram_proxy.py
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
- [[Result of the shared outbound text security scan.      processed a scan path (c]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True only when every Telegram-supported HTML open tag has a matching clos]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True when chat_id belongs to the configured owner.          Handles both]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return a safe-notice replacement when protected content would leak.          Cri]] - rationale - gateway/proxy/telegram_proxy.py
- [[Rewrite raw modelruntime error texts to actionable user-facing messages.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Send a user-friendly notification when a message is blocked.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip internal paths and module names from block reasons before user display.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - rationale - gateway/security/input_normalizer.py
- [[Validate normalized domain labels to avoid malformed allowlist entries.]] - rationale - gateway/proxy/telegram_proxy.py
- [[_OutboundScan]] - code - gateway/proxy/telegram_proxy.py
- [[input_normalizer.py]] - code - gateway/security/input_normalizer.py
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_filter_outbound
SORT file.name ASC
```

## Connections to other communities
- 41 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy (5)]]
- 4 edges to [[_COMMUNITY_dot-_proxy_request_impl]]
- 2 edges to [[_COMMUNITY_ProgressiveLockdown]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_RateLimiter]]
- 2 edges to [[_COMMUNITY_DelegationManager]]
- 2 edges to [[_COMMUNITY_TestEgressApprovalQueue (2)]]
- 2 edges to [[_COMMUNITY_RBACConfig]]
- 2 edges to [[_COMMUNITY_telegram_proxy.py]]
- 1 edge to [[_COMMUNITY_InjectionAction (2)]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]

## Top bridge nodes
- [[Any_4]] - degree 17, connects to 8 communities
- [[_OutboundScan]] - degree 9, connects to 7 communities
- [[strip_markdown_exfil()]] - degree 7, connects to 3 communities
- [[input_normalizer.py]] - degree 4, connects to 3 communities
- [[dot-_filter_outbound()_1]] - degree 19, connects to 2 communities
