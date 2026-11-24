---
type: community
members: 9
---

# _score_image_integrity

**Members:** 9 nodes

## Members
- [[dot-test_capped_at_five()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_four_when_sbom_and_clean_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_sbom_exists()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_no_sbom_no_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[Score domain 1 Image Integrity (0-5). 1=SBOM exists, 2=Trivy ran, 3=zero…]] - rationale - gateway/security/scanner_integration.py
- [[TestScoreImageIntegrity_1]] - code - gateway/tests/test_scanner_integration.py
- [[_score_image_integrity()]] - code - gateway/security/scanner_integration.py
- [[_trivy_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_trivy_not_run()]] - code - gateway/tests/test_scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_score_image_integrity
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 3 edges to [[_COMMUNITY_compute_scorecard]]
- 3 edges to [[_COMMUNITY_Any_1]]
- 2 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 2 edges to [[_COMMUNITY_Any]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]

## Top bridge nodes
- [[_score_image_integrity()]] - degree 10, connects to 5 communities
- [[_trivy_clean()]] - degree 7, connects to 5 communities
- [[_trivy_not_run()]] - degree 7, connects to 5 communities
- [[TestScoreImageIntegrity_1]] - degree 5, connects to 1 community
