---
type: community
members: 34
---

# CompetitiveIntelReport

**Members:** 34 nodes

## Members
- [[dot-_compute_content_hash()]] - code - gateway/security/intel_report.py
- [[dot-report_id_not_empty()]] - code - gateway/security/intel_report.py
- [[dot-source_not_empty()]] - code - gateway/security/intel_report.py
- [[dot-test_empty_report_id_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_empty_source_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_full_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_minimal_valid_report()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_missing_required_fields_raises()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_negative_security_score_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_report_roundtrips_via_json()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_report_serialises_to_json()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-test_security_score_above_max_rejected()]] - code - gateway/tests/test_intel_pipeline.py
- [[dot-verify_integrity()]] - code - gateway/security/intel_report.py
- [[A single competitor record in a competitive intel report.]] - rationale - gateway/security/intel_report.py
- [[A verified source backing a competitor claim. A Citation is only created by the…]] - rationale - gateway/security/intel_report.py
- [[BaseModel_9]] - code
- [[Citation]] - code - gateway/security/intel_report.py
- [[Citation verifier for competitive-intelligence reports (SCRUM-75). IEC 62443…]] - rationale - gateway/security/citation_verifier.py
- [[Competitive Intelligence Report — Schema, Integrity, and Store (B.2) IEC 62443…]] - rationale - gateway/security/intel_report.py
- [[CompetitiveIntelReport]] - code - gateway/security/intel_report.py
- [[CompetitorEntry]] - code - gateway/security/intel_report.py
- [[Compute SHA-256 over the canonical content fields of a report. Fields included…]] - rationale - gateway/security/intel_report.py
- [[Derive content_hash from the canonical content fields. Only computed when…]] - rationale - gateway/security/intel_report.py
- [[Return True iff the stored content_hash matches recomputation.]] - rationale - gateway/security/intel_report.py
- [[Schema for a Hermes-generated competitive intelligence report. The…]] - rationale - gateway/security/intel_report.py
- [[TestCompetitiveIntelReportSchema]] - code - gateway/tests/test_intel_pipeline.py
- [[Tests for B.2 — Competitive Intel Pipeline (schema validation + hash…]] - rationale - gateway/tests/test_intel_pipeline.py
- [[Tests for Pydantic model validation.]] - rationale - gateway/tests/test_intel_pipeline.py
- [[_compute_hash()]] - code - gateway/security/intel_report.py
- [[citation_verifier.py]] - code - gateway/security/citation_verifier.py
- [[field_validator_4]] - code
- [[intel_report.py]] - code - gateway/security/intel_report.py
- [[model_validator]] - code
- [[test_intel_pipeline.py]] - code - gateway/tests/test_intel_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CompetitiveIntelReport
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_DraftEntry]]
- 6 edges to [[_COMMUNITY_IntelReportStore]]
- 4 edges to [[_COMMUNITY_ReportIntegrityError]]
- 3 edges to [[_COMMUNITY_dot-verify_entry]]
- 2 edges to [[_COMMUNITY_TestIntelReportHashIntegrity]]
- 2 edges to [[_COMMUNITY_test_intel_endpoint.py]]
- 2 edges to [[_COMMUNITY_EgressFilter]]
- 2 edges to [[_COMMUNITY_GatewayConfig]]
- 1 edge to [[_COMMUNITY_make_httpx_fetcher]]

## Top bridge nodes
- [[CompetitiveIntelReport]] - degree 21, connects to 5 communities
- [[citation_verifier.py]] - degree 13, connects to 4 communities
- [[intel_report.py]] - degree 11, connects to 4 communities
- [[test_intel_pipeline.py]] - degree 10, connects to 4 communities
- [[CompetitorEntry]] - degree 12, connects to 2 communities
