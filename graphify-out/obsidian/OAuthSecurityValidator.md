---
source_file: "gateway/security/oauth_security.py"
type: "code"
community: "OAuth & Metadata Guard"
location: "L52"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/OAuth__Metadata_Guard
---

# OAuthSecurityValidator

## Connections
- [[.__init__()_14]] - `calls` [EXTRACTED]
- [[.__init__()_44]] - `calls` [EXTRACTED]
- [[.__init__()_102]] - `method` [EXTRACTED]
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
- [[Action]] - `uses` [INFERRED]
- [[Any_8]] - `uses` [INFERRED]
- [[Exception_2]] - `uses` [INFERRED]
- [[LogSanitizer]] - `uses` [INFERRED]
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
- [[web_proxy.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/OAuth__Metadata_Guard