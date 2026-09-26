---
type: community
cohesion: 0.08
members: 38
---

# Local-Model Job Quality Matrix

**Cohesion:** 0.08 - loosely connected
**Members:** 38 nodes

## Members
- [[._get_role_value()]] - code - gateway/security/privacy_policy.py
- [[._user_in_allowed_groups()]] - code - gateway/security/privacy_policy.py
- [[.contains_private_data()]] - code - gateway/security/privacy_policy.py
- [[.filter_response()_1]] - code - gateway/security/privacy_policy.py
- [[.is_service_allowed()]] - code - gateway/security/privacy_policy.py
- [[.should_alert()]] - code - gateway/security/privacy_policy.py
- [[.should_audit()]] - code - gateway/security/privacy_policy.py
- [[.test_admin_blocked_from_private_service()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_clean_response_not_modified()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_collaborator_allowed_shared_service()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_collaborator_api_key_redacted()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_collaborator_blocked_from_private_service()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_collaborator_email_content_redacted()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_contains_private_data_clean_text()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_contains_private_data_detects_email()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_extra_pattern_redacted()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_group_member_allowed_group_only_service()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_invalid_extra_pattern_does_not_crash()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_non_group_member_blocked_from_group_only_service()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_owner_can_access_private_service()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_owner_response_not_filtered()]] - code - gateway/tests/test_privacy_policy.py
- [[.test_unknown_service_allowed_by_default()]] - code - gateway/tests/test_privacy_policy.py
- [[Evaluates access control and filters responses per privacy policy.]] - rationale - gateway/security/privacy_policy.py
- [[Privacy Policy Enforcement Tests]] - code - gateway/tests/test_privacy_policy.py
- [[PrivacyPolicyEnforcer]] - code - gateway/security/privacy_policy.py
- [[RBACConfig_2]] - code - gateway/tests/test_privacy_policy.py
- [[Return True if an access attempt to this service should be logged.]] - rationale - gateway/security/privacy_policy.py
- [[Return True if text appears to contain admin-private data.]] - rationale - gateway/security/privacy_policy.py
- [[Return True if the owner should be alerted about this access attempt.]] - rationale - gateway/security/privacy_policy.py
- [[Return True if user_id may access the named service.]] - rationale - gateway/security/privacy_policy.py
- [[Strip admin-private content from a response before delivering to user.]] - rationale - gateway/security/privacy_policy.py
- [[TestResponseFiltering]] - code - gateway/tests/test_privacy_policy.py
- [[TestServiceAccessControl]] - code - gateway/tests/test_privacy_policy.py
- [[_make_rbac()]] - code - gateway/tests/test_privacy_policy.py
- [[default_policy()]] - code - gateway/tests/test_privacy_policy.py
- [[enforcer()_2]] - code - gateway/tests/test_privacy_policy.py
- [[rbac()_3]] - code - gateway/tests/test_privacy_policy.py
- [[test_privacy_policy.py]] - code - gateway/tests/test_privacy_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Local-Model_Job_Quality_Matrix
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_What You Must Do When Invoked]]
- 11 edges to [[_COMMUNITY_MiddlewareManager]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY__wrap_response()]]

## Top bridge nodes
- [[PrivacyPolicyEnforcer]] - degree 27, connects to 3 communities
- [[TestResponseFiltering]] - degree 15, connects to 3 communities
- [[test_privacy_policy.py]] - degree 14, connects to 3 communities
- [[TestServiceAccessControl]] - degree 14, connects to 3 communities
- [[RBACConfig_2]] - degree 7, connects to 3 communities