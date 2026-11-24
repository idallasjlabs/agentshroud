---
type: community
members: 53
---

# PipelineAction

**Members:** 53 nodes

## Members
- [[Build a minimal SecurityPipeline with passthrough PII + optional clamav.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[ClamAV scan_bytes returns error → fail-open CRITICAL log, FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Clean base64 payload → FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Enum_23]] - code
- [[Malware-infected base64 payload → BLOCK with signature in block_reason.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[No clamav_scanner configured → step skipped, no error.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[PipelineAction]] - code - gateway/proxy/pipeline.py
- [[Short base64 (64 groups of 4) skips ClamAV scan.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Stream bytes to clamdscan for inline malware scanning. Uses ``clamdscan…]] - rationale - gateway/security/clamav_scanner.py
- [[Test replacement for asyncio.wait_for — awaits coroutine directly.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Test replacement for asyncio.wait_for — raises TimeoutError. Closes the un-…]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Tests for ClamAV inline pipeline integration. Covers - scan_bytes() happy…]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[True if clamd accepts connections on its socket. Connects rather than testing…]] - rationale - gateway/security/clamav_scanner.py
- [[Wrap bytes in a long-enough base64 chunk to trigger the scan (= 64 groups of…]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[_b64_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_instant_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_make_pipeline()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_passthrough()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_run_capture()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_timeout_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[asyncio_31]] - code
- [[clamav_scanner.py_2]] - code - gateway/security/clamav_scanner.py
- [[clamd_available()]] - code - gateway/security/clamav_scanner.py
- [[clamd_sock_path()]] - code - gateway/tests/test_clamav_pipeline.py
- [[clamdscan' when the resident clamd can take the scan, else 'clamscan'.]] - rationale - gateway/security/clamav_scanner.py
- [[fake_run()_3]] - code - gateway/tests/test_clamav_pipeline.py
- [[fixture_58]] - code
- [[parametrize_12]] - code
- [[preferred_scan_binary()]] - code - gateway/security/clamav_scanner.py
- [[scan_bytes()]] - code - gateway/security/clamav_scanner.py
- [[str_14]] - code
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
TABLE source_file, type FROM #community/PipelineAction
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_test_e2e_proxy.py]]
- 7 edges to [[_COMMUNITY_AsyncMock]]
- 7 edges to [[_COMMUNITY_parse_clamscan_output]]
- 5 edges to [[_COMMUNITY_SecurityPipeline]]
- 4 edges to [[_COMMUNITY_test_e2e_watchtower.py]]
- 4 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]
- 3 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_test_telegram_pipeline.py]]
- 2 edges to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_run_trivy_scan]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_test_security_audit.py]]

## Top bridge nodes
- [[PipelineAction]] - degree 35, connects to 7 communities
- [[clamav_scanner.py_2]] - degree 13, connects to 6 communities
- [[test_clamav_pipeline.py]] - degree 34, connects to 2 communities
- [[scan_bytes()]] - degree 11, connects to 2 communities
- [[preferred_scan_binary()]] - degree 7, connects to 2 communities
