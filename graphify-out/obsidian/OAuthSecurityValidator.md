---
source_file: "gateway/security/oauth_security.py"
type: "code"
community: "test_security_audit.py"
location: "L52"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_security_auditpy
---

# OAuthSecurityValidator

## Connections
- [[.__init__()_12]] - `calls` [EXTRACTED]
- [[.__init__()_154]] - `calls` [EXTRACTED]
- [[.__init__()_87]] - `method` [EXTRACTED]
- [[.check_state_reuse()]] - `method` [EXTRACTED]
- [[.create_consent_cookie()]] - `method` [EXTRACTED]
- [[.record_state_used()]] - `method` [EXTRACTED]
- [[.register_known_shared_ids()]] - `method` [EXTRACTED]
- [[.test_cookie_custom_max_age_expires_sooner()]] - `calls` [EXTRACTED]
- [[.test_http_rejected()]] - `calls` [EXTRACTED]
- [[.validate_consent_cookie()]] - `method` [EXTRACTED]
- [[.validate_redirect_uri()]] - `method` [EXTRACTED]
- [[.validate_request()]] - `method` [EXTRACTED]
- [[.verify_pkce()]] - `method` [EXTRACTED]
- [[Action_1]] - `uses` [INFERRED]
- [[Any_2]] - `uses` [INFERRED]
- [[Exception_1]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
- [[MFAGuard_2]] - `semantically_similar_to` [INFERRED]
- [[MiddlewareManager]] - `uses` [INFERRED]
- [[MiddlewareResult]] - `uses` [INFERRED]
- [[RBACManager_1]] - `uses` [INFERRED]
- [[Resource_1]] - `uses` [INFERRED]
- [[TestClientValidation]] - `uses` [INFERRED]
- [[TestConsentCookieBinding]] - `uses` [INFERRED]
- [[TestPKCE]] - `uses` [INFERRED]
- [[TestRedirectURI]] - `uses` [INFERRED]
- [[TestStateValidation]] - `uses` [INFERRED]
- [[ToolTier_2]] - `uses` [INFERRED]
- [[middleware.py]] - `imports` [EXTRACTED]
- [[oauth_security.py]] - `contains` [EXTRACTED]
- [[validator()_1]] - `calls` [EXTRACTED]
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_security_auditpy