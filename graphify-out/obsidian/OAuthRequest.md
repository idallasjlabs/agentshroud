---
source_file: "gateway/security/oauth_security.py"
type: "code"
community: "Community 175"
location: "L44"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_175
---

# OAuthRequest

## Connections
- [[.test_empty_client_id_rejected()]] - `calls` [EXTRACTED]
- [[.test_empty_state_rejected()]] - `calls` [EXTRACTED]
- [[.test_pkce_plain_rejected_when_s256_required()]] - `calls` [EXTRACTED]
- [[.test_pkce_required_missing_challenge()]] - `calls` [EXTRACTED]
- [[.test_pkce_s256_accepted()]] - `calls` [EXTRACTED]
- [[.test_short_state_rejected()]] - `calls` [EXTRACTED]
- [[.test_state_replay_detected()]] - `calls` [EXTRACTED]
- [[.test_static_shared_client_id_rejected()]] - `calls` [EXTRACTED]
- [[.test_unique_client_id_accepted()]] - `calls` [EXTRACTED]
- [[.test_valid_state_accepted()]] - `calls` [EXTRACTED]
- [[.validate_request()]] - `references` [EXTRACTED]
- [[TestClientValidation]] - `uses` [INFERRED]
- [[TestConsentCookieBinding]] - `uses` [INFERRED]
- [[TestPKCE]] - `uses` [INFERRED]
- [[TestRedirectURI]] - `uses` [INFERRED]
- [[TestStateValidation]] - `uses` [INFERRED]
- [[oauth_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_175