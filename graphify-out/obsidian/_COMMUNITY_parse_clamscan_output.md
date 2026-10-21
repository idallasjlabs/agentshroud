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
- [[Any_38]] - code
- [[Generate a summary dict suitable for the health report. Args report Parsed…]] - rationale - gateway/security/clamav_scanner.py
- [[Parse clamscan output into structured results. Args output Raw stdout from…]] - rationale - gateway/security/clamav_scanner.py
- [[Run ClamAV scan and return parsed results. Args target Directory or file to…]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[Update ClamAV virus database using freshclam. Args freshclam_bin Path to…]] - rationale - gateway/security/clamav_scanner.py
- [[clamav_scanner.py]] - code - gateway/security/clamav_scanner.py
- [[generate_summary()]] - code - gateway/security/clamav_scanner.py
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
- 10 edges to [[_COMMUNITY_AlertDispatcher]]
- 7 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 7 edges to [[_COMMUNITY_asyncio]]
- 2 edges to [[_COMMUNITY_dot-proxy_messages()]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_dot-_process_connect]]
- 1 edge to [[_COMMUNITY_egress_filter.py]]
- 1 edge to [[_COMMUNITY_triage-cve-mitigations.py]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor (2)]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_lifespan()]]
- 1 edge to [[_COMMUNITY_egress_filter.py (3)]]
- 1 edge to [[_COMMUNITY_WebContentScanner]]
- 1 edge to [[_COMMUNITY_All Dependencies]]

## Top bridge nodes
- [[clamav_scanner.py]] - degree 17, connects to 8 communities
- [[run_clamscan()]] - degree 11, connects to 5 communities
- [[parse_clamscan_output()]] - degree 18, connects to 3 communities
- [[TestClamAVParser]] - degree 9, connects to 2 communities
- [[Any_38]] - degree 8, connects to 2 communities
