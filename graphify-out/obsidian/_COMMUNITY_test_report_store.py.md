---
type: community
members: 7
---

# test_report_store.py

**Members:** 7 nodes

## Members
- [[dot-test_delete()]] - code - gateway/tests/test_report_store.py
- [[dot-test_survives_new_instance()]] - code - gateway/tests/test_report_store.py
- [[Gateway-managed multi-bot report store (SCRUM-79). Both OpenClaw and Hermes…]] - rationale - gateway/security/report_store.py
- [[TestPersistence]] - code - gateway/tests/test_report_store.py
- [[Tests for ReportStore (SCRUM-79) — gateway-managed multi-bot report store.]] - rationale - gateway/tests/test_report_store.py
- [[report_store.py]] - code - gateway/security/report_store.py
- [[test_report_store.py]] - code - gateway/tests/test_report_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_report_storepy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ReportStore]]
- 2 edges to [[_COMMUNITY_TestReportAPI]]
- 1 edge to [[_COMMUNITY_TestAsyncSave]]
- 1 edge to [[_COMMUNITY_TestSecurity]]
- 1 edge to [[_COMMUNITY_TestReviewHardening]]
- 1 edge to [[_COMMUNITY_TestSaveAndGet]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[test_report_store.py]] - degree 11, connects to 7 communities
- [[TestPersistence]] - degree 4, connects to 1 community
- [[report_store.py]] - degree 3, connects to 1 community
- [[dot-test_survives_new_instance()]] - degree 2, connects to 1 community
