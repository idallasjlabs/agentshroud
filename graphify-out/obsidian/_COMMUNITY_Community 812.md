---
type: community
cohesion: 0.18
members: 11
---

# Community 812

**Cohesion:** 0.18 - loosely connected
**Members:** 11 nodes

## Members
- [[.setup_method()_8]] - code - gateway/tests/test_main_endpoints.py
- [[.teardown_method()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_clamav_default_target_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_clamav_invalid_target_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_openscap_default_profile_passes_regex()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_openscap_invalid_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_openscap_semicolon_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_trivy_default_scan_type_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[.test_trivy_invalid_scan_type_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[Allowlist validation on ClamAV target, Trivy scan type, OpenSCAP profile.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestScanParameterAllowlists]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_812
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]
- 1 edge to [[_COMMUNITY_Ingest API & Approval Routes]]

## Top bridge nodes
- [[TestScanParameterAllowlists]] - degree 12, connects to 2 communities