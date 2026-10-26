---
type: community
members: 76
---

# Community 845

**Members:** 76 nodes

## Members
- [[.test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_agent_failed_timeout_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_agent_failed_prefix_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_caption_tool_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_internal_tool_output_suppressed_notice_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_legacy_block_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_legacy_protected_prefix_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_not_authorized_command_text_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contextvar_takes_precedence_over_default()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_default_is_openclaw_when_not_injected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_embedded_tool_call_json_is_removed_from_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_fail_closed_replaces_caption_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_unknown_tool_call_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_sandbox_error_with_cannot_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_info_filter_redaction_escalates_to_block_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_injected_default_overrides_openclaw()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_long_outbound_message_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_hyphen_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_approval_normalizes_leading_dot_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_explicit_md_tld_domain_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_invalid_host_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_scheme_relative_url_queues_https_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_search_json_collaborator_safe_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_search_json_owner_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_collaborator_no_reply_gets_protected_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_draft_payload_tool_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_no_egress_filter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_query_truncation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Agent timeout prefix variants should also map to retry guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Any outbound info-filter redaction should be blocked for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Cannot access' phrasing should be rewritten for healthcheck SKILL.md sandbox mes]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Caption-only payloads should not bypass collaborator leak normalization.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator auth-denial command text should map to protected scope notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator chat raw web_search JSON produces a safe notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payloads should get protected notice, not suppression.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be blocked]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embedding provider wording variants should rewrite for urlencoded payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider memory errors should also be rewritten for urlencoded payload]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Explicitly schemed domains should still queue approvals even for .md ccTLD.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Fail-closed substitution must target the resolved text field.          Regressio]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form caption should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep healthcheck SKILL.md text unchanged when sandbox hint i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload agent-failed prefix should normalize to protected unavailable notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload internal tool-output suppression string should normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload legacy 'Protected' wording should normalize to canonical protected]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form-encoded draft payloads must not leak raw tool-call JSON.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Hyphen-separated embedding-provider wording should rewrite for form payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If tool-call JSON is embedded in prose, strip JSON block before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Legacy bracket-style block notices should normalize to Protect wording.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Malformed host with leading dot should still queue approval for normalized domai]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Messages above hard size cap should be blocked to prevent split bypass.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Multiline fenced NO_REPLY token should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-domain hosts should not queue egress approval requests.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner chat raw web_search JSON produces 'Switch to tool-capable model' message.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Queries longer than 200 chars are truncated in the SOC log reason.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Repeated identical web_fetch leaks should not spam approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Sandbox SKILL.md messages must include healthcheck context before rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Scheme-relative URLs in leaked JSON should normalize to HTTPS approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TelegramAPIProxy_3]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestDefaultBotId]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown raw tool-call JSON in form bodies is quarantined for audit.          Tig]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When outbound text matches the banner, text is replaced but owner is NOT notifie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker is None, activity returns honest error, not silent empty.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_active_bot_id returns the constructor-injected default when no contextvar is se]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_trigger_web_search_log returns silently when egress_filter is None.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_845
SORT file.name ASC
```

## Connections to other communities
- 73 edges to [[_COMMUNITY_Community 626]]
- 68 edges to [[_COMMUNITY_Community 2]]
- 13 edges to [[_COMMUNITY_Community 84]]
- 10 edges to [[_COMMUNITY_Community 436]]
- 8 edges to [[_COMMUNITY_Community 1273]]
- 5 edges to [[_COMMUNITY_Community 1947]]
- 4 edges to [[_COMMUNITY_Community 2007]]
- 4 edges to [[_COMMUNITY_Community 2008]]
- 3 edges to [[_COMMUNITY_Community 99]]
- 3 edges to [[_COMMUNITY_Community 2054]]
- 2 edges to [[_COMMUNITY_Community 14]]
- 2 edges to [[_COMMUNITY_Community 2181]]
- 2 edges to [[_COMMUNITY_Community 1074]]
- 1 edge to [[_COMMUNITY_Community 2433]]
- 1 edge to [[_COMMUNITY_Community 1558]]
- 1 edge to [[_COMMUNITY_Community 2419]]
- 1 edge to [[_COMMUNITY_Community 2423]]
- 1 edge to [[_COMMUNITY_Community 2424]]
- 1 edge to [[_COMMUNITY_Community 2434]]
- 1 edge to [[_COMMUNITY_Community 1565]]
- 1 edge to [[_COMMUNITY_Community 2435]]
- 1 edge to [[_COMMUNITY_Community 1566]]
- 1 edge to [[_COMMUNITY_Community 2436]]
- 1 edge to [[_COMMUNITY_Community 2437]]
- 1 edge to [[_COMMUNITY_Community 2438]]
- 1 edge to [[_COMMUNITY_Community 2439]]
- 1 edge to [[_COMMUNITY_Community 2440]]
- 1 edge to [[_COMMUNITY_Community 1569]]
- 1 edge to [[_COMMUNITY_Community 2441]]
- 1 edge to [[_COMMUNITY_Community 2442]]
- 1 edge to [[_COMMUNITY_Community 2443]]
- 1 edge to [[_COMMUNITY_Community 2444]]
- 1 edge to [[_COMMUNITY_Community 2395]]
- 1 edge to [[_COMMUNITY_Community 2396]]
- 1 edge to [[_COMMUNITY_Community 2397]]
- 1 edge to [[_COMMUNITY_Community 2398]]
- 1 edge to [[_COMMUNITY_Community 2399]]
- 1 edge to [[_COMMUNITY_Community 2400]]
- 1 edge to [[_COMMUNITY_Community 2401]]
- 1 edge to [[_COMMUNITY_Community 2402]]
- 1 edge to [[_COMMUNITY_Community 2403]]
- 1 edge to [[_COMMUNITY_Community 2404]]
- 1 edge to [[_COMMUNITY_Community 2405]]
- 1 edge to [[_COMMUNITY_Community 2406]]
- 1 edge to [[_COMMUNITY_Community 2407]]
- 1 edge to [[_COMMUNITY_Community 2408]]
- 1 edge to [[_COMMUNITY_Community 2409]]
- 1 edge to [[_COMMUNITY_Community 2410]]
- 1 edge to [[_COMMUNITY_Community 2411]]
- 1 edge to [[_COMMUNITY_Community 2412]]
- 1 edge to [[_COMMUNITY_Community 2413]]
- 1 edge to [[_COMMUNITY_Community 2414]]
- 1 edge to [[_COMMUNITY_Community 2415]]
- 1 edge to [[_COMMUNITY_Community 2416]]
- 1 edge to [[_COMMUNITY_Community 1559]]
- 1 edge to [[_COMMUNITY_Community 1560]]
- 1 edge to [[_COMMUNITY_Community 2417]]
- 1 edge to [[_COMMUNITY_Community 2418]]
- 1 edge to [[_COMMUNITY_Community 2420]]
- 1 edge to [[_COMMUNITY_Community 1561]]
- 1 edge to [[_COMMUNITY_Community 2421]]
- 1 edge to [[_COMMUNITY_Community 2422]]
- 1 edge to [[_COMMUNITY_Community 1563]]
- 1 edge to [[_COMMUNITY_Community 2425]]
- 1 edge to [[_COMMUNITY_Community 2426]]
- 1 edge to [[_COMMUNITY_Community 2427]]
- 1 edge to [[_COMMUNITY_Community 2428]]
- 1 edge to [[_COMMUNITY_Community 2429]]
- 1 edge to [[_COMMUNITY_Community 2430]]
- 1 edge to [[_COMMUNITY_Community 2431]]
- 1 edge to [[_COMMUNITY_Community 2432]]
- 1 edge to [[_COMMUNITY_Community 889]]
- 1 edge to [[_COMMUNITY_Community 2009]]

## Top bridge nodes
- [[TelegramAPIProxy_3]] - degree 220, connects to 73 communities
- [[TestDefaultBotId]] - degree 9, connects to 3 communities
- [[.test_long_outbound_message_blocked_for_non_owner()]] - degree 4, connects to 2 communities
- [[.test_info_filter_redaction_escalates_to_block_for_non_owner()]] - degree 4, connects to 2 communities
- [[.test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten()]] - degree 4, connects to 2 communities