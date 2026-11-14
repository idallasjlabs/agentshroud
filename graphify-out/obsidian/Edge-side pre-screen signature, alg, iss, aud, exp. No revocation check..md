---
source_file: "gateway/inbound_edge/edge_jwt.py"
type: "rationale"
community: "Community 25"
location: "L106"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/Community_25
---

# Edge-side pre-screen: signature, alg, iss, aud, exp. No revocation check.

## Connections
- [[verify_signature_only()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/Community_25