---
type: community
members: 6
---

# TestPIIDetection

**Members:** 6 nodes

## Members
- [[dot-test_aws_key_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_pii_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_pii_in_url_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_private_key_in_response_flagged()]] - code - gateway/tests/test_web_proxy.py
- [[dot-test_ssn_in_url_flagged()_1]] - code - gateway/tests/test_web_proxy.py
- [[TestPIIDetection]] - code - gateway/tests/test_web_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPIIDetection
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_WebProxy]]

## Top bridge nodes
- [[TestPIIDetection]] - degree 6, connects to 1 community
