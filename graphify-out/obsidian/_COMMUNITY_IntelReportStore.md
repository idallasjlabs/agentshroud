---
type: community
members: 28
---

# IntelReportStore

**Members:** 28 nodes

## Members
- [[dot-_make_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-load_all()_1]] - code - gateway/security/intel_report.py
- [[dot-store()_1]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-store_dir()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_chain_hash_links_reports()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_integrity_check_fails_for_tampered_file()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_integrity_check_passes_for_saved_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_load_all_returns_all_reports()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_load_all_skips_malformed_files()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_load_latest_returns_none_when_empty()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_multiple_saves_latest_is_newest()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_report_with_whitespace_only_id_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_report_with_whitespace_only_source_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_save_and_load_latest()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_save_with_corrupt_previous_file_falls_back_to_genesis()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_store_creates_directory()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_verify_chain_empty_store_is_valid()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_verify_chain_fails_for_tampered_entry()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_verify_chain_passes_for_intact_store()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-verify_chain()_1]] - code - gateway/security/intel_report.py
- [[If the previous report file is corrupt, save must not raise.]] - rationale - gateway/tests/test_intel_pipeline.py
- [[IntelReportStore]] - code - gateway/security/intel_report.py
- [[Load all reports in chronological order (oldest first).]] - rationale - gateway/security/intel_report.py
- [[Path_59]] - code
- [[Persistent store for competitive intelligence reports. Each report is saved as…]] - rationale - gateway/security/intel_report.py
- [[TestIntelReportStore]] - code - gateway/tests/test_intel_pipeline.py
- [[Walk the entire report chain and verify hash linkage. Returns (True, Chain…]] - rationale - gateway/security/intel_report.py
- [[fixture_114]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/IntelReportStore
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 5 edges to [[_COMMUNITY_ReportIntegrityError]]
- 3 edges to [[_COMMUNITY_DraftEntry]]
- 2 edges to [[_COMMUNITY_api.py]]

## Top bridge nodes
- [[IntelReportStore]] - degree 29, connects to 4 communities
- [[TestIntelReportStore]] - degree 22, connects to 2 communities
- [[dot-_make_report()]] - degree 13, connects to 1 community
- [[dot-load_all()_1]] - degree 4, connects to 1 community
