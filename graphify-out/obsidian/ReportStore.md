---
source_file: "gateway/security/report_store.py"
type: "code"
community: "Gateway Test Suite"
location: "L63"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# ReportStore

## Connections
- [[.__init__()_110]] - `method` [EXTRACTED]
- [[._check_size()]] - `method` [EXTRACTED]
- [[._enforce_count_cap()]] - `method` [EXTRACTED]
- [[._path()]] - `method` [EXTRACTED]
- [[._persist()]] - `method` [EXTRACTED]
- [[._sanitize_async()]] - `method` [EXTRACTED]
- [[._sanitize_sync()]] - `method` [EXTRACTED]
- [[._valid_id()]] - `method` [EXTRACTED]
- [[.client()_1]] - `calls` [EXTRACTED]
- [[.delete()_1]] - `method` [EXTRACTED]
- [[.get()_4]] - `method` [EXTRACTED]
- [[.list()]] - `method` [EXTRACTED]
- [[.save()_2]] - `method` [EXTRACTED]
- [[.save_async()]] - `method` [EXTRACTED]
- [[.test_async_sanitizer_refused_on_sync_save()]] - `calls` [EXTRACTED]
- [[.test_content_cap_default_is_1mb()]] - `calls` [EXTRACTED]
- [[.test_content_size_cap()]] - `calls` [EXTRACTED]
- [[.test_count_cap_prunes_oldest()]] - `calls` [EXTRACTED]
- [[.test_pii_redacted_on_save()]] - `calls` [EXTRACTED]
- [[.test_save_async_size_cap()]] - `calls` [EXTRACTED]
- [[.test_save_async_with_async_sanitizer()]] - `calls` [EXTRACTED]
- [[.test_save_async_with_sync_sanitizer()]] - `calls` [EXTRACTED]
- [[.test_survives_new_instance()]] - `calls` [EXTRACTED]
- [[.test_title_and_tags_sanitized_async()]] - `calls` [EXTRACTED]
- [[.test_title_and_tags_sanitized_sync()]] - `calls` [EXTRACTED]
- [[Filesystem-backed shared report store on the gateway-data volume.]] - `rationale_for` [EXTRACTED]
- [[GET socv1services (list_services endpoint)]] - `conceptually_related_to` [AMBIGUOUS]
- [[TestAsyncSave]] - `uses` [INFERRED]
- [[TestPersistence_1]] - `uses` [INFERRED]
- [[TestReportAPI]] - `uses` [INFERRED]
- [[TestReviewHardening]] - `uses` [INFERRED]
- [[TestSaveAndGet]] - `uses` [INFERRED]
- [[TestSecurity]] - `uses` [INFERRED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[report_store.py]] - `contains` [EXTRACTED]
- [[store()_2]] - `calls` [EXTRACTED]
- [[test_report_store.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite