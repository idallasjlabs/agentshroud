---
source_file: "gateway/security/oauth_security.py"
type: "code"
community: "AlertDispatcher"
location: "L52"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/AlertDispatcher
---

# OAuthSecurityValidator

## Connections
- [[dot-__init__()_10]] - `calls` [EXTRACTED]
- [[dot-__init__()_14]] - `method` [EXTRACTED]
- [[dot-check_state_reuse()]] - `method` [EXTRACTED]
- [[dot-create_consent_cookie()]] - `method` [EXTRACTED]
- [[dot-record_state_used()]] - `method` [EXTRACTED]
- [[dot-register_known_shared_ids()]] - `method` [EXTRACTED]
- [[dot-test_cookie_custom_max_age_expires_sooner()]] - `calls` [EXTRACTED]
- [[dot-test_http_rejected()]] - `calls` [EXTRACTED]
- [[dot-validate_consent_cookie()]] - `method` [EXTRACTED]
- [[dot-validate_redirect_uri()]] - `method` [EXTRACTED]
- [[dot-validate_request()]] - `method` [EXTRACTED]
- [[dot-verify_pkce()]] - `method` [EXTRACTED]
- [[Action]] - `uses` [INFERRED]
- [[Any]] - `uses` [INFERRED]
- [[Exception]] - `uses` [INFERRED]
- [[LogSanitizer_1]] - `uses` [INFERRED]
- [[MFAGuard_2]] - `semantically_similar_to` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager]] - `uses` [INFERRED]
- [[Resource]] - `uses` [INFERRED]
- [[TestClientValidation]] - `uses` [INFERRED]
- [[TestConsentCookieBinding]] - `uses` [INFERRED]
- [[TestPKCE]] - `uses` [INFERRED]
- [[TestRedirectURI]] - `uses` [INFERRED]
- [[TestStateValidation]] - `uses` [INFERRED]
- [[ToolTier]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[oauth_security.py]] - `contains` [EXTRACTED]
- [[validator()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/AlertDispatcher
