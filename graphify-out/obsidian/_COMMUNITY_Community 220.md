---
type: community
members: 74
---

# Community 220

**Members:** 74 nodes

## Members
- [[.test_clamav_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_parse_clean()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_parse_infected()]] - code - gateway/tests/test_security_audit.py
- [[.test_parse_clean_output()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_output()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_has_timestamp()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_infected_files_details()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_infected_output()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_scanner_name()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_signatures()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_error()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_infected()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_update_db_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_34]] - code - gateway/security/clamav_scanner.py
- [[Build a minimal SecurityPipeline with passthrough PII + optional clamav.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[ClamAV scan_bytes returns error → fail-open CRITICAL log, FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Clean base64 payload → FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Generate a summary dict suitable for the health report.      Args         repor]] - rationale - gateway/security/clamav_scanner.py
- [[Malware-infected base64 payload → BLOCK with signature in block_reason.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[No clamav_scanner configured → step skipped, no error.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Parse clamscan output into structured results.      Args         output Raw st]] - rationale - gateway/security/clamav_scanner.py
- [[Path_8]] - code - gateway/security/clamav_scanner.py
- [[Run ClamAV scan and return parsed results.      Args         target Directory]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[Short base64 (64 groups of 4) skips ClamAV scan.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Stream bytes to clamdscan for inline malware scanning.      Uses ``clamdscan --s]] - rationale - gateway/security/clamav_scanner.py
- [[Test replacement for asyncio.wait_for — awaits coroutine directly.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Test replacement for asyncio.wait_for — raises TimeoutError.      Closes the un-]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary]] - code - gateway/tests/test_security_toolchain.py
- [[True if clamd accepts connections on its socket.      Connects rather than testi]] - rationale - gateway/security/clamav_scanner.py
- [[Update ClamAV virus database using freshclam.      Args         freshclam_bin]] - rationale - gateway/security/clamav_scanner.py
- [[Wrap bytes in a long-enough base64 chunk to trigger the scan (= 64 groups of 4)]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[_b64_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_instant_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_make_pipeline()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_run_capture()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_timeout_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[clamav_scanner.py]] - code - gateway/security/clamav_scanner.py
- [[clamd_available()]] - code - gateway/security/clamav_scanner.py
- [[clamd_sock_path()]] - code - gateway/tests/test_clamav_pipeline.py
- [[clamdscan' when the resident clamd can take the scan, else 'clamscan'.]] - rationale - gateway/security/clamav_scanner.py
- [[generate_summary()]] - code - gateway/security/clamav_scanner.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py
- [[preferred_scan_binary()]] - code - gateway/security/clamav_scanner.py
- [[run_clamscan()]] - code - gateway/security/clamav_scanner.py
- [[save_report()]] - code - gateway/security/clamav_scanner.py
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
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_220
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 0]]
- 7 edges to [[_COMMUNITY_Community 185]]
- 7 edges to [[_COMMUNITY_Community 1127]]
- 4 edges to [[_COMMUNITY_Community 24]]
- 2 edges to [[_COMMUNITY_Community 6]]
- 2 edges to [[_COMMUNITY_Community 84]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 709]]
- 1 edge to [[_COMMUNITY_Community 29]]

## Top bridge nodes
- [[run_clamscan()]] - degree 10, connects to 4 communities
- [[clamav_scanner.py]] - degree 12, connects to 3 communities
- [[test_clamav_pipeline.py]] - degree 31, connects to 2 communities
- [[parse_clamscan_output()]] - degree 18, connects to 2 communities
- [[TestClamAVParser]] - degree 9, connects to 2 communities