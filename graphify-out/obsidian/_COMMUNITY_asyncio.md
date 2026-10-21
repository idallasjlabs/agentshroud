---
type: community
members: 64
---

# asyncio

**Members:** 64 nodes

## Members
- [[dot-test_collaborator_policy_bypass_request_is_blocked_and_quarantined()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_rate_limit_notice_includes_retry_window()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_collaborator_revoke_command_is_blocked()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_forward_file_download_aborts_at_size_limit()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_forward_file_download_returns_raw_body_sentinel()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_api_path_still_json_parsed()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_file_download_error_returns_502()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_proxy_request_file_prefix_returns_binary_sentinel()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[dot-test_within_limit_document_update_passes()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Build a minimal SecurityPipeline with passthrough PII + optional clamav.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Bypassdisable-policy prompts should be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[ClamAV scan_bytes returns error → fail-open CRITICAL log, FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Clean base64 payload → FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Collaborator revoke command must be blocked and quarantined.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Inbound update with document.file_size within limit must pass (CVE-2026-32049).]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Malware-infected base64 payload → BLOCK with signature in block_reason.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[No clamav_scanner configured → step skipped, no error.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Rate-limited collaborators should receive a deterministic retry-window notice.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[Short base64 (64 groups of 4) skips ClamAV scan.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Stream bytes to clamdscan for inline malware scanning. Uses ``clamdscan…]] - rationale - gateway/security/clamav_scanner.py
- [[TestFileDownload]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[Tests for ClamAV inline pipeline integration. Covers - scan_bytes() happy…]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Tests for _forward_file_download() and proxy_request() binary path. Regression…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[True if clamd accepts connections on its socket. Connects rather than testing…]] - rationale - gateway/security/clamav_scanner.py
- [[Wrap bytes in a long-enough base64 chunk to trigger the scan (= 64 groups of…]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[_b64_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_forward_file_download must raise when streamed bytes exceed limit…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_forward_file_download returns dict with _raw_body, _content_type, _status_code.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[_instant_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_make_pipeline()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_passthrough()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_run_capture()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_timeout_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[asyncio_3]] - code
- [[clamd_available()]] - code - gateway/security/clamav_scanner.py
- [[clamdscan' when the resident clamd can take the scan, else 'clamscan'.]] - rationale - gateway/security/clamav_scanner.py
- [[fake_notify()]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[fake_run()]] - code - gateway/tests/test_clamav_pipeline.py
- [[fake_urlopen()_21]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[preferred_scan_binary()]] - code - gateway/security/clamav_scanner.py
- [[proxy_request returns 502 sentinel when file download raises.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request with path_prefix='file' returns _raw_body sentinel (no JSON…]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[proxy_request without file prefix still JSON-parses the response.]] - rationale - gateway/tests/test_telegram_proxy_inbound.py
- [[read()_1]] - code - gateway/tests/test_telegram_proxy_inbound.py
- [[scan_bytes()]] - code - gateway/security/clamav_scanner.py
- [[test_clamav_pipeline.py]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_available_false_for_stale_socket_left_by_killed_daemon()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_available_false_when_socket_missing()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_available_true_when_daemon_listening()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_socket_constant_matches_both_images_clamd_conf()]] - code - gateway/tests/test_clamav_pipeline.py
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
- 113 edges to [[_COMMUNITY__wrap_response()]]
- 58 edges to [[_COMMUNITY_TestInboundPipelineOnGetUpdates]]
- 45 edges to [[_COMMUNITY_dot-_make_proxy()]]
- 20 edges to [[_COMMUNITY__make_proxy()]]
- 19 edges to [[_COMMUNITY_fake_owner_notice()]]
- 10 edges to [[_COMMUNITY_dot-test_collaborator_web_access_imperative_with_url_queues_owner_approval()]]
- 8 edges to [[_COMMUNITY_test_telegram_proxy_inbound.py]]
- 8 edges to [[_COMMUNITY_TestFullAccessMiddlewareBypass]]
- 7 edges to [[_COMMUNITY_parse_clamscan_output]]
- 6 edges to [[_COMMUNITY_dot-test_stranger_within_limit_triggers_approval_workflow()]]
- 3 edges to [[_COMMUNITY_dot-test_unknown_user_always_gets_pending_or_rate_limit_notice()]]
- 3 edges to [[_COMMUNITY_lifespan()]]
- 3 edges to [[_COMMUNITY_dot-test_proxy_request_returns_ack_only_updates_when_all_dropped()]]
- 3 edges to [[_COMMUNITY_dot-test_collaborator_rate_limit_notice_is_sent_for_each_limited_message()]]
- 2 edges to [[_COMMUNITY_dot-test_self_diagnose_dedupe_handles_missing_update_id_same_message()]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 2 edges to [[_COMMUNITY_test_image_verifier.py]]
- 1 edge to [[_COMMUNITY_test_security_regressions_v1_2.py]]
- 1 edge to [[_COMMUNITY_dot-test_egress_callback_from_collaborator_is_rejected()]]
- 1 edge to [[_COMMUNITY_test_fieldflare_route_strips_unsupported_fields_streaming]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]

## Top bridge nodes
- [[asyncio_3]] - degree 302, connects to 18 communities
- [[test_clamav_pipeline.py]] - degree 29, connects to 3 communities
- [[preferred_scan_binary()]] - degree 7, connects to 3 communities
- [[scan_bytes()]] - degree 11, connects to 2 communities
- [[TestFileDownload]] - degree 9, connects to 2 communities
