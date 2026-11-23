---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.png"
type: "concept"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
---

# HTTP CONNECT egress proxy (gateway:8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)

## Connections
- [[AgentShroud Gateway (Trust Zone 1) holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMACJWT validation]] - `conceptually_related_to` [EXTRACTED]
- [[Allowlisted domains (api.openai.com, api.anthropic.com, api.telegram.org, googleapis.com, .github.com, .githubusercontent.com, imapsmtp.mail.me.com)]] - `conceptually_related_to` [EXTRACTED]
- [[Network Security  Egress Control Flowchart]] - `conceptually_related_to` [EXTRACTED]
- [[Phase 2 — Security Core HTTP CONNECT Proxy, MCP Proxy Inspector, Approval Queue, SSH Proxy]] - `references` [EXTRACTED]
- [[Runbook branch Security alert → review blocked_domainHIGH threat entries → legitimate action allowlist vs kill switch]] - `references` [EXTRACTED]
- [[Telegram Message Sequence Diagram]] - `conceptually_related_to` [EXTRACTED]
- [[Trust Zone 2 — Bot (Supervised Agent no direct credentialinternet access)]] - `semantically_similar_to` [INFERRED]

#graphify/concept #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
