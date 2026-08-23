---
type: community
cohesion: 0.25
members: 8
---

# Api Contract Fuzz

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[(method, path) for every non-destructive route declaring a requestBody.]] - rationale - gateway/tests/test_api_contract_fuzz.py
- [[_deep_nest()]] - code - gateway/tests/test_api_contract_fuzz.py
- [[_fuzzable_endpoints()]] - code - gateway/tests/test_api_contract_fuzz.py
- [[client()_1]] - code - gateway/tests/test_api_contract_fuzz.py
- [[test_api_contract_fuzz.py]] - code - gateway/tests/test_api_contract_fuzz.py
- [[test_destructive_routes_are_excluded()]] - code - gateway/tests/test_api_contract_fuzz.py
- [[test_endpoint_survives_adversarial_body()]] - code - gateway/tests/test_api_contract_fuzz.py
- [[test_fuzz_surface_is_nonempty()]] - code - gateway/tests/test_api_contract_fuzz.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Api_Contract_Fuzz
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Docs Accuracy]]

## Top bridge nodes
- [[test_api_contract_fuzz.py]] - degree 7, connects to 1 community