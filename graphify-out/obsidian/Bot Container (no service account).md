---
source_file: "docs/diagrams/images/diagram-12-credential-flow.svg"
type: "image"
community: "Module Group 112"
tags:
  - graphify/image
  - graphify/EXPLICIT
  - community/Module_Group_112
---

# Bot Container (no service account)

## Connections
- [[Diagram 12 Credential Flow (PNG)]] - `contains` [EXPLICIT]
- [[Exported Secrets (ANTHROPIC_OAUTH_TOKEN, BRAVE_API_KEY, ICLOUD_APP_PASSWORD, ICLOUD_USERNAME, ICLOUD_EMAIL)]] - `contains` [EXPLICIT]
- [[POST credentialsop-proxy (credential proxy endpoint)]] - `calls` [EXPLICIT]
- [[Trust Zone 2 — Bot (Supervised Agent)]] - `conceptually_related_to` [INFERRED]
- [[op_proxy_read_with_retry() — Cascading retries 5s,10s,15s,30s,60s]] - `uses` [EXPLICIT]

#graphify/image #graphify/EXPLICIT #community/Module_Group_112