---
source_file: "docs/vault/01 - Architecture/Architecture Overview.md"
type: "concept"
community: "docs/vault"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/docs/vault
---

# agentshroud-gateway Container (Python 3.13 / FastAPI, port 8080, 1280 MB, read-only rootfs)

## Connections
- [[Architecture Overview — AgentShroud]] - `describes` [EXTRACTED]
- [[MCP Proxy Wrapper (mcp-proxy-wrapper.js — stdio to HTTP translation)]] - `routes_to` [EXTRACTED]
- [[Network Topology (agentshroud-internal 172.2016 + agentshroud-isolated 172.2116)]] - `participates_in` [EXTRACTED]
- [[Quick Reference — AgentShroud]] - `references` [EXTRACTED]
- [[Startup Sequence — AgentShroud]] - `references` [EXTRACTED]
- [[Two-Stage Startup (gateway healthy before bot starts — depends_on service_healthy)]] - `depends_on` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/docs/vault