---
type: community
members: 18
---

# Community 842

**Members:** 18 nodes

## Members
- [[.test_clean_when_installed_but_no_report()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_not_run_when_no_report_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_generate_summary_output()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_latest_sbom()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_none_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_none_when_no_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_two_when_sbom_present()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_zero_when_empty_sbom_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_zero_when_no_sbom_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[Return latest Trivy scan summary from saved reports.      When Trivy is installe]] - rationale - gateway/security/scanner_integration.py
- [[Return the latest SBOM (Software Bill of Materials) as parsed JSON.]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 3 Supply Chain (0-5).      0=no SBOM, 2=SBOM exists, 3=SBOM has pa]] - rationale - gateway/security/scanner_integration.py
- [[TestGetSbom]] - code - gateway/tests/test_scanner_integration.py
- [[TestGetTrivySummary]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSupplyChain]] - code - gateway/tests/test_scanner_integration.py
- [[_score_supply_chain()]] - code - gateway/security/scanner_integration.py
- [[get_sbom()]] - code - gateway/security/scanner_integration.py
- [[get_trivy_summary()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_842
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Community 67]]
- 6 edges to [[_COMMUNITY_Community 29]]
- 3 edges to [[_COMMUNITY_Community 10]]
- 3 edges to [[_COMMUNITY_Community 311]]
- 1 edge to [[_COMMUNITY_Community 151]]
- 1 edge to [[_COMMUNITY_Community 363]]
- 1 edge to [[_COMMUNITY_Community 102]]

## Top bridge nodes
- [[get_trivy_summary()]] - degree 16, connects to 6 communities
- [[get_sbom()]] - degree 9, connects to 3 communities
- [[_score_supply_chain()]] - degree 9, connects to 2 communities
- [[TestGetTrivySummary]] - degree 4, connects to 1 community
- [[TestGetSbom]] - degree 4, connects to 1 community