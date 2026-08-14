---
source_file: "docs/vault/01 - Architecture/Architecture Overview.md"
type: "concept"
community: "Security Docs"
tags:
  - graphify/concept
  - graphify/EXTRACTED
  - community/Security_Docs
---

# agentshroud-bot Container (Node.js 22 OpenClaw, port 18789, 4 GB, isolated network)

## Connections
- [[Architecture Overview — AgentShroud]] - `describes` [EXTRACTED]
- [[Gateway Container (Python 3.11FastAPI 8080)]] - `shares_data_with` [EXTRACTED]
- [[MCP Proxy Wrapper (mcp-proxy-wrapper.js — stdio to HTTP translation)]] - `contains` [EXTRACTED]
- [[Network Topology (agentshroud-internal 172.2016 + agentshroud-isolated 172.2116)]] - `participates_in` [EXTRACTED]
- [[Running Containers (gateway + bot, healthy)]] - `conceptually_related_to` [EXTRACTED]
- [[Startup Sequence — AgentShroud]] - `references` [EXTRACTED]
- [[Two-Stage Startup (gateway healthy before bot starts — depends_on service_healthy)]] - `sequences` [EXTRACTED]

#graphify/concept #graphify/EXTRACTED #community/Security_Docs