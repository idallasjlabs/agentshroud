---
type: community
cohesion: 0.15
members: 18
---

# Community 518

**Cohesion:** 0.15 - loosely connected
**Members:** 18 nodes

## Members
- [[dot-test_clean_when_installed_but_no_report()_1]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_not_run_when_no_report_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_generate_summary_output()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_latest_sbom()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_when_no_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_sbom_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_empty_sbom_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_no_sbom_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[Return latest Trivy scan summary from saved reports.      When Trivy is installe]] - rationale - gateway/security/scanner_integration.py
- [[Return the latest SBOM (Software Bill of Materials) as parsed JSON.]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 3 Supply Chain (0-5).      0=no SBOM, 2=SBOM exists, 3=SBOM has pa]] - rationale - gateway/security/scanner_integration.py
- [[TestGetSbom_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetTrivySummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSupplyChain]] - code - gateway/tests/test_scanner_integration.py
- [[_score_supply_chain()]] - code - gateway/security/scanner_integration.py
- [[get_sbom()_1]] - code - gateway/security/scanner_integration.py
- [[get_trivy_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_518
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 73]]
- 4 edges to [[_COMMUNITY_Community 60]]
- 3 edges to [[_COMMUNITY_SOC Correlation & Router]]
- 3 edges to [[_COMMUNITY_Community 275]]
- 2 edges to [[_COMMUNITY_Community 168]]
- 1 edge to [[_COMMUNITY_Approval Routing & Event Bus]]
- 1 edge to [[_COMMUNITY_Community 292]]
- 1 edge to [[_COMMUNITY_Community 550]]

## Top bridge nodes
- [[get_trivy_summary()]] - degree 16, connects to 7 communities
- [[get_sbom()_1]] - degree 9, connects to 3 communities
- [[_score_supply_chain()]] - degree 9, connects to 3 communities
- [[TestGetSbom_1]] - degree 4, connects to 1 community
- [[TestGetTrivySummary]] - degree 4, connects to 1 community