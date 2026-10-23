---
type: community
cohesion: 0.08
members: 36
---

# Common Queries

**Cohesion:** 0.08 - loosely connected
**Members:** 36 nodes

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
- [[dot-test_summary_clean()_3]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_error()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_infected()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_update_db_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_30]] - code
- [[Generate a summary dict suitable for the health report. Args report Parsed…]] - rationale - gateway/security/clamav_scanner.py
- [[Parse clamscan output into structured results. Args output Raw stdout from…]] - rationale - gateway/security/clamav_scanner.py
- [[Run ClamAV scan and return parsed results. Args target Directory or file to…]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[Stream bytes to clamdscan for inline malware scanning. Uses ``clamdscan…]] - rationale - gateway/security/clamav_scanner.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[True if clamd accepts connections on its socket. Connects rather than testing…]] - rationale - gateway/security/clamav_scanner.py
- [[Update ClamAV virus database using freshclam. Args freshclam_bin Path to…]] - rationale - gateway/security/clamav_scanner.py
- [[clamav_scanner.py]] - code - gateway/security/clamav_scanner.py
- [[clamd_available()]] - code - gateway/security/clamav_scanner.py
- [[clamdscan' when the resident clamd can take the scan, else 'clamscan'.]] - rationale - gateway/security/clamav_scanner.py
- [[generate_summary()]] - code - gateway/security/clamav_scanner.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py
- [[preferred_scan_binary()]] - code - gateway/security/clamav_scanner.py
- [[run_clamscan()]] - code - gateway/security/clamav_scanner.py
- [[save_report()]] - code - gateway/security/clamav_scanner.py
- [[scan_bytes()]] - code - gateway/security/clamav_scanner.py
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Common_Queries
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_ContextGuard]]
- 7 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 3 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_AgentTarget (2)]]
- 1 edge to [[_COMMUNITY_SecureBrowser (4) (2)]]
- 1 edge to [[_COMMUNITY_SecureBrowser (4)]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]
- 1 edge to [[_COMMUNITY_GitHub Skill]]
- 1 edge to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 1 edge to [[_COMMUNITY_dot-_run_and_read]]
- 1 edge to [[_COMMUNITY_test_main_endpoints.py]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_HeuristicClassifier]]
- 1 edge to [[_COMMUNITY_EgressFilter]]

## Top bridge nodes
- [[clamav_scanner.py]] - degree 17, connects to 8 communities
- [[run_clamscan()]] - degree 10, connects to 4 communities
- [[parse_clamscan_output()]] - degree 18, connects to 2 communities
- [[TestClamAVParser]] - degree 9, connects to 2 communities
- [[Any_30]] - degree 8, connects to 2 communities
