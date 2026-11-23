---
type: community
members: 11
---

# TestScanParameterAllowlists

**Members:** 11 nodes

## Members
- [[dot-setup_method()_10]] - code - gateway/tests/test_main_endpoints.py
- [[dot-teardown_method()_2]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_default_target_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_clamav_invalid_target_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_default_profile_passes_regex()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_invalid_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_openscap_semicolon_profile_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_trivy_default_scan_type_passes_allowlist()]] - code - gateway/tests/test_main_endpoints.py
- [[dot-test_trivy_invalid_scan_type_returns_400()]] - code - gateway/tests/test_main_endpoints.py
- [[Allowlist validation on ClamAV target, Trivy scan type, OpenSCAP profile.]] - rationale - gateway/tests/test_main_endpoints.py
- [[TestScanParameterAllowlists]] - code - gateway/tests/test_main_endpoints.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestScanParameterAllowlists
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_app]]
- 1 edge to [[_COMMUNITY_fastapi]]

## Top bridge nodes
- [[TestScanParameterAllowlists]] - degree 11, connects to 1 community
- [[dot-setup_method()_10]] - degree 2, connects to 1 community
- [[dot-teardown_method()_2]] - degree 2, connects to 1 community
