---
type: community
cohesion: 1.00
members: 2
---

# 3. Viewing Audit Logs

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[SOC Models SecurityEvent Tests]] - code - gateway/tests/test_soc_models.py
- [[SOC ServiceManager Tests (get_logs, module_filter)]] - code - gateway/tests/test_soc_services.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/3_Viewing_Audit_Logs
SORT file.name ASC
```
