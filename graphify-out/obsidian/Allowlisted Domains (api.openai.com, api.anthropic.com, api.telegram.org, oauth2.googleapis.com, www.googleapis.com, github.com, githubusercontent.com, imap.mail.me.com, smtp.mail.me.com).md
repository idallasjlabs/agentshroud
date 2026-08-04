---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.svg"
type: "image"
community: "Module Group 112"
tags:
  - graphify/image
  - graphify/EXPLICIT
  - community/Module_Group_112
---

# Allowlisted Domains (api.openai.com, api.anthropic.com, api.telegram.org, oauth2.googleapis.com, www.googleapis.com, github.com, githubusercontent.com, imap.mail.me.com, smtp.mail.me.com)

## Connections
- [[Domain Allowlisted (agentshroud.yaml proxy.allowed_domains)]] - `flows_to` [EXPLICIT]
- [[TCP Tunnel Established — Gateway Relays Traffic]] - `flows_to` [EXPLICIT]
- [[Trust Zone 3 — External Services (Conditional)]] - `conceptually_related_to` [INFERRED]

#graphify/image #graphify/EXPLICIT #community/Module_Group_112
