---
source_file: "docker/bots/hermes/start.sh"
type: "code"
community: "telegram_api_proxy (/telegram-api/{path})"
location: "L1-L463"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/telegram_api_proxy_/telegram-api/path
---

# start.sh (Hermes s6 main program / startup wrapper)

## Connections
- [[Crash backoff escalation (rolling 10-minute start window)]] - `implements` [EXTRACTED]
- [[HERMES_HOME]] - `defines` [EXTRACTED]
- [[HOME_1]] - `defines` [EXTRACTED]
- [[Missing-secret visibility banner (expected secrets loop)]] - `implements` [EXTRACTED]
- [[Post-migration model lock + sandboxed terminal + cron fleet default]] - `implements` [EXTRACTED]
- [[XDG_CACHE_HOME]] - `defines` [EXTRACTED]
- [[XDG_DATA_HOME]] - `defines` [EXTRACTED]
- [[XDG_STATE_HOME]] - `defines` [EXTRACTED]
- [[_email_owner]] - `defines` [EXTRACTED]
- [[_release_telegram_lock]] - `defines` [EXTRACTED]
- [[_telegram_bot_token]] - `defines` [EXTRACTED]
- [[_telegram_get_me_ready]] - `defines` [EXTRACTED]
- [[_telegram_send]] - `defines` [EXTRACTED]
- [[_telegram_send_photo]] - `defines` [EXTRACTED]
- [[cmd_up]] - `shares_data_with` [INFERRED]
- [[init-config.sh (Hermes first-boot config materialisation)]] - `calls` [EXTRACTED]
- [[start.sh script]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/telegram_api_proxy_/telegram-api/path
