---
type: community
cohesion: 0.13
members: 38
---

# Citation Verifier

**Cohesion:** 0.13 - loosely connected
**Members:** 38 nodes

## Members
- [[.__call__()_2]] - code - gateway/tests/test_citation_verifier.py
- [[.__init__()_141]] - code - gateway/tests/test_citation_verifier.py
- [[._verifier()]] - code - gateway/tests/test_citation_verifier.py
- [[._verifier()_1]] - code - gateway/tests/test_citation_verifier.py
- [[.test_allowlisted_live_source_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_dropped_count_is_tamper_evident()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_generated_at_is_preserved()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_host_confusion_urls_rejected_and_never_fetched()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_mixed_valid_and_invalid_keeps_only_valid()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_multiple_valid_citations_all_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_no_candidate_urls_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_not_ok_on_non_2xx()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_not_ok_without_content()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_off_allowlist_url_dropped_and_not_fetched()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_ok_requires_2xx_and_content()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_report_all_unverified_is_empty()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_report_keeps_verified_and_counts_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_self_asserted_verified_is_ignored()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_source_without_content_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_ssrf_unsafe_urls_rejected_before_fetch()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_unparseable_url_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_unreachable_source_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_verified_report_persists_with_intact_hashchain()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_wildcard_allowlist_match_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[An unverified competitor claim submitted for citation checking.]] - rationale - gateway/security/citation_verifier.py
- [[CitationVerifier]] - code - gateway/security/citation_verifier.py
- [[Deterministic fetcher maps url - (status, sha_or_None). Records calls.]] - rationale - gateway/tests/test_citation_verifier.py
- [[DraftEntry]] - code - gateway/security/citation_verifier.py
- [[FetchOutcome_1]] - code - gateway/tests/test_citation_verifier.py
- [[TestFetchOutcome]] - code - gateway/tests/test_citation_verifier.py
- [[TestVerifyEntry]] - code - gateway/tests/test_citation_verifier.py
- [[TestVerifyReport]] - code - gateway/tests/test_citation_verifier.py
- [[Verifies competitor claims against re-fetched, allowlisted sources.]] - rationale - gateway/security/citation_verifier.py
- [[_FakeFetcher]] - code - gateway/tests/test_citation_verifier.py
- [[citation_verifier module]] - code - gateway/security/citation_verifier.py
- [[intel_report module (CompetitiveIntelReport, IntelReportStore)]] - code - gateway/security/intel_report.py
- [[test_citation_verifier.py]] - code - gateway/tests/test_citation_verifier.py
- [[test_default_allowlist_uses_permanent_egress_domains()]] - code - gateway/tests/test_citation_verifier.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Citation_Verifier
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_Api (web)]]
- 21 edges to [[_COMMUNITY_Intel Endpoint]]
- 18 edges to [[_COMMUNITY_Intel Report (security)]]
- 6 edges to [[_COMMUNITY_Web Api Coverage]]
- 3 edges to [[_COMMUNITY_Intel Pipeline]]
- 2 edges to [[_COMMUNITY_Dashboard Endpoints (web)]]

## Top bridge nodes
- [[DraftEntry]] - degree 45, connects to 6 communities
- [[CitationVerifier]] - degree 43, connects to 6 communities
- [[TestVerifyEntry]] - degree 19, connects to 3 communities
- [[test_citation_verifier.py]] - degree 15, connects to 3 communities
- [[_FakeFetcher]] - degree 14, connects to 3 communities