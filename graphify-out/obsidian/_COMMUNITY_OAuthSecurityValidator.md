---
type: community
cohesion: 0.09
members: 46
---

# OAuthSecurityValidator

**Cohesion:** 0.09 - loosely connected
**Members:** 46 nodes

## Members
- [[dot-__init__()_176]] - code - gateway/security/oauth_security.py
- [[dot-check_state_reuse()]] - code - gateway/security/oauth_security.py
- [[dot-create_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[dot-record_state_used()]] - code - gateway/security/oauth_security.py
- [[dot-register_known_shared_ids()]] - code - gateway/security/oauth_security.py
- [[dot-test_cookie_custom_max_age_expires_sooner()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_expired_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_tamper_detected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_within_max_age_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_wrong_client_fails()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_cookie_wrong_scope_fails()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_create_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_different_uri_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_empty_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_empty_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_exact_match_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_http_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_path_traversal_rejected()_1]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_plain_rejected_when_s256_required()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_required_missing_challenge()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_s256_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_verifier_validation()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_short_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_state_replay_detected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_static_shared_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_unique_client_id_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_valid_state_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_validate_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[dot-validate_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[dot-validate_redirect_uri()]] - code - gateway/security/oauth_security.py
- [[dot-validate_request()]] - code - gateway/security/oauth_security.py
- [[dot-verify_pkce()]] - code - gateway/security/oauth_security.py
- [[ConfusedDeputyError]] - code - gateway/security/oauth_security.py
- [[OAuthError]] - code - gateway/security/oauth_security.py
- [[OAuthRequest]] - code - gateway/security/oauth_security.py
- [[OAuthSecurityValidator]] - code - gateway/security/oauth_security.py
- [[PKCEViolation]] - code - gateway/security/oauth_security.py
- [[RedirectMismatch]] - code - gateway/security/oauth_security.py
- [[TestClientValidation]] - code - gateway/tests/test_oauth_security.py
- [[TestConsentCookieBinding]] - code - gateway/tests/test_oauth_security.py
- [[TestPKCE]] - code - gateway/tests/test_oauth_security.py
- [[TestRedirectURI]] - code - gateway/tests/test_oauth_security.py
- [[TestStateValidation]] - code - gateway/tests/test_oauth_security.py
- [[oauth_security.py_2]] - code - gateway/security/oauth_security.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[validator()]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OAuthSecurityValidator
SORT file.name ASC
```

## Connections to other communities
- 37 edges to [[_COMMUNITY_AlertDispatcher]]
- 11 edges to [[_COMMUNITY_MiddlewareManager]]
- 3 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_SessionError]]
- 1 edge to [[_COMMUNITY_ConsentFramework]]
- 1 edge to [[_COMMUNITY_ThreatAssessment]]
- 1 edge to [[_COMMUNITY_test_mfa_guard.py]]

## Top bridge nodes
- [[oauth_security.py_2]] - degree 11, connects to 3 communities
- [[OAuthSecurityValidator]] - degree 30, connects to 2 communities
- [[ConfusedDeputyError]] - degree 21, connects to 2 communities
- [[PKCEViolation]] - degree 21, connects to 2 communities
- [[RedirectMismatch]] - degree 21, connects to 2 communities
