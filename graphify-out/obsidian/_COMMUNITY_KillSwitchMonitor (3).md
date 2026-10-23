---
type: community
cohesion: 0.06
members: 82
---

# KillSwitchMonitor (3)

**Cohesion:** 0.06 - loosely connected
**Members:** 82 nodes

## Members
- [[dot-__init__()_166]] - code - gateway/security/intel_report.py
- [[dot-_compute_content_hash()]] - code - gateway/security/intel_report.py
- [[dot-_load_latest_file()]] - code - gateway/security/intel_report.py
- [[dot-_make_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-load_all()_1]] - code - gateway/security/intel_report.py
- [[dot-load_latest()]] - code - gateway/security/intel_report.py
- [[dot-ok()_2]] - code - gateway/security/citation_verifier.py
- [[dot-report_id_not_empty()]] - code - gateway/security/intel_report.py
- [[dot-save()_2]] - code - gateway/security/intel_report.py
- [[dot-source_not_empty()]] - code - gateway/security/intel_report.py
- [[dot-store()_2]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-store_dir()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_chain_hash_links_reports()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_content_hash_is_deterministic()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_different_content_different_hash()_1]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_empty_report_id_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_empty_source_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_full_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_integrity_check_fails_for_tampered_file()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_integrity_check_passes_for_saved_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_load_all_returns_all_reports()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_load_all_skips_malformed_files()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_load_latest_returns_none_when_empty()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_minimal_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_missing_required_fields_raises()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_multiple_saves_latest_is_newest()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_negative_security_score_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_report_has_content_hash()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_report_roundtrips_via_json()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_report_serialises_to_json()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_report_with_whitespace_only_id_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_report_with_whitespace_only_source_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_save_and_load_latest()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_save_with_corrupt_previous_file_falls_back_to_genesis()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_security_score_above_max_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_store_creates_directory()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_verify_chain_empty_store_is_valid()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_verify_chain_fails_for_tampered_entry()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_verify_chain_passes_for_intact_store()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_verify_integrity_fails_after_tampering()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_verify_integrity_passes_for_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-verify_chain()_1]] - code - gateway/security/intel_report.py
- [[dot-verify_integrity()]] - code - gateway/security/intel_report.py
- [[A single competitor record in a competitive intel report.]] - rationale - gateway/security/intel_report.py
- [[A source counts as proven only on a 2xx with non-empty content.]] - rationale - gateway/security/citation_verifier.py
- [[A verified source backing a competitor claim.      A Citation is only created by]] - rationale - gateway/security/intel_report.py
- [[Citation]] - code - gateway/security/citation_verifier.py
- [[Citation_1]] - code - gateway/security/intel_report.py
- [[CitationVerifier.verify_report()]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport_1]] - code - gateway/tests/test_intel_pipeline.py
- [[CompetitiveIntelReport_2]] - code - gateway/security/intel_report.py
- [[CompetitorEntry]] - code - gateway/security/citation_verifier.py
- [[CompetitorEntry_1]] - code - gateway/security/intel_report.py
- [[Compute SHA-256 over the canonical content fields of a report.      Fields inclu]] - rationale - gateway/security/intel_report.py
- [[Derive content_hash from the canonical content fields.          Only computed wh]] - rationale - gateway/security/intel_report.py
- [[FetchOutcome_1]] - code - gateway/security/citation_verifier.py
- [[Fetcher]] - code - gateway/security/citation_verifier.py
- [[If the previous report file is corrupt, save must not raise.]] - rationale - gateway/tests/test_intel_pipeline.py
- [[IntelReportStore]] - code - gateway/tests/test_intel_pipeline.py
- [[IntelReportStore_1]] - code - gateway/security/intel_report.py
- [[Load all reports in chronological order (oldest first).]] - rationale - gateway/security/intel_report.py
- [[Load the most recently saved report.          Args             verify If True,]] - rationale - gateway/security/intel_report.py
- [[Path_51]] - code - gateway/security/intel_report.py
- [[Path_52]] - code - gateway/tests/test_intel_pipeline.py
- [[Persist report to the store, linking it to the previous report.          Sets]] - rationale - gateway/security/intel_report.py
- [[Persistent store for competitive intelligence reports.      Each report is saved]] - rationale - gateway/security/intel_report.py
- [[Raised when a loaded report fails its hash integrity check.]] - rationale - gateway/security/intel_report.py
- [[ReportIntegrityError]] - code - gateway/security/intel_report.py
- [[Result of re-fetching a candidate citation URL through the web proxy.]] - rationale - gateway/security/citation_verifier.py
- [[Return True iff the stored content_hash matches recomputation.]] - rationale - gateway/security/intel_report.py
- [[Return the most recent JSON file in the store, or None.]] - rationale - gateway/security/intel_report.py
- [[Schema for a Hermes-generated competitive intelligence report.      The ``conten]] - rationale - gateway/security/intel_report.py
- [[TestCompetitiveIntelReportSchema]] - code - gateway/tests/test_intel_pipeline.py
- [[TestIntelReportHashIntegrity]] - code - gateway/tests/test_intel_pipeline.py
- [[TestIntelReportStore]] - code - gateway/tests/test_intel_pipeline.py
- [[Tests for Pydantic model validation.]] - rationale - gateway/tests/test_intel_pipeline.py
- [[Walk the entire report chain and verify hash linkage.          Returns]] - rationale - gateway/security/intel_report.py
- [[_compute_hash()]] - code - gateway/security/intel_report.py
- [[citation_verifier.py]] - code - gateway/security/citation_verifier.py
- [[intel_report.py]] - code - gateway/security/intel_report.py
- [[test_intel_pipeline.py]] - code - gateway/tests/test_intel_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/KillSwitchMonitor_3
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_MCPPolicyEngine (2)]]
- 16 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 8 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 3 edges to [[_COMMUNITY_ServiceManager]]
- 3 edges to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_domain_matches()]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig (2)]]
- 1 edge to [[_COMMUNITY_AgentShroud™ README]]

## Top bridge nodes
- [[IntelReportStore_1]] - degree 39, connects to 4 communities
- [[citation_verifier.py]] - degree 10, connects to 4 communities
- [[CompetitiveIntelReport_2]] - degree 36, connects to 3 communities
- [[CompetitorEntry_1]] - degree 22, connects to 2 communities
- [[FetchOutcome_1]] - degree 21, connects to 2 communities
