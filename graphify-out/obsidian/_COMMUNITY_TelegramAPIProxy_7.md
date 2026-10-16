---
type: community
cohesion: 0.03
members: 61
---

# TelegramAPIProxy

**Cohesion:** 0.03 - loosely connected
**Members:** 61 nodes

## Members
- [[dot-test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_legacy_protected_prefix_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_pairing_code_leakage_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_llm_timeout_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_long_outbound_message_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_error_without_error_keyword_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_variant_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_plain_no_reply_token_for_collaborator_gets_protected_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_plain_no_reply_token_with_punctuation_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_allows_delayed_starting_then_online_sequence()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_duplicate_no_reply_messages_return_deterministic_reply()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_sends_no_reply_wait_message_once()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_suppresses_duplicate_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_approval_queue_is_cooldown_deduped()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_approval_strips_trailing_punctuation()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_invalid_host_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_numeric_tld_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_runtime_profile_memory_error_text_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_collaborator_no_reply_gets_protected_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_plain_no_reply_with_punctuation_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payloads should get protected notice, not suppression.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator plain NO_REPLY should become protected unavailable notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should never receive pairing codes or pairing approval commands.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should receive protected unavailable notice for timeout rewrite va]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a PIISanitizer with default enforce config.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting and online notices are distinct and should both forward.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Domains with numeric TLDs should not enter approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embedding provider wording variants should rewrite for urlencoded payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First NO_REPLY payload should send safe wait guidance to Telegram.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload NO_REPLY punctuation variant should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload embeddingprovider hints without 'error' should keep original text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload healthcheck SKILL text without sandbox context should keep original]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload legacy 'Protected' wording should normalize to canonical protected]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck sandbox messages without SKILL.md marker should not trigger rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep healthcheck SKILL.md text unchanged when sandbox]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Messages above hard size cap should be blocked to prevent split bypass.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[NO_REPLY wrapped with punctuation should still be normalized.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-domain hosts should not queue egress approval requests.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Outbound markdown exfil links should be stripped before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Previously emitted runtime-profile memory text should be normalized to generic g]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw timeout errors should be rewritten to deterministic retry guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Repeated NO_REPLY payloads should still return deterministic non-empty replies.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Repeated identical web_fetch leaks should not spam approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting notices should be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Trailing punctuation in leaked URL should be normalized before approval check.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Variant wording should still map to generic runtime guidance by default.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When outbound text matches the banner, text is replaced but owner is NOT notifie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker is None, activity returns honest error, not silent empty.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_sanitizer()]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TelegramAPIProxy
SORT file.name ASC
```

## Connections to other communities
- 60 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 57 edges to [[_COMMUNITY_ApprovalQueueConfig_5]]
- 9 edges to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 8 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 7 edges to [[_COMMUNITY_TestMultipartOutboundPipeline_1]]
- 5 edges to [[_COMMUNITY_TestWebSearchLog]]
- 4 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 4 edges to [[_COMMUNITY_TestPathIsolationManager_2]]
- 2 edges to [[_COMMUNITY_TestForwardToTelegramTimeouts]]
- 2 edges to [[_COMMUNITY_dot-test_proxy_request_suppresses_starting_notice_emoji_variants]]
- 2 edges to [[_COMMUNITY_dot-test_urlencoded_without_content_type_caption_is_still_filtered]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_5]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_6]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_dot-test_agent_failed_timeout_error_is_sanitized]]
- 1 edge to [[_COMMUNITY_dot-test_block_cascade_blocks_followup_fragment]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_access_not_configured_user_id_leakage_is_redacted_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_caption_tool_payload_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_egress_approval_banner_is_redacted_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_egress_approval_banner_is_redacted_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_form_caption_tool_payload_is_normalized]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_html_code_markup_is_stripped_and_parse_mode_removed]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_internal_tool_output_suppressed_notice_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_internal_tool_output_suppressed_notice_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_block_notice_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_protected_prefix_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_not_authorized_command_text_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_pairing_code_leakage_is_redacted_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_security_monitoring_threshold_notice_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_security_monitoring_threshold_notice_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_embedded_web_fetch_json_queues_approval_when_available]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_fails_closed_for_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_overlength_blocked_for_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_owner_exempt_from_fail_closed]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_pipeline_block_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_form_payload_with_draft_field_is_filtered]]
- 1 edge to [[_COMMUNITY_dot-test_generic_sessions_spawn_json_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_form_message]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_sandbox_cannot_variant_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_sandbox_error_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_sandbox_error_variant_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_html_parse_mode_preserved_without_redaction_placeholders]]
- 1 edge to [[_COMMUNITY_dot-test_json_without_content_type_is_still_filtered]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_embedding_provider_hint_is_not_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_embedding_provider_hint_is_not_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_error_keyword_is_not_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_error_keyword_is_not_rewritten_for_json_message_field]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_case_variant_is_rewritten_generic]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_hyphen_variant_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_hyphen_variant_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_for_json_draft_field]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_to_generic_runtime_guidance]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_slash_variant_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_underscore_variant_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_with_explicit_memory_command_keeps_memory_guidance]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_13]]
- 1 edge to [[_COMMUNITY_dot-test_ollama_tools_unsupported_error_is_sanitized]]
- 1 edge to [[_COMMUNITY_dot-test_outbound_owner_exempt_from_fail_closed]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_16]]
- 1 edge to [[_COMMUNITY_dot-test_pipeline_receives_trust_level]]
- 1 edge to [[_COMMUNITY_dot-test_plain_no_reply_token_in_markdown_fence_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_plain_no_reply_token_is_rewritten_to_wait_message]]
- 1 edge to [[_COMMUNITY_dot-test_proxy_request_allows_distinct_system_notices]]
- 1 edge to [[_COMMUNITY_dot-test_proxy_request_allows_starting_then_online_sequence]]
- 1 edge to [[_COMMUNITY_dot-test_proxy_request_suppresses_duplicate_delayed_starting_notice]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_12]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_cooldown_is_scheme_port_scoped]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_prunes_expired_cooldown_entries]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_domain_with_invalid_chars_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_filename_reference_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_10]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_9]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_non_http_scheme_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_11]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_overlong_fqdn_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_overlong_url_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_punycode_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_scheme_relative_url_queues_https_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_uppercase_http_scheme_queues_port_80_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_backslashes_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_html_entity_domain_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_trailing_backtick_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_trailing_quote_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_whitespace_queues_approval_using_first_token]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_userinfo_url_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_session_lock_error_is_sanitized_for_users]]
- 1 edge to [[_COMMUNITY_dot-test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_caption]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_14]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_17]]
- 1 edge to [[_COMMUNITY_dot-test_timeout_error_is_sanitized_for_json_message_field]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_15]]
- 1 edge to [[_COMMUNITY_dot-test_urlencoded_draft_payload_tool_json_is_rewritten]]

## Top bridge nodes
- [[_make_sanitizer()]] - degree 218, connects to 99 communities
- [[dot-test_redaction_silent_no_owner_notice()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_legacy_protected_prefix_is_normalized_form()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_json()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_pairing_code_leakage_is_redacted_json()]] - degree 4, connects to 2 communities
