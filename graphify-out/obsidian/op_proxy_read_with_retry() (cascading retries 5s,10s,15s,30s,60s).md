---
source_file: "docs/diagrams/images/diagram-12-credential-flow.svg"
type: "concept"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s) (3)"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s_3
---

# op_proxy_read_with_retry() (cascading retries 5s,10s,15s,30s,60s)

## Connections
- [[1Password Cloud]] - `calls` [EXTRACTED]
- [[Gateway Container (has service account)]] - `calls` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s_3
