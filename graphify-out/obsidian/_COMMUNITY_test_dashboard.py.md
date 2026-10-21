---
type: community
members: 58
---

# test_dashboard.py

**Members:** 58 nodes

## Members
- [[dot-__init__()_24]] - code - gateway/security/report_store.py
- [[dot-_check_size()]] - code - gateway/security/report_store.py
- [[dot-_enforce_count_cap()]] - code - gateway/security/report_store.py
- [[dot-_path()]] - code - gateway/security/report_store.py
- [[dot-_persist()]] - code - gateway/security/report_store.py
- [[dot-_sanitize_async()]] - code - gateway/security/report_store.py
- [[dot-_sanitize_sync()]] - code - gateway/security/report_store.py
- [[dot-_valid_id()]] - code - gateway/security/report_store.py
- [[dot-client()]] - code - gateway/tests/test_report_store.py
- [[dot-delete()]] - code - gateway/security/report_store.py
- [[dot-get()]] - code - gateway/security/report_store.py
- [[dot-list()]] - code - gateway/security/report_store.py
- [[dot-save()]] - code - gateway/security/report_store.py
- [[dot-save_async()]] - code - gateway/security/report_store.py
- [[dot-test_async_sanitizer_refused_on_sync_save()]] - code - gateway/tests/test_report_store.py
- [[dot-test_bot_and_title_length_capped()]] - code - gateway/tests/test_report_store.py
- [[dot-test_content_cap_default_is_1mb()]] - code - gateway/tests/test_report_store.py
- [[dot-test_content_size_cap()]] - code - gateway/tests/test_report_store.py
- [[dot-test_corrupt_metadata_skipped_in_list()]] - code - gateway/tests/test_report_store.py
- [[dot-test_count_cap_prunes_oldest()]] - code - gateway/tests/test_report_store.py
- [[dot-test_create_list_get_roundtrip()]] - code - gateway/tests/test_report_store.py
- [[dot-test_cross_bot_visibility()]] - code - gateway/tests/test_report_store.py
- [[dot-test_delete()]] - code - gateway/tests/test_report_store.py
- [[dot-test_get_missing_returns_none()]] - code - gateway/tests/test_report_store.py
- [[dot-test_get_rejects_path_traversal()]] - code - gateway/tests/test_report_store.py
- [[dot-test_list_filter_by_bot()]] - code - gateway/tests/test_report_store.py
- [[dot-test_list_returns_metadata_without_content()]] - code - gateway/tests/test_report_store.py
- [[dot-test_missing_content_422()]] - code - gateway/tests/test_report_store.py
- [[dot-test_pii_redacted_on_save()]] - code - gateway/tests/test_report_store.py
- [[dot-test_report_id_is_path_safe()]] - code - gateway/tests/test_report_store.py
- [[dot-test_round_trip()]] - code - gateway/tests/test_report_store.py
- [[dot-test_save_async_size_cap()]] - code - gateway/tests/test_report_store.py
- [[dot-test_save_async_with_async_sanitizer()]] - code - gateway/tests/test_report_store.py
- [[dot-test_save_async_with_sync_sanitizer()]] - code - gateway/tests/test_report_store.py
- [[dot-test_survives_new_instance()]] - code - gateway/tests/test_report_store.py
- [[dot-test_tags_preserved()]] - code - gateway/tests/test_report_store.py
- [[dot-test_title_and_tags_sanitized_async()]] - code - gateway/tests/test_report_store.py
- [[dot-test_title_and_tags_sanitized_sync()]] - code - gateway/tests/test_report_store.py
- [[dot-test_traversal_id_rejected_not_500()]] - code - gateway/tests/test_report_store.py
- [[dot-test_unknown_report_404()]] - code - gateway/tests/test_report_store.py
- [[Any_5]] - code - gateway/security/report_store.py
- [[Filesystem-backed shared report store on the gateway-data volume.]] - rationale - gateway/security/report_store.py
- [[Metadata (no content) for all reports, newest first.          O(n) file reads pe]] - rationale - gateway/security/report_store.py
- [[Persist a report (sync sanitizer path); return its id.          Sanitizes ALL fr]] - rationale - gateway/security/report_store.py
- [[Persist a report awaiting an async sanitizer (presidio) if injected.          Sa]] - rationale - gateway/security/report_store.py
- [[Prune oldest reports so the shared volume can't be filled.]] - rationale - gateway/security/report_store.py
- [[ReportStore]] - code - gateway/security/report_store.py
- [[Route-level POSTGET apireports through the FastAPI app (SCRUM-79).]] - rationale - gateway/tests/test_report_store.py
- [[SCRUM-79 adversarial-review follow-ups (2026-07-13).]] - rationale - gateway/tests/test_report_store.py
- [[TestAsyncSave]] - code - gateway/tests/test_report_store.py
- [[TestPersistence]] - code - gateway/tests/test_report_store.py
- [[TestReportAPI]] - code - gateway/tests/test_report_store.py
- [[TestReviewHardening]] - code - gateway/tests/test_report_store.py
- [[TestSaveAndGet]] - code - gateway/tests/test_report_store.py
- [[TestSecurity]] - code - gateway/tests/test_report_store.py
- [[report_store.py]] - code - gateway/security/report_store.py
- [[store()]] - code - gateway/tests/test_report_store.py
- [[test_report_store.py]] - code - gateway/tests/test_report_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_dashboardpy
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_MCPPolicyEngine]]
- 1 edge to [[_COMMUNITY_TrustConfig]]

## Top bridge nodes
- [[test_report_store.py]] - degree 10, connects to 1 community
- [[dot-_path()]] - degree 5, connects to 1 community
