---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.png"
type: "image"
community: "AgentShroud Gateway (Trust Zone 1): holds 1Passw"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/AgentShroud_Gateway_Trust_Zone_1_holds_1Passw
---

# Allowlisted domains (api.openai.com, api.anthropic.com, api.telegram.org, googleapis.com, *.github.com, *.githubusercontent.com, imap/smtp.mail.me.com)

## Connections
- [[HTTP CONNECT egress proxy (gateway8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)]] - `conceptually_related_to` [EXTRACTED]
- [[Trust Zone 3 — External Services (OpenAI, Anthropic, Telegram, GitHub, 1Password; allowlisted HTTPS only)]] - `semantically_similar_to` [INFERRED]

#graphify/image #graphify/EXTRACTED #community/AgentShroud_Gateway_Trust_Zone_1_holds_1Passw