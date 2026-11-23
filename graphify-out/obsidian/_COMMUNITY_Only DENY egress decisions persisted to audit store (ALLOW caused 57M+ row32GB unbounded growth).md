---
type: community
members: 1
---

# Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row/32GB unbounded growth)

**Members:** 1 nodes

## Members
- [[Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row32GB unbounded growth)]] - rationale - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Only_DENY_egress_decisions_persisted_to_audit_store_ALLOW_caused_57M_row/32GB_unbounded_growth
SORT file.name ASC
```
