---
type: community
cohesion: 0.10
members: 42
---

# Module Group 103

**Cohesion:** 0.10 - loosely connected
**Members:** 42 nodes

## Members
- [[.__init__()_80]] - code - gateway/security/oauth_security.py
- [[.check_state_reuse()]] - code - gateway/security/oauth_security.py
- [[.create_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.record_state_used()]] - code - gateway/security/oauth_security.py
- [[.register_known_shared_ids()]] - code - gateway/security/oauth_security.py
- [[.test_cookie_tamper_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_client_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_scope_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_create_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.test_different_uri_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_empty_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_empty_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_exact_match_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_http_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_path_traversal_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_plain_rejected_when_s256_required()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_required_missing_challenge()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_s256_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_verifier_validation()]] - code - gateway/tests/test_oauth_security.py
- [[.test_short_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_state_replay_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_static_shared_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_unique_client_id_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_valid_state_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_validate_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.validate_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.validate_redirect_uri()]] - code - gateway/security/oauth_security.py
- [[.validate_request()]] - code - gateway/security/oauth_security.py
- [[.verify_pkce()]] - code - gateway/security/oauth_security.py
- [[ConfusedDeputyError]] - code - gateway/security/oauth_security.py
- [[OAuthError]] - code - gateway/security/oauth_security.py
- [[OAuthRequest]] - code - gateway/security/oauth_security.py
- [[OAuthSecurityValidator]] - code - gateway/security/oauth_security.py
- [[PKCEViolation]] - code - gateway/security/oauth_security.py
- [[TestClientValidation]] - code - gateway/tests/test_oauth_security.py
- [[TestConsentCookieBinding]] - code - gateway/tests/test_oauth_security.py
- [[TestPKCE]] - code - gateway/tests/test_oauth_security.py
- [[TestRedirectURI]] - code - gateway/tests/test_oauth_security.py
- [[TestStateValidation]] - code - gateway/tests/test_oauth_security.py
- [[oauth_security.py]] - code - gateway/security/oauth_security.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[validator()]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_103
SORT file.name ASC
```

## Connections to other communities
- 26 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 13 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 2 edges to [[_COMMUNITY_Alert Dispatcher]]
- 2 edges to [[_COMMUNITY_Module Group 137]]
- 2 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 2 edges to [[_COMMUNITY_Module Group 110]]
- 1 edge to [[_COMMUNITY_Module Group 113]]

## Top bridge nodes
- [[ConfusedDeputyError]] - degree 21, connects to 5 communities
- [[PKCEViolation]] - degree 21, connects to 5 communities
- [[OAuthError]] - degree 12, connects to 2 communities
- [[oauth_security.py]] - degree 8, connects to 2 communities
- [[OAuthSecurityValidator]] - degree 29, connects to 1 community