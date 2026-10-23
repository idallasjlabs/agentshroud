---
type: community
cohesion: 0.33
members: 6
---

# TestPIIInURLs

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[dot-test_credit_card_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_email_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_phone_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[dot-test_ssn_in_url_flagged()]] - code - gateway/tests/test_url_analyzer.py
- [[PII detection in URLs — flagged, not blocked.]] - rationale - gateway/tests/test_url_analyzer.py
- [[TestPIIInURLs]] - code - gateway/tests/test_url_analyzer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPIIInURLs
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_URLAnalyzer]]
- 1 edge to [[_COMMUNITY_Enum]]

## Top bridge nodes
- [[TestPIIInURLs]] - degree 8, connects to 2 communities
