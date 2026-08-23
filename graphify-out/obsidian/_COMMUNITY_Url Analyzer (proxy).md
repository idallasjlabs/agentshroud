---
type: community
cohesion: 1.00
members: 2
---

# Url Analyzer (proxy)

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[_PII_PATTERNS (URL PII regex set)]] - code - gateway/proxy/url_analyzer.py
- [[_RESPONSE_PII_PATTERNS (content PII regex set)]] - code - gateway/proxy/web_content_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Url_Analyzer_proxy
SORT file.name ASC
```
