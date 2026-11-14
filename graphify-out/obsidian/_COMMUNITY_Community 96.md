---
type: community
members: 50
---

# Community 96

**Members:** 50 nodes

## Members
- [[.__init__()_23]] - code - gateway/inbound_edge/store.py
- [[._one()]] - code - gateway/inbound_edge/store.py
- [[.add_client()]] - code - gateway/inbound_edge/store.py
- [[.add_ticket()]] - code - gateway/inbound_edge/store.py
- [[.approval_for_ticket()]] - code - gateway/inbound_edge/store.py
- [[.close()_6]] - code - gateway/inbound_edge/store.py
- [[.consume_approval()]] - code - gateway/inbound_edge/store.py
- [[.consume_enrollment()]] - code - gateway/inbound_edge/store.py
- [[.db()]] - code - gateway/inbound_edge/store.py
- [[.enrollment_window_vendor()]] - code - gateway/inbound_edge/store.py
- [[.get_client()_2]] - code - gateway/inbound_edge/store.py
- [[.has_jti()]] - code - gateway/inbound_edge/store.py
- [[.jti_issued()]] - code - gateway/inbound_edge/store.py
- [[.kill()]] - code - gateway/inbound_edge/store.py
- [[.killed_reason()]] - code - gateway/inbound_edge/store.py
- [[.list_clients()]] - code - gateway/inbound_edge/store.py
- [[.list_kills()]] - code - gateway/inbound_edge/store.py
- [[.open_approval_for()]] - code - gateway/inbound_edge/store.py
- [[.open_enrollment()]] - code - gateway/inbound_edge/store.py
- [[.peek_code()]] - code - gateway/inbound_edge/store.py
- [[.peek_pending()]] - code - gateway/inbound_edge/store.py
- [[.peek_refresh()]] - code - gateway/inbound_edge/store.py
- [[.purge_expired()]] - code - gateway/inbound_edge/store.py
- [[.put_approval()]] - code - gateway/inbound_edge/store.py
- [[.put_code()]] - code - gateway/inbound_edge/store.py
- [[.put_pending()]] - code - gateway/inbound_edge/store.py
- [[.put_refresh()]] - code - gateway/inbound_edge/store.py
- [[.record_jti()]] - code - gateway/inbound_edge/store.py
- [[.revoke_refresh_family()]] - code - gateway/inbound_edge/store.py
- [[.rotate_refresh()]] - code - gateway/inbound_edge/store.py
- [[.take_code()]] - code - gateway/inbound_edge/store.py
- [[.take_pending()]] - code - gateway/inbound_edge/store.py
- [[.unkill()]] - code - gateway/inbound_edge/store.py
- [[Any_14]] - code - gateway/inbound_edge/store.py
- [[Async SQLite store. One instance per gateway process.]] - rationale - gateway/inbound_edge/store.py
- [[Atomically mark an approval used. True for exactly one caller.]] - rationale - gateway/inbound_edge/store.py
- [[Connection]] - code - gateway/inbound_edge/store.py
- [[Consume a refresh token. Reuse of a consumed token revokes its family.]] - rationale - gateway/inbound_edge/store.py
- [[EdgeStore_4]] - code - gateway/inbound_edge/store.py
- [[Mint a one-time code the owner types on the consent page. Returned once.]] - rationale - gateway/inbound_edge/store.py
- [[Path_2]] - code - gateway/inbound_edge/store.py
- [[RFC 7009 revocation of a refresh token kills its whole family.]] - rationale - gateway/inbound_edge/store.py
- [[Return and delete an unexpired code. A second call returns None.]] - rationale - gateway/inbound_edge/store.py
- [[The newest unconsumed, unexpired request_id for this idempotency key.]] - rationale - gateway/inbound_edge/store.py
- [[The vendor with an open (unused, unexpired) enrollment, if exactly one.]] - rationale - gateway/inbound_edge/store.py
- [[True exactly once for an unexpired code bound to ``vendor``; else None.]] - rationale - gateway/inbound_edge/store.py
- [[Whether ``jti`` was ever issued (and not yet purged) — guards a typo'd kill.]] - rationale - gateway/inbound_edge/store.py
- [[_h()]] - code - gateway/inbound_edge/store.py
- [[store()_2]] - code - gateway/tests/test_edge_jwt.py
- [[store.py_1]] - code - gateway/inbound_edge/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_96
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_Community 25]]
- 2 edges to [[_COMMUNITY_Community 65]]
- 1 edge to [[_COMMUNITY_Community 30]]

## Top bridge nodes
- [[EdgeStore_4]] - degree 53, connects to 3 communities
- [[store()_2]] - degree 2, connects to 1 community