---
source_file: "docs/diagrams/images/diagram-17-state-bot-session.png"
type: "image"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
tags:
  - graphify/image
  - graphify/AMBIGUOUS
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
---

# Bot Session State Diagram (fresh → active → idle/compacting → reset)

## Connections
- [[OpenClaw auto-compaction (reserveTokensFloor=4000; triggers at ~196K of 200K tokens; hard overflow 200K after 3 failed retries → session reset)]] - `conceptually_related_to` [EXTRACTED]
- [[flowsREADME]] - `conceptually_related_to` [AMBIGUOUS]

#graphify/image #graphify/AMBIGUOUS #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
