---
type: community
cohesion: 0.05
members: 60
---

# Module Group 60

**Cohesion:** 0.05 - loosely connected
**Members:** 60 nodes

## Members
- [[._apply_outbound_model_error_rewrites()]] - code - gateway/proxy/telegram_proxy.py
- [[._apply_outbound_status_notices()]] - code - gateway/proxy/telegram_proxy.py
- [[._build_ack_only_updates()]] - code - gateway/proxy/telegram_proxy.py
- [[._check_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[._collaborator_safe_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_high_risk_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[._extract_embedded_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[._filter_outbound()_1]] - code - gateway/proxy/telegram_proxy.py
- [[._filter_outbound_multipart()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_outbound_tool_calls()]] - code - gateway/proxy/telegram_proxy.py
- [[._html_tags_balanced()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_no_reply_token()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_owner_chat()]] - code - gateway/proxy/telegram_proxy.py
- [[._multipart_boundary()]] - code - gateway/proxy/telegram_proxy.py
- [[._multipart_get_field()]] - code - gateway/proxy/telegram_proxy.py
- [[._multipart_replace_field()]] - code - gateway/proxy/telegram_proxy.py
- [[._notify_user_blocked()]] - code - gateway/proxy/telegram_proxy.py
- [[._parse_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[._quarantine_outbound_block()]] - code - gateway/proxy/telegram_proxy.py
- [[._redact_owner_ids()]] - code - gateway/proxy/telegram_proxy.py
- [[._resolve_collaborator_mode()]] - code - gateway/proxy/telegram_proxy.py
- [[._rewrite_known_runtime_errors()]] - code - gateway/proxy/telegram_proxy.py
- [[._sanitize_reason()]] - code - gateway/proxy/telegram_proxy.py
- [[._scan_outbound_text()]] - code - gateway/proxy/telegram_proxy.py
- [[._set_outbound_block_cascade()]] - code - gateway/proxy/telegram_proxy.py
- [[._strip_collaborator_html_markup()]] - code - gateway/proxy/telegram_proxy.py
- [[._trigger_web_search_log()]] - code - gateway/proxy/telegram_proxy.py
- [[.scan_tool_result()_2]] - code - gateway/security/tool_result_injection.py
- [[Activate per-chat cascade window to prevent streaming-fragment leak-through.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Any_18]] - code - gateway/proxy/telegram_proxy.py
- [[Concise collaborator-safe reason text without internal leakage.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Core outbound security scan shared by JSON, form, and multipart branches.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect leakage patterns blocked for local_onlyproject_scoped collaborators.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect plain NO_REPLY sentinel with light punctuation wrapping.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract a non-file text field value from a multipartform-data body.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract the boundary token from a multipart Content-Type header.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter multipartform-data outbound bodies (sendPhotosendDocument).          Te]] - rationale - gateway/proxy/telegram_proxy.py
- [[Filter outbound bot messages (sendMessage, etc.).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Find first embedded tool-call JSON object inside arbitrary text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Intercept leaked raw tool-call JSON in outbound text.          Shared by the JSO]] - rationale - gateway/proxy/telegram_proxy.py
- [[Log a web_search egress event with user attribution when raw JSON leaks.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Map internal statuspolicy texts to user-safe replacement notices.          Pure]] - rationale - gateway/proxy/telegram_proxy.py
- [[Map recurring runtimeprovider failures to deterministic operator guidance.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Parse leaked model tool-call JSON blobs (e.g. {'name' 'NO_REPLY', ...}).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Persist blocked outbound messages for admin review.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Redact the owner's Telegram user ID from collaborator-bound text.          Strip]] - rationale - gateway/proxy/telegram_proxy.py
- [[Remove Telegram HTML formatting tags from collaborator outbound text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Replace a non-file text field value in a multipartform-data body.          Only]] - rationale - gateway/proxy/telegram_proxy.py
- [[Resolve effective collaboration mode for a user.          Resolution order]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True only when every Telegram-supported HTML open tag has a matching clos]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True when chat_id belongs to the configured owner.          Handles both]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return a safe-notice replacement when protected content would leak.          Cri]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return minimal getUpdates payload entries containing only update_id.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Rewrite raw modelruntime error texts to actionable user-facing messages.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Scan tool result content for injection attempts.          Args             tool]] - rationale - gateway/security/tool_result_injection.py
- [[Send a user-friendly notification when a message is blocked.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip internal paths and module names from block reasons before user display.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - rationale - gateway/security/input_normalizer.py
- [[input_normalizer.py]] - code - gateway/security/input_normalizer.py
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_60
SORT file.name ASC
```

## Connections to other communities
- 45 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 8 edges to [[_COMMUNITY_Module Group 160]]
- 4 edges to [[_COMMUNITY_Module Group 76]]
- 2 edges to [[_COMMUNITY_Module Group 208]]
- 1 edge to [[_COMMUNITY_Authentication & Rate Limiting]]
- 1 edge to [[_COMMUNITY_Module Group 190]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Progressive Lockdown]]
- 1 edge to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 1 edge to [[_COMMUNITY_Context Guard & Integrity]]
- 1 edge to [[_COMMUNITY_RBAC Middleware & Ingest API]]

## Top bridge nodes
- [[Any_18]] - degree 16, connects to 7 communities
- [[.scan_tool_result()_2]] - degree 7, connects to 3 communities
- [[._filter_outbound()_1]] - degree 18, connects to 2 communities
- [[._collaborator_safe_notice()]] - degree 14, connects to 2 communities
- [[._scan_outbound_text()]] - degree 8, connects to 2 communities
