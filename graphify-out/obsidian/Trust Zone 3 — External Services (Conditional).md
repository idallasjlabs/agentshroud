---
source_file: "docs/diagrams/images/diagram-11-trust-boundary.svg"
type: "image"
community: "Module Group 112"
tags:
  - graphify/image
  - graphify/EXPLICIT
  - community/Module_Group_112
---

# Trust Zone 3 — External Services (Conditional)

## Connections
- [[1Password — Trusted for secrets, Gateway-only access]] - `contains` [EXPLICIT]
- [[Allowlisted Domains (api.openai.com, api.anthropic.com, api.telegram.org, oauth2.googleapis.com, www.googleapis.com, github.com, githubusercontent.com, imap.mail.me.com, smtp.mail.me.com)]] - `conceptually_related_to` [INFERRED]
- [[Anthropic API — Trusted for inference, Allowlisted domain]] - `contains` [EXPLICIT]
- [[Diagram 11 Trust Boundary (PNG)]] - `contains` [EXPLICIT]
- [[GitHub — Trusted for code ops, Allowlisted domain]] - `contains` [EXPLICIT]
- [[OpenAI API — Trusted for inference, Allowlisted domain]] - `contains` [EXPLICIT]
- [[Telegram API — Trusted for messaging, Allowlisted domain]] - `contains` [EXPLICIT]
- [[Trust Zone 1 — Gateway (Trusted Enforcer)]] - `controls` [EXPLICIT]

#graphify/image #graphify/EXPLICIT #community/Module_Group_112
