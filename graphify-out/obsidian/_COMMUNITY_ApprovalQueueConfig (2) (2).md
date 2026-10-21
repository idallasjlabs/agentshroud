---
type: community
members: 71
---

# ApprovalQueueConfig (2) (2)

**Members:** 71 nodes

## Members
- [[dot-test_blocked_command_uppercase_is_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_archive_exfil_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_function_calls_payload_text_is_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_hidden_channel_exfil_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_log_access_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_sensitive_path_probe_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_system_prompt_probe_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_forward_file_download_aborts_at_size_limit()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_forward_file_download_returns_raw_body_sentinel()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_no_alert_when_registry_current()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_no_telegram_send_when_no_token()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_non_owner_activity_is_tracked_for_unknown_user()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_domain_like_token_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_domain_with_invalid_chars_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_mixed_scheme_prefers_http_url_for_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_non_standard_web_port_does_not_queue_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_non_owner_url_with_trailing_backtick_still_queues_egress_preflight()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_oversized_document_update_is_dropped()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_api_path_still_json_parsed()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_file_download_error_returns_502()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_file_prefix_returns_binary_sentinel()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_rate_limit_notice_mentions_configured_limit()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_returns_error_on_github_api_failure()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_safe_info_response_exception_sends_unavailable_fallback()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_sends_alert_when_new_cves_found()]] - code - gateway/tests/test_daily_cve_report.py
- [[dot-test_start_resets_multi_turn_tracker_for_collaborator()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_within_limit_document_update_passes()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Archivebulk-export exfil prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator start should reset blocked multi-turn tracker session.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator function_calls payload should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Collaborator messages must not queue preflight approval even with valid https…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Direct log-content requests should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Domain-like tokens followed by identifier chars should not be treated as URLs.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Domains containing invalid hostname chars should not queue preflight approvals.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Exception in safe-info response should still deliver unavailable notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Hidden-channel exfil prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size  limit must be dropped (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size within limit must pass (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Rate-limit notice must reflect configured collaborator limit.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Sensitive path probes should be blockedquarantined for collaborators.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[System promptinstruction leakage probes should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[TestFileDownload]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[TestRunUpstreamCveCheck]] - code - gateway/tests/test_daily_cve_report.py
- [[Tests for _forward_file_download() and proxy_request() binary path. Regression…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Trailing markdown backticks should not prevent preflight queueing.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Unknown non-owner users should still be tracked at gateway level.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Uppercase collaborator blocked commands should still be quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[__init__()_2]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[_fake_send()_17]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_18]] - code - gateway/tests/test_daily_cve_report.py
- [[_fake_send()_19]] - code - gateway/tests/test_daily_cve_report.py
- [[_forward_file_download must raise when streamed bytes exceed limit…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_forward_file_download returns dict with _raw_body, _content_type, _status_code.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_instant_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[always_raise()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[asyncio_3]] - code
- [[check_async()_24]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_25]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_26]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_27]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[check_async()_28]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_urlopen()_75]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request returns 502 sentinel when file download raises.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request with path_prefix='file' returns _raw_body sentinel (no JSON…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request without file prefix still JSON-parses the response.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[read()_3]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[record_activity()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[reset_session()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[test_scan_bytes_clean()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_infected()]] - code - gateway/tests/test_clamav_pipeline.py
- [[web_fetch preflight approvals should only allow standard web ports.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig_2_2
SORT file.name ASC
```

## Connections to other communities
- 220 edges to [[_COMMUNITY_ApprovalQueueConfig (2)]]
- 47 edges to [[_COMMUNITY_SecurityPipeline]]
- 20 edges to [[_COMMUNITY_TestCollaboratorPromptClassifiers]]
- 19 edges to [[_COMMUNITY_fake_owner_notice()]]
- 15 edges to [[_COMMUNITY_climain.py]]
- 15 edges to [[_COMMUNITY_OpenClaw and Hermes are processed on fully separate paths; one failing never… (2)]]
- 11 edges to [[_COMMUNITY_First iteration ingests + records; second sees dedup and skips.]]
- 10 edges to [[_COMMUNITY_SlackSocketClient]]
- 8 edges to [[_COMMUNITY_iCloud Services (4)]]
- 6 edges to [[_COMMUNITY_sync-cve-registry.py]]
- 6 edges to [[_COMMUNITY_format_cve_report() (2)]]
- 6 edges to [[_COMMUNITY_Sunday Upgrade Report — 2026-09-17 (prod, on-demand)]]
- 6 edges to [[_COMMUNITY_GroupApprovalRouter]]
- 3 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py (2)]]
- 3 edges to [[_COMMUNITY_AgentShroud Enterprise Governance for Autonomous AI Agents (3)]]
- 2 edges to [[_COMMUNITY_TestSendTelegramTruncation (2)]]
- 1 edge to [[_COMMUNITY_ServiceManager]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (2) (5)]]
- 1 edge to [[_COMMUNITY_TestScoreMalwareDefense]]
- 1 edge to [[_COMMUNITY_Regression guard (2026-08-30) the report scanned latest tags while deploys… (2)]]
- 1 edge to [[_COMMUNITY_🛡️ AgentShroud Release Plan (2)]]
- 1 edge to [[_COMMUNITY_browserscriptsbrowse.py (2)]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_test_voice_gateway.py]]

## Top bridge nodes
- [[asyncio_3]] - degree 344, connects to 24 communities
- [[dot-test_safe_info_response_exception_sends_unavailable_fallback()]] - degree 5, connects to 2 communities
- [[TestFileDownload]] - degree 9, connects to 1 community
- [[dot-test_non_owner_activity_is_tracked_for_unknown_user()]] - degree 9, connects to 1 community
- [[dot-test_non_owner_domain_like_token_does_not_queue_egress_preflight()]] - degree 8, connects to 1 community
