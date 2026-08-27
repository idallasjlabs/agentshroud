---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.png"
type: "concept"
community: "Community 280"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Community_280
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

#graphify/concept #graphify/EXTRACTED #community/Community_280