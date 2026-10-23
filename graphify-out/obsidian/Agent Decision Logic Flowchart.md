---
source_file: "docs/diagrams/images/diagram-14-logic-flow.png"
type: "image"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
---

# Agent Decision Logic Flowchart

## Connections
- [[Agent routing (bindings config; e.g. Telegram ID 8096968754 → main agent)]] - `conceptually_related_to` [EXTRACTED]
- [[Approval Queue (human-in-the-loop)_1]] - `conceptually_related_to` [EXTRACTED]
- [[MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONELOWMEDIUMHIGH)]] - `conceptually_related_to` [EXTRACTED]
- [[Telegram Message Sequence Diagram]] - `semantically_similar_to` [INFERRED]

#graphify/image #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
