---
type: community
members: 74
---

# MCPPolicyEngine (2)

**Members:** 74 nodes

## Members
- [[dot-__call__()_9]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__call__()_10]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__init__()_171]] - code - gateway/security/citation_verifier.py
- [[dot-__init__()_172]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__init__()_173]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-_verifier()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-_verifier()_1]] - code - gateway/tests/test_citation_verifier.py
- [[dot-_verify_url()]] - code - gateway/security/citation_verifier.py
- [[dot-ok()_2]] - code - gateway/security/citation_verifier.py
- [[dot-test_all_unverified_yields_empty_report()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_allowlisted_live_source_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_dropped_count_is_tamper_evident()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_generated_at_is_preserved()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_host_confusion_urls_rejected_and_never_fetched()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_keeps_verified_drops_unverified()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_missing_required_field_returns_422()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_mixed_valid_and_invalid_keeps_only_valid()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_multiple_valid_citations_all_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_no_candidate_urls_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_not_ok_on_non_2xx()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_not_ok_without_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_off_allowlist_url_dropped_and_not_fetched()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_ok_requires_2xx_and_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_persisted_report_is_retrievable_and_chain_valid()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_report_all_unverified_is_empty()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_report_keeps_verified_and_counts_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_requires_auth()_4]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_self_asserted_verified_is_ignored()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_source_without_content_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_ssrf_unsafe_urls_rejected_before_fetch()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_too_many_candidate_urls_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_too_many_entries_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_unparseable_url_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_unreachable_source_dropped()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_verified_report_persists_with_intact_hashchain()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_wildcard_allowlist_match_kept()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-verify_entry()]] - code - gateway/security/citation_verifier.py
- [[dot-verify_report()]] - code - gateway/security/citation_verifier.py
- [[A source counts as proven only on a 2xx with non-empty content.]] - rationale - gateway/security/citation_verifier.py
- [[A verified source backing a competitor claim.      A Citation is only created by]] - rationale - gateway/security/intel_report.py
- [[An unverified competitor claim submitted for citation checking.]] - rationale - gateway/security/citation_verifier.py
- [[Citation]] - code - gateway/security/citation_verifier.py
- [[Citation_1]] - code - gateway/security/intel_report.py
- [[CitationVerifier]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport]] - code - gateway/security/citation_verifier.py
- [[CompetitorEntry]] - code - gateway/security/citation_verifier.py
- [[Deterministic fetcher maps url - (status, sha_or_None). Records calls.]] - rationale - gateway/tests/test_citation_verifier.py
- [[DraftEntry]] - code - gateway/security/citation_verifier.py
- [[FetchOutcome]] - code - gateway/tests/test_citation_verifier.py
- [[FetchOutcome_1]] - code - gateway/security/citation_verifier.py
- [[Fetcher]] - code - gateway/security/citation_verifier.py
- [[Point the endpoint's verifier at a deterministic fake fetcher.]] - rationale - gateway/tests/test_intel_endpoint.py
- [[Re-fetch url and return a Citation iff it is allowlisted + live.          SSRF]] - rationale - gateway/security/citation_verifier.py
- [[Result of re-fetching a candidate citation URL through the web proxy.]] - rationale - gateway/security/citation_verifier.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard). Single…]] - rationale - gateway/security/egress_config.py
- [[Return a CompetitorEntry with only its valid citations, or None.          None m]] - rationale - gateway/security/citation_verifier.py
- [[TestFetchOutcome]] - code - gateway/tests/test_citation_verifier.py
- [[TestSubmitAuth]] - code - gateway/tests/test_intel_endpoint.py
- [[TestSubmitEndpoint]] - code - gateway/tests/test_intel_endpoint.py
- [[TestVerifyEntry]] - code - gateway/tests/test_citation_verifier.py
- [[TestVerifyReport]] - code - gateway/tests/test_citation_verifier.py
- [[Verifies competitor claims against re-fetched, allowlisted sources.]] - rationale - gateway/security/citation_verifier.py
- [[Verify every draft claim; return a report of only verified claims.          Clai]] - rationale - gateway/security/citation_verifier.py
- [[_FakeFetcher]] - code - gateway/tests/test_citation_verifier.py
- [[_FakeFetcher_1]] - code - gateway/tests/test_intel_endpoint.py
- [[_draft()]] - code - gateway/tests/test_intel_endpoint.py
- [[_inject_fetcher()]] - code - gateway/tests/test_intel_endpoint.py
- [[citation_verifier module]] - code - gateway/security/citation_verifier.py
- [[citation_verifier.py]] - code - gateway/security/citation_verifier.py
- [[client()_19]] - code - gateway/tests/test_intel_endpoint.py
- [[domain_matches()]] - code - gateway/security/egress_config.py
- [[test_citation_verifier.py]] - code - gateway/tests/test_citation_verifier.py
- [[test_default_allowlist_uses_permanent_egress_domains()]] - code - gateway/tests/test_citation_verifier.py
- [[test_intel_endpoint.py]] - code - gateway/tests/test_intel_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MCPPolicyEngine_2
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_KillSwitchMonitor (3)]]
- 19 edges to [[_COMMUNITY_MCPPolicyEngine]]
- 18 edges to [[_COMMUNITY_TelegramAPIProxy (3)]]
- 10 edges to [[_COMMUNITY_AsyncMock]]
- 5 edges to [[_COMMUNITY_EgressFilterConfig (2)]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig (3)]]

## Top bridge nodes
- [[DraftEntry]] - degree 45, connects to 4 communities
- [[CitationVerifier]] - degree 43, connects to 4 communities
- [[citation_verifier.py]] - degree 10, connects to 3 communities
- [[FetchOutcome_1]] - degree 21, connects to 2 communities
- [[test_citation_verifier.py]] - degree 15, connects to 2 communities
