---
type: community
members: 57
---

# _make_sanitizer()

**Members:** 57 nodes

## Members
- [[dot-_make_proxy_with_mock_buffer()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_caption_tool_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_internal_tool_output_suppressed_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_pairing_code_leakage_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_embedded_tool_call_json_is_removed_from_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sessions_spawn_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_sandbox_error_variant_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_long_outbound_message_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_error_without_error_keyword_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_error_without_error_keyword_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_hyphen_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_underscore_variant_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_with_explicit_memory_command_keeps_memory_guidance()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_plain_no_reply_token_in_markdown_fence_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_suppresses_duplicate_delayed_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_suppresses_duplicate_system_startup_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_suppresses_starting_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_suppresses_startup_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_tool_call_json_never_leaks()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_overlong_url_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_urlencoded_draft_payload_tool_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Blocked outbound messages should be stored in outbound quarantine.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Caption-only payloads should not bypass collaborator leak normalization.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be blocked]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a PIISanitizer with default enforce config.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting notices should also be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider hints without explicit error marker should not trigger rewrit]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Explicit memory-search command context should keep memory-specific remediation t]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload embeddingprovider hints without 'error' should keep original text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payloads containing pairing secrets must be blocked for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form-encoded draft payloads must not leak raw tool-call JSON.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck tool-call JSON should be rewritten to friendly status text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Hyphen-separated embedding-provider wording should rewrite for form payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If tool-call JSON is embedded in prose, strip JSON block before delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON caption field should keep healthcheck SKILL.md text unchanged when sandbox]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Legacy internal tool-output suppression string should normalize to Protect wordi]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Malformed domain labels should be rejected before approval queueing.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory provider runtime errors should rewrite when payload uses message field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[NO_REPLY wrapped in markdown fence should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Overly long URLs should be rejected before approval queueing.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw tool-call JSON blobs must be suppressed before Telegram delivery.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting notice dedupe should tolerate emoji variation drift.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[System startup notice should be deduplicated in a short cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Underscore-delimited embedding_provider wording should still trigger rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When outbound text matches the banner, text is replaced but owner is NOT notifie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Wording variants for healthcheck SKILL.md sandbox errors should be rewritten.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_sanitizer()]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_sanitizer
SORT file.name ASC
```

## Connections to other communities
- 59 edges to [[_COMMUNITY_TestOutboundPipelineIntegration]]
- 58 edges to [[_COMMUNITY_TelegramAPIProxy (2)]]
- 10 edges to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 8 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 6 edges to [[_COMMUNITY_TestMultipartOutboundPipeline (2)]]
- 5 edges to [[_COMMUNITY_TestWebSearchLog]]
- 4 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 4 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 4 edges to [[_COMMUNITY_TestPathIsolationManager (2)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_TestForwardToTelegramTimeouts]]
- 2 edges to [[_COMMUNITY_dot-test_urlencoded_without_content_type_caption_is_still_filtered]]
- 1 edge to [[_COMMUNITY_dot-test_agent_failed_timeout_error_is_sanitized]]
- 1 edge to [[_COMMUNITY_dot-test_block_cascade_blocks_followup_fragment]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (9)]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_access_not_configured_user_id_leakage_is_redacted_json]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (13)]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_form_caption_tool_payload_is_normalized]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (5)]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_internal_tool_output_suppressed_notice_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_block_notice_is_normalized_json]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (34)]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_protected_prefix_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_form]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (38)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (7)]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_security_monitoring_threshold_notice_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_security_monitoring_threshold_notice_is_normalized_json]]
- 1 edge to [[_COMMUNITY_dot-test_embedded_web_fetch_json_queues_approval_when_available]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_fails_closed_for_non_owner]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_owner_exempt_from_fail_closed]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (13)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (16)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (11)]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (12)]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_sandbox_cannot_variant_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (8)]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_skill_sandbox_error_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_html_parse_mode_preserved_without_redaction_placeholders]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (10)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (37)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (25)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (30)]]
- 1 edge to [[_COMMUNITY_dot-test_memory_error_without_embedding_provider_hint_is_not_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (14)]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_case_variant_is_rewritten_generic]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_for_form_payload]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_for_json_draft_field]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_is_rewritten_to_generic_runtime_guidance]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (9)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (41)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (32)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (15)]]
- 1 edge to [[_COMMUNITY_dot-test_ollama_tools_unsupported_error_is_sanitized]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (6)]]
- 1 edge to [[_COMMUNITY_dot-test_outbound_owner_exempt_from_fail_closed]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (39)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (29)]]
- 1 edge to [[_COMMUNITY_dot-test_pipeline_receives_trust_level]]
- 1 edge to [[_COMMUNITY_dot-test_plain_no_reply_token_is_rewritten_to_wait_message]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (33)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (18)]]
- 1 edge to [[_COMMUNITY_dot-test_proxy_request_allows_distinct_system_notices]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (31)]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_cooldown_is_scheme_port_scoped]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (21)]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_prunes_expired_cooldown_entries]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (20)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (22)]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_filename_reference_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (12)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (23)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (24)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (19)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (28)]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_overlong_fqdn_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_punycode_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (11)]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_scheme_relative_url_queues_https_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_uppercase_http_scheme_queues_port_80_approval]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (26)]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_html_entity_domain_still_queues_approval]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (27)]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_trailing_backtick_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_trailing_quote_still_queues_approval]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_whitespace_queues_approval_using_first_token]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_userinfo_url_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (42)]]
- 1 edge to [[_COMMUNITY_dot-test_session_lock_error_is_sanitized_for_users]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (10)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (35)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (40)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (14)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (36)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (17)]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py (5)]]

## Top bridge nodes
- [[_make_sanitizer()]] - degree 218, connects to 98 communities
- [[dot-_make_proxy_with_mock_buffer()]] - degree 5, connects to 2 communities
- [[dot-test_redaction_silent_no_owner_notice()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_caption_tool_payload_is_normalized_json()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_high_risk_leakage_text_is_normalized()]] - degree 4, connects to 2 communities
