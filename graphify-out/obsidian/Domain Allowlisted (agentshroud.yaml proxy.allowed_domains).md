---
source_file: "docs/diagrams/images/diagram-13-network-security-egress.svg"
type: "image"
community: "Module Group 112"
tags:
  - graphify/image
  - graphify/EXPLICIT
  - community/Module_Group_112
---

# Domain Allowlisted? (agentshroud.yaml proxy.allowed_domains)

## Connections
- [[Allowlisted Domains (api.openai.com, api.anthropic.com, api.telegram.org, oauth2.googleapis.com, www.googleapis.com, github.com, githubusercontent.com, imap.mail.me.com, smtp.mail.me.com)]] - `flows_to` [EXPLICIT]
- [[Blocked (403 Forbidden) — All other domains, All RFC1918 addresses (10.x, 172.16.x, 192.168.x)]] - `flows_to` [EXPLICIT]
- [[HTTP CONNECT Tunnel — request to gateway8181]] - `flows_to` [EXPLICIT]

#graphify/image #graphify/EXPLICIT #community/Module_Group_112
