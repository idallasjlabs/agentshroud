---
type: community
cohesion: 0.07
members: 64
---

# api.py

**Cohesion:** 0.07 - loosely connected
**Members:** 64 nodes

## Members
- [[dot-__call__()_10]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__init__()_198]] - code - gateway/security/citation_verifier.py
- [[dot-__init__()_199]] - code - gateway/tests/test_citation_verifier.py
- [[dot-_verifier()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-_verifier()_1]] - code - gateway/tests/test_citation_verifier.py
- [[dot-_verify_url()]] - code - gateway/security/citation_verifier.py
- [[dot-ok()_2]] - code - gateway/security/citation_verifier.py
- [[dot-test_allowlisted_live_source_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_dropped_count_is_tamper_evident()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_generated_at_is_preserved()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_host_confusion_urls_rejected_and_never_fetched()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_mixed_valid_and_invalid_keeps_only_valid()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_multiple_valid_citations_all_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_no_candidate_urls_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_not_ok_on_non_2xx()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_not_ok_without_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_off_allowlist_url_dropped_and_not_fetched()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_ok_requires_2xx_and_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_report_all_unverified_is_empty()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_report_keeps_verified_and_counts_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_self_asserted_verified_is_ignored()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_source_without_content_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_ssrf_unsafe_urls_rejected_before_fetch()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_unparseable_url_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_unreachable_source_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_verified_report_persists_with_intact_hashchain()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_wildcard_allowlist_match_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-verify_entry()]] - code - gateway/security/citation_verifier.py
- [[dot-verify_report()]] - code - gateway/security/citation_verifier.py
- [[A draft competitive-intel report submitted for citation verification.]] - rationale - gateway/web/api.py
- [[A source counts as proven only on a 2xx with non-empty content.]] - rationale - gateway/security/citation_verifier.py
- [[A verified source backing a competitor claim.      A Citation is only created by]] - rationale - gateway/security/intel_report.py
- [[An unverified competitor claim submitted for citation checking.]] - rationale - gateway/security/citation_verifier.py
- [[Build a CitationVerifier wired to the production (httpx) fetcher.      Isolated]] - rationale - gateway/web/api.py
- [[Citation]] - code - gateway/security/citation_verifier.py
- [[Citation_1]] - code - gateway/security/intel_report.py
- [[CitationVerifier]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport_2]] - code - gateway/security/citation_verifier.py
- [[CompetitorEntry_1]] - code - gateway/security/citation_verifier.py
- [[Deterministic fetcher maps url - (status, sha_or_None). Records calls.]] - rationale - gateway/tests/test_citation_verifier.py
- [[DraftEntry]] - code - gateway/security/citation_verifier.py
- [[FetchOutcome]] - code - gateway/tests/test_citation_verifier.py
- [[FetchOutcome_1]] - code - gateway/security/citation_verifier.py
- [[Fetcher]] - code - gateway/security/citation_verifier.py
- [[IntelDraftEntry]] - code - gateway/web/api.py
- [[IntelDraftRequest]] - code - gateway/web/api.py
- [[One unverified competitor claim + its candidate source URLs.]] - rationale - gateway/web/api.py
- [[Re-fetch url and return a Citation iff it is allowlisted + live.          SSRF]] - rationale - gateway/security/citation_verifier.py
- [[Result of re-fetching a candidate citation URL through the web proxy.]] - rationale - gateway/security/citation_verifier.py
- [[Return a CompetitorEntry with only its valid citations, or None.          None m]] - rationale - gateway/security/citation_verifier.py
- [[TestFetchOutcome]] - code - gateway/tests/test_citation_verifier.py
- [[TestVerifyEntry]] - code - gateway/tests/test_citation_verifier.py
- [[TestVerifyReport]] - code - gateway/tests/test_citation_verifier.py
- [[Verifies competitor claims against re-fetched, allowlisted sources.]] - rationale - gateway/security/citation_verifier.py
- [[Verify and persist a draft competitive-intel report (SCRUM-75).      Each draft]] - rationale - gateway/web/api.py
- [[Verify every draft claim; return a report of only verified claims.          Clai]] - rationale - gateway/security/citation_verifier.py
- [[_FakeFetcher_1]] - code - gateway/tests/test_citation_verifier.py
- [[_intel_verifier()]] - code - gateway/web/api.py
- [[citation_verifier module]] - code - gateway/security/citation_verifier.py
- [[citation_verifier.py]] - code - gateway/security/citation_verifier.py
- [[intel_report.py]] - code - gateway/security/intel_report.py
- [[submit_competitive_intel()]] - code - gateway/web/api.py
- [[test_citation_verifier.py]] - code - gateway/tests/test_citation_verifier.py
- [[test_default_allowlist_uses_permanent_egress_domains()]] - code - gateway/tests/test_citation_verifier.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/apipy
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 17 edges to [[_COMMUNITY_api.py]]
- 16 edges to [[_COMMUNITY_FetchOutcome]]
- 11 edges to [[_COMMUNITY_FetchOutcome_1]]
- 8 edges to [[_COMMUNITY_ModeRequest]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig]]
- 3 edges to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[CitationVerifier]] - degree 43, connects to 5 communities
- [[DraftEntry]] - degree 45, connects to 4 communities
- [[FetchOutcome_1]] - degree 21, connects to 3 communities
- [[citation_verifier.py]] - degree 10, connects to 3 communities
- [[IntelDraftRequest]] - degree 7, connects to 3 communities
