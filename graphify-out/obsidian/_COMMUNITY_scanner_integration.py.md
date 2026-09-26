---
type: community
cohesion: 0.04
members: 65
---

# scanner_integration.py

**Cohesion:** 0.04 - loosely connected
**Members:** 65 nodes

## Members
- [[.test_collaborator_caption_tool_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_empty_text_with_caption_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_empty_text_with_content_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_empty_text_with_draft_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_empty_text_with_message_payload_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_high_risk_leakage_text_is_normalized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_html_code_markup_is_stripped_and_parse_mode_removed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_pairing_code_leakage_is_redacted_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_security_monitoring_threshold_notice_is_normalized_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_forward_to_telegram_handles_http_error_non_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_forward_to_telegram_returns_http_error_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_without_content_type_empty_text_with_caption_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_without_content_type_empty_text_with_content_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_without_content_type_empty_text_with_draft_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_without_content_type_empty_text_with_message_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_llm_timeout_error_is_sanitized()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_json_draft_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_pipeline_receives_trust_level()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_for_collaborator_gets_protected_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_allows_delayed_starting_then_online_sequence()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_duplicate_no_reply_messages_return_deterministic_reply()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_delayed_starting_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_starting_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_proxy_request_suppresses_startup_notice_emoji_variants()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_approval_cooldown_is_scheme_port_scoped()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_sanitize_reason_hides_internal_paths()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_collaborator_no_reply_gets_protected_notice()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_without_content_type_empty_text_with_caption_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_without_content_type_empty_text_with_content_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_without_content_type_empty_text_with_draft_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_without_content_type_empty_text_with_message_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Caption-only payloads should not bypass collaborator leak normalization.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator form payloads should get protected notice, not suppression.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound HTML codepre markup should be stripped to plain text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator outbound text with raw filetrace leakage markers should be blocked]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborator plain NO_REPLY should become protected unavailable notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should never receive pairing codes or pairing approval commands.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Cooldown dedupe must not suppress approvals when schemeport risk changes.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting and online notices are distinct and should both forward.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Delayed-starting notices should also be deduplicated in cooldown window.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Embeddingprovider memory errors should also be rewritten for urlencoded payload]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Empty text field must not bypass filtering when caption contains tool payload.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload healthcheck SKILL text without sandbox context should keep original]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[HTTPError JSON payloads should be returned as structured API responses.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL messages without sandbox context should not trigger sandbox re]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[JSON message field should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Missing content-type + empty text must not bypass caption filtering for collabor]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Multiline fenced NO_REPLY token should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-JSON HTTPError payloads should still produce a safe fallback dict.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Proxy should pass ownernon-owner trust level into outbound pipeline.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Raw timeout errors should be rewritten to deterministic retry guidance.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Repeated NO_REPLY payloads should still return deterministic non-empty replies.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Runtime memory provider errors should rewrite when payload uses draft field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Starting notice dedupe should tolerate emoji variation drift.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Startup notice dedupe should still apply when sender forgets system header.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundPipelineIntegration]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tests that _filter_outbound calls the full security pipeline.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Threshold status disclosures should normalize to collaborator policy-block notic]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[User-facing block reasons should not expose modules or file paths.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/scanner_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 63 edges to [[_COMMUNITY__make_proxy()]]
- 62 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 4 edges to [[_COMMUNITY_TestParserAndCommandResolution]]
- 3 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_blucliSKILL]]
- 1 edge to [[_COMMUNITY_falco_monitor.py]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY__wrap_response()]]
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

## Top bridge nodes
- [[TestOutboundPipelineIntegration]] - degree 189, connects to 92 communities
- [[.test_collaborator_caption_tool_payload_is_normalized_json()]] - degree 4, connects to 2 communities
- [[.test_collaborator_empty_text_with_caption_payload_is_normalized_json()]] - degree 4, connects to 2 communities
- [[.test_collaborator_empty_text_with_content_payload_is_normalized_json()]] - degree 4, connects to 2 communities
- [[.test_collaborator_empty_text_with_draft_payload_is_normalized_json()]] - degree 4, connects to 2 communities