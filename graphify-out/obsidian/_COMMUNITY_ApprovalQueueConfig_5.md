---
type: community
cohesion: 0.04
members: 53
---

# ApprovalQueueConfig

**Cohesion:** 0.04 - loosely connected
**Members:** 53 nodes

## Members
- [[dot-test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_access_not_configured_user_id_leakage_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_agent_failed_prefix_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_agent_failed_prefix_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_multiturn_block_text_is_normalized_to_protected_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_contextvar_takes_precedence_over_default()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_default_is_openclaw_when_not_injected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_forward_to_telegram_handles_http_error_non_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sessions_spawn_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_html_parse_mode_removed_for_redaction_placeholders()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_injected_default_overrides_openclaw()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_without_content_type_empty_text_with_caption_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_without_content_type_empty_text_with_content_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_without_content_type_empty_text_with_draft_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_without_content_type_empty_text_with_message_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_long_outbound_message_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_suppresses_duplicate_system_startup_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_tool_call_json_never_leaks()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_explicit_md_tld_domain_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_internal_suffix_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_queues_egress_approval_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_truncated_model_sentence_is_rewritten_to_active_model_hint()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_without_content_type_empty_text_with_caption_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_without_content_type_empty_text_with_content_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_without_content_type_empty_text_with_draft_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_without_content_type_empty_text_with_message_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Blocked outbound messages should be stored in outbound quarantine.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator agent-failed prefix should normalize to protected unavailable notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator multi-turn disclosure block prose should be normalized.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be blocked]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Explicitly schemed domains should still queue approvals even for .md ccTLD.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload agent-failed prefix should normalize to protected unavailable notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload user-id enrollment leakage should also be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck tool-call JSON should be rewritten to friendly status text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Internal pseudo-TLD hosts should be rejected from approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory provider runtime errors should rewrite when payload uses message field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Missing content-type + empty text must not bypass caption filtering for collabor]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-JSON HTTPError payloads should still produce a safe fallback dict.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw tool-call JSON blobs must be suppressed before Telegram delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw web_fetch JSON should queue interactive egress approval for the destination.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Redaction placeholder tokens should be HTML-escaped, not strip         parse_mod]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Startup notice dedupe should still apply when sender forgets system header.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[System startup notice should be deduplicated in a short cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TelegramAPIProxy_1]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestDefaultBotId]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Truncated 'current model' replies should be rewritten to deterministic model hin]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_active_bot_id returns the constructor-injected default when no contextvar is se]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig
SORT file.name ASC
```

## Connections to other communities
- 61 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 57 edges to [[_COMMUNITY_TelegramAPIProxy_7]]
- 9 edges to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 7 edges to [[_COMMUNITY_TestMultipartOutboundPipeline_1]]
- 6 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 5 edges to [[_COMMUNITY_TestWebSearchLog]]
- 4 edges to [[_COMMUNITY_TestPathIsolationManager_2]]
- 2 edges to [[_COMMUNITY_PIIConfig]]
- 2 edges to [[_COMMUNITY_TestForwardToTelegramTimeouts]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 2 edges to [[_COMMUNITY_dot-test_urlencoded_without_content_type_caption_is_still_filtered]]
- 2 edges to [[_COMMUNITY_dot-test_proxy_request_suppresses_starting_notice_emoji_variants]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_5]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_6]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_9]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_10]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_11]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_12]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_13]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_14]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_15]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_16]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_17]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_underscore_variant_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_caption_tool_payload_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_form_caption_tool_payload_is_normalized]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_egress_approval_banner_is_redacted_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_egress_approval_banner_is_redacted_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_pairing_code_leakage_is_redacted_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_access_not_configured_user_id_leakage_is_redacted_json]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_sandbox_error_variant_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_for_json_draft_field]]
- 1 edge to [[_COMMUNITY_dot-test_outbound_owner_exempt_from_fail_closed]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_slash_variant_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_hyphen_variant_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_embedding_provider_hint_is_not_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_error_keyword_is_not_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_error_keyword_is_not_rewritten_for_json_message_field]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_embedding_provider_hint_is_not_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_caption]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_form_message]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_sandbox_error_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_sandbox_cannot_variant_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_urlencoded_draft_payload_tool_json_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_json_without_content_type_is_still_filtered]]
- 1 edge to [[_COMMUNITY_dot-test_html_parse_mode_preserved_without_redaction_placeholders]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_html_code_markup_is_stripped_and_parse_mode_removed]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_pipeline_block_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_proxy_request_allows_distinct_system_notices]]
- 1 edge to [[_COMMUNITY_dot-test_proxy_request_allows_starting_then_online_sequence]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_fails_closed_for_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_proxy_request_suppresses_duplicate_delayed_starting_notice]]
- 1 edge to [[_COMMUNITY_dot-test_form_payload_with_draft_field_is_filtered]]
- 1 edge to [[_COMMUNITY_dot-test_embedded_web_fetch_json_queues_approval_when_available]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_owner_exempt_from_fail_closed]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_cooldown_is_scheme_port_scoped]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_prunes_expired_cooldown_entries]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_overlength_blocked_for_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_filename_reference_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_domain_with_invalid_chars_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_trailing_quote_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_trailing_backtick_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_backslashes_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_whitespace_queues_approval_using_first_token]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_non_http_scheme_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_userinfo_url_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_overlong_url_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_overlong_fqdn_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_punycode_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_uppercase_http_scheme_queues_port_80_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_scheme_relative_url_queues_https_approval]]
- 1 edge to [[_COMMUNITY_dot-test_block_cascade_blocks_followup_fragment]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_html_entity_domain_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_pipeline_receives_trust_level]]
- 1 edge to [[_COMMUNITY_dot-test_plain_no_reply_token_is_rewritten_to_wait_message]]
- 1 edge to [[_COMMUNITY_dot-test_plain_no_reply_token_in_markdown_fence_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_generic_sessions_spawn_json_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_session_lock_error_is_sanitized_for_users]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_not_authorized_command_text_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_block_notice_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_protected_prefix_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_internal_tool_output_suppressed_notice_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_internal_tool_output_suppressed_notice_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_security_monitoring_threshold_notice_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_security_monitoring_threshold_notice_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_ollama_tools_unsupported_error_is_sanitized]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_form]]
- 1 edge to [[_COMMUNITY_dot-test_agent_failed_timeout_error_is_sanitized]]
- 1 edge to [[_COMMUNITY_dot-test_timeout_error_is_sanitized_for_json_message_field]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_to_generic_runtime_guidance]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_case_variant_is_rewritten_generic]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_with_explicit_memory_command_keeps_memory_guidance]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_hyphen_variant_is_rewritten]]

## Top bridge nodes
- [[TelegramAPIProxy_1]] - degree 220, connects to 100 communities
- [[TestDefaultBotId]] - degree 9, connects to 4 communities
- [[dot-test_collaborator_access_not_configured_user_id_leakage_is_redacted_form()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_agent_failed_prefix_is_normalized_form()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_agent_failed_prefix_is_normalized_json()]] - degree 4, connects to 2 communities
