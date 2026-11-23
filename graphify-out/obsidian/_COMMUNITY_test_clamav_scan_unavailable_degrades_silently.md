---
type: community
members: 9
---

# test_clamav_scan_unavailable_degrades_silently

**Members:** 9 nodes

## Members
- [[_fake_clamscan()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_fake_clamscan()_1]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_fake_clamscan()_2]] - code - gateway/tests/test_http_proxy_coverage.py
- [[_fake_clamscan()_3]] - code - gateway/tests/test_http_proxy_coverage.py
- [[clamscan binary missing (sidecar down) - no exception, temp file removed.]] - rationale - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_clean_records_nothing()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_infected_records_stats()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_unavailable_degrades_silently()]] - code - gateway/tests/test_http_proxy_coverage.py
- [[test_clamav_scan_unlink_failure_swallowed()]] - code - gateway/tests/test_http_proxy_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_clamav_scan_unavailable_degrades_silently
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_HTTPConnectProxy]]
- 4 edges to [[_COMMUNITY_test_http_proxy_coverage.py]]

## Top bridge nodes
- [[test_clamav_scan_unavailable_degrades_silently()]] - degree 5, connects to 2 communities
- [[test_clamav_scan_clean_records_nothing()]] - degree 4, connects to 2 communities
- [[test_clamav_scan_unlink_failure_swallowed()]] - degree 4, connects to 2 communities
- [[test_clamav_scan_infected_records_stats()]] - degree 3, connects to 2 communities
