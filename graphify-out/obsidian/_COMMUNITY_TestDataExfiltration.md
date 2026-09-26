---
type: community
cohesion: 0.18
members: 13
---

# TestDataExfiltration

**Cohesion:** 0.18 - loosely connected
**Members:** 13 nodes

## Members
- [[.test_basic_auth_invalid_base64()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_basic_auth_no_password_configured()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_basic_auth_not_basic_scheme()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_basic_auth_valid()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_basic_auth_wrong_password()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_build_proxy_headers_strips_hop_by_hop_and_auth()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_read_password_env_fallback()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_read_password_from_file()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_token_auth_empty_expected_password()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_token_auth_valid()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[.test_token_auth_wrong_and_missing()]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[TestCanvasAuthHelpers]] - code - gateway/tests/test_dns_canvas_coverage.py
- [[_basic()]] - code - gateway/tests/test_dns_canvas_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestDataExfiltration
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_AgentShroud Operations Cheat Sheet]]
- 2 edges to [[_COMMUNITY_Seccomp Profiles]]
- 1 edge to [[_COMMUNITY_DNSBlocklist]]
- 1 edge to [[_COMMUNITY_canvas_proxy_app()]]

## Top bridge nodes
- [[TestCanvasAuthHelpers]] - degree 14, connects to 3 communities
- [[_basic()]] - degree 7, connects to 2 communities