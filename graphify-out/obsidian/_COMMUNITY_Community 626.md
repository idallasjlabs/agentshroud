---
type: community
members: 67
---

# Community 626

**Members:** 67 nodes

## Members
- [[.test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_caption_tool_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_egress_approval_banner_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_form_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_pairing_code_leakage_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_embedded_web_fetch_json_queues_approval_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_fail_closed_replaces_caption_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_unknown_tool_call_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_content()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_draft()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_sandbox_error_variant_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_caption_pipeline_block_replaces_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_caption_sanitized_in_place()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_long_outbound_message_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_error_keyword_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_hyphen_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_form_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_json_draft_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_variant_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_with_punctuation_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_sends_no_reply_wait_message_once()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_approval_prunes_expired_cooldown_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_percent_encoded_control_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_trailing_backtick_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_trailing_quote_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_search_json_collaborator_safe_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_log_called_with_correct_params()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_query_truncation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Caption-only payloads should not bypass collaborator leak normalization.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator chat raw web_search JSON produces a safe notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payload with raw toolfile leakage markers should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should not receive internal egress approval banners.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should receive protected unavailable notice for timeout rewrite va]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Cooldown cache should prune expired entries when size exceeds threshold.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a PIISanitizer with default enforce config.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embedded web_fetch JSON should still queue interactive egress approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Fail-closed substitution must target the resolved text field.          Regressio]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First NO_REPLY payload should send safe wait guidance to Telegram.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form content should keep healthcheck sandbox text unchanged when SKILL.md marker]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form draft should keep healthcheck sandbox text unchanged when SKILL.md marker i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload embeddingprovider hints without 'error' should keep original text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payloads containing pairing secrets must be blocked for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL messages without sandbox context should not trigger sandbox re]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Hyphen-separated embedding-provider wording should rewrite for form payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If the pipeline crashes on a form payload, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory provider runtime errors should rewrite when form payload uses caption fie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Messages above hard size cap should be blocked to prevent split bypass.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[NO_REPLY wrapped with punctuation should still be normalized.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Percent-encoded control bytes should be rejected before queueing approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked caption payloads must have the caption replaced.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-sanitized sendPhoto captions must replace the caption itself.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Queries longer than 200 chars are truncated in the SOC log reason.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Runtime memory provider errors should rewrite when payload uses draft field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Trailing markdown backtick in leaked URL should normalize for approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Trailing quote punctuation in leaked URL should still normalize and queue approv]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown raw tool-call JSON in form bodies is quarantined for audit.          Tig]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Variant wording should still map to generic runtime guidance by default.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Wording variants for healthcheck SKILL.md sandbox errors should be rewritten.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_sanitizer()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[_trigger_web_search_log calls log_external_decision with Brave domain and query.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_626
SORT file.name ASC
```

## Connections to other communities
- 63 edges to [[_COMMUNITY_Community 845]]
- 57 edges to [[_COMMUNITY_Community 2]]
- 13 edges to [[_COMMUNITY_Community 99]]
- 10 edges to [[_COMMUNITY_Community 436]]
- 8 edges to [[_COMMUNITY_Community 1273]]
- 5 edges to [[_COMMUNITY_Community 1947]]
- 4 edges to [[_COMMUNITY_Community 2007]]
- 4 edges to [[_COMMUNITY_Community 2008]]
- 4 edges to [[_COMMUNITY_Community 889]]
- 3 edges to [[_COMMUNITY_Community 2054]]
- 2 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 1074]]
- 2 edges to [[_COMMUNITY_Community 2327]]
- 2 edges to [[_COMMUNITY_Community 2181]]
- 1 edge to [[_COMMUNITY_Community 1130]]
- 1 edge to [[_COMMUNITY_Community 2405]]
- 1 edge to [[_COMMUNITY_Community 2369]]
- 1 edge to [[_COMMUNITY_Community 2341]]
- 1 edge to [[_COMMUNITY_Community 2351]]
- 1 edge to [[_COMMUNITY_Community 2399]]
- 1 edge to [[_COMMUNITY_Community 2436]]
- 1 edge to [[_COMMUNITY_Community 2437]]
- 1 edge to [[_COMMUNITY_Community 2404]]
- 1 edge to [[_COMMUNITY_Community 2396]]
- 1 edge to [[_COMMUNITY_Community 2397]]
- 1 edge to [[_COMMUNITY_Community 2400]]
- 1 edge to [[_COMMUNITY_Community 2354]]
- 1 edge to [[_COMMUNITY_Community 2424]]
- 1 edge to [[_COMMUNITY_Community 2348]]
- 1 edge to [[_COMMUNITY_Community 2373]]
- 1 edge to [[_COMMUNITY_Community 2401]]
- 1 edge to [[_COMMUNITY_Community 2412]]
- 1 edge to [[_COMMUNITY_Community 2342]]
- 1 edge to [[_COMMUNITY_Community 2350]]
- 1 edge to [[_COMMUNITY_Community 2363]]
- 1 edge to [[_COMMUNITY_Community 2438]]
- 1 edge to [[_COMMUNITY_Community 2362]]
- 1 edge to [[_COMMUNITY_Community 2407]]
- 1 edge to [[_COMMUNITY_Community 2344]]
- 1 edge to [[_COMMUNITY_Community 2403]]
- 1 edge to [[_COMMUNITY_Community 2444]]
- 1 edge to [[_COMMUNITY_Community 2408]]
- 1 edge to [[_COMMUNITY_Community 2409]]
- 1 edge to [[_COMMUNITY_Community 1565]]
- 1 edge to [[_COMMUNITY_Community 2343]]
- 1 edge to [[_COMMUNITY_Community 2406]]
- 1 edge to [[_COMMUNITY_Community 2433]]
- 1 edge to [[_COMMUNITY_Community 2372]]
- 1 edge to [[_COMMUNITY_Community 1566]]
- 1 edge to [[_COMMUNITY_Community 2435]]
- 1 edge to [[_COMMUNITY_Community 1561]]
- 1 edge to [[_COMMUNITY_Community 2352]]
- 1 edge to [[_COMMUNITY_Community 1559]]
- 1 edge to [[_COMMUNITY_Community 2353]]
- 1 edge to [[_COMMUNITY_Community 1560]]
- 1 edge to [[_COMMUNITY_Community 2370]]
- 1 edge to [[_COMMUNITY_Community 2371]]
- 1 edge to [[_COMMUNITY_Community 2356]]
- 1 edge to [[_COMMUNITY_Community 2357]]
- 1 edge to [[_COMMUNITY_Community 1563]]
- 1 edge to [[_COMMUNITY_Community 2360]]
- 1 edge to [[_COMMUNITY_Community 2361]]
- 1 edge to [[_COMMUNITY_Community 2359]]
- 1 edge to [[_COMMUNITY_Community 2358]]
- 1 edge to [[_COMMUNITY_Community 2431]]
- 1 edge to [[_COMMUNITY_Community 2430]]
- 1 edge to [[_COMMUNITY_Community 2364]]
- 1 edge to [[_COMMUNITY_Community 2365]]
- 1 edge to [[_COMMUNITY_Community 2432]]
- 1 edge to [[_COMMUNITY_Community 2366]]
- 1 edge to [[_COMMUNITY_Community 2355]]
- 1 edge to [[_COMMUNITY_Community 2368]]
- 1 edge to [[_COMMUNITY_Community 2367]]
- 1 edge to [[_COMMUNITY_Community 2426]]
- 1 edge to [[_COMMUNITY_Community 2425]]
- 1 edge to [[_COMMUNITY_Community 2441]]
- 1 edge to [[_COMMUNITY_Community 2395]]
- 1 edge to [[_COMMUNITY_Community 2345]]
- 1 edge to [[_COMMUNITY_Community 2398]]
- 1 edge to [[_COMMUNITY_Community 2440]]
- 1 edge to [[_COMMUNITY_Community 1569]]
- 1 edge to [[_COMMUNITY_Community 2402]]
- 1 edge to [[_COMMUNITY_Community 2349]]
- 1 edge to [[_COMMUNITY_Community 2346]]
- 1 edge to [[_COMMUNITY_Community 2347]]
- 1 edge to [[_COMMUNITY_Community 2416]]
- 1 edge to [[_COMMUNITY_Community 2325]]

## Top bridge nodes
- [[_make_sanitizer()]] - degree 218, connects to 86 communities
- [[.test_json_caption_pipeline_block_replaces_caption()]] - degree 5, connects to 3 communities
- [[.test_form_outbound_fails_closed_for_non_owner()]] - degree 4, connects to 2 communities
- [[.test_long_outbound_message_blocked_for_non_owner()]] - degree 4, connects to 2 communities
- [[.test_plain_no_reply_token_with_punctuation_is_rewritten()]] - degree 4, connects to 2 communities