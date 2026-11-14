---
type: community
members: 64
---

# Community 57

**Members:** 64 nodes

## Members
- [[._compute_content_hash()]] - code - gateway/security/intel_report.py
- [[._make_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[.load_all()_1]] - code - gateway/security/intel_report.py
- [[.load_latest()]] - code - gateway/security/intel_report.py
- [[.report_id_not_empty()]] - code - gateway/security/intel_report.py
- [[.source_not_empty()]] - code - gateway/security/intel_report.py
- [[.store()_2]] - code - gateway/tests/test_intel_pipeline.py
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
- [[.verify_chain()_2]] - code - gateway/security/intel_report.py
- [[.verify_integrity()]] - code - gateway/security/intel_report.py
- [[A single competitor record in a competitive intel report.]] - rationale - gateway/security/intel_report.py
- [[CitationVerifier.verify_report()]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport_1]] - code - gateway/security/intel_report.py
- [[CompetitiveIntelReport_2]] - code - gateway/tests/test_intel_pipeline.py
- [[CompetitorEntry_1]] - code - gateway/security/intel_report.py
- [[Compute SHA-256 over the canonical content fields of a report.      Fields inclu]] - rationale - gateway/security/intel_report.py
- [[Derive content_hash from the canonical content fields.          Only computed wh]] - rationale - gateway/security/intel_report.py
- [[If the previous report file is corrupt, save must not raise.]] - rationale - gateway/tests/test_intel_pipeline.py
- [[IntelReportStore_1]] - code - gateway/tests/test_intel_pipeline.py
- [[Load all reports in chronological order (oldest first).]] - rationale - gateway/security/intel_report.py
- [[Load the most recently saved report.          Args             verify If True,]] - rationale - gateway/security/intel_report.py
- [[Path_34]] - code - gateway/tests/test_intel_pipeline.py
- [[Raised when a loaded report fails its hash integrity check.]] - rationale - gateway/security/intel_report.py
- [[ReportIntegrityError]] - code - gateway/security/intel_report.py
- [[Return True iff the stored content_hash matches recomputation.]] - rationale - gateway/security/intel_report.py
- [[Schema for a Hermes-generated competitive intelligence report.      The ``conten]] - rationale - gateway/security/intel_report.py
- [[TestCompetitiveIntelReportSchema]] - code - gateway/tests/test_intel_pipeline.py
- [[TestIntelReportHashIntegrity]] - code - gateway/tests/test_intel_pipeline.py
- [[TestIntelReportStore]] - code - gateway/tests/test_intel_pipeline.py
- [[Tests for Pydantic model validation.]] - rationale - gateway/tests/test_intel_pipeline.py
- [[Walk the entire report chain and verify hash linkage.          Returns]] - rationale - gateway/security/intel_report.py
- [[_compute_hash()]] - code - gateway/security/intel_report.py
- [[intel_report module (CompetitiveIntelReport, IntelReportStore)]] - code - gateway/security/intel_report.py
- [[intel_report.py]] - code - gateway/security/intel_report.py
- [[test_intel_pipeline.py]] - code - gateway/tests/test_intel_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_57
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_Community 125]]
- 14 edges to [[_COMMUNITY_Community 2017]]
- 4 edges to [[_COMMUNITY_Community 137]]
- 2 edges to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 25]]

## Top bridge nodes
- [[CompetitiveIntelReport_1]] - degree 36, connects to 4 communities
- [[CompetitorEntry_1]] - degree 22, connects to 3 communities
- [[intel_report.py]] - degree 7, connects to 2 communities
- [[TestIntelReportStore]] - degree 23, connects to 1 community
- [[CompetitiveIntelReport_2]] - degree 19, connects to 1 community