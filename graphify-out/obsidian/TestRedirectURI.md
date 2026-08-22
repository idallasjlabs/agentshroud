---
source_file: "gateway/tests/test_oauth_security.py"
type: "code"
community: "OAuth & Metadata Guard"
location: "L163"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/OAuth__Metadata_Guard
---

# TestRedirectURI

## Connections
- [[.test_different_uri_rejected()]] - `method` [EXTRACTED]
- [[.test_exact_match_accepted()]] - `method` [EXTRACTED]
- [[.test_http_rejected()]] - `method` [EXTRACTED]
- [[.test_path_traversal_rejected()]] - `method` [EXTRACTED]
- [[ConfusedDeputyError]] - `uses` [INFERRED]
- [[OAuthError]] - `uses` [INFERRED]
- [[OAuthRequest]] - `uses` [INFERRED]
- [[OAuthSecurityValidator]] - `uses` [INFERRED]
- [[PKCEViolation]] - `uses` [INFERRED]
- [[RedirectMismatch]] - `uses` [INFERRED]
- [[test_oauth_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/OAuth__Metadata_Guard