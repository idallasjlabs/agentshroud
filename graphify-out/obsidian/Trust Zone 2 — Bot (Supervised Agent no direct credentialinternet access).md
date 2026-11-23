---
source_file: "docs/diagrams/images/diagram-11-trust-boundary.png"
type: "image"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
---

# Trust Zone 2 — Bot (Supervised Agent: no direct credential/internet access)

## Connections
- [[1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]] - `semantically_similar_to` [INFERRED]
- [[AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]] - `conceptually_related_to` [EXTRACTED]
- [[BlockedUntrusted (LAN RFC1918, unlisted domains)]] - `conceptually_related_to` [EXTRACTED]
- [[HTTP CONNECT egress proxy (gateway8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)]] - `semantically_similar_to` [INFERRED]
- [[Trust Boundary Diagram]] - `conceptually_related_to` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
