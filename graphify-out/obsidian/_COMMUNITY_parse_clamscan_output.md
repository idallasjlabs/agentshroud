---
type: community
members: 34
---

# parse_clamscan_output

**Members:** 34 nodes

## Members
- [[dot-test_agent_isolation_module()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clamav_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clamav_parse_clean()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_clamav_parse_infected()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_network_validator_init()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_parse_clean_output()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_empty_output()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_has_timestamp()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_infected_files_details()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_infected_output()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_scanner_name()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_parse_signatures()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_security_toolchain_clamav()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_security_toolchain_falco()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_security_toolchain_trivy()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_security_toolchain_wazuh()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_summary_clean()_3]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_error()_1]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_summary_infected()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_trivy_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[Any_74]] - code
- [[Generate a summary dict suitable for the health report. Args report Parsed…_1]] - rationale - gateway/security/clamav_scanner.py
- [[Parse clamscan output into structured results. Args output Raw stdout from…]] - rationale - gateway/security/clamav_scanner.py
- [[Path_63]] - code
- [[Run ClamAV scan and return parsed results. Args target Directory or file to…]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[Test container hardening and runtime security.]] - rationale - gateway/tests/test_security_audit.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[TestContainerSecurity]] - code - gateway/tests/test_security_audit.py
- [[generate_summary()_3]] - code - gateway/security/clamav_scanner.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py
- [[run_clamscan()_1]] - code - gateway/security/clamav_scanner.py
- [[save_report()_1]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/parse_clamscan_output
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_PipelineAction]]
- 5 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 3 edges to [[_COMMUNITY_test_security_audit.py]]
- 3 edges to [[_COMMUNITY_run_trivy_scan]]
- 2 edges to [[_COMMUNITY_NetworkValidator]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_dot-_relay]]
- 1 edge to [[_COMMUNITY_WebProxy]]

## Top bridge nodes
- [[run_clamscan()_1]] - degree 11, connects to 6 communities
- [[parse_clamscan_output()]] - degree 18, connects to 3 communities
- [[TestContainerSecurity]] - degree 14, connects to 3 communities
- [[generate_summary()_3]] - degree 5, connects to 3 communities
- [[Any_74]] - degree 6, connects to 2 communities
