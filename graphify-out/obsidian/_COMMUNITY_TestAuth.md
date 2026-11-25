---
type: community
members: 61
---

# TestAuth

**Members:** 61 nodes

## Members
- [[dot-__init__()_202]] - code - gateway/security/oauth_security.py
- [[dot-check_state_reuse()]] - code - gateway/security/oauth_security.py
- [[dot-create_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[dot-record_state_used()]] - code - gateway/security/oauth_security.py
- [[dot-register_known_shared_ids()]] - code - gateway/security/oauth_security.py
- [[dot-test_agent_registry_module()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_consent_framework_loads()]] - code - gateway/tests/test_security_audit.py
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
- [[dot-test_oauth_confused_deputy()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_oauth_pkce_violation()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_path_traversal_rejected()_1]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_plain_rejected_when_s256_required()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_required_missing_challenge()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_s256_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_pkce_verifier_validation()]] - code - gateway/tests/test_oauth_security.py
- [[dot-test_reject_empty_token()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_garbage_token()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_malformed_jwt()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_reject_none_algorithm()]] - code - gateway/tests/test_security_audit.py
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
- [[Agent registry should be importable.]] - rationale - gateway/tests/test_security_audit.py
- [[ConfusedDeputyError]] - code - gateway/security/oauth_security.py
- [[Exception_20]] - code
- [[OAuth Security Module - Prevents confused deputy attacks on MCP OAuth proxy…]] - rationale - gateway/security/oauth_security.py
- [[OAuthError]] - code - gateway/security/oauth_security.py
- [[OAuthRequest]] - code - gateway/security/oauth_security.py
- [[OAuthSecurityValidator]] - code - gateway/security/oauth_security.py
- [[PKCEViolation]] - code - gateway/security/oauth_security.py
- [[Reject JWTs with alg=none (classic attack).]] - rationale - gateway/tests/test_security_audit.py
- [[Test authentication and authorization enforcement.]] - rationale - gateway/tests/test_security_audit.py
- [[TestAuth]] - code - gateway/tests/test_security_audit.py
- [[TestClientValidation]] - code - gateway/tests/test_oauth_security.py
- [[TestConsentCookieBinding]] - code - gateway/tests/test_oauth_security.py
- [[TestPKCE]] - code - gateway/tests/test_oauth_security.py
- [[TestRedirectURI]] - code - gateway/tests/test_oauth_security.py
- [[TestStateValidation]] - code - gateway/tests/test_oauth_security.py
- [[Tests for oauth_security module - MCP OAuth proxy security. TDD Written before…]] - rationale - gateway/tests/test_oauth_security.py
- [[fixture_126]] - code
- [[oauth_security.py_2]] - code - gateway/security/oauth_security.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[validator()_1]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestAuth
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_middleware.py]]
- 4 edges to [[_COMMUNITY_lifespan.py]]
- 3 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_Session]]
- 1 edge to [[_COMMUNITY_TokenValidator]]
- 1 edge to [[_COMMUNITY_test_all_modules_enforce.py]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]
- 1 edge to [[_COMMUNITY_ServerConfig]]
- 1 edge to [[_COMMUNITY_ContextGuard]]
- 1 edge to [[_COMMUNITY_TestFileSandbox]]
- 1 edge to [[_COMMUNITY_secrets.py]]

## Top bridge nodes
- [[TestAuth]] - degree 22, connects to 7 communities
- [[OAuthSecurityValidator]] - degree 21, connects to 4 communities
- [[oauth_security.py_2]] - degree 11, connects to 3 communities
- [[OAuthError]] - degree 9, connects to 1 community
- [[TestRedirectURI]] - degree 7, connects to 1 community
