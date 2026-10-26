---
source_file: "docker/bots/hermes/start.sh"
type: "code"
community: "Community 290"
location: "L1-L463"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_290
---

# start.sh (Hermes s6 main program / startup wrapper)

## Connections
- [[Crash backoff escalation (rolling 10-minute start window)]] - `implements` [EXTRACTED]
- [[Missing-secret visibility banner (expected secrets loop)]] - `implements` [EXTRACTED]
- [[Post-migration model lock + sandboxed terminal + cron fleet default]] - `implements` [EXTRACTED]
- [[S13 Hermes start.sh expected-secrets banner accepts env vars in place of mounted files]] - `references` [EXTRACTED]
- [[_email_owner]] - `defines` [EXTRACTED]
- [[_release_telegram_lock]] - `defines` [EXTRACTED]
- [[_telegram_bot_token]] - `defines` [EXTRACTED]
- [[_telegram_get_me_ready]] - `defines` [EXTRACTED]
- [[_telegram_send]] - `defines` [EXTRACTED]
- [[_telegram_send_photo]] - `defines` [EXTRACTED]
- [[init-config.sh (Hermes first-boot config materialisation)]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_290