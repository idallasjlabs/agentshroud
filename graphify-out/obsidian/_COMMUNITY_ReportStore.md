---
type: community
members: 15
---

# ReportStore

**Members:** 15 nodes

## Members
- [[dot-__init__()_8]] - code - gateway/security/report_store.py
- [[dot-_check_size()]] - code - gateway/security/report_store.py
- [[dot-_enforce_count_cap()]] - code - gateway/security/report_store.py
- [[dot-_path()]] - code - gateway/security/report_store.py
- [[dot-_persist()]] - code - gateway/security/report_store.py
- [[dot-_sanitize_async()]] - code - gateway/security/report_store.py
- [[dot-_sanitize_sync()]] - code - gateway/security/report_store.py
- [[dot-delete()]] - code - gateway/security/report_store.py
- [[dot-save()]] - code - gateway/security/report_store.py
- [[dot-save_async()]] - code - gateway/security/report_store.py
- [[Filesystem-backed shared report store on the gateway-data volume.]] - rationale - gateway/security/report_store.py
- [[Persist a report (sync sanitizer path); return its id. Sanitizes ALL free-text…]] - rationale - gateway/security/report_store.py
- [[Persist a report awaiting an async sanitizer (presidio) if injected. Sanitizes…]] - rationale - gateway/security/report_store.py
- [[Prune oldest reports so the shared volume can't be filled.]] - rationale - gateway/security/report_store.py
- [[ReportStore]] - code - gateway/security/report_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ReportStore
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TestAsyncSave]]
- 5 edges to [[_COMMUNITY_TestReviewHardening]]
- 5 edges to [[_COMMUNITY_dot-get]]
- 4 edges to [[_COMMUNITY_test_report_store.py]]
- 3 edges to [[_COMMUNITY_TestReportAPI]]
- 3 edges to [[_COMMUNITY_TestSecurity]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_lifespan]]

## Top bridge nodes
- [[ReportStore]] - degree 36, connects to 8 communities
- [[dot-delete()]] - degree 4, connects to 1 community
- [[dot-_path()]] - degree 4, connects to 1 community
