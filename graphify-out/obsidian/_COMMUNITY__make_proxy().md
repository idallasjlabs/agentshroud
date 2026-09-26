---
type: community
cohesion: 0.04
members: 60
---

# _make_proxy()

**Cohesion:** 0.04 - loosely connected
**Members:** 60 nodes

## Members
- [[.test_activity_command_renders_entries()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_activity_command_reports_tracker_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_egress_approval_banner_is_redacted_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_legacy_block_notice_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_legacy_protected_prefix_is_normalized_form()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_json()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_contextvar_takes_precedence_over_default()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_default_is_openclaw_when_not_injected()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_generic_sessions_spawn_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_form_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_form_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_json_caption_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_json_content_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_healthcheck_skill_sandbox_error_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_info_filter_redaction_escalates_to_block_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_injected_default_overrides_openclaw()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_long_outbound_message_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_embedding_provider_hint_is_not_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_error_without_error_keyword_is_not_rewritten_for_form_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_hyphen_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_is_rewritten_for_json_message_field()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_slash_variant_is_rewritten_for_form_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_error_variant_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_memory_provider_guidance_phrase_is_rewritten_generic()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_outbound_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_explicit_md_tld_domain_still_queues_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_numeric_tld_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_raw_web_fetch_json_url_with_control_character_does_not_queue_approval()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_message()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_draft_payload_tool_json_is_rewritten()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_urlencoded_plain_no_reply_with_punctuation_is_still_filtered()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Any outbound info-filter redaction should be blocked for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Collaborators should receive protected unavailable notice for timeout rewrite va]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Control characters in leaked URL should be rejected before queueing approval.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Domains with numeric TLDs should not enter approval queue.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Explicitly schemed domains should still queue approvals even for .md ccTLD.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message field with embeddingprovider hints but no error keyword should rem]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form message should keep non-healthcheck SKILL.md sandbox text unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload NO_REPLY punctuation variant should still normalize.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload approval banners must be redacted for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload legacy 'Protected' wording should normalize to canonical protected]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form payload legacy notices should normalize to Protect wording.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Form-encoded draft payloads must not leak raw tool-call JSON.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Generic session spawn JSON should be rewritten, not shown raw.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should be rewritten for urlencoded payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Healthcheck SKILL.md sandbox errors should rewrite when payload uses caption fie]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Hyphen-separated embedding-provider wording should rewrite for form payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If pipeline crashes, non-owner messages must be blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory guidance mentioning agents.defaults.memorySearch.provider should normaliz]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Memory provider runtime errors should rewrite when payload uses message field.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Messages above hard size cap should be blocked to prevent split bypass.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Non-embedding memory errors should not be forced into embedding guidance text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Slash-separated embeddingprovider wording should rewrite for form payloads.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TelegramAPIProxy_3]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestDefaultBotId]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Variant wording should still map to generic runtime guidance by default.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker has entries, activity renders them.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[When tracker is None, activity returns honest error, not silent empty.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_active_bot_id returns the constructor-injected default when no contextvar is se]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_make_proxy
SORT file.name ASC
```

## Connections to other communities
- 63 edges to [[_COMMUNITY_scanner_integration.py]]
- 61 edges to [[_COMMUNITY_test_llm_proxy.py]]
- 9 edges to [[_COMMUNITY_test_ptt_state.c]]
- 8 edges to [[_COMMUNITY_ResourceGuard]]
- 7 edges to [[_COMMUNITY_Mode A — Single task]]
- 5 edges to [[_COMMUNITY_TestGroupMemoryNamespaceIsolation]]
- 4 edges to [[_COMMUNITY_TestParserAndCommandResolution]]
- 2 edges to [[_COMMUNITY_FileSandbox]]
- 2 edges to [[_COMMUNITY__wrap_response()]]
- 2 edges to [[_COMMUNITY_blucliSKILL]]
- 2 edges to [[_COMMUNITY_OPENCLAW_DISABLE_HOST_FILESYSTEM]]
- 1 edge to [[_COMMUNITY_Internal MCP gateway pattern (Entra-fronted)]]
- 1 edge to [[_COMMUNITY_Rationale agentshroud-gateway MCP server disabl]]
- 1 edge to [[_COMMUNITY_activate-lockdown.sh]]
- 1 edge to [[_COMMUNITY_ElevenLabs Text-to-Dialogue API]]
- 1 edge to [[_COMMUNITY_hermesskillsi-incident-responseSKILL]]
- 1 edge to [[_COMMUNITY_graphify.serve MCP stdio Server]]
- 1 edge to [[_COMMUNITY_openclawskillsi-agileSKILL]]
- 1 edge to [[_COMMUNITY_APPROVAL_ITEMS entity]]
- 1 edge to [[_COMMUNITY_.test_hermes_soul_documents_ssh_hosts()]]
- 1 edge to [[_COMMUNITY_sunday-upgrade-report.sh]]
- 1 edge to [[_COMMUNITY_Red-Green-Refactor TDD loop (playbook)]]
- 1 edge to [[_COMMUNITY_install.sh]]
- 1 edge to [[_COMMUNITY_pre-commit]]
- 1 edge to [[_COMMUNITY_clean-env-keep-local.sh]]
- 1 edge to [[_COMMUNITY_clean-env-keep-local.sh (untrack .env, keep loca]]
- 1 edge to [[_COMMUNITY_clean-env-quick-keep-local.sh]]
- 1 edge to [[_COMMUNITY_perform_mcp_oauth_preflight.sh]]
- 1 edge to [[_COMMUNITY_setup-mcp-user.sh]]
- 1 edge to [[_COMMUNITY_setup-mcp-user.sh (user-level MCP config)]]
- 1 edge to [[_COMMUNITY_Branding Specialist README (OpenClaw)]]
- 1 edge to [[_COMMUNITY_Daedalus Concept Illustrator README (OpenClaw)]]
- 1 edge to [[_COMMUNITY_ordercliSKILL]]
- 1 edge to [[_COMMUNITY_bspesp-bsp.h stub (playback state test)]]
- 1 edge to [[_COMMUNITY_freertosFreeRTOS.h stub (playback state test)]]
- 1 edge to [[_COMMUNITY_feature-priorities]]
- 1 edge to [[_COMMUNITY_plan]]
- 1 edge to [[_COMMUNITY_ContextGuard Bug — should_block_message() Always]]
- 1 edge to [[_COMMUNITY_canary-cron.sh]]
- 1 edge to [[_COMMUNITY_check-status.sh]]
- 1 edge to [[_COMMUNITY_codex-review.sh]]
- 1 edge to [[_COMMUNITY_deploy-gateway.sh]]
- 1 edge to [[_COMMUNITY_egress-iptables.sh]]
- 1 edge to [[_COMMUNITY_emergency-rollback.sh]]
- 1 edge to [[_COMMUNITY_Control-Plane  Data-Plane Separation]]
- 1 edge to [[_COMMUNITY_GitGuardian ignored-paths + ignored-matches for]]
- 1 edge to [[_COMMUNITY_Trivy (vulnerability scanner)]]
- 1 edge to [[_COMMUNITY_patch_telegram_send_base_url.py]]
- 1 edge to [[_COMMUNITY_Cron AgentShroud Daily Check-in]]
- 1 edge to [[_COMMUNITY_hermesskillsgraphifyreferencesextraction-spe]]
- 1 edge to [[_COMMUNITY_Constrained query-vocabulary expansion]]
- 1 edge to [[_COMMUNITY_hermesskillsi-architecture-reviewSKILL]]
- 1 edge to [[_COMMUNITY_hermesskillsi-chaos-engineeringSKILL]]
- 1 edge to [[_COMMUNITY_i-daedalus README — Concept Illustrator]]
- 1 edge to [[_COMMUNITY_hermesskillsi-devsecopsSKILL]]
- 1 edge to [[_COMMUNITY_i-hermes README — Podcast Production Orchestrato]]
- 1 edge to [[_COMMUNITY_i-incident-response SKILL (stub)]]
- 1 edge to [[_COMMUNITY_hermesskillsi-kaizenSKILL]]
- 1 edge to [[_COMMUNITY_hermesskillsi-kanbanSKILL]]
- 1 edge to [[_COMMUNITY_i-mac README — macOS System Administrator (MAC)]]
- 1 edge to [[_COMMUNITY_hermesskillsi-observabilitySKILL]]
- 1 edge to [[_COMMUNITY_hermesskillsi-scrumSKILL]]
- 1 edge to [[_COMMUNITY_hermesskillsi-value-stream-mappingSKILL]]
- 1 edge to [[_COMMUNITY_prefetch-ghsa-registry.sh]]
- 1 edge to [[_COMMUNITY_openclawskillsgraphifyreferencesextraction-s]]
- 1 edge to [[_COMMUNITY_graphify clone command]]
- 1 edge to [[_COMMUNITY_openclawskillsi-architecture-reviewSKILL]]
- 1 edge to [[_COMMUNITY_curriculum.md (input requirement)]]
- 1 edge to [[_COMMUNITY_openclawskillsi-chaos-engineeringSKILL]]
- 1 edge to [[_COMMUNITY_openclawskillsi-incident-responseSKILL]]
- 1 edge to [[_COMMUNITY_openclawskillsi-observabilitySKILL]]
- 1 edge to [[_COMMUNITY_openclawskillsi-value-stream-mappingSKILL]]
- 1 edge to [[_COMMUNITY_gateway-start.sh]]
- 1 edge to [[_COMMUNITY_get-credential.sh]]
- 1 edge to [[_COMMUNITY_Diagram 18 Runbook]]
- 1 edge to [[_COMMUNITY_Alert Thresholds (approval queue 1h timeout, con]]
- 1 edge to [[_COMMUNITY_Hermes Cannot Force-Switch to Custom-Named Local]]
- 1 edge to [[_COMMUNITY_Obsidian workspace.json (open-tab layout)]]
- 1 edge to [[_COMMUNITY_lvgl_kawaii_face.h (face animation public API)]]
- 1 edge to [[_COMMUNITY_audio.c (ES7210 mic  ES8311 speaker driver)]]
- 1 edge to [[_COMMUNITY__PII_PATTERNS (URL PII regex set)]]
- 1 edge to [[_COMMUNITY_LogSanitizer PII-Scrubbing Log Filter]]
- 1 edge to [[_COMMUNITY_.test_openclaw_version_pin_is_consistent_across_]]
- 1 edge to [[_COMMUNITY_.test_switch_model_script_uses_current_target_sy]]
- 1 edge to [[_COMMUNITY_Scorecard Data Integrity Tests (no stub inflatio]]
- 1 edge to [[_COMMUNITY_MiddlewareManager Session Enforcement Tests]]
- 1 edge to [[_COMMUNITY_SharedMemoryManager Merged Memory Tests]]
- 1 edge to [[_COMMUNITY_SlackAPIProxy Socket Mode Relay (apps.connection]]
- 1 edge to [[_COMMUNITY_SOC Auth WS Token IssuanceRedemption Tests]]
- 1 edge to [[_COMMUNITY_SOC Models SecurityEvent Tests]]
- 1 edge to [[_COMMUNITY_checkPrereqs()]]
- 1 edge to [[_COMMUNITY_loadRuntimes()]]
- 1 edge to [[_COMMUNITY_Dependabot Configuration]]
- 1 edge to [[_COMMUNITY_Release Workflow]]
- 1 edge to [[_COMMUNITY_i-tdd README]]
- 1 edge to [[_COMMUNITY_sidecar.py]]
- 1 edge to [[_COMMUNITY_CI test job (matrix ubuntumacos x py3.113.13)]]

## Top bridge nodes
- [[TelegramAPIProxy_3]] - degree 220, connects to 97 communities
- [[TestDefaultBotId]] - degree 9, connects to 3 communities
- [[.test_collaborator_egress_approval_banner_is_redacted_form()]] - degree 4, connects to 2 communities
- [[.test_collaborator_legacy_block_notice_is_normalized_form()]] - degree 4, connects to 2 communities
- [[.test_collaborator_legacy_protected_prefix_is_normalized_form()]] - degree 4, connects to 2 communities