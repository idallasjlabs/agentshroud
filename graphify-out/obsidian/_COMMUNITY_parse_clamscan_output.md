---
type: community
members: 30
---

# parse_clamscan_output

**Members:** 30 nodes

## Members
- [[dot-test_clamav_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clamav_parse_clean()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clamav_parse_infected()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_parse_clean_output()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_output()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_has_timestamp()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_infected_files_details()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_infected_output()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_scanner_name()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_signatures()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_2]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_error()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_infected()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_update_db_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_39]] - code - gateway/security/clamav_scanner.py
- [[Generate a summary dict suitable for the health report.      Args         alert]] - rationale - gateway/security/falco_monitor.py
- [[Parse clamscan output into structured results.      Args         output Raw st]] - rationale - gateway/security/clamav_scanner.py
- [[Path_30]] - code - gateway/security/clamav_scanner.py
- [[Run ClamAV scan and return parsed results.      Args         target Directory]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[Update ClamAV virus database using freshclam.      Args         freshclam_bin]] - rationale - gateway/security/clamav_scanner.py
- [[generate_summary()_1]] - code - gateway/security/clamav_scanner.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py
- [[run_clamscan()]] - code - gateway/security/clamav_scanner.py
- [[save_report()_1]] - code - gateway/security/clamav_scanner.py
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/parse_clamscan_output
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AlertDispatcher (2)]]
- 7 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_test_clamav_pipeline.py]]
- 1 edge to [[_COMMUNITY_FalcoAlertWatcher]]
- 1 edge to [[_COMMUNITY_dot-_process_connect]]
- 1 edge to [[_COMMUNITY_WebProxyConfig]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]

## Top bridge nodes
- [[run_clamscan()]] - degree 10, connects to 4 communities
- [[parse_clamscan_output()]] - degree 18, connects to 3 communities
- [[generate_summary()_1]] - degree 5, connects to 3 communities
- [[TestClamAVParser]] - degree 9, connects to 2 communities
- [[update_virus_db()]] - degree 5, connects to 2 communities
