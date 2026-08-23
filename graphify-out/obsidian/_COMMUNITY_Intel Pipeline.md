---
type: community
cohesion: 0.11
members: 45
---

# Intel Pipeline

**Cohesion:** 0.11 - loosely connected
**Members:** 45 nodes

## Members
- [[._make_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[.store()_1]] - code - gateway/tests/test_intel_pipeline.py
- [[.store_dir()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_chain_hash_links_reports()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_content_hash_is_deterministic()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_different_content_different_hash()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_empty_report_id_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_empty_source_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_full_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_integrity_check_fails_for_tampered_file()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_integrity_check_passes_for_saved_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_load_all_returns_all_reports()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_load_all_skips_malformed_files()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_load_latest_returns_none_when_empty()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_minimal_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_missing_required_fields_raises()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_multiple_saves_latest_is_newest()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_negative_security_score_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_report_has_content_hash()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_report_roundtrips_via_json()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_report_serialises_to_json()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_report_with_whitespace_only_id_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_report_with_whitespace_only_source_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_save_and_load_latest()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_save_with_corrupt_previous_file_falls_back_to_genesis()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_security_score_above_max_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_store_creates_directory()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_verify_chain_empty_store_is_valid()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_verify_chain_fails_for_tampered_entry()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_verify_chain_passes_for_intact_store()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_verify_integrity_fails_after_tampering()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_verify_integrity_passes_for_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[A single competitor record in a competitive intel report.]] - rationale - gateway/security/intel_report.py
- [[CompetitiveIntelReport_2]] - code - gateway/tests/test_intel_pipeline.py
- [[CompetitorEntry_1]] - code - gateway/security/intel_report.py
- [[If the previous report file is corrupt, save must not raise.]] - rationale - gateway/tests/test_intel_pipeline.py
- [[IntelReportStore_1]] - code - gateway/tests/test_intel_pipeline.py
- [[Path_30]] - code - gateway/tests/test_intel_pipeline.py
- [[Raised when a loaded report fails its hash integrity check.]] - rationale - gateway/security/intel_report.py
- [[ReportIntegrityError]] - code - gateway/security/intel_report.py
- [[TestCompetitiveIntelReportSchema]] - code - gateway/tests/test_intel_pipeline.py
- [[TestIntelReportHashIntegrity]] - code - gateway/tests/test_intel_pipeline.py
- [[TestIntelReportStore]] - code - gateway/tests/test_intel_pipeline.py
- [[Tests for Pydantic model validation.]] - rationale - gateway/tests/test_intel_pipeline.py
- [[test_intel_pipeline.py]] - code - gateway/tests/test_intel_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Intel_Pipeline
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Intel Report (security)]]
- 7 edges to [[_COMMUNITY_Api (web)]]
- 3 edges to [[_COMMUNITY_Citation Verifier]]
- 1 edge to [[_COMMUNITY_Browser Security]]
- 1 edge to [[_COMMUNITY_Router (soc)]]
- 1 edge to [[_COMMUNITY_Intel Endpoint]]

## Top bridge nodes
- [[CompetitorEntry_1]] - degree 22, connects to 4 communities
- [[test_intel_pipeline.py]] - degree 8, connects to 3 communities
- [[TestIntelReportStore]] - degree 23, connects to 2 communities
- [[CompetitiveIntelReport_2]] - degree 19, connects to 2 communities
- [[IntelReportStore_1]] - degree 18, connects to 2 communities