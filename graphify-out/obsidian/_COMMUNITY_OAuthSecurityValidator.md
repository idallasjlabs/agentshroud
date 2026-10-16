---
type: community
cohesion: 0.09
members: 31
---

# OAuthSecurityValidator

**Cohesion:** 0.09 - loosely connected
**Members:** 31 nodes

## Members
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
- [[OAuthRequest]] - code - gateway/security/oauth_security.py
- [[TestClientValidation]] - code - gateway/tests/test_oauth_security.py
- [[TestConsentCookieBinding]] - code - gateway/tests/test_oauth_security.py
- [[TestPKCE]] - code - gateway/tests/test_oauth_security.py
- [[TestRedirectURI]] - code - gateway/tests/test_oauth_security.py
- [[TestStateValidation]] - code - gateway/tests/test_oauth_security.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[validator()]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OAuthSecurityValidator
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_AlertDispatcher]]
- 8 edges to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[TestConsentCookieBinding]] - degree 15, connects to 2 communities
- [[TestPKCE]] - degree 11, connects to 2 communities
- [[TestRedirectURI]] - degree 11, connects to 2 communities
- [[TestStateValidation]] - degree 11, connects to 2 communities
- [[TestClientValidation]] - degree 10, connects to 2 communities
