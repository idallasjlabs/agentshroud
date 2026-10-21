---
type: community
members: 7
---

# _make_cve (2)

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
TABLE source_file, type FROM #community/_make_cve_2
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY__make_cve]]

## Top bridge nodes
- [[_telegram_alert()]] - degree 3, connects to 1 community
