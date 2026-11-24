---
type: community
members: 77
---

# _make_sanitizer

**Members:** 77 nodes

## Members
- [[dot-test_collaborator_caption_tool_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_empty_text_with_caption_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_form_empty_text_with_draft_payload_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_form_empty_text_with_message_payload_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_form_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_multiturn_block_text_is_normalized_to_protected_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_pairing_code_leakage_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_outbound_pipeline_called_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_draft()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sessions_spawn_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_error_is_rewritten_for_form_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_sandbox_cannot_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_without_content_type_empty_text_with_caption_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_llm_timeout_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_error_without_embedding_provider_hint_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_error_without_error_keyword_is_not_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_hyphen_variant_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_is_rewritten_to_generic_runtime_guidance()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_no_reply_tool_token_is_rewritten_to_wait_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_ollama_auth_required_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_plain_no_reply_token_is_rewritten_to_wait_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_prefixed_model_sentence_is_rewritten_to_active_model_hint()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_tool_call_json_with_zero_width_chars_is_suppressed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_domain_with_invalid_chars_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_runtime_profile_memory_error_text_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_skill_sandbox_message_without_healthcheck_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_timeout_error_is_sanitized_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_plain_no_reply_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_plain_no_reply_with_punctuation_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_without_content_type_empty_text_with_caption_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Cannot access' healthcheck SKILL.md sandbox wording should rewrite for form…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Caption-only payloads should not bypass collaborator leak normalization.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payload with raw toolfile leakage markers should be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator multi-turn disclosure block prose should be normalized.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should never receive pairing codes or pairing approval commands.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Consecutive-dot domains should be rejected before approval queueing.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a PIISanitizer with default enforce config.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Domains containing invalid hostname characters must be rejected.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider errors without explicit memory command context should be…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Empty text field must not bypass filtering when caption contains tool payload.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form draft should keep healthcheck sandbox text unchanged when SKILL.md marker…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload NO_REPLY punctuation variant should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload empty text should not shadow draft filtering.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload empty text should not shadow message filtering.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload plain NO_REPLY should map to deterministic wait guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form-encoded sendMessage bodies must also be scanned by the pipeline.…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should rewrite when form payload uses…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should rewrite when payload uses message…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck tool-call JSON should be rewritten to friendly status text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Hyphenated embedding-provider wording should still trigger rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep healthcheck SKILL.md text unchanged when sandbox…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field with embeddingprovider hints but no error keyword should…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Missing content-type + empty text must not bypass caption filtering (json path).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Missing content-type + empty text must not bypass caption filtering for…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[NO_REPLY tool JSON should be converted into a user-safe wait message.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-embedding memory errors should not be forced into embedding guidance text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Obfuscated tool-call JSON should still be normalized and suppressed.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Ollama auth errors should map to concise operator guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Partial model sentence variants should still be rewritten deterministically.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Plain NO_REPLY text should still be normalized to deterministic wait guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Previously emitted runtime-profile memory text should be normalized to generic…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw timeout errors should be rewritten to deterministic retry guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Sandbox SKILL.md messages must include healthcheck context before rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Timeout rewrites should apply when JSON payload uses message field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_sanitizer()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[check_async()_36]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[check_async()_37]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound()_15]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_sanitizer
SORT file.name ASC
```

## Connections to other communities
- 78 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 71 edges to [[_COMMUNITY_asyncio_5]]
- 12 edges to [[_COMMUNITY__mock_forward]]
- 9 edges to [[_COMMUNITY__make_multipart_body]]
- 7 edges to [[_COMMUNITY_TestOutboundScanUnification]]
- 5 edges to [[_COMMUNITY_TestWebSearchLog]]
- 4 edges to [[_COMMUNITY_TestParseModeStrippedAfterPIIRedaction]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_dot-test_activity_command_renders_entries]]
- 3 edges to [[_COMMUNITY_TestReplayBufferOffsetParsing]]
- 2 edges to [[_COMMUNITY_TestOwnerMirrorCoalescing]]
- 1 edge to [[_COMMUNITY_TestTelegram400Retry]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_egress_approval_banner_is_redacted_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_protected_prefix_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_protected_prefix_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_not_authorized_command_text_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_embedded_web_fetch_json_queues_approval_when_available]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_fails_closed_for_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_owner_exempt_from_fail_closed]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_pipeline_block_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_pipeline_sanitized_text_applied]]
- 1 edge to [[_COMMUNITY_dot-test_form_payload_with_draft_field_is_filtered]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_content_field]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_content]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_html_parse_mode_preserved_without_redaction_placeholders]]
- 1 edge to [[_COMMUNITY_dot-test_info_filter_redaction_escalates_to_block_for_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_json_without_content_type_empty_text_with_message_is_still_filtered]]
- 1 edge to [[_COMMUNITY_dot-test_json_without_content_type_is_still_filtered]]
- 1 edge to [[_COMMUNITY_dot-test_long_outbound_message_quarantined]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_embedding_provider_hint_is_not_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_for_form_caption_field]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_for_json_message_field]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_slash_variant_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_variant_is_rewritten_generic]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_with_explicit_memory_command_keeps_memory_guidance]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_guidance_phrase_is_rewritten_generic]]
- 1 edge to [[_COMMUNITY_dot-test_ollama_tools_unsupported_error_is_sanitized]]
- 1 edge to [[_COMMUNITY_dot-test_outbound_owner_exempt_from_fail_closed]]
- 1 edge to [[_COMMUNITY_dot-test_pii_redacted_on_outbound]]
- 1 edge to [[_COMMUNITY_dot-test_pipeline_receives_trust_level]]
- 1 edge to [[_COMMUNITY_dot-test_plain_no_reply_token_for_collaborator_gets_protected_notice]]
- 1 edge to [[_COMMUNITY_dot-test_plain_no_reply_token_with_punctuation_is_rewritten]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_cooldown_is_scheme_port_scoped]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_normalizes_leading_dot_domain]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_prunes_expired_cooldown_entries]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_queue_is_cooldown_deduped]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_strips_trailing_punctuation]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_explicit_md_tld_domain_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_filename_reference_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_internal_suffix_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_invalid_host_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_ip_host_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_non_http_scheme_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_non_standard_port_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_numeric_tld_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_overlong_fqdn_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_queues_egress_approval_when_available]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_scheme_relative_url_queues_https_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_backslashes_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_control_character_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_html_entity_domain_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_trailing_backtick_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_userinfo_url_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_truncated_model_sentence_is_rewritten_to_active_model_hint]]
- 1 edge to [[_COMMUNITY_dot-test_urlencoded_collaborator_no_reply_gets_protected_notice]]

## Top bridge nodes
- [[_make_sanitizer()]] - degree 218, connects to 67 communities
- [[dot-test_form_outbound_pipeline_called_when_available()]] - degree 5, connects to 2 communities
- [[dot-test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval()]] - degree 5, connects to 2 communities
- [[dot-test_raw_web_fetch_json_domain_with_invalid_chars_does_not_queue_approval()]] - degree 5, connects to 2 communities
- [[dot-test_collaborator_caption_tool_payload_is_normalized_json()]] - degree 4, connects to 2 communities
