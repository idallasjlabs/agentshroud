---
source_file: "docker/bots/hermes/init-config.sh"
type: "rationale"
community: "TestFabricatedSecurityNotice (2)"
location: "L689-L764"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestFabricatedSecurityNotice_2
---

# Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)

## Connections
- [[Missing-secret visibility banner (expected secrets loop)]] - `shares_data_with` [EXTRACTED]
- [[_hermes_cron_ids_names]] - `calls` [EXTRACTED]
- [[init-config.sh (Hermes first-boot config materialisation)]] - `implements` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestFabricatedSecurityNotice_2
