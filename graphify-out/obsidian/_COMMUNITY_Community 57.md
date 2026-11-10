---
type: community
members: 62
---

# Community 57

**Members:** 62 nodes

## Members
- [[.__init__()_87]] - code - gateway/security/intel_report.py
- [[._compute_content_hash()]] - code - gateway/security/intel_report.py
- [[._load_latest_file()]] - code - gateway/security/intel_report.py
- [[.load_all()_1]] - code - gateway/security/intel_report.py
- [[.load_latest()]] - code - gateway/security/intel_report.py
- [[.report_id_not_empty()]] - code - gateway/security/intel_report.py
- [[.save()_1]] - code - gateway/security/intel_report.py
- [[.source_not_empty()]] - code - gateway/security/intel_report.py
- [[.test_content_hash_is_deterministic()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_different_content_different_hash()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_empty_report_id_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_empty_source_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_full_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_minimal_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_missing_required_fields_raises()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_negative_security_score_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_report_has_content_hash()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_report_roundtrips_via_json()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_report_serialises_to_json()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_security_score_above_max_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_verify_integrity_fails_after_tampering()]] - code - gateway/tests/test_intel_pipeline.py
- [[.test_verify_integrity_passes_for_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[.verify_chain()_2]] - code - gateway/security/intel_report.py
- [[.verify_integrity()]] - code - gateway/security/intel_report.py
- [[A single competitor record in a competitive intel report.]] - rationale - gateway/security/intel_report.py
- [[A verified source backing a competitor claim.      A Citation is only created by]] - rationale - gateway/security/intel_report.py
- [[Citation]] - code - gateway/security/citation_verifier.py
- [[Citation_1]] - code - gateway/security/intel_report.py
- [[CitationVerifier.verify_report()]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport_1]] - code - gateway/security/intel_report.py
- [[CompetitiveIntelReport_2]] - code - gateway/tests/test_intel_pipeline.py
- [[CompetitorEntry]] - code - gateway/security/citation_verifier.py
- [[CompetitorEntry_1]] - code - gateway/security/intel_report.py
- [[Compute SHA-256 over the canonical content fields of a report.      Fields inclu]] - rationale - gateway/security/intel_report.py
- [[Derive content_hash from the canonical content fields.          Only computed wh]] - rationale - gateway/security/intel_report.py
- [[Fetcher]] - code - gateway/security/citation_verifier.py
- [[IntelReportStore]] - code - gateway/security/intel_report.py
- [[Load all reports in chronological order (oldest first).]] - rationale - gateway/security/intel_report.py
- [[Load the most recently saved report.          Args             verify If True,]] - rationale - gateway/security/intel_report.py
- [[Path_14]] - code - gateway/security/intel_report.py
- [[Persist report to the store, linking it to the previous report.          Sets]] - rationale - gateway/security/intel_report.py
- [[Persistent store for competitive intelligence reports.      Each report is saved]] - rationale - gateway/security/intel_report.py
- [[Raised when a loaded report fails its hash integrity check.]] - rationale - gateway/security/intel_report.py
- [[ReportIntegrityError]] - code - gateway/security/intel_report.py
- [[Return True iff the stored content_hash matches recomputation.]] - rationale - gateway/security/intel_report.py
- [[Return an IntelReportStore pointed at the configured data directory.]] - rationale - gateway/web/api.py
- [[Return recent competitive-intelligence reports in reverse-chronological order.]] - rationale - gateway/web/api.py
- [[Return the latest validated competitive-intelligence report.      Auth-gated (ow]] - rationale - gateway/web/api.py
- [[Return the most recent JSON file in the store, or None.]] - rationale - gateway/security/intel_report.py
- [[Schema for a Hermes-generated competitive intelligence report.      The ``conten]] - rationale - gateway/security/intel_report.py
- [[TestCompetitiveIntelReportSchema]] - code - gateway/tests/test_intel_pipeline.py
- [[TestIntelReportHashIntegrity]] - code - gateway/tests/test_intel_pipeline.py
- [[Tests for Pydantic model validation.]] - rationale - gateway/tests/test_intel_pipeline.py
- [[Walk the entire report chain and verify hash linkage.          Returns]] - rationale - gateway/security/intel_report.py
- [[_compute_hash()]] - code - gateway/security/intel_report.py
- [[_intel_store()]] - code - gateway/web/api.py
- [[citation_verifier.py]] - code - gateway/security/citation_verifier.py
- [[get_competitive_intel()]] - code - gateway/web/api.py
- [[get_competitive_intel_history()]] - code - gateway/web/api.py
- [[intel_report.py]] - code - gateway/security/intel_report.py
- [[test_intel_pipeline.py]] - code - gateway/tests/test_intel_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_57
SORT file.name ASC
```

## Connections to other communities
- 33 edges to [[_COMMUNITY_Community 125]]
- 16 edges to [[_COMMUNITY_Community 788]]
- 10 edges to [[_COMMUNITY_Community 137]]
- 5 edges to [[_COMMUNITY_Community 49]]
- 4 edges to [[_COMMUNITY_Community 40]]
- 3 edges to [[_COMMUNITY_Community 10]]
- 1 edge to [[_COMMUNITY_Community 152]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 2178]]
- 1 edge to [[_COMMUNITY_Community 110]]

## Top bridge nodes
- [[IntelReportStore]] - degree 39, connects to 5 communities
- [[CompetitiveIntelReport_1]] - degree 36, connects to 4 communities
- [[CompetitorEntry_1]] - degree 22, connects to 4 communities
- [[citation_verifier.py]] - degree 10, connects to 4 communities
- [[Citation_1]] - degree 11, connects to 3 communities