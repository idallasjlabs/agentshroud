---
type: community
cohesion: 1.00
members: 2
---

# i-hermes README (Podcast Production Orchestrator

**Cohesion:** 1.00 - tightly connected
**Members:** 2 nodes

## Members
- [[_PII_PATTERNS (URL PII regex set)]] - code - gateway/proxy/url_analyzer.py
- [[_RESPONSE_PII_PATTERNS (content PII regex set)]] - code - gateway/proxy/web_content_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/i-hermes_README_Podcast_Production_Orchestrator
SORT file.name ASC
```
