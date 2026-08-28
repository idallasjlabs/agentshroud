---
type: community
cohesion: 0.08
members: 55
---

# Community 105

**Cohesion:** 0.08 - loosely connected
**Members:** 55 nodes

## Members
- [[.__call__()_2]] - code - gateway/tests/test_citation_verifier.py
- [[.__init__()_61]] - code - gateway/security/citation_verifier.py
- [[.__init__()_141]] - code - gateway/tests/test_citation_verifier.py
- [[._verifier()]] - code - gateway/tests/test_citation_verifier.py
- [[._verifier()_1]] - code - gateway/tests/test_citation_verifier.py
- [[._verify_url()]] - code - gateway/security/citation_verifier.py
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
- [[.verify_entry()]] - code - gateway/security/citation_verifier.py
- [[.verify_report()]] - code - gateway/security/citation_verifier.py
- [[A draft competitive-intel report submitted for citation verification.]] - rationale - gateway/web/api.py
- [[An unverified competitor claim submitted for citation checking.]] - rationale - gateway/security/citation_verifier.py
- [[Build a CitationVerifier wired to the production (httpx) fetcher.      Isolated]] - rationale - gateway/web/api.py
- [[CitationVerifier]] - code - gateway/security/citation_verifier.py
- [[Deterministic fetcher maps url - (status, sha_or_None). Records calls.]] - rationale - gateway/tests/test_citation_verifier.py
- [[DraftEntry]] - code - gateway/security/citation_verifier.py
- [[FetchOutcome_1]] - code - gateway/tests/test_citation_verifier.py
- [[IntelDraftEntry]] - code - gateway/web/api.py
- [[IntelDraftRequest]] - code - gateway/web/api.py
- [[One unverified competitor claim + its candidate source URLs.]] - rationale - gateway/web/api.py
- [[Re-fetch url and return a Citation iff it is allowlisted + live.          SSRF]] - rationale - gateway/security/citation_verifier.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard).      Sin]] - rationale - gateway/security/egress_config.py
- [[Return a CompetitorEntry with only its valid citations, or None.          None m]] - rationale - gateway/security/citation_verifier.py
- [[TestFetchOutcome]] - code - gateway/tests/test_citation_verifier.py
- [[TestVerifyEntry]] - code - gateway/tests/test_citation_verifier.py
- [[TestVerifyReport]] - code - gateway/tests/test_citation_verifier.py
- [[Verifies competitor claims against re-fetched, allowlisted sources.]] - rationale - gateway/security/citation_verifier.py
- [[Verify and persist a draft competitive-intel report (SCRUM-75).      Each draft]] - rationale - gateway/web/api.py
- [[Verify every draft claim; return a report of only verified claims.          Clai]] - rationale - gateway/security/citation_verifier.py
- [[_FakeFetcher]] - code - gateway/tests/test_citation_verifier.py
- [[_intel_verifier()]] - code - gateway/web/api.py
- [[citation_verifier module]] - code - gateway/security/citation_verifier.py
- [[domain_matches()]] - code - gateway/security/egress_config.py
- [[intel_report module (CompetitiveIntelReport, IntelReportStore)]] - code - gateway/security/intel_report.py
- [[submit_competitive_intel()]] - code - gateway/web/api.py
- [[test_citation_verifier.py]] - code - gateway/tests/test_citation_verifier.py
- [[test_default_allowlist_uses_permanent_egress_domains()]] - code - gateway/tests/test_citation_verifier.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_105
SORT file.name ASC
```

## Connections to other communities
- 29 edges to [[_COMMUNITY_Community 58]]
- 22 edges to [[_COMMUNITY_Community 113]]
- 17 edges to [[_COMMUNITY_Community 37]]
- 8 edges to [[_COMMUNITY_Community 29]]
- 2 edges to [[_COMMUNITY_Community 14]]
- 2 edges to [[_COMMUNITY_Community 50]]
- 1 edge to [[_COMMUNITY_Community 174]]

## Top bridge nodes
- [[DraftEntry]] - degree 45, connects to 4 communities
- [[CitationVerifier]] - degree 43, connects to 4 communities
- [[IntelDraftRequest]] - degree 7, connects to 3 communities
- [[domain_matches()]] - degree 6, connects to 3 communities
- [[IntelDraftEntry]] - degree 6, connects to 3 communities