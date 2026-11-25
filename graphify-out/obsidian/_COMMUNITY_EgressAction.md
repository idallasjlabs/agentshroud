---
type: community
members: 56
---

# EgressAction

**Members:** 56 nodes

## Members
- [[dot-__init__()_165]] - code - gateway/tests/test_egress_filter.py
- [[dot-log_event()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allow_is_not_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_allowlisted_domain_still_prompts_when_approval_all_enabled()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_deny_is_persisted_to_audit_store()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_in_default_allowlist()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_domains_not_denylisted()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_egress_filter_allows_in_enforce_mode()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_emits_egress_event_to_event_bus()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unknown_domain_allowed_when_approved()]] - code - gateway/tests/test_egress_filter.py
- [[dot-test_unknown_domain_denied_when_denied()]] - code - gateway/tests/test_egress_filter.py
- [[A domain with an active timed approval should be allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[All four domains must be in EgressFilterConfig's default allowlist.]] - rationale - gateway/tests/test_egress_filter.py
- [[An expired timed approval should be evicted and the domain denied.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressAction]] - code - gateway/security/egress_filter.py
- [[EgressFilter in enforce mode allows all four domains for openclaw.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must NOT notify when domain is allowed.]] - rationale - gateway/tests/test_egress_filter.py
- [[EgressFilter must call notifier when blocking an unknown domain.]] - rationale - gateway/tests/test_egress_filter.py
- [[Enum_37]] - code
- [[FakeAuditStore_1]] - code - gateway/tests/test_egress_filter.py
- [[Interactive egress approval flow (allow once  deny).]] - rationale - gateway/tests/test_egress_filter.py
- [[None of the four domains should match the default denylist.]] - rationale - gateway/tests/test_egress_filter.py
- [[Only DENY decisions are persisted to the tamper-evident audit store. ALLOW…]] - rationale - gateway/tests/test_egress_filter.py
- [[Ports 465 (SMTPS), 587 (SMTP submission), 993 (IMAPS) must be allowed by the…]] - rationale - gateway/tests/test_egress_filter.py
- [[TestAuditStorePersistence]] - code - gateway/tests/test_egress_filter.py
- [[TestInteractiveApproval]] - code - gateway/tests/test_egress_filter.py
- [[TestOpenClawResearchDomainsAllowlisted]] - code - gateway/tests/test_egress_filter.py
- [[TestSMTPIMAPPorts]] - code - gateway/tests/test_egress_filter.py
- [[Timed approval for one domain must not allow other domains.]] - rationale - gateway/tests/test_egress_filter.py
- [[Verify that OpenClaw's web_searchresearch destinations are pre-approved. These…]] - rationale - gateway/tests/test_egress_filter.py
- [[__init__()_16]] - code - gateway/tests/test_egress_filter.py
- [[__init__()_17]] - code - gateway/tests/test_egress_filter.py
- [[_make_deny_all_filter()]] - code - gateway/tests/test_egress_filter.py
- [[asyncio_63]] - code
- [[emit()_8]] - code - gateway/tests/test_egress_filter.py
- [[flush_notifications with no notifier set should not crash.]] - rationale - gateway/tests/test_egress_filter.py
- [[get_pending_requests()_1]] - code - gateway/tests/test_egress_filter.py
- [[get_pending_requests()_2]] - code - gateway/tests/test_egress_filter.py
- [[get_pending_requests()_3]] - code - gateway/tests/test_egress_filter.py
- [[grant_timed_approval should purge expired entries on each call.]] - rationale - gateway/tests/test_egress_filter.py
- [[grant_timed_approval with a malformed date should not raise or store anything.]] - rationale - gateway/tests/test_egress_filter.py
- [[notify_pending()]] - code - gateway/tests/test_egress_filter.py
- [[notify_pending()_1]] - code - gateway/tests/test_egress_filter.py
- [[request_approval()]] - code - gateway/tests/test_egress_filter.py
- [[request_approval()_1]] - code - gateway/tests/test_egress_filter.py
- [[request_approval()_2]] - code - gateway/tests/test_egress_filter.py
- [[str_19]] - code
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
TABLE source_file, type FROM #community/EgressAction
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_EgressFilterConfig]]
- 16 edges to [[_COMMUNITY_EgressPolicy]]
- 16 edges to [[_COMMUNITY__make_filter]]
- 12 edges to [[_COMMUNITY_EgressFilter]]
- 5 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 3 edges to [[_COMMUNITY_make_proxy]]
- 3 edges to [[_COMMUNITY_ingest_apiconfig.py]]
- 2 edges to [[_COMMUNITY_ApprovalMode]]
- 2 edges to [[_COMMUNITY_test_module_stats.py]]
- 2 edges to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]

## Top bridge nodes
- [[EgressAction]] - degree 36, connects to 10 communities
- [[test_egress_filter.py]] - degree 30, connects to 5 communities
- [[TestSMTPIMAPPorts]] - degree 12, connects to 3 communities
- [[TestInteractiveApproval]] - degree 10, connects to 3 communities
- [[_make_deny_all_filter()]] - degree 9, connects to 3 communities
