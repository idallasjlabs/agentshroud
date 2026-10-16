---
type: community
cohesion: 0.04
members: 65
---

# TelegramAPIProxy

**Cohesion:** 0.04 - loosely connected
**Members:** 65 nodes

## Members
- [[dot-test_collaborator_empty_text_with_caption_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_empty_text_with_content_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_empty_text_with_draft_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_empty_text_with_message_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_form_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_legacy_block_notice_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_not_authorized_command_text_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_embedded_tool_call_json_is_removed_from_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_outbound_pipeline_called_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_forward_to_telegram_returns_http_error_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_content()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_draft()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_error_is_rewritten_for_form_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_error_is_rewritten_for_form_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_error_is_rewritten_for_json_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_error_is_rewritten_for_json_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_sandbox_error_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_sandbox_error_with_cannot_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_info_filter_redaction_escalates_to_block_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_error_without_error_keyword_is_not_rewritten_for_form_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_is_rewritten_for_form_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_guidance_phrase_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_pii_redacted_on_outbound()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_prefixed_model_sentence_is_rewritten_to_active_model_hint()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_suppresses_delayed_starting_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_approval_normalizes_leading_dot_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_url_with_control_character_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_url_with_percent_encoded_control_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_sanitize_reason_hides_internal_paths()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_skill_sandbox_message_without_healthcheck_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_plain_no_reply_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Any outbound info-filter redaction should be blocked for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Cannot access' phrasing should be rewritten for healthcheck SKILL.md sandbox mes]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator auth-denial command text should map to protected scope notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payload with raw toolfile leakage markers should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Control characters in leaked URL should be rejected before queueing approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting dedupe should tolerate emoji variation drift.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Empty text field must not bypass filtering when caption contains tool payload.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form content should keep healthcheck sandbox text unchanged when SKILL.md marker]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form draft should keep healthcheck sandbox text unchanged when SKILL.md marker i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message field with embeddingprovider hints but no error keyword should rem]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload legacy notices should normalize to Protect wording.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload plain NO_REPLY should map to deterministic wait guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form-encoded sendMessage bodies must also be scanned by the pipeline.          R]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[HTTPError JSON payloads should be returned as structured API responses.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should be rewritten to local-healthcheck gui]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should rewrite when payload uses caption fie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If tool-call JSON is embedded in prose, strip JSON block before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON caption field should keep healthcheck SKILL.md text unchanged when sandbox]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Malformed host with leading dot should still queue approval for normalized domai]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory guidance mentioning agents.defaults.memorySearch.provider should normaliz]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory provider runtime errors should rewrite when form payload uses caption fie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Partial model sentence variants should still be rewritten deterministically.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Percent-encoded control bytes should be rejected before queueing approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Phone numbers in outbound messages must be redacted by PII sanitizer.          R]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Sandbox SKILL.md messages must include healthcheck context before rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundPipelineIntegration]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests that _filter_outbound calls the full security pipeline.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[User-facing block reasons should not expose modules or file paths.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TelegramAPIProxy
SORT file.name ASC
```

## Connections to other communities
- 61 edges to [[_COMMUNITY_ApprovalQueueConfig_5]]
- 60 edges to [[_COMMUNITY_TelegramAPIProxy_7]]
- 4 edges to [[_COMMUNITY_TestPathIsolationManager_2]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_dot-test_urlencoded_without_content_type_caption_is_still_filtered]]
- 2 edges to [[_COMMUNITY_dot-test_proxy_request_suppresses_starting_notice_emoji_variants]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
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
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]
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
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_PipelineAction]]

## Top bridge nodes
- [[TestOutboundPipelineIntegration]] - degree 189, connects to 96 communities
- [[dot-test_collaborator_empty_text_with_caption_payload_is_normalized_json()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_empty_text_with_content_payload_is_normalized_json()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_empty_text_with_draft_payload_is_normalized_json()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_empty_text_with_message_payload_is_normalized_json()]] - degree 4, connects to 2 communities
