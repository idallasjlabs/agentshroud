---
type: community
members: 76
---

# Community 2

**Members:** 76 nodes

## Members
- [[.test_collaborator_access_not_configured_user_id_leakage_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_agent_failed_prefix_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_egress_approval_banner_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_internal_tool_output_suppressed_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_legacy_protected_prefix_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_pairing_code_leakage_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_security_monitoring_threshold_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_pipeline_called_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_payload_with_draft_field_is_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_forward_to_telegram_handles_http_error_non_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_forward_to_telegram_returns_http_error_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_generic_sessions_spawn_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_html_parse_mode_preserved_without_redaction_placeholders()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_error_keyword_is_not_rewritten_for_form_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_case_variant_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_guidance_phrase_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_ollama_tools_unsupported_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_invalid_host_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_is_rewritten_to_actionable_guidance()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_html_entity_domain_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_whitespace_queues_approval_using_first_token()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_userinfo_url_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_sanitize_reason_hides_internal_paths()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_truncated_model_sentence_is_rewritten_to_active_model_hint()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should never receive pairing codes or pairing approval commands.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embedding provider wording variants should rewrite for urlencoded payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form caption should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message field with embeddingprovider hints but no error keyword should rem]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep healthcheck SKILL.md text unchanged when sandbox hint i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload agent-failed prefix should normalize to protected unavailable notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload approval banners must be redacted for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload healthcheck SKILL text without sandbox context should keep original]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload legacy 'Protected' wording should normalize to canonical protected]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload user-id enrollment leakage should also be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload using draft field should still suppress tool-call JSON.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form-encoded sendMessage bodies must also be scanned by the pipeline.          R]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Generic session spawn JSON should be rewritten, not shown raw.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[HTML-entity encoded domains in leaked JSON should normalize before approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[HTTPError JSON payloads should be returned as structured API responses.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck sandbox messages without SKILL.md marker should not trigger rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep healthcheck SKILL.md text unchanged when sandbox]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Legacy internal tool-output suppression string should normalize to Protect wordi]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Malformed domain labels should be rejected before approval queueing.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory guidance mentioning agents.defaults.memorySearch.provider should normaliz]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory provider runtime errors should rewrite when payload uses message field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Mixed-case wording variants should still trigger generic runtime guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Multiline fenced NO_REPLY token should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-JSON HTTPError payloads should still produce a safe fallback dict.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-domain hosts should not queue egress approval requests.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner HTML formatting should preserve parse_mode.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pure web_fetch tool-call JSON should be rewritten to user guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw model capability errors should be rewritten to actionable guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Repeated identical web_fetch leaks should not spam approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Sandbox SKILL.md messages must include healthcheck context before rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting notices should be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundPipelineIntegration]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests that _filter_outbound calls the full security pipeline.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Threshold status disclosures should normalize to collaborator policy-block notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Truncated 'current model' replies should be rewritten to deterministic model hin]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[URLs with credentials should not be queued for web-fetch approvals.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[User-facing block reasons should not expose modules or file paths.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Whitespace in leaked URL should queue approval using first URL token.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_2
SORT file.name ASC
```

## Connections to other communities
- 59 edges to [[_COMMUNITY_Community 845]]
- 57 edges to [[_COMMUNITY_Community 626]]
- 8 edges to [[_COMMUNITY_Community 1273]]
- 5 edges to [[_COMMUNITY_Community 1947]]
- 4 edges to [[_COMMUNITY_Community 2007]]
- 4 edges to [[_COMMUNITY_Community 2008]]
- 3 edges to [[_COMMUNITY_Community 2054]]
- 2 edges to [[_COMMUNITY_Community 7]]
- 2 edges to [[_COMMUNITY_Community 99]]
- 2 edges to [[_COMMUNITY_Community 2327]]
- 2 edges to [[_COMMUNITY_Community 2181]]
- 1 edge to [[_COMMUNITY_Community 63]]
- 1 edge to [[_COMMUNITY_Community 14]]
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

## Top bridge nodes
- [[TestOutboundPipelineIntegration]] - degree 189, connects to 84 communities
- [[.test_form_outbound_pipeline_called_when_available()]] - degree 4, connects to 2 communities
- [[.test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten()]] - degree 4, connects to 2 communities
- [[.test_generic_sessions_spawn_json_is_rewritten()]] - degree 4, connects to 2 communities
- [[.test_collaborator_agent_failed_prefix_is_normalized_form()]] - degree 4, connects to 2 communities