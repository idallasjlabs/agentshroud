---
type: community
cohesion: 1.00
members: 2
---

# LogSanitizer PII-Scrubbing Log Filter

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[LogSanitizer PII-Scrubbing Log Filter]] - code - gateway/security/log_sanitizer.py
- [[Test Log Sanitizer PII Scrubbing]] - code - gateway/tests/test_log_sanitizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/LogSanitizer_PII-Scrubbing_Log_Filter
SORT file.name ASC
```
