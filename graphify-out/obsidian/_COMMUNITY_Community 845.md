---
type: community
members: 64
---

# Community 845

**Members:** 64 nodes

## Members
- [[.test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_agent_failed_prefix_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_form_caption_tool_payload_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_legacy_block_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_not_authorized_command_text_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contextvar_takes_precedence_over_default()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_default_is_openclaw_when_not_injected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_pipeline_block_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_owner_id_redaction_continues_to_pipeline_scan()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_sandbox_cannot_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_injected_default_overrides_openclaw()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_without_content_type_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_embedding_provider_hint_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_slash_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_underscore_variant_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_ollama_auth_required_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pipeline_receives_trust_level()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_prefixed_model_sentence_is_rewritten_to_active_model_hint()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_allows_starting_then_online_sequence()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_delayed_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_system_startup_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_ip_host_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_non_http_scheme_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_search_json_owner_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_web_search_no_egress_filter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Cannot access' healthcheck SKILL.md sandbox wording should rewrite for form payl]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator agent-failed prefix should normalize to protected unavailable notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be blocked]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting notices should also be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider memory errors should also be rewritten for urlencoded payload]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form caption field should be filtered the same as textdraftmessage fields.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload auth-denial command text should map to protected scope notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Legacy bracket-style block notices should normalize to Protect wording.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Literal IP targets should not enter interactive domain approval flow.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from form bodies (parity with JSON).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Missing content-type must not bypass outbound JSON leak filtering.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-embedding memory errors should not be forced into embedding guidance text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-http schemes should never queue web-fetch approvals.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Ollama auth errors should map to concise operator guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound markdown exfil links should be stripped before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner chat raw web_search JSON produces 'Switch to tool-capable model' message.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner form messages still pass through when the pipeline crashes.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner-ID-redacted form text must still reach the pipeline scan.          Regress]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Partial model sentence variants should still be rewritten deterministically.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked form payloads to non-owners must be replaced with a safe notice]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Proxy should pass ownernon-owner trust level into outbound pipeline.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Slash-separated embeddingprovider wording should rewrite for form payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting and online notices are distinct and should both forward.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[System startup notice should be deduplicated in a short cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TelegramAPIProxy_3]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestDefaultBotId]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Underscore-delimited embedding_provider wording should still trigger rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
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
- 63 edges to [[_COMMUNITY_Community 626]]
- 59 edges to [[_COMMUNITY_Community 2]]
- 10 edges to [[_COMMUNITY_Community 99]]
- 10 edges to [[_COMMUNITY_Community 436]]
- 8 edges to [[_COMMUNITY_Community 1273]]
- 5 edges to [[_COMMUNITY_Community 1947]]
- 4 edges to [[_COMMUNITY_Community 7]]
- 4 edges to [[_COMMUNITY_Community 2007]]
- 4 edges to [[_COMMUNITY_Community 2008]]
- 3 edges to [[_COMMUNITY_Community 2054]]
- 2 edges to [[_COMMUNITY_Community 14]]
- 2 edges to [[_COMMUNITY_Community 2181]]
- 2 edges to [[_COMMUNITY_Community 2327]]
- 2 edges to [[_COMMUNITY_Community 1074]]
- 1 edge to [[_COMMUNITY_Community 1130]]
- 1 edge to [[_COMMUNITY_Community 2433]]
- 1 edge to [[_COMMUNITY_Community 2398]]
- 1 edge to [[_COMMUNITY_Community 2406]]
- 1 edge to [[_COMMUNITY_Community 2343]]
- 1 edge to [[_COMMUNITY_Community 2348]]
- 1 edge to [[_COMMUNITY_Community 2424]]
- 1 edge to [[_COMMUNITY_Community 2362]]
- 1 edge to [[_COMMUNITY_Community 2363]]
- 1 edge to [[_COMMUNITY_Community 2369]]
- 1 edge to [[_COMMUNITY_Community 2370]]
- 1 edge to [[_COMMUNITY_Community 2371]]
- 1 edge to [[_COMMUNITY_Community 1565]]
- 1 edge to [[_COMMUNITY_Community 2435]]
- 1 edge to [[_COMMUNITY_Community 2372]]
- 1 edge to [[_COMMUNITY_Community 1566]]
- 1 edge to [[_COMMUNITY_Community 2373]]
- 1 edge to [[_COMMUNITY_Community 2395]]
- 1 edge to [[_COMMUNITY_Community 2397]]
- 1 edge to [[_COMMUNITY_Community 2436]]
- 1 edge to [[_COMMUNITY_Community 2437]]
- 1 edge to [[_COMMUNITY_Community 2399]]
- 1 edge to [[_COMMUNITY_Community 2400]]
- 1 edge to [[_COMMUNITY_Community 2402]]
- 1 edge to [[_COMMUNITY_Community 2438]]
- 1 edge to [[_COMMUNITY_Community 2404]]
- 1 edge to [[_COMMUNITY_Community 2405]]
- 1 edge to [[_COMMUNITY_Community 2440]]
- 1 edge to [[_COMMUNITY_Community 1569]]
- 1 edge to [[_COMMUNITY_Community 2408]]
- 1 edge to [[_COMMUNITY_Community 2441]]
- 1 edge to [[_COMMUNITY_Community 2409]]
- 1 edge to [[_COMMUNITY_Community 2444]]
- 1 edge to [[_COMMUNITY_Community 2396]]
- 1 edge to [[_COMMUNITY_Community 2341]]
- 1 edge to [[_COMMUNITY_Community 2401]]
- 1 edge to [[_COMMUNITY_Community 2342]]
- 1 edge to [[_COMMUNITY_Community 2344]]
- 1 edge to [[_COMMUNITY_Community 2403]]
- 1 edge to [[_COMMUNITY_Community 2345]]
- 1 edge to [[_COMMUNITY_Community 2407]]
- 1 edge to [[_COMMUNITY_Community 2412]]
- 1 edge to [[_COMMUNITY_Community 2346]]
- 1 edge to [[_COMMUNITY_Community 2347]]
- 1 edge to [[_COMMUNITY_Community 2416]]
- 1 edge to [[_COMMUNITY_Community 2349]]
- 1 edge to [[_COMMUNITY_Community 2350]]
- 1 edge to [[_COMMUNITY_Community 2351]]
- 1 edge to [[_COMMUNITY_Community 1559]]
- 1 edge to [[_COMMUNITY_Community 1560]]
- 1 edge to [[_COMMUNITY_Community 2352]]
- 1 edge to [[_COMMUNITY_Community 2353]]
- 1 edge to [[_COMMUNITY_Community 1561]]
- 1 edge to [[_COMMUNITY_Community 2354]]
- 1 edge to [[_COMMUNITY_Community 2355]]
- 1 edge to [[_COMMUNITY_Community 2356]]
- 1 edge to [[_COMMUNITY_Community 2357]]
- 1 edge to [[_COMMUNITY_Community 1563]]
- 1 edge to [[_COMMUNITY_Community 2358]]
- 1 edge to [[_COMMUNITY_Community 2359]]
- 1 edge to [[_COMMUNITY_Community 2360]]
- 1 edge to [[_COMMUNITY_Community 2361]]
- 1 edge to [[_COMMUNITY_Community 2425]]
- 1 edge to [[_COMMUNITY_Community 2426]]
- 1 edge to [[_COMMUNITY_Community 2430]]
- 1 edge to [[_COMMUNITY_Community 2431]]
- 1 edge to [[_COMMUNITY_Community 2432]]
- 1 edge to [[_COMMUNITY_Community 2364]]
- 1 edge to [[_COMMUNITY_Community 2365]]
- 1 edge to [[_COMMUNITY_Community 2366]]
- 1 edge to [[_COMMUNITY_Community 2367]]
- 1 edge to [[_COMMUNITY_Community 2368]]
- 1 edge to [[_COMMUNITY_Community 889]]
- 1 edge to [[_COMMUNITY_Community 2325]]

## Top bridge nodes
- [[TelegramAPIProxy_3]] - degree 220, connects to 87 communities
- [[TestDefaultBotId]] - degree 9, connects to 3 communities
- [[.test_form_outbound_pipeline_block_non_owner()]] - degree 5, connects to 3 communities
- [[.test_outbound_fails_closed_for_non_owner()]] - degree 4, connects to 2 communities
- [[.test_form_outbound_owner_exempt_from_fail_closed()]] - degree 4, connects to 2 communities