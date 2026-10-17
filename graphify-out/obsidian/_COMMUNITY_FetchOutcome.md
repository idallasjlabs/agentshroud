---
type: community
members: 50
---

# FetchOutcome

**Members:** 50 nodes

## Members
- [[dot-__call__()_3]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__enter__()_1]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__enter__()_2]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__exit__()_1]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__exit__()_2]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__init__()_50]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__init__()_51]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__init__()_52]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-_patch_stream()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-iter_bytes()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-iter_bytes()_1]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-ok()]] - code - gateway/security/citation_verifier.py
- [[dot-test_2xx_with_body_hashes_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_2xx_with_body_is_proven()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_all_unverified_yields_empty_report()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_byte_budget_caps_reads()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_empty_body_is_not_proven()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_empty_body_yields_no_hash()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_keeps_verified_drops_unverified()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_missing_required_field_returns_422()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_network_error_maps_to_599()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_network_error_maps_to_599()_1]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_non_2xx_status_passed_through()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_oversize_body_is_capped()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_persisted_report_is_retrievable_and_chain_valid()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_redirect_is_not_proven()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_requires_auth()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_secure_stream_kwargs_are_pinned()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_too_many_candidate_urls_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_too_many_entries_rejected()]] - code - gateway/tests/test_intel_endpoint.py
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
- [[_FakeFetcher]] - code - gateway/tests/test_intel_endpoint.py
- [[_FakeStreamResponse_1]] - code - gateway/tests/test_citation_verifier.py
- [[_StreamResp]] - code - gateway/tests/test_intel_endpoint.py
- [[_draft()]] - code - gateway/tests/test_intel_endpoint.py
- [[_inject_fetcher()]] - code - gateway/tests/test_intel_endpoint.py
- [[client()_5]] - code - gateway/tests/test_intel_endpoint.py
- [[make_httpx_fetcher()]] - code - gateway/security/citation_verifier.py
- [[test_intel_endpoint.py]] - code - gateway/tests/test_intel_endpoint.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FetchOutcome
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_api.py (2)_1]]
- 8 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 4 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_ModeRequest]]

## Top bridge nodes
- [[make_httpx_fetcher()]] - degree 18, connects to 3 communities
- [[_FakeStreamResponse_1]] - degree 16, connects to 3 communities
- [[TestMakeHttpxFetcher]] - degree 13, connects to 3 communities
- [[FetchOutcome]] - degree 21, connects to 2 communities
- [[test_intel_endpoint.py]] - degree 14, connects to 2 communities
