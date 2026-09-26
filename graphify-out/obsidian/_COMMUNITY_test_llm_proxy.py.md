---
type: community
cohesion: 0.03
members: 61
---

# test_llm_proxy.py

**Cohesion:** 0.03 - loosely connected
**Members:** 61 nodes

## Members
- [[.test_collaborator_egress_approval_banner_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_form_caption_tool_payload_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_not_authorized_command_text_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_not_authorized_command_text_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_security_monitoring_threshold_notice_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_outbound_overlength_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_draft()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_sandbox_error_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_sandbox_error_with_cannot_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_case_variant_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_hyphen_variant_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_form_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pending_includes_egress_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_with_punctuation_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_prefixed_model_sentence_is_rewritten_to_active_model_hint()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_allows_starting_then_online_sequence()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_sends_no_reply_wait_message_once()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_tool_call_json_with_zero_width_chars_is_suppressed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_approval_normalizes_leading_dot_domain()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_internal_suffix_domain_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_ip_host_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_percent_encoded_control_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_trailing_backtick_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_redaction_silent_no_owner_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_second_message_after_window_sends_again()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_two_messages_within_window_send_only_one_mirror()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Cannot access' phrasing should be rewritten for healthcheck SKILL.md sandbox mes]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator auth-denial command text should map to protected scope notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should not receive internal egress approval banners.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a PIISanitizer with default enforce config.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[First NO_REPLY payload should send safe wait guidance to Telegram.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form caption field should be filtered the same as textdraftmessage fields.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form draft should keep healthcheck sandbox text unchanged when SKILL.md marker i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep healthcheck SKILL.md text unchanged when sandbox hint i]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload auth-denial command text should map to protected scope notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload threshold disclosures should normalize to policy-block notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should be rewritten to local-healthcheck gui]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Hyphenated embedding-provider wording should still trigger rewrite.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If the pipeline crashes on a form payload, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Internal pseudo-TLD hosts should be rejected from approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON caption field should keep healthcheck SKILL.md text unchanged when sandbox]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep healthcheck SKILL.md text unchanged when sandbox]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Literal IP targets should not enter interactive domain approval flow.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Malformed host with leading dot should still queue approval for normalized domai]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory provider runtime errors should rewrite when form payload uses caption fie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Mixed-case wording variants should still trigger generic runtime guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[NO_REPLY wrapped with punctuation should still be normalized.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Obfuscated tool-call JSON should still be normalized and suppressed.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Over-length form messages to non-owners must be blocked like JSON ones.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Partial model sentence variants should still be rewritten deterministically.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Percent-encoded control bytes should be rejected before queueing approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting and online notices are distinct and should both forward.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Trailing markdown backtick in leaked URL should normalize for approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When outbound text matches the banner, text is replaced but owner is NOT notifie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_sanitizer()]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_llm_proxypy
SORT file.name ASC
```

## Connections to other communities
- 62 edges to [[_COMMUNITY_scanner_integration.py]]
- 61 edges to [[_COMMUNITY__make_proxy()]]
- 9 edges to [[_COMMUNITY_test_ptt_state.c]]
- 8 edges to [[_COMMUNITY_ResourceGuard]]
- 7 edges to [[_COMMUNITY_Mode A — Single task]]
- 5 edges to [[_COMMUNITY_TestGroupMemoryNamespaceIsolation]]
- 4 edges to [[_COMMUNITY_TestParserAndCommandResolution]]
- 4 edges to [[_COMMUNITY_sidecar.py]]
- 2 edges to [[_COMMUNITY_OPENCLAW_DISABLE_HOST_FILESYSTEM]]
- 2 edges to [[_COMMUNITY_blucliSKILL]]
- 1 edge to [[_COMMUNITY_ContextGuard Bug — should_block_message() Always]]
- 1 edge to [[_COMMUNITY_sunday-upgrade-report.sh]]
- 1 edge to [[_COMMUNITY_hermesskillsgraphifyreferencesextraction-spe]]
- 1 edge to [[_COMMUNITY_Cron AgentShroud Daily Check-in]]
- 1 edge to [[_COMMUNITY_setup-mcp-user.sh (user-level MCP config)]]
- 1 edge to [[_COMMUNITY_setup-mcp-user.sh]]
- 1 edge to [[_COMMUNITY_Trivy (vulnerability scanner)]]
- 1 edge to [[_COMMUNITY_bspesp-bsp.h stub (playback state test)]]
- 1 edge to [[_COMMUNITY_ordercliSKILL]]
- 1 edge to [[_COMMUNITY_Branding Specialist README (OpenClaw)]]
- 1 edge to [[_COMMUNITY_Daedalus Concept Illustrator README (OpenClaw)]]
- 1 edge to [[_COMMUNITY_plan]]
- 1 edge to [[_COMMUNITY_GitGuardian ignored-paths + ignored-matches for]]
- 1 edge to [[_COMMUNITY_patch_telegram_send_base_url.py]]
- 1 edge to [[_COMMUNITY_openclawskillsi-value-stream-mappingSKILL]]
- 1 edge to [[_COMMUNITY_gateway-start.sh]]
- 1 edge to [[_COMMUNITY_APPROVAL_ITEMS entity]]
- 1 edge to [[_COMMUNITY_openclawskillsi-agileSKILL]]
- 1 edge to [[_COMMUNITY_hermesskillsi-incident-responseSKILL]]
- 1 edge to [[_COMMUNITY_graphify.serve MCP stdio Server]]
- 1 edge to [[_COMMUNITY_openclawskillsi-observabilitySKILL]]
- 1 edge to [[_COMMUNITY_i-hermes README — Podcast Production Orchestrato]]
- 1 edge to [[_COMMUNITY_i-mac README — macOS System Administrator (MAC)]]
- 1 edge to [[_COMMUNITY_clean-env-quick-keep-local.sh]]
- 1 edge to [[_COMMUNITY_hermesskillsi-observabilitySKILL]]
- 1 edge to [[_COMMUNITY_Constrained query-vocabulary expansion]]
- 1 edge to [[_COMMUNITY_graphify clone command]]
- 1 edge to [[_COMMUNITY_openclawskillsgraphifyreferencesextraction-s]]
- 1 edge to [[_COMMUNITY_hermesskillsi-value-stream-mappingSKILL]]
- 1 edge to [[_COMMUNITY_.test_hermes_soul_documents_ssh_hosts()]]
- 1 edge to [[_COMMUNITY_Red-Green-Refactor TDD loop (playbook)]]
- 1 edge to [[_COMMUNITY_i-incident-response SKILL (stub)]]
- 1 edge to [[_COMMUNITY_hermesskillsi-chaos-engineeringSKILL]]
- 1 edge to [[_COMMUNITY_hermesskillsi-kaizenSKILL]]
- 1 edge to [[_COMMUNITY_i-daedalus README — Concept Illustrator]]
- 1 edge to [[_COMMUNITY_codex-review.sh]]
- 1 edge to [[_COMMUNITY_Control-Plane  Data-Plane Separation]]
- 1 edge to [[_COMMUNITY_hermesskillsi-architecture-reviewSKILL]]
- 1 edge to [[_COMMUNITY_emergency-rollback.sh]]
- 1 edge to [[_COMMUNITY_pre-commit]]
- 1 edge to [[_COMMUNITY_hermesskillsi-scrumSKILL]]
- 1 edge to [[_COMMUNITY_freertosFreeRTOS.h stub (playback state test)]]
- 1 edge to [[_COMMUNITY_ElevenLabs Text-to-Dialogue API]]
- 1 edge to [[_COMMUNITY_activate-lockdown.sh]]
- 1 edge to [[_COMMUNITY_Internal MCP gateway pattern (Entra-fronted)]]
- 1 edge to [[_COMMUNITY_clean-env-keep-local.sh (untrack .env, keep loca]]
- 1 edge to [[_COMMUNITY_clean-env-keep-local.sh]]
- 1 edge to [[_COMMUNITY_curriculum.md (input requirement)]]
- 1 edge to [[_COMMUNITY_openclawskillsi-incident-responseSKILL]]
- 1 edge to [[_COMMUNITY_openclawskillsi-chaos-engineeringSKILL]]
- 1 edge to [[_COMMUNITY_openclawskillsi-architecture-reviewSKILL]]
- 1 edge to [[_COMMUNITY_install.sh]]
- 1 edge to [[_COMMUNITY_Hermes Cannot Force-Switch to Custom-Named Local]]
- 1 edge to [[_COMMUNITY_Alert Thresholds (approval queue 1h timeout, con]]
- 1 edge to [[_COMMUNITY_Obsidian workspace.json (open-tab layout)]]
- 1 edge to [[_COMMUNITY_LogSanitizer PII-Scrubbing Log Filter]]
- 1 edge to [[_COMMUNITY_.test_openclaw_version_pin_is_consistent_across_]]
- 1 edge to [[_COMMUNITY_audio.c (ES7210 mic  ES8311 speaker driver)]]
- 1 edge to [[_COMMUNITY_lvgl_kawaii_face.h (face animation public API)]]
- 1 edge to [[_COMMUNITY_get-credential.sh]]
- 1 edge to [[_COMMUNITY__PII_PATTERNS (URL PII regex set)]]
- 1 edge to [[_COMMUNITY_SharedMemoryManager Merged Memory Tests]]
- 1 edge to [[_COMMUNITY_SOC Auth WS Token IssuanceRedemption Tests]]
- 1 edge to [[_COMMUNITY_checkPrereqs()]]
- 1 edge to [[_COMMUNITY_SOC Models SecurityEvent Tests]]
- 1 edge to [[_COMMUNITY_loadRuntimes()]]
- 1 edge to [[_COMMUNITY_Diagram 18 Runbook]]
- 1 edge to [[_COMMUNITY_Release Workflow]]
- 1 edge to [[_COMMUNITY_Dependabot Configuration]]
- 1 edge to [[_COMMUNITY_Scorecard Data Integrity Tests (no stub inflatio]]
- 1 edge to [[_COMMUNITY_i-tdd README]]
- 1 edge to [[_COMMUNITY_.test_switch_model_script_uses_current_target_sy]]
- 1 edge to [[_COMMUNITY_MiddlewareManager Session Enforcement Tests]]
- 1 edge to [[_COMMUNITY_SlackAPIProxy Socket Mode Relay (apps.connection]]
- 1 edge to [[_COMMUNITY_deploy-gateway.sh]]
- 1 edge to [[_COMMUNITY_perform_mcp_oauth_preflight.sh]]
- 1 edge to [[_COMMUNITY_hermesskillsi-devsecopsSKILL]]
- 1 edge to [[_COMMUNITY_hermesskillsi-kanbanSKILL]]
- 1 edge to [[_COMMUNITY_Rationale agentshroud-gateway MCP server disabl]]
- 1 edge to [[_COMMUNITY_canary-cron.sh]]
- 1 edge to [[_COMMUNITY_check-status.sh]]
- 1 edge to [[_COMMUNITY_egress-iptables.sh]]
- 1 edge to [[_COMMUNITY_feature-priorities]]
- 1 edge to [[_COMMUNITY_prefetch-ghsa-registry.sh]]
- 1 edge to [[_COMMUNITY_CI test job (matrix ubuntumacos x py3.113.13)]]

## Top bridge nodes
- [[_make_sanitizer()]] - degree 218, connects to 95 communities
- [[.test_redaction_silent_no_owner_notice()]] - degree 4, connects to 2 communities
- [[.test_collaborator_egress_approval_banner_is_redacted_json()]] - degree 4, connects to 2 communities
- [[.test_collaborator_form_caption_tool_payload_is_normalized()]] - degree 4, connects to 2 communities
- [[.test_collaborator_not_authorized_command_text_is_normalized_form()]] - degree 4, connects to 2 communities