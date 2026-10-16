---
type: community
cohesion: 0.20
members: 18
---

# FetchOutcome

**Cohesion:** 0.20 - loosely connected
**Members:** 18 nodes

## Members
- [[dot-__call__()_9]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-__init__()_157]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_all_unverified_yields_empty_report()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_keeps_verified_drops_unverified()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_missing_required_field_returns_422()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_persisted_report_is_retrievable_and_chain_valid()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_requires_auth()_2]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_too_many_candidate_urls_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[dot-test_too_many_entries_rejected()]] - code - gateway/tests/test_intel_endpoint.py
- [[Point the endpoint's verifier at a deterministic fake fetcher.]] - rationale - gateway/tests/test_intel_endpoint.py
- [[TestSubmitAuth]] - code - gateway/tests/test_intel_endpoint.py
- [[TestSubmitEndpoint]] - code - gateway/tests/test_intel_endpoint.py
- [[_FakeFetcher]] - code - gateway/tests/test_intel_endpoint.py
- [[_draft()]] - code - gateway/tests/test_intel_endpoint.py
- [[_inject_fetcher()]] - code - gateway/tests/test_intel_endpoint.py
- [[client()_11]] - code - gateway/tests/test_intel_endpoint.py
- [[test_intel_endpoint.py]] - code - gateway/tests/test_intel_endpoint.py
- [[webapi.py (POST apiintelreports)]] - code - gateway/web/api.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/FetchOutcome
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_api.py_1]]
- 3 edges to [[_COMMUNITY_FetchOutcome]]
- 2 edges to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_Path]]

## Top bridge nodes
- [[webapi.py (POST apiintelreports)]] - degree 5, connects to 4 communities
- [[test_intel_endpoint.py]] - degree 14, connects to 3 communities
- [[_inject_fetcher()]] - degree 10, connects to 1 community
- [[TestSubmitEndpoint]] - degree 9, connects to 1 community
- [[_FakeFetcher]] - degree 6, connects to 1 community
