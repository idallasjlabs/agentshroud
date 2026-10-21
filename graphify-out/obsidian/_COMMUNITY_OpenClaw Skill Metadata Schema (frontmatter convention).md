---
type: community
members: 22
---

# OpenClaw Skill Metadata Schema (frontmatter convention)

**Members:** 22 nodes

## Members
- [[dot-test_bot_id_filter_matches_bot_image()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_bot_id_filter_unknown_bot_returns_all()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_corrupt_report_file_is_skipped()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_critical_report_status_is_critical()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_each_entry_has_image_key()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_ignores_non_image_prefixed_files()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_empty_list_when_dir_missing()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_empty_when_no_image_reports()]] - code - gateway/tests/test_scanner_integration.py
- [[dot-test_returns_one_entry_per_report_file()]] - code - gateway/tests/test_scanner_integration.py
- [[A JSON-corrupt file is silently skipped, others are still returned.]] - rationale - gateway/tests/test_scanner_integration.py
- [[Directory exists but contains only fs scan files — returns .]] - rationale - gateway/tests/test_scanner_integration.py
- [[Files named trivy-.json (fs scans) are not included.]] - rationale - gateway/tests/test_scanner_integration.py
- [[Path_43]] - code - gateway/tests/test_scanner_integration.py
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
TABLE source_file, type FROM #community/OpenClaw_Skill_Metadata_Schema_frontmatter_convention
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_parse_clamscan_output]]
- 3 edges to [[_COMMUNITY_PipelineAction (2)_1]]
- 3 edges to [[_COMMUNITY_FalcoAlertWatcher (2)]]
- 2 edges to [[_COMMUNITY__load_latest_json]]
- 1 edge to [[_COMMUNITY_server.py (2)]]
- 1 edge to [[_COMMUNITY_TestVersionRoutes]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]

## Top bridge nodes
- [[Path_43]] - degree 18, connects to 4 communities
- [[get_trivy_image_summaries()]] - degree 14, connects to 4 communities
- [[_write_image_report()]] - degree 11, connects to 1 community
- [[_clean_trivy_report()]] - degree 10, connects to 1 community
- [[TestGetTrivyImageSummaries]] - degree 10, connects to 1 community
