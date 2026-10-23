---
type: community
cohesion: 0.04
members: 84
---

# asyncio

**Cohesion:** 0.04 - loosely connected
**Members:** 84 nodes

## Members
- [[dot-test_agent_label_falls_back_when_source_missing()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_alert_send_failure_is_swallowed()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_all_agents_omitting_bot_tokens_preserves_default_behavior()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_all_agents_runs_each_independently_and_isolates_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_all_agents_uses_per_agent_token_when_provided()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_check_scoped_to_agent_registry_and_repo()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_forward_file_download_aborts_at_size_limit()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_forward_file_download_returns_raw_body_sentinel()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_hermes_zero_stays_silent_via_all_agents()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_hermes_zero_still_reports_when_always_report_zero()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_openclaw_zero_stays_silent()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_oversized_document_update_is_dropped()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_api_path_still_json_parsed()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_file_download_error_returns_502()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_file_prefix_returns_binary_sentinel()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_within_limit_document_update_passes()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_zero_report_send_failure_is_swallowed()]] - code - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 fix Hermes zero-CVE heartbeats confused the owner because they're…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[2026-08-04 each wrapped agent's alert must go out via ITS OWN bot token (so it…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A Telegram failure on the new-CVE alert path never raises.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[A Telegram failure on the zero-report path never raises.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Backward compatibility no bot_tokens arg means every agent still gets the…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Build a minimal SecurityPipeline with passthrough PII + optional clamav.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[ClamAV scan_bytes returns error → fail-open CRITICAL log, FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Clean base64 payload → FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[If the per-agent source config is missing, the label falls back gracefully.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Inbound update with document.file_size  limit must be dropped (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size within limit must pass (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Malware-infected base64 payload → BLOCK with signature in block_reason.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[No clamav_scanner configured → step skipped, no error.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[OpenClaw and Hermes are processed on fully separate paths; one failing never…]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Owner wants to SEE a Hermes report even with 0 new advisories.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[Short base64 (64 groups of 4) skips ClamAV scan.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[TestFileDownload]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestPerAgentUpstreamChecks]] - code - gateway/tests/test_daily_cve_report.py
- [[Tests for ClamAV inline pipeline integration. Covers - scan_bytes() happy…]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Tests for _forward_file_download() and proxy_request() binary path. Regression…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Wrap bytes in a long-enough base64 chunk to trigger the scan (= 64 groups of…]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[_b64_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_boom_send()]] - code - gateway/tests/test_daily_cve_report.py
- [[_boom_send()_1]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_check()]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_15]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_16]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_17]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_18]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_19]] - code - gateway/tests/test_daily_cve_report.py
- [[_forward_file_download must raise when streamed bytes exceed limit…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_forward_file_download returns dict with _raw_body, _content_type, _status_code.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_instant_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_make_pipeline()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_passthrough()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_run_capture()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_timeout_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[asyncio_3]] - code
- [[check_upstream_cves(agent_id=...) selects that agent's OWN repo + list.]] - rationale - gateway/tests/test_daily_cve_report.py
- [[fake_run()]] - code - gateway/tests/test_clamav_pipeline.py
- [[parametrize_1]] - code
- [[proxy_request returns 502 sentinel when file download raises.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request with path_prefix='file' returns _raw_body sentinel (no JSON…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request without file prefix still JSON-parses the response.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[read()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[test_apt_repo_signatures_are_verified()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamav_comes_from_proposed_updates_and_nothing_else_does()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamav_pipeline.py]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_available_false_for_stale_socket_left_by_killed_daemon()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_available_false_when_socket_missing()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_available_true_when_daemon_listening()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_socket_constant_matches_both_images_clamd_conf()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_gateway_upgrades_pip_past_the_vendored_certifi_advisory()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_clean_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_error_fail_open()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_malware_blocked()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_not_configured()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_short_base64_not_scanned()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_preferred_scan_binary_falls_back_when_daemon_dead()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_preferred_scan_binary_uses_daemon_when_listening()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_run_clamscan_clamdscan_command_has_no_clamscan_only_flags()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_run_clamscan_clamscan_command_unchanged()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_binary_not_found()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_clean()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_empty_input()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_infected()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_timeout()]] - code - gateway/tests/test_clamav_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asyncio
SORT file.name ASC
```

## Connections to other communities
- 102 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 54 edges to [[_COMMUNITY_TestInboundPipelineOnGetUpdates]]
- 47 edges to [[_COMMUNITY_SecurityPipeline]]
- 20 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 19 edges to [[_COMMUNITY_fake_owner_notice()]]
- 16 edges to [[_COMMUNITY_format_cve_report() (2)]]
- 10 edges to [[_COMMUNITY_SlackSocketClient]]
- 8 edges to [[_COMMUNITY_First iteration ingests + records; second sees dedup and skips.]]
- 8 edges to [[_COMMUNITY_iCloud Services (4)]]
- 6 edges to [[_COMMUNITY_Sunday Upgrade Report — 2026-09-17 (prod, on-demand)]]
- 6 edges to [[_COMMUNITY_GroupApprovalRouter]]
- 5 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 4 edges to [[_COMMUNITY_dot-test_gives_up_and_marks_sent_after_max_retries()]]
- 3 edges to [[_COMMUNITY_OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)]]
- 3 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py (2)]]
- 3 edges to [[_COMMUNITY_dot-test_proxy_request_returns_ack_only_updates_when_all_dropped()]]
- 3 edges to [[_COMMUNITY_AgentShroud Enterprise Governance for Autonomous AI Agents (3)]]
- 2 edges to [[_COMMUNITY_dot-test_self_diagnose_dedupe_handles_missing_update_id_same_message()]]
- 2 edges to [[_COMMUNITY_climain.py]]
- 2 edges to [[_COMMUNITY_TestSendTelegramTruncation (2)]]
- 1 edge to [[_COMMUNITY_Regression guard (2026-08-30) the report scanned latest tags while deploys… (2)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (2) (2)]]
- 1 edge to [[_COMMUNITY_dot-test_collaborator_security_architecture_question_gets_safe_guidance()]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_with_mention_and_punctuation_is_handled_locally()]]
- 1 edge to [[_COMMUNITY_dot-test_healthcheck_word_with_punctuation_is_handled_locally()]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_🛡️ AgentShroud Release Plan (2)]]
- 1 edge to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_browserscriptsbrowse.py (2)]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_Common Queries]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]

## Top bridge nodes
- [[asyncio_3]] - degree 344, connects to 28 communities
- [[test_clamav_pipeline.py]] - degree 31, connects to 3 communities
- [[TestPerAgentUpstreamChecks]] - degree 11, connects to 1 community
- [[TestFileDownload]] - degree 9, connects to 1 community
- [[dot-test_oversized_document_update_is_dropped()]] - degree 6, connects to 1 community
