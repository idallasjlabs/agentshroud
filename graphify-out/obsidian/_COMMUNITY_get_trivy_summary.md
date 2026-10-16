---
type: community
cohesion: 0.23
members: 12
---

# get_trivy_summary

**Cohesion:** 0.23 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-test_returns_latest_sbom()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_for_empty_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_none_when_no_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_two_when_sbom_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_empty_sbom_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_no_sbom_dir()]] - code - gateway/tests/test_scanner_integration.py
- [[Return the latest SBOM (Software Bill of Materials) as parsed JSON.]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 3 Supply Chain (0-5).      0=no SBOM, 2=SBOM exists, 3=SBOM has pa]] - rationale - gateway/security/scanner_integration.py
- [[TestGetSbom_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreSupplyChain]] - code - gateway/tests/test_scanner_integration.py
- [[_score_supply_chain()]] - code - gateway/security/scanner_integration.py
- [[get_sbom()_1]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/get_trivy_summary
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_Path_2]]
- 1 edge to [[_COMMUNITY_AgentTarget_4]]
- 1 edge to [[_COMMUNITY_test_collaborator_greeter.py_1]]
- 1 edge to [[_COMMUNITY__load_latest_json]]

## Top bridge nodes
- [[get_sbom()_1]] - degree 9, connects to 4 communities
- [[_score_supply_chain()]] - degree 9, connects to 4 communities
- [[TestGetSbom_1]] - degree 4, connects to 1 community
- [[TestScoreSupplyChain]] - degree 4, connects to 1 community
- [[dot-test_returns_none_when_no_dir()]] - degree 3, connects to 1 community
