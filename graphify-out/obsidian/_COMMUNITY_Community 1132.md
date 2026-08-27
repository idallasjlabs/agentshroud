---
type: community
members: 6
---

# Community 1132

**Members:** 6 nodes

## Members
- [[.compute_content_hash()]] - code - gateway/security/audit_store.py
- [[.compute_entry_hash()]] - code - gateway/security/audit_store.py
- [[.verify_hash_chain()]] - code - gateway/security/audit_store.py
- [[Compute SHA-256 hash of event content (excluding hashes).]] - rationale - gateway/security/audit_store.py
- [[Compute entry hash including previous hash (chain).]] - rationale - gateway/security/audit_store.py
- [[Verify the integrity of the hash chain.          Args             start_id Sta]] - rationale - gateway/security/audit_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1132
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 89]]
- 2 edges to [[_COMMUNITY_Community 232]]

## Top bridge nodes
- [[.compute_entry_hash()]] - degree 5, connects to 2 communities
- [[.verify_hash_chain()]] - degree 4, connects to 2 communities
- [[.compute_content_hash()]] - degree 3, connects to 1 community