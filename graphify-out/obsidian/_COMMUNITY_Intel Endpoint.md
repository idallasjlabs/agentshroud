---
type: community
cohesion: 0.08
members: 50
---

# Intel Endpoint

**Cohesion:** 0.08 - loosely connected
**Members:** 50 nodes

## Members
- [[.__call__()_6]] - code - gateway/tests/test_intel_endpoint.py
- [[.__enter__()]] - code - gateway/tests/test_citation_verifier.py
- [[.__enter__()_3]] - code - gateway/tests/test_intel_endpoint.py
- [[.__exit__()]] - code - gateway/tests/test_citation_verifier.py
- [[.__exit__()_3]] - code - gateway/tests/test_intel_endpoint.py
- [[.__init__()_142]] - code - gateway/tests/test_citation_verifier.py
- [[.__init__()_165]] - code - gateway/tests/test_intel_endpoint.py
- [[.__init__()_166]] - code - gateway/tests/test_intel_endpoint.py
- [[._patch_stream()]] - code - gateway/tests/test_citation_verifier.py
- [[.iter_bytes()]] - code - gateway/tests/test_citation_verifier.py
- [[.iter_bytes()_1]] - code - gateway/tests/test_intel_endpoint.py
- [[.ok()_1]] - code - gateway/security/citation_verifier.py
- [[.test_2xx_with_body_hashes_content()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_2xx_with_body_is_proven()]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_all_unverified_yields_empty_report()]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_byte_budget_caps_reads()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_empty_body_is_not_proven()]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_empty_body_yields_no_hash()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_keeps_verified_drops_unverified()]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_missing_required_field_returns_422()]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_network_error_maps_to_599()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_network_error_maps_to_599()_1]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_non_2xx_status_passed_through()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_oversize_body_is_capped()]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_persisted_report_is_retrievable_and_chain_valid()]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_redirect_is_not_proven()]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_requires_auth()_2]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_secure_stream_kwargs_are_pinned()]] - code - gateway/tests/test_citation_verifier.py
- [[.test_too_many_candidate_urls_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[.test_too_many_entries_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[A source counts as proven only on a 2xx with non-empty content.]] - rationale - gateway/security/citation_verifier.py
- [[Fake httpx.stream context manager yielding a body in chunks.]] - rationale - gateway/tests/test_intel_endpoint.py
- [[FetchOutcome]] - code - gateway/security/citation_verifier.py
- [[Patch httpx.stream; return a list that records the call kwargs.]] - rationale - gateway/tests/test_citation_verifier.py
- [[Point the endpoint's verifier at a deterministic fake fetcher.]] - rationale - gateway/tests/test_intel_endpoint.py
- [[Production fetcher stream the URL and hash the body as proof-of-source.      SE]] - rationale - gateway/security/citation_verifier.py
- [[Result of re-fetching a candidate citation URL through the web proxy.]] - rationale - gateway/security/citation_verifier.py
- [[Stand-in for the object httpx.stream() yields as a context manager.]] - rationale - gateway/tests/test_citation_verifier.py
- [[TestHttpxFetcher]] - code - gateway/tests/test_intel_endpoint.py
- [[TestMakeHttpxFetcher]] - code - gateway/tests/test_citation_verifier.py
- [[TestSubmitAuth]] - code - gateway/tests/test_intel_endpoint.py
- [[TestSubmitEndpoint]] - code - gateway/tests/test_intel_endpoint.py
- [[_FakeFetcher_1]] - code - gateway/tests/test_intel_endpoint.py
- [[_FakeStreamResponse]] - code - gateway/tests/test_citation_verifier.py
- [[_StreamResp]] - code - gateway/tests/test_intel_endpoint.py
- [[_draft()]] - code - gateway/tests/test_intel_endpoint.py
- [[_inject_fetcher()]] - code - gateway/tests/test_intel_endpoint.py
- [[client()_8]] - code - gateway/tests/test_intel_endpoint.py
- [[make_httpx_fetcher()]] - code - gateway/security/citation_verifier.py
- [[test_intel_endpoint.py]] - code - gateway/tests/test_intel_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Intel_Endpoint
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_Citation Verifier]]
- 7 edges to [[_COMMUNITY_Intel Report (security)]]
- 4 edges to [[_COMMUNITY_Api (web)]]
- 1 edge to [[_COMMUNITY_Intel Pipeline]]
- 1 edge to [[_COMMUNITY_Web Api Coverage]]
- 1 edge to [[_COMMUNITY_Dashboard Endpoints (web)]]

## Top bridge nodes
- [[FetchOutcome]] - degree 21, connects to 3 communities
- [[make_httpx_fetcher()]] - degree 18, connects to 3 communities
- [[_FakeStreamResponse]] - degree 16, connects to 3 communities
- [[test_intel_endpoint.py]] - degree 14, connects to 3 communities
- [[TestMakeHttpxFetcher]] - degree 13, connects to 3 communities