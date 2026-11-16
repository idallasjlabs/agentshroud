---
type: community
members: 82
---

# Community 626

**Members:** 82 nodes

## Members
- [[.test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_access_not_configured_user_id_leakage_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_caption_tool_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_legacy_block_notice_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_not_authorized_command_text_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contextvar_takes_precedence_over_default()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_default_is_openclaw_when_not_injected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_embedded_tool_call_json_is_removed_from_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_fail_closed_replaces_caption_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_pipeline_sanitized_text_applied()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_forward_to_telegram_handles_http_error_non_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_draft()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_html_parse_mode_preserved_without_redaction_placeholders()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_info_filter_redaction_escalates_to_block_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_injected_default_overrides_openclaw()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_caption_pipeline_block_replaces_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_caption_sanitized_in_place()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_long_outbound_message_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_error_keyword_is_not_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_no_reply_tool_token_is_rewritten_to_wait_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_outbound_pipeline_called_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pipeline_receives_trust_level()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_for_collaborator_gets_protected_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_delayed_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_explicit_md_tld_domain_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_filename_reference_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_ip_host_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_is_rewritten_to_actionable_guidance()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_scheme_relative_url_queues_https_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_percent_encoded_control_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_search_json_collaborator_safe_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_ssn_redacted_on_outbound()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_collaborator_no_reply_gets_protected_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_draft_payload_tool_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_log_called_with_correct_params()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_query_truncation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Any outbound info-filter redaction should be blocked for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Caption-only payloads should not bypass collaborator leak normalization.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator chat raw web_search JSON produces a safe notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payloads should get protected notice, not suppression.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be blocked]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator plain NO_REPLY should become protected unavailable notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting notices should also be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider memory errors should also be rewritten for urlencoded payload]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Explicitly schemed domains should still queue approvals even for .md ccTLD.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Fail-closed substitution must target the resolved text field.          Regressio]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Filename-like references must not be interpreted as egress domains.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form draft should keep healthcheck sandbox text unchanged when SKILL.md marker i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload auth-denial command text should map to protected scope notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload legacy notices should normalize to Protect wording.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload user-id enrollment leakage should also be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form-encoded draft payloads must not leak raw tool-call JSON.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck sandbox messages without SKILL.md marker should not trigger rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If tool-call JSON is embedded in prose, strip JSON block before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field with embeddingprovider hints but no error keyword should rem]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Literal IP targets should not enter interactive domain approval flow.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Messages above hard size cap should be blocked to prevent split bypass.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[NO_REPLY tool JSON should be converted into a user-safe wait message.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-JSON HTTPError payloads should still produce a safe fallback dict.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound markdown exfil links should be stripped before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner HTML formatting should preserve parse_mode.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Percent-encoded control bytes should be rejected before queueing approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked caption payloads must have the caption replaced.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-sanitized sendPhoto captions must replace the caption itself.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-sanitized text must replace the original in form payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Proxy should pass ownernon-owner trust level into outbound pipeline.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pure web_fetch tool-call JSON should be rewritten to user guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Queries longer than 200 chars are truncated in the SOC log reason.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[SSN in outbound messages must be redacted.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Scheme-relative URLs in leaked JSON should normalize to HTTPS approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TelegramAPIProxy_3]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestDefaultBotId]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[When pipeline is set, process_outbound must be called on outbound messages.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker is None, activity returns honest error, not silent empty.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_active_bot_id returns the constructor-injected default when no contextvar is se]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_trigger_web_search_log calls log_external_decision with Brave domain and query.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_626
SORT file.name ASC
```

## Connections to other communities
- 77 edges to [[_COMMUNITY_Community 845]]
- 75 edges to [[_COMMUNITY_Community 2]]
- 12 edges to [[_COMMUNITY_Community 84]]
- 10 edges to [[_COMMUNITY_Community 436]]
- 8 edges to [[_COMMUNITY_Community 1273]]
- 5 edges to [[_COMMUNITY_Community 1947]]
- 4 edges to [[_COMMUNITY_Community 2007]]
- 4 edges to [[_COMMUNITY_Community 2008]]
- 3 edges to [[_COMMUNITY_Community 2054]]
- 2 edges to [[_COMMUNITY_Community 14]]
- 2 edges to [[_COMMUNITY_Community 329]]
- 2 edges to [[_COMMUNITY_Community 2181]]
- 2 edges to [[_COMMUNITY_Community 2327]]
- 2 edges to [[_COMMUNITY_Community 1074]]
- 1 edge to [[_COMMUNITY_Community 1130]]
- 1 edge to [[_COMMUNITY_Community 2369]]
- 1 edge to [[_COMMUNITY_Community 2398]]
- 1 edge to [[_COMMUNITY_Community 2409]]
- 1 edge to [[_COMMUNITY_Community 2413]]
- 1 edge to [[_COMMUNITY_Community 2414]]
- 1 edge to [[_COMMUNITY_Community 2415]]
- 1 edge to [[_COMMUNITY_Community 2416]]
- 1 edge to [[_COMMUNITY_Community 2417]]
- 1 edge to [[_COMMUNITY_Community 2418]]
- 1 edge to [[_COMMUNITY_Community 2419]]
- 1 edge to [[_COMMUNITY_Community 2420]]
- 1 edge to [[_COMMUNITY_Community 2421]]
- 1 edge to [[_COMMUNITY_Community 2422]]
- 1 edge to [[_COMMUNITY_Community 2423]]
- 1 edge to [[_COMMUNITY_Community 2424]]
- 1 edge to [[_COMMUNITY_Community 2425]]
- 1 edge to [[_COMMUNITY_Community 2357]]
- 1 edge to [[_COMMUNITY_Community 2358]]
- 1 edge to [[_COMMUNITY_Community 2359]]
- 1 edge to [[_COMMUNITY_Community 2360]]
- 1 edge to [[_COMMUNITY_Community 2361]]
- 1 edge to [[_COMMUNITY_Community 2362]]
- 1 edge to [[_COMMUNITY_Community 2363]]
- 1 edge to [[_COMMUNITY_Community 2364]]
- 1 edge to [[_COMMUNITY_Community 2365]]
- 1 edge to [[_COMMUNITY_Community 2366]]
- 1 edge to [[_COMMUNITY_Community 2367]]
- 1 edge to [[_COMMUNITY_Community 2368]]
- 1 edge to [[_COMMUNITY_Community 2370]]
- 1 edge to [[_COMMUNITY_Community 2371]]
- 1 edge to [[_COMMUNITY_Community 2372]]
- 1 edge to [[_COMMUNITY_Community 2373]]
- 1 edge to [[_COMMUNITY_Community 2395]]
- 1 edge to [[_COMMUNITY_Community 2396]]
- 1 edge to [[_COMMUNITY_Community 2397]]
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
- 1 edge to [[_COMMUNITY_Community 2410]]
- 1 edge to [[_COMMUNITY_Community 2411]]
- 1 edge to [[_COMMUNITY_Community 2412]]
- 1 edge to [[_COMMUNITY_Community 889]]
- 1 edge to [[_COMMUNITY_Community 2062]]
- 1 edge to [[_COMMUNITY_Community 1565]]

## Top bridge nodes
- [[TelegramAPIProxy_3]] - degree 220, connects to 65 communities
- [[TestDefaultBotId]] - degree 9, connects to 3 communities
- [[.test_json_caption_pipeline_block_replaces_caption()]] - degree 5, connects to 3 communities
- [[.test_ssn_redacted_on_outbound()]] - degree 4, connects to 2 communities
- [[.test_outbound_pipeline_called_when_available()]] - degree 4, connects to 2 communities