---
source_file: "docs/diagrams/images/diagram-12-credential-flow.svg"
type: "image"
community: "Module Group 112"
tags:
  - graphify/image
  - graphify/EXPLICIT
  - community/Module_Group_112
---

# Gateway Container (has service account)

## Connections
- [[1Password Cloud]] - `calls` [EXPLICIT]
- [[Diagram 12 Credential Flow (PNG)]] - `contains` [EXPLICIT]
- [[OP_SERVICE_ACCOUNT_TOKEN (loaded from Docker secret runsecrets1password_service_account)]] - `contains` [EXPLICIT]
- [[Trust Zone 1 — Gateway (Trusted Enforcer)]] - `conceptually_related_to` [INFERRED]
- [[Validates GATEWAY_AUTH_TOKEN, checks allowed_op_paths pattern]] - `contains` [EXPLICIT]

#graphify/image #graphify/EXPLICIT #community/Module_Group_112