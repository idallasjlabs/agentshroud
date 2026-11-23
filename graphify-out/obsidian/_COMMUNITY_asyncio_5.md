---
type: community
members: 29
---

# asyncio

**Members:** 29 nodes

## Members
- [[dot-__init__()_169]] - code - gateway/tests/test_egress_filter.py
- [[dot-log_event()_1]] - code - gateway/tests/test_egress_filter.py
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
- [[__init__()_19]] - code - gateway/tests/test_egress_filter.py
- [[__init__()_20]] - code - gateway/tests/test_egress_filter.py
- [[asyncio_66]] - code
- [[emit()_9]] - code - gateway/tests/test_egress_filter.py
- [[flush_notifications with no notifier set should not crash.]] - rationale - gateway/tests/test_egress_filter.py
- [[get_pending_requests()_1]] - code - gateway/tests/test_egress_filter.py
- [[get_pending_requests()_2]] - code - gateway/tests/test_egress_filter.py
- [[get_pending_requests()_3]] - code - gateway/tests/test_egress_filter.py
- [[notify_pending()]] - code - gateway/tests/test_egress_filter.py
- [[notify_pending()_1]] - code - gateway/tests/test_egress_filter.py
- [[request_approval()]] - code - gateway/tests/test_egress_filter.py
- [[request_approval()_1]] - code - gateway/tests/test_egress_filter.py
- [[request_approval()_2]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_flush_without_notifier()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_no_notification_on_allow()]] - code - gateway/tests/test_egress_filter.py
- [[test_egress_filter_notifies_on_deny()]] - code - gateway/tests/test_egress_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/asyncio
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_EgressPolicy]]
- 11 edges to [[_COMMUNITY_EgressFilter]]
- 3 edges to [[_COMMUNITY_test_mcp_proxy_coverage.py]]
- 3 edges to [[_COMMUNITY__make_filter]]

## Top bridge nodes
- [[dot-test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - degree 7, connects to 3 communities
- [[dot-test_unknown_domain_allowed_when_approved()]] - degree 6, connects to 3 communities
- [[dot-test_unknown_domain_denied_when_denied()]] - degree 6, connects to 3 communities
- [[TestAuditStorePersistence]] - degree 7, connects to 2 communities
- [[test_egress_filter_no_notification_on_allow()]] - degree 7, connects to 2 communities
