---
type: community
cohesion: 0.11
members: 19
---

# test_ledger.py

**Cohesion:** 0.11 - loosely connected
**Members:** 19 nodes

## Members
- [[Test creating a ledger entry]] - rationale - gateway/tests/test_ledger.py
- [[Test deleting a ledger entry]] - rationale - gateway/tests/test_ledger.py
- [[Test deleting a non-existent entry]] - rationale - gateway/tests/test_ledger.py
- [[Test ledger query with source filter]] - rationale - gateway/tests/test_ledger.py
- [[Test paginated ledger query]] - rationale - gateway/tests/test_ledger.py
- [[Test querying ledger with forwarded_to filter]] - rationale - gateway/tests/test_ledger.py
- [[Test querying ledger with time range filters]] - rationale - gateway/tests/test_ledger.py
- [[Test retrieving a ledger entry by ID]] - rationale - gateway/tests/test_ledger.py
- [[Test stats calculation]] - rationale - gateway/tests/test_ledger.py
- [[test_delete_entry()]] - code - gateway/tests/test_ledger.py
- [[test_delete_nonexistent()]] - code - gateway/tests/test_ledger.py
- [[test_get_entry()]] - code - gateway/tests/test_ledger.py
- [[test_get_stats()_1]] - code - gateway/tests/test_ledger.py
- [[test_ledger.py]] - code - gateway/tests/test_ledger.py
- [[test_query_ledger()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_forwarded_to_filter()]] - code - gateway/tests/test_ledger.py
- [[test_query_with_time_filters()]] - code - gateway/tests/test_ledger.py
- [[test_record_entry()]] - code - gateway/tests/test_ledger.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_ledgerpy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_SSHProxy]]

## Top bridge nodes
- [[test_ledger.py]] - degree 12, connects to 1 community