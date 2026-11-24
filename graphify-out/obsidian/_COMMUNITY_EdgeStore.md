---
type: community
members: 49
---

# EdgeStore

**Members:** 49 nodes

## Members
- [[dot-__init__()_148]] - code - gateway/inbound_edge/approvals.py
- [[dot-__init__()_149]] - code - gateway/inbound_edge/edge_jwt.py
- [[dot-__init__()_150]] - code - gateway/inbound_edge/store.py
- [[dot-_one()]] - code - gateway/inbound_edge/store.py
- [[dot-add_client()]] - code - gateway/inbound_edge/store.py
- [[dot-add_ticket()]] - code - gateway/inbound_edge/store.py
- [[dot-approval_for_ticket()]] - code - gateway/inbound_edge/store.py
- [[dot-close()_11]] - code - gateway/inbound_edge/store.py
- [[dot-consume_approval()]] - code - gateway/inbound_edge/store.py
- [[dot-consume_enrollment()]] - code - gateway/inbound_edge/store.py
- [[dot-enrollment_window_vendor()]] - code - gateway/inbound_edge/store.py
- [[dot-get_client()_2]] - code - gateway/inbound_edge/store.py
- [[dot-has_jti()]] - code - gateway/inbound_edge/store.py
- [[dot-init()]] - code - gateway/inbound_edge/store.py
- [[dot-jti_issued()]] - code - gateway/inbound_edge/store.py
- [[dot-kill()_1]] - code - gateway/inbound_edge/store.py
- [[dot-killed_reason()]] - code - gateway/inbound_edge/store.py
- [[dot-list_clients()]] - code - gateway/inbound_edge/store.py
- [[dot-list_kills()]] - code - gateway/inbound_edge/store.py
- [[dot-open_approval_for()]] - code - gateway/inbound_edge/store.py
- [[dot-open_enrollment()]] - code - gateway/inbound_edge/store.py
- [[dot-peek_code()]] - code - gateway/inbound_edge/store.py
- [[dot-peek_pending()]] - code - gateway/inbound_edge/store.py
- [[dot-peek_refresh()]] - code - gateway/inbound_edge/store.py
- [[dot-put_approval()]] - code - gateway/inbound_edge/store.py
- [[dot-put_code()]] - code - gateway/inbound_edge/store.py
- [[dot-put_pending()]] - code - gateway/inbound_edge/store.py
- [[dot-put_refresh()]] - code - gateway/inbound_edge/store.py
- [[dot-record_jti()]] - code - gateway/inbound_edge/store.py
- [[dot-revoke_refresh_family()]] - code - gateway/inbound_edge/store.py
- [[dot-rotate_refresh()]] - code - gateway/inbound_edge/store.py
- [[dot-take_code()]] - code - gateway/inbound_edge/store.py
- [[dot-take_pending()]] - code - gateway/inbound_edge/store.py
- [[dot-unkill()]] - code - gateway/inbound_edge/store.py
- [[Any_59]] - code
- [[Async SQLite store. One instance per gateway process.]] - rationale - gateway/inbound_edge/store.py
- [[Atomically mark an approval used. True for exactly one caller.]] - rationale - gateway/inbound_edge/store.py
- [[Consume a refresh token. Reuse of a consumed token revokes its family.]] - rationale - gateway/inbound_edge/store.py
- [[EdgeStore]] - code - gateway/inbound_edge/store.py
- [[Mint a one-time code the owner types on the consent page. Returned once.]] - rationale - gateway/inbound_edge/store.py
- [[Notifier]] - code
- [[Path_54]] - code
- [[RFC 7009 revocation of a refresh token kills its whole family.]] - rationale - gateway/inbound_edge/store.py
- [[Return and delete an unexpired code. A second call returns None.]] - rationale - gateway/inbound_edge/store.py
- [[The newest unconsumed, unexpired request_id for this idempotency key.]] - rationale - gateway/inbound_edge/store.py
- [[The vendor with an open (unused, unexpired) enrollment, if exactly one.]] - rationale - gateway/inbound_edge/store.py
- [[True exactly once for an unexpired code bound to ``vendor``; else None.]] - rationale - gateway/inbound_edge/store.py
- [[Whether ``jti`` was ever issued (and not yet purged) — guards a typo'd kill.]] - rationale - gateway/inbound_edge/store.py
- [[_h()]] - code - gateway/inbound_edge/store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EdgeStore
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 4 edges to [[_COMMUNITY_test_edge_approvals.py]]
- 2 edges to [[_COMMUNITY_test_mfa_guard.py]]
- 2 edges to [[_COMMUNITY_EdgeOAuthService]]
- 2 edges to [[_COMMUNITY_test_edge_service_routes.py]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_make_event]]
- 1 edge to [[_COMMUNITY_archive_old_events]]

## Top bridge nodes
- [[EdgeStore]] - degree 62, connects to 8 communities
- [[dot-__init__()_148]] - degree 4, connects to 2 communities
- [[_h()]] - degree 15, connects to 1 community
- [[dot-__init__()_149]] - degree 2, connects to 1 community
