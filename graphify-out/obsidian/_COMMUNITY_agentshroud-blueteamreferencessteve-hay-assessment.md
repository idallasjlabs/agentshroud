---
type: community
members: 2
---

# agentshroud-blueteam/references/steve-hay-assessment.md

**Members:** 2 nodes

## Members
- [[S3 apply-patches.js validates xoxb-xapp- Slack token prefixes]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[S7 apply-patches.js deletes stale channels.slack block when no tokens present]] - concept - tests/startup_smoke/test_bot_boot_static.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/agentshroud-blueteam/references/steve-hay-assessmentmd
SORT file.name ASC
```
