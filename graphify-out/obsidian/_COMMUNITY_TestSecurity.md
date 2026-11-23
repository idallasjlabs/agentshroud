---
type: community
members: 8
---

# TestSecurity

**Members:** 8 nodes

## Members
- [[dot-test_bot_and_title_length_capped()]] - code - gateway/tests/test_report_store.py
- [[dot-test_content_size_cap()]] - code - gateway/tests/test_report_store.py
- [[dot-test_corrupt_metadata_skipped_in_list()]] - code - gateway/tests/test_report_store.py
- [[dot-test_get_rejects_path_traversal()]] - code - gateway/tests/test_report_store.py
- [[dot-test_pii_redacted_on_save()]] - code - gateway/tests/test_report_store.py
- [[dot-test_report_id_is_path_safe()]] - code - gateway/tests/test_report_store.py
- [[TestSecurity]] - code - gateway/tests/test_report_store.py
- [[_redact()]] - code - gateway/tests/test_report_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestSecurity
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_ReportStore]]
- 1 edge to [[_COMMUNITY_test_report_store.py]]

## Top bridge nodes
- [[TestSecurity]] - degree 8, connects to 2 communities
- [[dot-test_pii_redacted_on_save()]] - degree 3, connects to 1 community
- [[dot-test_content_size_cap()]] - degree 2, connects to 1 community
