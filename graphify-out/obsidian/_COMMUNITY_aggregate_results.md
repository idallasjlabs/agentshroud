---
type: community
members: 20
---

# aggregate_results

**Members:** 20 nodes

## Members
- [[dot-_patch_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_capped_at_five()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_four_when_sbom_and_clean_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_one_when_sbom_exists()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_clean_when_all_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_critical_when_any_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_not_configured_when_all_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_overall_warning_when_high_only()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_scanners_dict_has_all_tools()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_timestamp_present()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_totals_sum_across_scanners()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_zero_when_no_sbom_no_trivy()]] - code - gateway/tests/test_scanner_integration.py
- [[Aggregate results from all security scanners into a unified dict. Returns Dict…]] - rationale - gateway/security/scanner_integration.py
- [[Score domain 1 Image Integrity (0-5). 1=SBOM exists, 2=Trivy ran, 3=zero…]] - rationale - gateway/security/scanner_integration.py
- [[TestAggregateResults_1]] - code - gateway/tests/test_scanner_integration.py
- [[TestScoreImageIntegrity_1]] - code - gateway/tests/test_scanner_integration.py
- [[_score_image_integrity()]] - code - gateway/security/scanner_integration.py
- [[_trivy_clean()]] - code - gateway/tests/test_scanner_integration.py
- [[_trivy_not_run()]] - code - gateway/tests/test_scanner_integration.py
- [[aggregate_results()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/aggregate_results
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_test_scanner_integration.py]]
- 5 edges to [[_COMMUNITY_Any]]
- 3 edges to [[_COMMUNITY_compute_scorecard]]
- 3 edges to [[_COMMUNITY_test_scorecard_integrity.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_get_trivy_summary]]
- 1 edge to [[_COMMUNITY_generate_summary]]
- 1 edge to [[_COMMUNITY_get_wazuh_summary]]

## Top bridge nodes
- [[aggregate_results()]] - degree 19, connects to 7 communities
- [[_score_image_integrity()]] - degree 10, connects to 5 communities
- [[_trivy_clean()]] - degree 7, connects to 3 communities
- [[_trivy_not_run()]] - degree 7, connects to 3 communities
- [[dot-_patch_all_not_run()]] - degree 10, connects to 1 community
