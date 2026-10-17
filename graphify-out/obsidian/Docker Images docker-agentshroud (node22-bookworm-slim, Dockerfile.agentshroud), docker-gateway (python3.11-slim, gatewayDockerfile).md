---
source_file: "docs/diagrams/images/diagram-22-dependency-graph.png"
type: "image"
community: "AgentShroud Gateway (Trust Zone 1): holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMAC/JWT validation (2)"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/AgentShroud_Gateway_Trust_Zone_1_holds_1Password_service_account_enforces_policy_signs_ledger_entries_controls_approval_queue_HMAC/JWT_validation_2
---

# Docker Images: docker-agentshroud (node:22-bookworm-slim, Dockerfile.agentshroud), docker-gateway (python:3.11-slim, gateway/Dockerfile)

## Connections
- [[Containers startup order agentshroud-gateway starts first, agentshroud-bot starts after gateway healthy]] - `shares_data_with` [EXTRACTED]
- [[Docker Deployment Dependency Graph]] - `conceptually_related_to` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/AgentShroud_Gateway_Trust_Zone_1_holds_1Password_service_account_enforces_policy_signs_ledger_entries_controls_approval_queue_HMAC/JWT_validation_2
