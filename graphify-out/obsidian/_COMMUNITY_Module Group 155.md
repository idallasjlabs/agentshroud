---
type: community
cohesion: 0.09
members: 31
---

# Module Group 155

**Cohesion:** 0.09 - loosely connected
**Members:** 31 nodes

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
- [[Any_30]] - code - gateway/security/clamav_scanner.py
- [[Generate a summary dict suitable for the health report.      Args         repor]] - rationale - gateway/security/clamav_scanner.py
- [[Parse clamscan output into structured results.      Args         output Raw st]] - rationale - gateway/security/clamav_scanner.py
- [[Path_7]] - code - gateway/security/clamav_scanner.py
- [[Run ClamAV scan and return parsed results.      Args         target Directory]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary]] - code - gateway/tests/test_security_toolchain.py
- [[Update ClamAV virus database using freshclam.      Args         freshclam_bin]] - rationale - gateway/security/clamav_scanner.py
- [[clamav_scanner.py]] - code - gateway/security/clamav_scanner.py
- [[generate_summary()]] - code - gateway/security/clamav_scanner.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py
- [[run_clamscan()]] - code - gateway/security/clamav_scanner.py
- [[save_report()]] - code - gateway/security/clamav_scanner.py
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_155
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Module Group 141]]
- 6 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 3 edges to [[_COMMUNITY_Alert Dispatcher]]
- 3 edges to [[_COMMUNITY_Module Group 184]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Module Group 240]]
- 1 edge to [[_COMMUNITY_Module Group 303]]
- 1 edge to [[_COMMUNITY_Security Scanner Integration]]

## Top bridge nodes
- [[run_clamscan()]] - degree 10, connects to 4 communities
- [[parse_clamscan_output()]] - degree 18, connects to 3 communities
- [[clamav_scanner.py]] - degree 8, connects to 3 communities
- [[TestClamAVParser]] - degree 9, connects to 2 communities
- [[generate_summary()]] - degree 5, connects to 2 communities