---
type: community
cohesion: 0.10
members: 25
---

# test_egress_filter.py

**Cohesion:** 0.10 - loosely connected
**Members:** 25 nodes

## Members
- [[dot-__init__()_123]] - code - gateway/tests/test_egress_filter.py
- [[dot-log_event()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allow_is_not_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_deny_is_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[A domain with an active timed approval should be allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[An expired timed approval should be evicted and the domain denied.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[FakeAuditStore_1]] - code - gateway/tests/test_egress_filter.py
- [[Only DENY decisions are persisted to the tamper-evident audit store.      ALLOW]] - rationale - gateway/tests/test_egress_filter.py
- [[TestAuditStorePersistence]] - code - gateway/tests/test_egress_filter.py
- [[Timed approval for one domain must not allow other domains.]] - rationale - gateway/tests/test_egress_filter.py
- [[_make_deny_all_filter()]] - code - gateway/tests/test_egress_filter.py
- [[flush_notifications with no notifier set should not crash.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval should purge expired entries on each call.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval with a malformed date should not raise or store anything.]] - rationale - gateway/tests/test_egress_filter.py
- [[test_egress_filter.py]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_flush_without_notifier()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_no_notification_on_allow()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_notifies_on_deny()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_allows_domain()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_cleans_stale_entries()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_does_not_affect_other_domains()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_expired_falls_back_to_deny()]] - code - gateway/tests/test_egress_filter.py
- [[test_grant_timed_approval_invalid_iso_is_ignored()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_egress_filterpy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY__make_filter]]
- 13 edges to [[_COMMUNITY_EgressFilterConfig]]
- 10 edges to [[_COMMUNITY_EgressPolicy]]
- 4 edges to [[_COMMUNITY_EgressFilter]]
- 3 edges to [[_COMMUNITY_EgressAttempt]]

## Top bridge nodes
- [[test_egress_filter.py]] - degree 29, connects to 5 communities
- [[FakeAuditStore_1]] - degree 11, connects to 5 communities
- [[TestAuditStorePersistence]] - degree 10, connects to 5 communities
- [[_make_deny_all_filter()]] - degree 10, connects to 4 communities
- [[test_egress_filter_flush_without_notifier()]] - degree 5, connects to 3 communities
