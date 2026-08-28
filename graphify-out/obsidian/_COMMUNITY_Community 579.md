---
type: community
cohesion: 0.18
members: 16
---

# Community 579

**Cohesion:** 0.18 - loosely connected
**Members:** 16 nodes

## Members
- [[.test_clamav_parse_clean()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_parse_infected()]] - code - gateway/tests/test_security_audit.py
- [[.test_parse_clean_output()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_empty_output()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_has_timestamp()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_infected_files_details()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_infected_output()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_scanner_name()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_parse_signatures()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_clean()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_error()_1]] - code - gateway/tests/test_security_toolchain.py
- [[.test_summary_infected()]] - code - gateway/tests/test_security_toolchain.py
- [[Parse clamscan output into structured results.      Args         output Raw st]] - rationale - gateway/security/clamav_scanner.py
- [[TestClamAVParser]] - code - gateway/tests/test_security_toolchain.py
- [[TestClamAVSummary]] - code - gateway/tests/test_security_toolchain.py
- [[parse_clamscan_output()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_579
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 5 edges to [[_COMMUNITY_Community 112]]
- 1 edge to [[_COMMUNITY_Community 410]]
- 1 edge to [[_COMMUNITY_Community 330]]

## Top bridge nodes
- [[parse_clamscan_output()]] - degree 18, connects to 4 communities
- [[TestClamAVParser]] - degree 9, connects to 2 communities
- [[TestClamAVSummary]] - degree 5, connects to 2 communities
- [[.test_clamav_parse_clean()]] - degree 2, connects to 1 community
- [[.test_clamav_parse_infected()]] - degree 2, connects to 1 community