---
source_file: "docs/diagrams/images/diagram-15-sequence-telegram.png"
type: "image"
community: "Community 353"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/Community_353
---

# Telegram Message Sequence Diagram

## Connections
- [[1Password op-proxy (POST credentialsop-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)]] - `conceptually_related_to` [EXTRACTED]
- [[Agent Decision Logic Flowchart]] - `semantically_similar_to` [INFERRED]
- [[HTTP CONNECT egress proxy (gateway8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)]] - `conceptually_related_to` [EXTRACTED]
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - `conceptually_related_to` [EXTRACTED]
- [[Peer binding Telegram 8096968754 → agentmain]] - `conceptually_related_to` [EXTRACTED]
- [[README_121]] - `conceptually_related_to` [AMBIGUOUS]
- [[ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at)]] - `conceptually_related_to` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/Community_353