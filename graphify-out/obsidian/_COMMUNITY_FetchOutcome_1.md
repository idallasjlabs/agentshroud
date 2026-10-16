---
type: community
cohesion: 0.17
members: 22
---

# FetchOutcome

**Cohesion:** 0.17 - loosely connected
**Members:** 22 nodes

## Members
- [[dot-__call__()_9]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__init__()_137]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-ok()_1]] - code - gateway/security/citation_verifier.py
- [[dot-test_all_unverified_yields_empty_report()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_keeps_verified_drops_unverified()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_missing_required_field_returns_422()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_persisted_report_is_retrievable_and_chain_valid()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_requires_auth()_3]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_too_many_candidate_urls_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_too_many_entries_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[A source counts as proven only on a 2xx with non-empty content.]] - rationale - gateway/security/citation_verifier.py
- [[FetchOutcome_1]] - code - gateway/security/citation_verifier.py
- [[Point the endpoint's verifier at a deterministic fake fetcher.]] - rationale - gateway/tests/test_intel_endpoint.py
- [[Result of re-fetching a candidate citation URL through the web proxy.]] - rationale - gateway/security/citation_verifier.py
- [[TestSubmitAuth]] - code - gateway/tests/test_intel_endpoint.py
- [[TestSubmitEndpoint]] - code - gateway/tests/test_intel_endpoint.py
- [[_FakeFetcher_1]] - code - gateway/tests/test_intel_endpoint.py
- [[_draft()]] - code - gateway/tests/test_intel_endpoint.py
- [[_inject_fetcher()]] - code - gateway/tests/test_intel_endpoint.py
- [[client()_17]] - code - gateway/tests/test_intel_endpoint.py
- [[test_intel_endpoint.py]] - code - gateway/tests/test_intel_endpoint.py
- [[webapi.py (POST apiintelreports)]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FetchOutcome
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_api.py_1]]
- 7 edges to [[_COMMUNITY_FetchOutcome]]
- 3 edges to [[_COMMUNITY_CompetitiveIntelReport_1]]
- 2 edges to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_CompetitiveIntelReport]]
- 1 edge to [[_COMMUNITY_Path]]

## Top bridge nodes
- [[FetchOutcome_1]] - degree 21, connects to 4 communities
- [[webapi.py (POST apiintelreports)]] - degree 5, connects to 4 communities
- [[test_intel_endpoint.py]] - degree 14, connects to 3 communities
- [[_inject_fetcher()]] - degree 10, connects to 1 community
- [[TestSubmitEndpoint]] - degree 9, connects to 1 community
