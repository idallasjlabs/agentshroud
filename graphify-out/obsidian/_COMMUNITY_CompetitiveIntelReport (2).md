---
type: community
members: 6
---

# CompetitiveIntelReport (2)

**Members:** 6 nodes

## Members
- [[dot-__init__()_41]] - code - gateway/security/intel_report.py
- [[dot-_load_latest_file()]] - code - gateway/security/intel_report.py
- [[dot-save()_2]] - code - gateway/security/intel_report.py
- [[Path_7]] - code - gateway/security/intel_report.py
- [[Persist report to the store, linking it to the previous report.          Sets]] - rationale - gateway/security/intel_report.py
- [[Return the most recent JSON file in the store, or None.]] - rationale - gateway/security/intel_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CompetitiveIntelReport_2
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_api.py]]
- 2 edges to [[_COMMUNITY_CompetitiveIntelReport]]

## Top bridge nodes
- [[dot-_load_latest_file()]] - degree 5, connects to 2 communities
- [[dot-save()_2]] - degree 5, connects to 2 communities
- [[dot-__init__()_41]] - degree 2, connects to 1 community
