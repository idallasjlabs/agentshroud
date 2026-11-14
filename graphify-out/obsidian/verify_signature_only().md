---
source_file: "gateway/inbound_edge/edge_jwt.py"
type: "code"
community: "Community 25"
location: "L103"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_25
---

# verify_signature_only()

## Connections
- [[.load_access_token()]] - `calls` [EXTRACTED]
- [[.test_edge_can_check_signature_with_public_key_only()]] - `calls` [EXTRACTED]
- [[.test_hs256_signed_with_public_key()]] - `calls` [EXTRACTED]
- [[Any_9]] - `references` [EXTRACTED]
- [[Edge-side pre-screen signature, alg, iss, aud, exp. No revocation check.]] - `rationale_for` [EXTRACTED]
- [[_decode()]] - `calls` [EXTRACTED]
- [[edge_app.py]] - `imports` [EXTRACTED]
- [[edge_jwt.py]] - `contains` [EXTRACTED]
- [[test_edge_jwt.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_25