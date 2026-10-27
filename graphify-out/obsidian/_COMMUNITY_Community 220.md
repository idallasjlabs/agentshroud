---
type: community
members: 40
---

# Community 220

**Members:** 40 nodes

## Members
- [[Build a minimal SecurityPipeline with passthrough PII + optional clamav.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[ClamAV scan_bytes returns error → fail-open CRITICAL log, FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Clean base64 payload → FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Malware-infected base64 payload → BLOCK with signature in block_reason.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[No clamav_scanner configured → step skipped, no error.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Path_8]] - code - gateway/security/clamav_scanner.py
- [[Short base64 (64 groups of 4) skips ClamAV scan.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Stream bytes to clamdscan for inline malware scanning.      Uses ``clamdscan --s]] - rationale - gateway/security/clamav_scanner.py
- [[Test replacement for asyncio.wait_for — awaits coroutine directly.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Test replacement for asyncio.wait_for — raises TimeoutError.      Closes the un-]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Wrap bytes in a long-enough base64 chunk to trigger the scan (= 64 groups of 4)]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[_b64_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_instant_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_make_pipeline()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_run_capture()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_timeout_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[clamd_sock_path()]] - code - gateway/tests/test_clamav_pipeline.py
- [[scan_bytes()]] - code - gateway/security/clamav_scanner.py
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
TABLE source_file, type FROM #community/Community_220
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 37]]
- 5 edges to [[_COMMUNITY_Community 148]]
- 2 edges to [[_COMMUNITY_Community 24]]
- 1 edge to [[_COMMUNITY_Community 104]]
- 1 edge to [[_COMMUNITY_Community 63]]

## Top bridge nodes
- [[test_clamav_pipeline.py]] - degree 31, connects to 3 communities
- [[scan_bytes()]] - degree 11, connects to 2 communities
- [[_make_pipeline()]] - degree 8, connects to 1 community
- [[Path_8]] - degree 5, connects to 1 community
- [[test_pipeline_clamav_clean_payload()]] - degree 5, connects to 1 community