---
type: community
cohesion: 0.22
members: 11
---

# Module Group 348

**Cohesion:** 0.22 - loosely connected
**Members:** 11 nodes

## Members
- [[Build normalized scanner summary for SOCdashboard telemetry.]] - rationale - gateway/ingest_api/main.py
- [[Persist last scanner result and emit live event-bus telemetry.]] - rationale - gateway/ingest_api/main.py
- [[Return normalized scanner state + latest results for SOCdashboard views.]] - rationale - gateway/ingest_api/main.py
- [[Run OpenSCAP XCCDF evaluation against the running container.]] - rationale - gateway/ingest_api/main.py
- [[Run Trivy vulnerability scan.]] - rationale - gateway/ingest_api/main.py
- [[Run all locally available security scanners and return consolidated results.]] - rationale - gateway/ingest_api/main.py
- [[_record_scanner_result()]] - code - gateway/ingest_api/main.py
- [[_scanner_summary()]] - code - gateway/ingest_api/main.py
- [[run_all_scanners()]] - code - gateway/ingest_api/main.py
- [[run_openscap_scan()]] - code - gateway/ingest_api/main.py
- [[run_trivy_scan()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_348
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Dashboard Routes & WebSocket]]

## Top bridge nodes
- [[_record_scanner_result()]] - degree 8, connects to 2 communities
- [[run_all_scanners()]] - degree 6, connects to 1 community
- [[_scanner_summary()]] - degree 6, connects to 1 community
- [[run_trivy_scan()]] - degree 5, connects to 1 community
- [[run_openscap_scan()]] - degree 4, connects to 1 community