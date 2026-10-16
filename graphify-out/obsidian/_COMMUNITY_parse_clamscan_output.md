---
type: community
cohesion: 0.09
members: 31
---

# parse_clamscan_output

**Cohesion:** 0.09 - loosely connected
**Members:** 31 nodes

## Members
- [[dot-test_clamav_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clamav_parse_clean()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clamav_parse_infected()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_parse_clean_output()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_output()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_has_timestamp()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_infected_files_details()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_infected_output()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_scanner_name()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_signatures()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_run_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_clean()_2]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_error()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_infected()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_update_db_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_38]] - code - gateway/security/clamav_scanner.py
- [[Parse clamscan output into structured results.      Args         output Raw st]] - rationale - gateway/security/clamav_scanner.py
- [[Path_25]] - code - gateway/security/clamav_scanner.py
- [[Run ClamAV scan and return parsed results.      Args         target Directory]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[Update ClamAV virus database using freshclam.      Args         freshclam_bin]] - rationale - gateway/security/clamav_scanner.py
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[clamav_scanner.py]] - code - gateway/security/clamav_scanner.py
- [[drift_detector.py]] - code - gateway/security/drift_detector.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py
- [[run_clamscan()]] - code - gateway/security/clamav_scanner.py
- [[save_report()]] - code - gateway/security/clamav_scanner.py
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/parse_clamscan_output
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AlertDispatcher]]
- 6 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 3 edges to [[_COMMUNITY_test_clamav_pipeline.py]]
- 2 edges to [[_COMMUNITY_FalcoAlertWatcher]]
- 2 edges to [[_COMMUNITY_AgentRegistry]]
- 2 edges to [[_COMMUNITY_All Dependencies]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_WebContentScanner]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py_1]]
- 1 edge to [[_COMMUNITY_test_e2e_proxy.py]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_FR3 System Integrity]]
- 1 edge to [[_COMMUNITY_dot-_process_connect]]
- 1 edge to [[_COMMUNITY_WebProxyConfig]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]]

## Top bridge nodes
- [[clamav_scanner.py]] - degree 13, connects to 7 communities
- [[alert_dispatcher.py]] - degree 10, connects to 7 communities
- [[run_clamscan()]] - degree 10, connects to 4 communities
- [[parse_clamscan_output()]] - degree 18, connects to 3 communities
- [[drift_detector.py]] - degree 7, connects to 3 communities
