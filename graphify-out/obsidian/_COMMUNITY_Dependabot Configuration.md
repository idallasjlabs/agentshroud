---
type: community
members: 2
---

# Dependabot Configuration

**Members:** 2 nodes

## Members
- [[SOC Models SecurityEvent Tests]] - code - gateway/tests/test_soc_models.py
- [[SOC ServiceManager Tests (get_logs, module_filter)]] - code - gateway/tests/test_soc_services.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Dependabot_Configuration
SORT file.name ASC
```
