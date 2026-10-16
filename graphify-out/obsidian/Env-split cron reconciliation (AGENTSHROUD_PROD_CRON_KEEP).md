---
source_file: "docker/bots/hermes/init-config.sh"
type: "rationale"
community: "test_hermes_cron_seed.py"
location: "L689-L764"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/test_hermes_cron_seedpy
---

# Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)

## Connections
- [[Missing-secret visibility banner (expected secrets loop)]] - `shares_data_with` [EXTRACTED]
- [[_hermes_cron_ids_names]] - `calls` [EXTRACTED]
- [[cmd_up]] - `shares_data_with` [EXTRACTED]
- [[init-config.sh (Hermes first-boot config materialisation)]] - `implements` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/test_hermes_cron_seedpy
