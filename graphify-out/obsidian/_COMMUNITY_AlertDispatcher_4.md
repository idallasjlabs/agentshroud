---
type: community
cohesion: 0.40
members: 5
---

# AlertDispatcher

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[dot-_sanitize_text()]] - code - gateway/security/log_sanitizer.py
- [[dot-filter()]] - code - gateway/security/log_sanitizer.py
- [[Filter log record, sanitizing sensitive content.]] - rationale - gateway/security/log_sanitizer.py
- [[LogRecord]] - code - gateway/security/log_sanitizer.py
- [[Sanitize sensitive data in text.]] - rationale - gateway/security/log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AlertDispatcher
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[dot-filter()]] - degree 4, connects to 1 community
- [[dot-_sanitize_text()]] - degree 3, connects to 1 community
