---
source_file: "docs/SECURITY_PLAN.md"
type: "concept"
community: "Gateway Test Suite"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# Security Hardening Phases P0–FINAL

## Connections
- [[Credential Isolation (gateway as sole credential holder via op-proxy)]] - `implements` [EXTRACTED]
- [[Docker Network Isolation (agentshroud-internal 172.20.016, agentshroud-isolated 172.21.016)]] - `culminates_in` [EXTRACTED]
- [[MCP Proxy (tool call inspection layer)]] - `implements` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Gateway_Test_Suite