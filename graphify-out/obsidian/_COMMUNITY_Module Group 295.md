---
type: community
cohesion: 0.20
members: 15
---

# Module Group 295

**Cohesion:** 0.20 - loosely connected
**Members:** 15 nodes

## Members
- [[.test_five_optimal()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_five_sbom_and_trivy_clean()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_four_sbom_and_trivy_with_criticals()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_four_with_zero_highs()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_one_when_only_sbom_exists()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_three_sbom_has_packages_no_trivy()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_three_with_sbom_trivy_no_criticals_but_has_highs()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_two_empty_sbom()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_zero_when_nothing_present()]] - code - gateway/tests/test_scorecard_scoring.py
- [[.test_zero_without_sbom()]] - code - gateway/tests/test_scorecard_scoring.py
- [[Return a mock Path that exists and whose glob() returns named mock files.]] - rationale - gateway/tests/test_scorecard_scoring.py
- [[TestScoreImageIntegrity_1]] - code - gateway/tests/test_scorecard_scoring.py
- [[TestScoreSupplyChain_1]] - code - gateway/tests/test_scorecard_scoring.py
- [[_mock_dir_with_files()]] - code - gateway/tests/test_scorecard_scoring.py
- [[_mock_missing_dir()]] - code - gateway/tests/test_scorecard_scoring.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_295
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Module Group 294]]
- 3 edges to [[_COMMUNITY_Module Group 413]]
- 2 edges to [[_COMMUNITY_Module Group 470]]
- 2 edges to [[_COMMUNITY_Module Group 493]]
- 1 edge to [[_COMMUNITY_Module Group 494]]

## Top bridge nodes
- [[_mock_dir_with_files()]] - degree 13, connects to 5 communities
- [[_mock_missing_dir()]] - degree 6, connects to 3 communities
- [[TestScoreImageIntegrity_1]] - degree 7, connects to 2 communities
- [[TestScoreSupplyChain_1]] - degree 6, connects to 1 community
- [[.test_five_optimal()]] - degree 2, connects to 1 community