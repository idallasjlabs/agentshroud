---
source_file: "docs/diagrams/images/diagram-22-dependency-graph.png"
type: "image"
community: "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
---

# Docker Images: docker-agentshroud (node:22-bookworm-slim, Dockerfile.agentshroud), docker-gateway (python:3.11-slim, gateway/Dockerfile)

## Connections
- [[Containers startup order agentshroud-gateway starts first, agentshroud-bot starts after gateway healthy]] - `shares_data_with` [EXTRACTED]
- [[Docker Deployment Dependency Graph]] - `conceptually_related_to` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/1Password_op-proxy_POST_/credentials/op-proxy_validates_GATEWAY_AUTH_TOKEN__allowed_op_paths_cascading_retry_5s10s15s30s60s
