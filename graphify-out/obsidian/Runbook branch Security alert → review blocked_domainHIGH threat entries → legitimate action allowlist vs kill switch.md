---
source_file: "docs/diagrams/images/diagram-18-runbook.png"
type: "image"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
---

# Runbook branch: Security alert → review blocked_domain/HIGH threat entries → legitimate action? allowlist vs kill switch

## Connections
- [[HTTP CONNECT egress proxy (gateway8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections)]] - `references` [EXTRACTED]
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - `references` [EXTRACTED]
- [[Troubleshooting Runbook Decision Tree]] - `conceptually_related_to` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
