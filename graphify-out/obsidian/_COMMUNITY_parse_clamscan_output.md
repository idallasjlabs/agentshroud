---
type: community
members: 25
---

# parse_clamscan_output

**Members:** 25 nodes

## Members
- [[dot-test_agent_isolation_module()]] - code - gateway/tests/test_security_audit.py
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
- [[Parse clamscan output into structured results. Args output Raw stdout from…]] - rationale - gateway/security/clamav_scanner.py
- [[Test container hardening and runtime security.]] - rationale - gateway/tests/test_security_audit.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary_1]] - code - gateway/tests/test_security_toolchain.py
- [[TestContainerSecurity]] - code - gateway/tests/test_security_audit.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/parse_clamscan_output
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_test_clamav_pipeline.py]]
- 3 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_NetworkValidator]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_run_trivy_scan]]

## Top bridge nodes
- [[TestContainerSecurity]] - degree 14, connects to 4 communities
- [[parse_clamscan_output()]] - degree 18, connects to 3 communities
- [[TestClamAVParser]] - degree 8, connects to 1 community
- [[TestClamAVSummary_1]] - degree 4, connects to 1 community
- [[dot-test_network_validator_init()]] - degree 2, connects to 1 community
