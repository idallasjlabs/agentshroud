---
source_file: "docker/docker-compose.agentshroud-bot.marvin.yml"
type: "rationale"
community: "test_main_endpoints.py"
location: "docker/docker-compose.agentshroud-bot.marvin.yml:26"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_main_endpointspy
---

# HERMES_DASHBOARD_UPSTREAM / *_HOST_UPSTREAM dev hostnames

## Connections
- [[gateway service (dev override)]] - `shares_data_with` [EXTRACTED]
- [[hermes-dashboard-relay bypass of the gateway proxy]] - `references` [EXTRACTED]
- [[hermes_dashboard_proxy (hermes-dashboard{path} HTTP reverse proxy)]] - `references` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_main_endpointspy
