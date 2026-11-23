---
type: community
members: 7
---

# crashwatch.sh

**Members:** 7 nodes

## Members
- [[_count_recent_restarts()]] - code - docker/bots/hermes/crashwatch.sh
- [[_log()]] - code - docker/bots/hermes/crashwatch.sh
- [[_read_last_alert_epoch()]] - code - docker/bots/hermes/crashwatch.sh
- [[_telegram_alert()]] - code - docker/bots/hermes/crashwatch.sh
- [[_write_last_alert_epoch()]] - code - docker/bots/hermes/crashwatch.sh
- [[crashwatch.sh]] - code - docker/bots/hermes/crashwatch.sh
- [[crashwatch.sh script]] - code - docker/bots/hermes/crashwatch.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/crashwatchsh
SORT file.name ASC
```
