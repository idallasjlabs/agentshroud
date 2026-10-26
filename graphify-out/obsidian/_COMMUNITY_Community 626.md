---
type: community
members: 75
---

# Community 626

**Members:** 75 nodes

## Members
- [[.test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_egress_approval_banner_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_form_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_internal_tool_output_suppressed_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_owner_id_redaction_continues_to_pipeline_scan()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_generic_sessions_spawn_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sessions_spawn_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_sandbox_cannot_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_html_parse_mode_removed_for_redaction_placeholders()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_caption_pipeline_block_replaces_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_caption_sanitized_in_place()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_error_keyword_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_json_draft_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_outbound_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_outbound_pipeline_called_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_with_punctuation_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_system_startup_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_starting_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_startup_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_filename_reference_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_ip_host_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_overlong_fqdn_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_punycode_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_queues_egress_approval_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_uppercase_http_scheme_queues_port_80_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_userinfo_url_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_session_lock_error_is_sanitized_for_users()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_unknown_model_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_log_called_with_correct_params()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Cannot access' healthcheck SKILL.md sandbox wording should rewrite for form payl]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payload with raw toolfile leakage markers should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Consecutive-dot domains should be rejected before approval queueing.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a PIISanitizer with default enforce config.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Domains over 253 chars should be rejected before queueing approvals.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider hints without explicit error marker should not trigger rewrit]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Filename-like references must not be interpreted as egress domains.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload approval banners must be redacted for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload timeout rewrites should also map to protected unavailable notice fo]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Generic session spawn JSON should be rewritten, not shown raw.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck tool-call JSON should be rewritten to friendly status text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, owner messages should still go through.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Internal session lock errors should be rewritten to safe user guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Legacy internal tool-output suppression string should normalize to Protect wordi]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Literal IP targets should not enter interactive domain approval flow.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Malformed domain labels should be rejected before approval queueing.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from form bodies (parity with JSON).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[NO_REPLY wrapped with punctuation should still be normalized.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound markdown exfil links should be stripped before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner-ID-redacted form text must still reach the pipeline scan.          Regress]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked caption payloads must have the caption replaced.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-sanitized sendPhoto captions must replace the caption itself.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[PunycodeIDN domains should be rejected from approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw web_fetch JSON should queue interactive egress approval for the destination.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Redaction placeholder tokens should be HTML-escaped, not strip         parse_mod]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Runtime memory provider errors should rewrite when payload uses draft field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting notice dedupe should tolerate emoji variation drift.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Startup notice dedupe should tolerate emoji variation drift.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[System startup notice should be deduplicated in a short cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[URLs with credentials should not be queued for web-fetch approvals.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown model errors should be rewritten without leaking raw stack text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Uppercase HTTP schemes should normalize and queue on port 80.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When pipeline is set, process_outbound must be called on outbound messages.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_sanitizer()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_trigger_web_search_log calls log_external_decision with Brave domain and query.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_626
SORT file.name ASC
```

## Connections to other communities
- 73 edges to [[_COMMUNITY_Community 845]]
- 68 edges to [[_COMMUNITY_Community 2]]
- 12 edges to [[_COMMUNITY_Community 84]]
- 10 edges to [[_COMMUNITY_Community 436]]
- 8 edges to [[_COMMUNITY_Community 1273]]
- 5 edges to [[_COMMUNITY_Community 1947]]
- 4 edges to [[_COMMUNITY_Community 2007]]
- 4 edges to [[_COMMUNITY_Community 2008]]
- 4 edges to [[_COMMUNITY_Community 889]]
- 3 edges to [[_COMMUNITY_Community 2054]]
- 2 edges to [[_COMMUNITY_Community 1074]]
- 2 edges to [[_COMMUNITY_Community 2181]]
- 1 edge to [[_COMMUNITY_Community 1130]]
- 1 edge to [[_COMMUNITY_Community 2400]]
- 1 edge to [[_COMMUNITY_Community 2397]]
- 1 edge to [[_COMMUNITY_Community 2436]]
- 1 edge to [[_COMMUNITY_Community 2437]]
- 1 edge to [[_COMMUNITY_Community 2439]]
- 1 edge to [[_COMMUNITY_Community 2396]]
- 1 edge to [[_COMMUNITY_Community 2399]]
- 1 edge to [[_COMMUNITY_Community 2398]]
- 1 edge to [[_COMMUNITY_Community 2422]]
- 1 edge to [[_COMMUNITY_Community 2419]]
- 1 edge to [[_COMMUNITY_Community 2424]]
- 1 edge to [[_COMMUNITY_Community 2423]]
- 1 edge to [[_COMMUNITY_Community 1558]]
- 1 edge to [[_COMMUNITY_Community 2421]]
- 1 edge to [[_COMMUNITY_Community 2405]]
- 1 edge to [[_COMMUNITY_Community 2410]]
- 1 edge to [[_COMMUNITY_Community 2411]]
- 1 edge to [[_COMMUNITY_Community 2404]]
- 1 edge to [[_COMMUNITY_Community 2406]]
- 1 edge to [[_COMMUNITY_Community 2401]]
- 1 edge to [[_COMMUNITY_Community 2412]]
- 1 edge to [[_COMMUNITY_Community 2415]]
- 1 edge to [[_COMMUNITY_Community 2438]]
- 1 edge to [[_COMMUNITY_Community 2402]]
- 1 edge to [[_COMMUNITY_Community 2407]]
- 1 edge to [[_COMMUNITY_Community 2408]]
- 1 edge to [[_COMMUNITY_Community 2403]]
- 1 edge to [[_COMMUNITY_Community 2444]]
- 1 edge to [[_COMMUNITY_Community 2413]]
- 1 edge to [[_COMMUNITY_Community 2395]]
- 1 edge to [[_COMMUNITY_Community 1565]]
- 1 edge to [[_COMMUNITY_Community 2414]]
- 1 edge to [[_COMMUNITY_Community 2433]]
- 1 edge to [[_COMMUNITY_Community 2434]]
- 1 edge to [[_COMMUNITY_Community 1566]]
- 1 edge to [[_COMMUNITY_Community 2435]]
- 1 edge to [[_COMMUNITY_Community 2443]]
- 1 edge to [[_COMMUNITY_Community 1561]]
- 1 edge to [[_COMMUNITY_Community 2418]]
- 1 edge to [[_COMMUNITY_Community 1559]]
- 1 edge to [[_COMMUNITY_Community 2420]]
- 1 edge to [[_COMMUNITY_Community 2417]]
- 1 edge to [[_COMMUNITY_Community 1560]]
- 1 edge to [[_COMMUNITY_Community 1563]]
- 1 edge to [[_COMMUNITY_Community 2431]]
- 1 edge to [[_COMMUNITY_Community 2429]]
- 1 edge to [[_COMMUNITY_Community 2430]]
- 1 edge to [[_COMMUNITY_Community 2432]]
- 1 edge to [[_COMMUNITY_Community 2426]]
- 1 edge to [[_COMMUNITY_Community 2425]]
- 1 edge to [[_COMMUNITY_Community 2427]]
- 1 edge to [[_COMMUNITY_Community 2428]]
- 1 edge to [[_COMMUNITY_Community 2441]]
- 1 edge to [[_COMMUNITY_Community 2409]]
- 1 edge to [[_COMMUNITY_Community 2440]]
- 1 edge to [[_COMMUNITY_Community 1569]]
- 1 edge to [[_COMMUNITY_Community 2442]]
- 1 edge to [[_COMMUNITY_Community 2416]]
- 1 edge to [[_COMMUNITY_Community 2009]]
- 1 edge to [[_COMMUNITY_Community 99]]

## Top bridge nodes
- [[_make_sanitizer()]] - degree 218, connects to 72 communities
- [[.test_json_caption_pipeline_block_replaces_caption()]] - degree 5, connects to 3 communities
- [[.test_proxy_request_suppresses_startup_notice_emoji_variants()]] - degree 5, connects to 2 communities
- [[.test_outbound_pipeline_called_when_available()]] - degree 4, connects to 2 communities
- [[.test_outbound_fails_closed_for_non_owner()]] - degree 4, connects to 2 communities