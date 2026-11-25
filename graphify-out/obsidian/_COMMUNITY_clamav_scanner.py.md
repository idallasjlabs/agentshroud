---
type: community
members: 15
---

# clamav_scanner.py

**Members:** 15 nodes

## Members
- [[dot-test_clamav_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_run_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[dot-test_update_db_not_found()]] - code - gateway/tests/test_security_toolchain.py
- [[Any_89]] - code
- [[Generate a summary dict suitable for the health report. Args report Parsed…_1]] - rationale - gateway/security/clamav_scanner.py
- [[Path_76]] - code
- [[Run ClamAV scan and return parsed results. Args target Directory or file to…]] - rationale - gateway/security/clamav_scanner.py
- [[Save a ClamAV report to the log directory.]] - rationale - gateway/security/clamav_scanner.py
- [[TestClamAVRun]] - code - gateway/tests/test_security_toolchain.py
- [[Update ClamAV virus database using freshclam. Args freshclam_bin Path to…]] - rationale - gateway/security/clamav_scanner.py
- [[clamav_scanner.py_2]] - code - gateway/security/clamav_scanner.py
- [[generate_summary()_3]] - code - gateway/security/clamav_scanner.py
- [[run_clamscan()_1]] - code - gateway/security/clamav_scanner.py
- [[save_report()_1]] - code - gateway/security/clamav_scanner.py
- [[update_virus_db()]] - code - gateway/security/clamav_scanner.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/clamav_scannerpy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_clamav_pipeline.py]]
- 5 edges to [[_COMMUNITY_test_security_toolchain.py]]
- 4 edges to [[_COMMUNITY_parse_clamscan_output]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_middleware.py]]
- 2 edges to [[_COMMUNITY_run_trivy_scan]]
- 1 edge to [[_COMMUNITY_dot-_relay]]
- 1 edge to [[_COMMUNITY_scanner_integration.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]

## Top bridge nodes
- [[clamav_scanner.py_2]] - degree 13, connects to 6 communities
- [[run_clamscan()_1]] - degree 11, connects to 6 communities
- [[Any_89]] - degree 6, connects to 2 communities
- [[generate_summary()_3]] - degree 5, connects to 2 communities
- [[update_virus_db()]] - degree 5, connects to 1 community
