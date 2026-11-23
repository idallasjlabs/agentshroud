---
type: community
members: 66
---

# PrivacyPolicyEnforcer

**Members:** 66 nodes

## Members
- [[dot-__init__()_13]] - code - gateway/security/privacy_policy.py
- [[dot-_get_role_value()]] - code - gateway/security/privacy_policy.py
- [[dot-_user_in_allowed_groups()]] - code - gateway/security/privacy_policy.py
- [[dot-contains_private_data()]] - code - gateway/security/privacy_policy.py
- [[dot-default()]] - code - gateway/security/privacy_policy.py
- [[dot-filter_response()]] - code - gateway/security/privacy_policy.py
- [[dot-from_dict()]] - code - gateway/security/privacy_policy.py
- [[dot-from_dict()_1]] - code - gateway/security/privacy_policy.py
- [[dot-is_service_allowed()]] - code - gateway/security/privacy_policy.py
- [[dot-should_alert()]] - code - gateway/security/privacy_policy.py
- [[dot-should_audit()]] - code - gateway/security/privacy_policy.py
- [[dot-test_admin_blocked_from_private_service()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_audit_disabled_globally()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_clean_response_not_modified()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_collaborator_allowed_shared_service()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_collaborator_api_key_redacted()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_collaborator_blocked_from_private_service()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_collaborator_email_content_redacted()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_contains_private_data_clean_text()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_contains_private_data_detects_email()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_default_policy_marks_gmail_private()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_extra_pattern_redacted()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_extra_redact_patterns_loaded()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_from_dict_adds_new_service()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_from_dict_overrides_existing()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_from_dict_unknown_privacy_defaults_to_private()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_group_member_allowed_group_only_service()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_invalid_extra_pattern_does_not_crash()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_non_group_member_blocked_from_group_only_service()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_owner_can_access_private_service()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_owner_response_not_filtered()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_should_alert_non_owner()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_should_audit_private_service()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_should_not_alert_owner()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_should_not_audit_unknown_service()]] - code - gateway/tests/test_privacy_policy.py
- [[dot-test_unknown_service_allowed_by_default()]] - code - gateway/tests/test_privacy_policy.py
- [[Enum_8]] - code
- [[Evaluates access control and filters responses per privacy policy.]] - rationale - gateway/security/privacy_policy.py
- [[Parse from a YAMLdict representation. Example YAML privacy services gmail…]] - rationale - gateway/security/privacy_policy.py
- [[Privacy Policy Enforcer (v0.9.0 Tranche 2) Admin-defined configuration…]] - rationale - gateway/security/privacy_policy.py
- [[Privacy classification for a service.]] - rationale - gateway/security/privacy_policy.py
- [[Privacy policy configuration. Loaded from agentshroud.yaml `privacy` section.]] - rationale - gateway/security/privacy_policy.py
- [[Privacy policy for a single service.]] - rationale - gateway/security/privacy_policy.py
- [[PrivacyPolicy]] - code - gateway/security/privacy_policy.py
- [[PrivacyPolicyEnforcer]] - code - gateway/security/privacy_policy.py
- [[Return True if an access attempt to this service should be logged.]] - rationale - gateway/security/privacy_policy.py
- [[Return True if text appears to contain admin-private data.]] - rationale - gateway/security/privacy_policy.py
- [[Return True if the owner should be alerted about this access attempt.]] - rationale - gateway/security/privacy_policy.py
- [[Return True if user_id may access the named service.]] - rationale - gateway/security/privacy_policy.py
- [[Return a default policy with all known private services locked down.]] - rationale - gateway/security/privacy_policy.py
- [[ServicePolicy]] - code - gateway/security/privacy_policy.py
- [[ServicePrivacy]] - code - gateway/security/privacy_policy.py
- [[Strip admin-private content from a response before delivering to user. Args…]] - rationale - gateway/security/privacy_policy.py
- [[TestAuditAndAlert]] - code - gateway/tests/test_privacy_policy.py
- [[TestPrivacyPolicyParsing]] - code - gateway/tests/test_privacy_policy.py
- [[TestResponseFiltering]] - code - gateway/tests/test_privacy_policy.py
- [[TestServiceAccessControl]] - code - gateway/tests/test_privacy_policy.py
- [[Tests for gatewaysecurityprivacy_policy.py — V9-T2 Privacy policy…]] - rationale - gateway/tests/test_privacy_policy.py
- [[_make_rbac()]] - code - gateway/tests/test_privacy_policy.py
- [[default_policy()]] - code - gateway/tests/test_privacy_policy.py
- [[enforcer()]] - code - gateway/tests/test_privacy_policy.py
- [[fixture_10]] - code
- [[privacy_policy.py]] - code - gateway/security/privacy_policy.py
- [[rbac()]] - code - gateway/tests/test_privacy_policy.py
- [[str_4]] - code
- [[test_privacy_policy.py]] - code - gateway/tests/test_privacy_policy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PrivacyPolicyEnforcer
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_socrouter.py]]
- 3 edges to [[_COMMUNITY_lifespan]]
- 3 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_test_soc_bots.py]]
- 1 edge to [[_COMMUNITY_telegram_proxy.py]]

## Top bridge nodes
- [[test_privacy_policy.py]] - degree 18, connects to 4 communities
- [[_make_rbac()]] - degree 8, connects to 3 communities
- [[PrivacyPolicyEnforcer]] - degree 23, connects to 2 communities
- [[PrivacyPolicy]] - degree 13, connects to 2 communities
- [[privacy_policy.py]] - degree 9, connects to 2 communities
