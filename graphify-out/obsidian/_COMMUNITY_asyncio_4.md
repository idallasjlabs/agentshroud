---
type: community
members: 27
---

# asyncio

**Members:** 27 nodes

## Members
- [[dot-__init__()_160]] - code - gateway/tests/test_egress_filter.py
- [[dot-log_event()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allow_is_not_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_deny_is_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_emits_egress_event_to_event_bus()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unknown_domain_allowed_when_approved()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unknown_domain_denied_when_denied()]] - code - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[FakeAuditStore_1]] - code - gateway/tests/test_egress_filter.py
- [[Only DENY decisions are persisted to the tamper-evident audit store. ALLOW…]] - rationale - gateway/tests/test_egress_filter.py
- [[TestAuditStorePersistence]] - code - gateway/tests/test_egress_filter.py
- [[__init__()_15]] - code - gateway/tests/test_egress_filter.py
- [[__init__()_16]] - code - gateway/tests/test_egress_filter.py
- [[asyncio_63]] - code
- [[emit()_7]] - code - gateway/tests/test_egress_filter.py
- [[get_pending_requests()_2]] - code - gateway/tests/test_egress_filter.py
- [[get_pending_requests()_3]] - code - gateway/tests/test_egress_filter.py
- [[get_pending_requests()_4]] - code - gateway/tests/test_egress_filter.py
- [[notify_pending()]] - code - gateway/tests/test_egress_filter.py
- [[notify_pending()_1]] - code - gateway/tests/test_egress_filter.py
- [[request_approval()]] - code - gateway/tests/test_egress_filter.py
- [[request_approval()_1]] - code - gateway/tests/test_egress_filter.py
- [[request_approval()_2]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_no_notification_on_allow()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_notifies_on_deny()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asyncio
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_EgressFilter]]
- 3 edges to [[_COMMUNITY_make_proxy]]
- 3 edges to [[_COMMUNITY__make_filter]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]

## Top bridge nodes
- [[dot-test_unknown_domain_allowed_when_approved()]] - degree 6, connects to 3 communities
- [[dot-test_unknown_domain_denied_when_denied()]] - degree 6, connects to 3 communities
- [[test_egress_filter_no_notification_on_allow()]] - degree 7, connects to 2 communities
- [[test_egress_filter_notifies_on_deny()]] - degree 7, connects to 2 communities
- [[dot-test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - degree 7, connects to 2 communities
