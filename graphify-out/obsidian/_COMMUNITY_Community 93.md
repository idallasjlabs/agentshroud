---
type: community
members: 37
---

# Community 93

**Members:** 37 nodes

## Members
- [[._apply_outbound_model_error_rewrites()]] - code - gateway/proxy/telegram_proxy.py
- [[._apply_outbound_status_notices()]] - code - gateway/proxy/telegram_proxy.py
- [[._build_ack_only_updates()]] - code - gateway/proxy/telegram_proxy.py
- [[._check_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_critical_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_high_risk_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_internal_approval_banner()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_legacy_block_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._extract_embedded_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[._handle_outbound_tool_calls()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_no_reply_token()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_valid_domain_name()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_filename_reference()]] - code - gateway/proxy/telegram_proxy.py
- [[._parse_tool_call_json()]] - code - gateway/proxy/telegram_proxy.py
- [[._rewrite_known_runtime_errors()]] - code - gateway/proxy/telegram_proxy.py
- [[._strip_json_fence()]] - code - gateway/proxy/telegram_proxy.py
- [[._trigger_web_fetch_approval()]] - code - gateway/proxy/telegram_proxy.py
- [[._trigger_web_search_log()]] - code - gateway/proxy/telegram_proxy.py
- [[Any_21]] - code - gateway/proxy/telegram_proxy.py
- [[Best-effort check to avoid treating local file names as egress domains.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect internal approvalegress banner text that must remain owner-only.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect leakage patterns blocked for local_onlyproject_scoped collaborators.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect legacy bracket-style block notices for collaborator normalization.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect patterns that must redact for ALL non-owner chats, including full_access.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect plain NO_REPLY sentinel with light punctuation wrapping.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Find first embedded tool-call JSON object inside arbitrary text.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Intercept leaked raw tool-call JSON in outbound text.          Shared by the JSO]] - rationale - gateway/proxy/telegram_proxy.py
- [[Log a web_search egress event with user attribution when raw JSON leaks.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Map internal statuspolicy texts to user-safe replacement notices.          Pure]] - rationale - gateway/proxy/telegram_proxy.py
- [[Map recurring runtimeprovider failures to deterministic operator guidance.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Parse leaked model tool-call JSON blobs (e.g. {'name' 'NO_REPLY', ...}).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Queue an interactive egress approval when raw web_fetch JSON leaks.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return a safe-notice replacement when protected content would leak.          Cri]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return minimal getUpdates payload entries containing only update_id.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Rewrite raw modelruntime error texts to actionable user-facing messages.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip optional markdown json fences around model output.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Validate normalized domain labels to avoid malformed allowlist entries.]] - rationale - gateway/proxy/telegram_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_93
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_Community 4]]
- 10 edges to [[_COMMUNITY_Community 263]]
- 7 edges to [[_COMMUNITY_Community 862]]
- 1 edge to [[_COMMUNITY_Community 124]]
- 1 edge to [[_COMMUNITY_Community 77]]
- 1 edge to [[_COMMUNITY_Community 9]]
- 1 edge to [[_COMMUNITY_Community 61]]
- 1 edge to [[_COMMUNITY_Community 62]]
- 1 edge to [[_COMMUNITY_Community 15]]

## Top bridge nodes
- [[Any_21]] - degree 17, connects to 7 communities
- [[._apply_outbound_status_notices()]] - degree 9, connects to 3 communities
- [[._handle_outbound_tool_calls()]] - degree 11, connects to 2 communities
- [[._check_collaborator_leakage()]] - degree 8, connects to 2 communities
- [[._trigger_web_fetch_approval()]] - degree 8, connects to 2 communities