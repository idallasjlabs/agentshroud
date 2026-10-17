---
type: community
members: 5
---

# ResourceGuard (3)

**Members:** 5 nodes

## Members
- [[dot-export_findings_report()]] - code - gateway/security/git_guard.py
- [[dot-get_findings_summary()]] - code - gateway/security/git_guard.py
- [[Any_16]] - code - gateway/security/git_guard.py
- [[Export findings to a detailed report.]] - rationale - gateway/security/git_guard.py
- [[Get a summary of all findings.]] - rationale - gateway/security/git_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ResourceGuard_3
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[dot-get_findings_summary()]] - degree 4, connects to 1 community
- [[dot-export_findings_report()]] - degree 3, connects to 1 community
