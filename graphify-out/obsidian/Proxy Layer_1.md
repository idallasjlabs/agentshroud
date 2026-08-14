---
source_file: "docs/diagrams/images/diagram-03-gateway-components.svg"
type: "image"
community: "Bot Skill Config"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/Bot_Skill_Config
---

# Proxy Layer

## Connections
- [[Op-Proxy (Credential Gateway)]] - `shares_data_with` [EXTRACTED]
- [[http_proxy.py (HTTP CONNECT 8181, domain allowlist)]] - `shares_data_with` [EXTRACTED]
- [[mcp_proxy.py (MCP tool call gate)]] - `shares_data_with` [EXTRACTED]
- [[ssh_proxy (approved hosts only)]] - `shares_data_with` [EXTRACTED]
- [[web_proxy.py (domain allowlist engine)]] - `shares_data_with` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/Bot_Skill_Config