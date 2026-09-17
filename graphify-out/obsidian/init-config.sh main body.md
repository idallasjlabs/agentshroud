---
source_file: "docker/bots/hermes/init-config.sh"
type: "code"
community: "_seed_cron"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/_seed_cron
---

# init-config.sh main body

## Connections
- [[_seed_cron]] - `calls` [EXTRACTED]
- [[_write_soul]] - `calls` [EXTRACTED]
- [[gateway LLM proxy local-model routing (llm_proxy.py)]] - `references` [INFERRED]
- [[inject (Docker secret - s6 env)]] - `references` [EXTRACTED]
- [[start.sh (Hermes s6 main program)]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/_seed_cron