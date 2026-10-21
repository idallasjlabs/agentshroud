---
type: community
members: 2
---

# MiddlewareManager Session Enforcement Tests

**Members:** 2 nodes

## Members
- [[APPROVAL_ITEMS entity]] - concept - docs/diagrams/images/diagram-08-erd.svg
- [[LEDGER entity (id, timestamp, source, content_hash, original_content_hash, sanitized, size, redaction_count, redaction_types, forwarded_to, content_type, metadata, created_at, expires_at)]] - concept - docs/diagrams/images/diagram-08-erd.svg

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/MiddlewareManager_Session_Enforcement_Tests
SORT file.name ASC
```
