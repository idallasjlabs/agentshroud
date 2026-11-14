---
type: community
members: 42
---

# Community 148

**Members:** 42 nodes

## Members
- [[.test_agent_isolation_module()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_parse_clean()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_parse_infected()]] - code - gateway/tests/test_security_audit.py
- [[.test_network_validator_init()]] - code - gateway/tests/test_security_audit.py
- [[.test_parse_clean_output()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_output()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_has_timestamp()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_infected_files_details()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_infected_output()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_scanner_name()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_signatures()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_run_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_security_toolchain_clamav()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_falco()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_trivy()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_wazuh()]] - code - gateway/tests/test_security_audit.py
- [[.test_summary_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_error()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_infected()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_update_db_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_44]] - code - gateway/security/clamav_scanner.py
- [[Generate a summary dict suitable for the health report.      Args         repor]] - rationale - gateway/security/clamav_scanner.py
- [[Parse clamscan output into structured results.      Args         output Raw st]] - rationale - gateway/security/clamav_scanner.py
- [[Run ClamAV scan and return parsed results.      Args         target Directory]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[Test container hardening and runtime security.]] - rationale - gateway/tests/test_security_audit.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary]] - code - gateway/tests/test_security_toolchain.py
- [[TestContainerSecurity]] - code - gateway/tests/test_security_audit.py
- [[True if clamd accepts connections on its socket.      Connects rather than testi]] - rationale - gateway/security/clamav_scanner.py
- [[Update ClamAV virus database using freshclam.      Args         freshclam_bin]] - rationale - gateway/security/clamav_scanner.py
- [[clamav_scanner.py]] - code - gateway/security/clamav_scanner.py
- [[clamd_available()]] - code - gateway/security/clamav_scanner.py
- [[clamdscan' when the resident clamd can take the scan, else 'clamscan'.]] - rationale - gateway/security/clamav_scanner.py
- [[generate_summary()]] - code - gateway/security/clamav_scanner.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py
- [[preferred_scan_binary()]] - code - gateway/security/clamav_scanner.py
- [[run_clamscan()]] - code - gateway/security/clamav_scanner.py
- [[save_report()]] - code - gateway/security/clamav_scanner.py
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_148
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Community 41]]
- 7 edges to [[_COMMUNITY_Community 185]]
- 5 edges to [[_COMMUNITY_Community 7]]
- 5 edges to [[_COMMUNITY_Community 220]]
- 4 edges to [[_COMMUNITY_Community 0]]
- 4 edges to [[_COMMUNITY_Community 557]]
- 3 edges to [[_COMMUNITY_Community 162]]
- 2 edges to [[_COMMUNITY_Community 978]]
- 2 edges to [[_COMMUNITY_Community 72]]
- 2 edges to [[_COMMUNITY_Community 684]]
- 2 edges to [[_COMMUNITY_Community 71]]
- 2 edges to [[_COMMUNITY_Community 5]]
- 2 edges to [[_COMMUNITY_Community 146]]
- 1 edge to [[_COMMUNITY_Community 27]]
- 1 edge to [[_COMMUNITY_Community 709]]
- 1 edge to [[_COMMUNITY_Community 29]]
- 1 edge to [[_COMMUNITY_Community 166]]
- 1 edge to [[_COMMUNITY_Community 93]]
- 1 edge to [[_COMMUNITY_Community 108]]
- 1 edge to [[_COMMUNITY_Community 477]]
- 1 edge to [[_COMMUNITY_Community 235]]
- 1 edge to [[_COMMUNITY_Community 32]]
- 1 edge to [[_COMMUNITY_Community 121]]
- 1 edge to [[_COMMUNITY_Community 809]]
- 1 edge to [[_COMMUNITY_Community 365]]
- 1 edge to [[_COMMUNITY_Community 131]]

## Top bridge nodes
- [[TestContainerSecurity]] - degree 45, connects to 20 communities
- [[clamav_scanner.py]] - degree 12, connects to 4 communities
- [[run_clamscan()]] - degree 10, connects to 4 communities
- [[parse_clamscan_output()]] - degree 18, connects to 3 communities
- [[TestClamAVParser]] - degree 9, connects to 2 communities