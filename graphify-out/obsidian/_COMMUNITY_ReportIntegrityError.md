---
type: community
members: 11
---

# ReportIntegrityError

**Members:** 11 nodes

## Members
- [[dot-__init__()_61]] - code - gateway/security/intel_report.py
- [[dot-_load_latest_file()]] - code - gateway/security/intel_report.py
- [[dot-load_latest()]] - code - gateway/security/intel_report.py
- [[dot-save()_1]] - code - gateway/security/intel_report.py
- [[Exception_3]] - code
- [[Load the most recently saved report. Args verify If True, raise…]] - rationale - gateway/security/intel_report.py
- [[Path_23]] - code
- [[Persist report to the store, linking it to the previous report. Sets…]] - rationale - gateway/security/intel_report.py
- [[Raised when a loaded report fails its hash integrity check.]] - rationale - gateway/security/intel_report.py
- [[ReportIntegrityError]] - code - gateway/security/intel_report.py
- [[Return the most recent JSON file in the store, or None.]] - rationale - gateway/security/intel_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ReportIntegrityError
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_IntelReportStore]]
- 4 edges to [[_COMMUNITY_CompetitiveIntelReport]]

## Top bridge nodes
- [[ReportIntegrityError]] - degree 6, connects to 2 communities
- [[dot-load_latest()]] - degree 5, connects to 2 communities
- [[dot-save()_1]] - degree 5, connects to 2 communities
- [[dot-_load_latest_file()]] - degree 5, connects to 1 community
- [[dot-__init__()_61]] - degree 2, connects to 1 community
