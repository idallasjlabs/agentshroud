---
source_file: "docs/diagrams/04-security.md"
type: "concept"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
---

# Trust Boundary Diagram

## Connections
- [[04-security]] - `conceptually_related_to` [EXTRACTED]
- [[AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]] - `conceptually_related_to` [EXTRACTED]
- [[BlockedUntrusted (LAN RFC1918, unlisted domains)]] - `conceptually_related_to` [EXTRACTED]
- [[Shared-Nothing Isolation Design Principle]] - `semantically_similar_to` [INFERRED]
- [[Trust Zone 0 — Owner (Isaiah Jefferson approvereject, gateway admin, container restart, secret rotation)]] - `conceptually_related_to` [EXTRACTED]
- [[Trust Zone 2 — Bot (Supervised Agent no direct credentialinternet access)]] - `conceptually_related_to` [EXTRACTED]
- [[Trust Zone 3 — External Services (OpenAI, Anthropic, Telegram, GitHub, 1Password; allowlisted HTTPS only)]] - `conceptually_related_to` [EXTRACTED]
- [[Trust Zone 4 — Infrastructure Nodes (raspberrypi, marvin, trillian; SSH-gated)]] - `conceptually_related_to` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
