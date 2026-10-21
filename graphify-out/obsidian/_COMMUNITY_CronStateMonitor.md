---
type: community
members: 57
---

# CronStateMonitor

**Members:** 57 nodes

## Members
- [[dot-test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_agent_failed_timeout_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_agent_failed_prefix_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_caption_tool_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_egress_approval_banner_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_not_authorized_command_text_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_collaborator_security_monitoring_threshold_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_outbound_overlength_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_payload_with_draft_field_is_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_sessions_spawn_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_info_filter_redaction_escalates_to_block_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_long_outbound_message_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_error_without_embedding_provider_hint_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_error_without_error_keyword_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_memory_provider_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_outbound_pipeline_called_when_available()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_prefixed_model_sentence_is_rewritten_to_active_model_hint()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_proxy_request_sends_no_reply_wait_message_once()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_scheme_relative_url_queues_https_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_raw_web_fetch_json_url_with_backslashes_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_session_lock_error_is_sanitized_for_users()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Agent timeout prefix variants should also map to retry guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Any outbound info-filter redaction should be blocked for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Backslash-containing URLs should be rejected to avoid parser confusion.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Caption-only payloads should not bypass collaborator leak normalization.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be blocked]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should not receive internal egress approval banners.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a PIISanitizer with default enforce config.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First NO_REPLY payload should send safe wait guidance to Telegram.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload agent-failed prefix should normalize to protected unavailable notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload auth-denial command text should map to protected scope notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload embeddingprovider hints without 'error' should keep original text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload healthcheck SKILL text without sandbox context should keep original]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload using draft field should still suppress tool-call JSON.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck tool-call JSON should be rewritten to friendly status text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Internal session lock errors should be rewritten to safe user guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON caption field should keep healthcheck SKILL.md text unchanged when sandbox]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory provider runtime errors should rewrite when payload uses message field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Messages above hard size cap should be blocked to prevent split bypass.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-embedding memory errors should not be forced into embedding guidance text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Over-length form messages to non-owners must be blocked like JSON ones.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Partial model sentence variants should still be rewritten deterministically.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Scheme-relative URLs in leaked JSON should normalize to HTTPS approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Threshold status disclosures should normalize to collaborator policy-block notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When outbound text matches the banner, text is replaced but owner is NOT notifie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When pipeline is set, process_outbound must be called on outbound messages.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_sanitizer()]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CronStateMonitor
SORT file.name ASC
```

## Connections to other communities
- 58 edges to [[_COMMUNITY_UserSessionManager (2)]]
- 57 edges to [[_COMMUNITY__req]]
- 16 edges to [[_COMMUNITY_ESP32-S3-BOX-3 Voice Terminal for Hermes (behind AgentShroud)]]
- 9 edges to [[_COMMUNITY_EgressFilterConfig]]
- 5 edges to [[_COMMUNITY__fw_client]]
- 4 edges to [[_COMMUNITY_MCP OAuth preflight checker (mcp_oauth_preflight.py)]]
- 4 edges to [[_COMMUNITY_All Dependencies.md (2)]]
- 2 edges to [[_COMMUNITY_hermesskillsi-bsREADME.md (5)]]
- 2 edges to [[_COMMUNITY_CronStateMonitor (2)]]
- 2 edges to [[_COMMUNITY_Scrum Ceremony Facilitation]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_form]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration (4)]]
- 1 edge to [[_COMMUNITY_dot-test_html_parse_mode_preserved_without_redaction_placeholders]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2) (4)_1]]
- 1 edge to [[_COMMUNITY__make_sanitizer() (7)]]
- 1 edge to [[_COMMUNITY__req (4)]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (13)]]
- 1 edge to [[_COMMUNITY_Agile Skill (stub)]]
- 1 edge to [[_COMMUNITY_Architecture Review Skill (stub)]]
- 1 edge to [[_COMMUNITY_Build-config pinning — sdkconfig.defaults pins TCP_MSSstackWDTTCP buffers]]
- 1 edge to [[_COMMUNITY_Value Stream Mapping Skill]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (9)]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (4)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (17)]]
- 1 edge to [[_COMMUNITY_Observability Skill]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_url_with_whitespace_queues_approval_using_first_token]]
- 1 edge to [[_COMMUNITY__make_sanitizer() (10)]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration (6)]]
- 1 edge to [[_COMMUNITY__req (8)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (20)]]
- 1 edge to [[_COMMUNITY__req (3)]]
- 1 edge to [[_COMMUNITY_dot-test_form_outbound_owner_exempt_from_fail_closed]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (3)]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_approval_cooldown_is_scheme_port_scoped]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (5)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (26)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (5)]]
- 1 edge to [[_COMMUNITY_SRE Practices]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (9)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (21)]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (6)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2) (6)_1]]
- 1 edge to [[_COMMUNITY_Approval queue — emailfile-deletionexternal-APIskill-install must route through it]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (11)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (4)]]
- 1 edge to [[_COMMUNITY_omlx-keepwarm.sh — keeps gemma model resident (cold 5.06s vs warm 0.69s)]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (3)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (19)]]
- 1 edge to [[_COMMUNITY_Voice robustness — volume-command STT tolerance + stream timeoutrepr logging]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (14)]]
- 1 edge to [[_COMMUNITY__req (9)]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_Pre-Change Analysis (PCA)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (16)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2) (5)_1]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2) (9)]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (12)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (8)]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration (9)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (27)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (6)]]
- 1 edge to [[_COMMUNITY__req (5)]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (11)]]
- 1 edge to [[_COMMUNITY_dot-test_memory_provider_error_case_variant_is_rewritten_generic]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_punycode_domain_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY_dot-test_block_cascade_blocks_followup_fragment]]
- 1 edge to [[_COMMUNITY_dot-test_raw_web_fetch_json_overlong_fqdn_does_not_queue_approval]]
- 1 edge to [[_COMMUNITY__make_sanitizer() (12)]]
- 1 edge to [[_COMMUNITY__req (6)]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (7)]]
- 1 edge to [[_COMMUNITY__make_sanitizer() (11)]]
- 1 edge to [[_COMMUNITY__make_sanitizer() (13)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (31)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (12)]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (8)]]
- 1 edge to [[_COMMUNITY__req (7)]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_security_monitoring_threshold_notice_is_normalized_form]]
- 1 edge to [[_COMMUNITY_dot-test_ollama_tools_unsupported_error_is_sanitized]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (10)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (36)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (28)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (37)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (2) (8)]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (40)]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_block_notice_is_normalized_json]]
- 1 edge to [[_COMMUNITY_TestOutboundPipelineIntegration (8)]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_legacy_protected_prefix_is_normalized_json]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy (35)]]
- 1 edge to [[_COMMUNITY_Docker sidecar integrity — falcoclamavfluent-bit in-process, wazuh-agent standalone sidecar]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (11)]]
- 1 edge to [[_COMMUNITY__req (2)]]
- 1 edge to [[_COMMUNITY_Chaos Engineering Skill]]
- 1 edge to [[_COMMUNITY_nemotron-named models misclassified as needing cloud provider in local mode]]
- 1 edge to [[_COMMUNITY_UserSessionManager (2) (10)]]
- 1 edge to [[_COMMUNITY_System Audit Documentation (SAD)]]
- 1 edge to [[_COMMUNITY__make_sanitizer() (9)]]
- 1 edge to [[_COMMUNITY_CronStateMonitor (7)]]
- 1 edge to [[_COMMUNITY_test_colima_and_sdk_patch_fallback_resolution.sh]]

## Top bridge nodes
- [[_make_sanitizer()]] - degree 218, connects to 98 communities
- [[dot-test_redaction_silent_no_owner_notice()]] - degree 4, connects to 2 communities
- [[dot-test_agent_failed_timeout_error_is_sanitized()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_agent_failed_prefix_is_normalized_form()]] - degree 4, connects to 2 communities
- [[dot-test_collaborator_caption_tool_payload_is_normalized_json()]] - degree 4, connects to 2 communities
