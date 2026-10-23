---
type: community
cohesion: 0.25
members: 8
---

# Phase 2 — Security Core (HMAC Auth + PII Sanitizer, HTTP CONNECT Proxy, Approval Queue)

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[Database Files]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Purpose_4]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Related Notes_6]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[WAL Mode]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[Where Used]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[aiosqlite_1]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[aiosqlite]] - document - docs/vault/05 - Dependencies/aiosqlite.md
- [[store.py]] - code - gateway/approval_queue/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Phase_2__Security_Core_HMAC_Auth__PII_Sanitizer_HTTP_CONNECT_Proxy_Approval_Queue
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY__make_proxy()]]
- 2 edges to [[_COMMUNITY_Restart Procedure]]
- 1 edge to [[_COMMUNITY_ContextSegment]]
- 1 edge to [[_COMMUNITY_ApprovalStore]]
- 1 edge to [[_COMMUNITY_test_voice_latency_guard.py]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]

## Top bridge nodes
- [[store.py]] - degree 7, connects to 5 communities
- [[aiosqlite]] - degree 5, connects to 3 communities
