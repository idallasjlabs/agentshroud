---
type: community
cohesion: 0.12
members: 29
---

# FetchOutcome

**Cohesion:** 0.12 - loosely connected
**Members:** 29 nodes

## Members
- [[dot-__enter__()_1]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__enter__()_2]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__exit__()_1]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__exit__()_2]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__init__()_113]] - code - gateway/tests/test_citation_verifier.py
- [[dot-__init__()_114]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-_patch_stream()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-iter_bytes()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-iter_bytes()_1]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_2xx_with_body_hashes_content()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_2xx_with_body_is_proven()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_byte_budget_caps_reads()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_empty_body_is_not_proven()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_empty_body_yields_no_hash()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_network_error_maps_to_599()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_network_error_maps_to_599()_1]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_non_2xx_status_passed_through()]] - code - gateway/tests/test_citation_verifier.py
- [[dot-test_oversize_body_is_capped()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_redirect_is_not_proven()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_secure_stream_kwargs_are_pinned()]] - code - gateway/tests/test_citation_verifier.py
- [[Fake httpx.stream context manager yielding a body in chunks.]] - rationale - gateway/tests/test_intel_endpoint.py
- [[Patch httpx.stream; return a list that records the call kwargs.]] - rationale - gateway/tests/test_citation_verifier.py
- [[Production fetcher stream the URL and hash the body as proof-of-source.      SE]] - rationale - gateway/security/citation_verifier.py
- [[Stand-in for the object httpx.stream() yields as a context manager.]] - rationale - gateway/tests/test_citation_verifier.py
- [[TestHttpxFetcher]] - code - gateway/tests/test_intel_endpoint.py
- [[TestMakeHttpxFetcher]] - code - gateway/tests/test_citation_verifier.py
- [[_FakeStreamResponse_1]] - code - gateway/tests/test_citation_verifier.py
- [[_StreamResp]] - code - gateway/tests/test_intel_endpoint.py
- [[make_httpx_fetcher()]] - code - gateway/security/citation_verifier.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FetchOutcome
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_api.py_1]]
- 4 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 3 edges to [[_COMMUNITY_FetchOutcome_1]]
- 1 edge to [[_COMMUNITY_api.py]]

## Top bridge nodes
- [[make_httpx_fetcher()]] - degree 18, connects to 3 communities
- [[_FakeStreamResponse_1]] - degree 16, connects to 2 communities
- [[TestMakeHttpxFetcher]] - degree 13, connects to 2 communities
- [[_StreamResp]] - degree 12, connects to 2 communities
- [[TestHttpxFetcher]] - degree 8, connects to 2 communities
