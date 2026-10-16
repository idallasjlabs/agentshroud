---
source_file: "gateway/tests/test_oauth_security.py"
type: "code"
community: "OAuthSecurityValidator"
location: "L163"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/OAuthSecurityValidator
---

# TestRedirectURI

## Connections
- [[dot-test_different_uri_rejected()]] - `method` [EXTRACTED]
- [[dot-test_exact_match_accepted()]] - `method` [EXTRACTED]
- [[dot-test_http_rejected()]] - `method` [EXTRACTED]
- [[dot-test_path_traversal_rejected()_1]] - `method` [EXTRACTED]
- [[ConfusedDeputyError]] - `uses` [INFERRED]
- [[OAuthError]] - `uses` [INFERRED]
- [[OAuthRequest]] - `uses` [INFERRED]
- [[OAuthSecurityValidator]] - `uses` [INFERRED]
- [[PKCEViolation]] - `uses` [INFERRED]
- [[RedirectMismatch]] - `uses` [INFERRED]
- [[test_oauth_security.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/OAuthSecurityValidator
