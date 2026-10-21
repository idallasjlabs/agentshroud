---
type: community
members: 3
---

# test_bot_boot_live.sh

**Members:** 3 nodes

## Members
- [[Test Kill Switch Monitor]] - code - gateway/tests/test_killswitch_monitor.py
- [[Test Kill Switch Script Modes]] - code - gateway/tests/test_killswitch_modes.py
- [[Test Observatory Mode API and Kill Switch Verification]] - code - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_bot_boot_livesh
SORT file.name ASC
```
