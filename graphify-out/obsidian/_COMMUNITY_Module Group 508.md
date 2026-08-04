---
type: community
cohesion: 0.40
members: 5
---

# Module Group 508

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[._sanitize_text()]] - code - gateway/security/log_sanitizer.py
- [[.filter()_1]] - code - gateway/security/log_sanitizer.py
- [[Filter log record, sanitizing sensitive content.]] - rationale - gateway/security/log_sanitizer.py
- [[LogRecord_1]] - code - gateway/security/log_sanitizer.py
- [[Sanitize sensitive data in text.]] - rationale - gateway/security/log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_508
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]

## Top bridge nodes
- [[.filter()_1]] - degree 4, connects to 1 community
- [[._sanitize_text()]] - degree 3, connects to 1 community
