---
type: community
members: 7
---

# TestReviewHardening

**Members:** 7 nodes

## Members
- [[dot-test_async_sanitizer_refused_on_sync_save()]] - code - gateway/tests/test_report_store.py
- [[dot-test_content_cap_default_is_1mb()]] - code - gateway/tests/test_report_store.py
- [[dot-test_count_cap_prunes_oldest()]] - code - gateway/tests/test_report_store.py
- [[dot-test_title_and_tags_sanitized_sync()]] - code - gateway/tests/test_report_store.py
- [[SCRUM-79 adversarial-review follow-ups (2026-07-13).]] - rationale - gateway/tests/test_report_store.py
- [[TestReviewHardening]] - code - gateway/tests/test_report_store.py
- [[_san()_2]] - code - gateway/tests/test_report_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestReviewHardening
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_ReportStore]]
- 2 edges to [[_COMMUNITY_TestAsyncSave]]
- 1 edge to [[_COMMUNITY_test_report_store.py]]

## Top bridge nodes
- [[TestReviewHardening]] - degree 8, connects to 3 communities
- [[dot-test_async_sanitizer_refused_on_sync_save()]] - degree 4, connects to 2 communities
- [[dot-test_content_cap_default_is_1mb()]] - degree 2, connects to 1 community
- [[dot-test_count_cap_prunes_oldest()]] - degree 2, connects to 1 community
- [[dot-test_title_and_tags_sanitized_sync()]] - degree 2, connects to 1 community
