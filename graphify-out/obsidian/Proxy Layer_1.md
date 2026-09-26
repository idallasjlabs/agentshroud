---
source_file: "docs/diagrams/images/diagram-03-gateway-components.svg"
type: "image"
community: "ADR-007: Zero-Config Security (docker-compose up"
tags:
  - graphify/image
  - graphify/EXTRACTED
  - community/ADR-007_Zero-Config_Security_docker-compose_up
---

# Proxy Layer

## Connections
- [[Op-Proxy (Credential Gateway)]] - `shares_data_with` [EXTRACTED]
- [[http_proxy.py (HTTP CONNECT 8181, domain allowlist)]] - `shares_data_with` [EXTRACTED]
- [[mcp_proxy.py (MCP tool call gate)]] - `shares_data_with` [EXTRACTED]
- [[ssh_proxy (approved hosts only)]] - `shares_data_with` [EXTRACTED]
- [[web_proxy.py (domain allowlist engine)]] - `shares_data_with` [EXTRACTED]

#graphify/image #graphify/EXTRACTED #community/ADR-007_Zero-Config_Security_docker-compose_up