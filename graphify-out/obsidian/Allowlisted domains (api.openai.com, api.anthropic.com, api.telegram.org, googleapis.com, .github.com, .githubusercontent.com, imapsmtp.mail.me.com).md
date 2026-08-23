---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.png"
type: "image"
community: "Diagram 11 Trust Boundary (images)"
tags:
  - graphify/image
  - graphify/INFERRED
  - community/Diagram_11_Trust_Boundary_images
---

# Allowlisted domains (api.openai.com, api.anthropic.com, api.telegram.org, googleapis.com, *.github.com, *.githubusercontent.com, imap/smtp.mail.me.com)

## Connections
- [[HTTP CONNECT egress proxy (gateway8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)]] - `conceptually_related_to` [EXTRACTED]
- [[Trust Zone 3 — External Services (OpenAI, Anthropic, Telegram, GitHub, 1Password; allowlisted HTTPS only)]] - `semantically_similar_to` [INFERRED]

#graphify/image #graphify/INFERRED #community/Diagram_11_Trust_Boundary_images