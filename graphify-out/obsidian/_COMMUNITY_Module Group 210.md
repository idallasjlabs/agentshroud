---
type: community
cohesion: 0.22
members: 22
---

# Module Group 210

**Cohesion:** 0.22 - loosely connected
**Members:** 22 nodes

## Members
- [[.test_bot_id_filter_matches_bot_image()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_bot_id_filter_unknown_bot_returns_all()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_corrupt_report_file_is_skipped()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_critical_report_status_is_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_each_entry_has_image_key()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_ignores_non_image_prefixed_files()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_empty_list_when_dir_missing()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_empty_when_no_image_reports()]] - code - gateway/tests/test_scanner_integration.py
- [[.test_returns_one_entry_per_report_file()]] - code - gateway/tests/test_scanner_integration.py
- [[A JSON-corrupt file is silently skipped, others are still returned.]] - rationale - gateway/tests/test_scanner_integration.py
- [[Directory exists but contains only fs scan files — returns .]] - rationale - gateway/tests/test_scanner_integration.py
- [[Files named trivy-.json (fs scans) are not included.]] - rationale - gateway/tests/test_scanner_integration.py
- [[Path_28]] - code - gateway/tests/test_scanner_integration.py
- [[Return per-image Trivy scan summaries from saved image reports.      Reads repor]] - rationale - gateway/security/scanner_integration.py
- [[TestGetTrivyImageSummaries]] - code - gateway/tests/test_scanner_integration.py
- [[Unknown bot_id with no config match falls through and returns all entries.]] - rationale - gateway/tests/test_scanner_integration.py
- [[Write a fake image report file in the expected filename format.]] - rationale - gateway/tests/test_scanner_integration.py
- [[_clean_trivy_report()]] - code - gateway/tests/test_scanner_integration.py
- [[_critical_trivy_report()]] - code - gateway/tests/test_scanner_integration.py
- [[_write_image_report()]] - code - gateway/tests/test_scanner_integration.py
- [[bot_id + config param restricts results to that bot's image.]] - rationale - gateway/tests/test_scanner_integration.py
- [[get_trivy_image_summaries()]] - code - gateway/security/scanner_integration.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_210
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Scanner Integration Tests]]
- 2 edges to [[_COMMUNITY_Module Group 228]]
- 2 edges to [[_COMMUNITY_Module Group 163]]
- 2 edges to [[_COMMUNITY_Module Group 381]]
- 2 edges to [[_COMMUNITY_Module Group 437]]
- 1 edge to [[_COMMUNITY_Security Scanner Integration]]
- 1 edge to [[_COMMUNITY_Module Group 269]]
- 1 edge to [[_COMMUNITY_Module Group 335]]

## Top bridge nodes
- [[Path_28]] - degree 18, connects to 6 communities
- [[get_trivy_image_summaries()]] - degree 14, connects to 4 communities
- [[_write_image_report()]] - degree 11, connects to 1 community
- [[_clean_trivy_report()]] - degree 10, connects to 1 community
- [[TestGetTrivyImageSummaries]] - degree 10, connects to 1 community