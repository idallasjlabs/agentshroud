---
type: community
members: 7
---

# Phase 2 — Security Core (HMAC Auth + PII Sanitizer, HTTP CONNECT Proxy, Approval Queue)

**Members:** 7 nodes

## Members
- [[Database Files]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Purpose_6]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Related Notes_10]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[WAL Mode]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Where Used_1]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[aiosqlite_1]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[aiosqlite]] - document - docs/vault/05 - Dependencies/aiosqlite.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Phase_2__Security_Core_HMAC_Auth__PII_Sanitizer_HTTP_CONNECT_Proxy_Approval_Queue
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY__make_proxy()]]
- 1 edge to [[_COMMUNITY_AlertDispatcher (5)]]

## Top bridge nodes
- [[aiosqlite]] - degree 5, connects to 4 communities
