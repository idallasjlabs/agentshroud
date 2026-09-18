---
source_file: "gateway/tests/test_credential_injector.py"
type: "rationale"
community: "TestOAuthInjection"
location: "L216"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestOAuthInjection
---

# inject_headers sets anthropic-beta: oauth-2025-04-20 when Bearer is injected.

## Connections
- [[.test_adds_oauth_beta_header_when_injecting()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestOAuthInjection