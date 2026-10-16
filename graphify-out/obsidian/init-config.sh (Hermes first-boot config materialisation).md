---
source_file: "docker/bots/hermes/init-config.sh"
type: "code"
community: "test_hermes_cron_seed.py"
location: "L1-L767"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_hermes_cron_seedpy
---

# init-config.sh (Hermes first-boot config materialisation)

## Connections
- [[Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP)]] - `implements` [EXTRACTED]
- [[First-boot gateway-default s6 service auto-start]] - `implements` [EXTRACTED]
- [[MCP servers reconciliation from mcpservers.json into config.yaml]] - `implements` [EXTRACTED]
- [[S12 Hermes init-config.sh seeds jira_dev_ticket.py into live Hermes workspace]] - `references` [EXTRACTED]
- [[Tirith trust seeding (lookalike_tld + internal gateway HTTP rule)]] - `implements` [EXTRACTED]
- [[_hermes_cron_ids_names]] - `defines` [EXTRACTED]
- [[_seed_cron]] - `defines` [EXTRACTED]
- [[_write_soul]] - `defines` [EXTRACTED]
- [[init-config.sh script]] - `contains` [EXTRACTED]
- [[start.sh (Hermes s6 main program  startup wrapper)]] - `calls` [EXTRACTED]
- [[test_hermes_cron_seed.py]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_hermes_cron_seedpy
