---
type: community
members: 27
---

# test_intel_endpoint.py

**Members:** 27 nodes

## Members
- [[dot-__call__()_12]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__init__()_176]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-ok()]] - code - gateway/security/citation_verifier.py
- [[dot-test_all_unverified_yields_empty_report()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_keeps_verified_drops_unverified()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_missing_required_field_returns_422()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_not_ok_on_non_2xx()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_not_ok_without_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_ok_requires_2xx_and_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_persisted_report_is_retrievable_and_chain_valid()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_requires_auth()_2]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_too_many_candidate_urls_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_too_many_entries_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[A source counts as proven only on a 2xx with non-empty content.]] - rationale - gateway/security/citation_verifier.py
- [[FetchOutcome]] - code - gateway/security/citation_verifier.py
- [[Point the endpoint's verifier at a deterministic fake fetcher.]] - rationale - gateway/tests/test_intel_endpoint.py
- [[Result of re-fetching a candidate citation URL through the web proxy.]] - rationale - gateway/security/citation_verifier.py
- [[TestFetchOutcome]] - code - gateway/tests/test_citation_verifier.py
- [[TestSubmitAuth]] - code - gateway/tests/test_intel_endpoint.py
- [[TestSubmitEndpoint]] - code - gateway/tests/test_intel_endpoint.py
- [[Tests for POST apiintelreports — verified competitive-intel submission…]] - rationale - gateway/tests/test_intel_endpoint.py
- [[_FakeFetcher]] - code - gateway/tests/test_intel_endpoint.py
- [[_draft()]] - code - gateway/tests/test_intel_endpoint.py
- [[_inject_fetcher()]] - code - gateway/tests/test_intel_endpoint.py
- [[client()_17]] - code - gateway/tests/test_intel_endpoint.py
- [[fixture_118]] - code
- [[test_intel_endpoint.py]] - code - gateway/tests/test_intel_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_intel_endpointpy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_DraftEntry]]
- 3 edges to [[_COMMUNITY_make_httpx_fetcher]]
- 2 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 1 edge to [[_COMMUNITY_dot-verify_entry]]
- 1 edge to [[_COMMUNITY_require_auth]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[test_intel_endpoint.py]] - degree 16, connects to 6 communities
- [[FetchOutcome]] - degree 11, connects to 3 communities
- [[_inject_fetcher()]] - degree 10, connects to 1 community
- [[TestFetchOutcome]] - degree 5, connects to 1 community
