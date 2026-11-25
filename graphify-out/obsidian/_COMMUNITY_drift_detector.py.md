---
type: community
members: 8
---

# drift_detector.py

**Members:** 8 nodes

## Members
- [[dot-check_drift()]] - code - gateway/security/drift_detector.py
- [[dot-from_dict()_5]] - code - gateway/security/drift_detector.py
- [[dot-get_baseline()]] - code - gateway/security/drift_detector.py
- [[Compare current config against baseline, return any drift alerts.]] - rationale - gateway/security/drift_detector.py
- [[Drift Detection — detect unauthorized container config changes. Snapshots…]] - rationale - gateway/security/drift_detector.py
- [[DriftAlert]] - code - gateway/security/drift_detector.py
- [[Retrieve baseline snapshot for a container.]] - rationale - gateway/security/drift_detector.py
- [[drift_detector.py]] - code - gateway/security/drift_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/drift_detectorpy
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_ContainerSnapshot]]
- 3 edges to [[_COMMUNITY_DriftDetector]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_AgentRegistry]]
- 1 edge to [[_COMMUNITY_ingest_apiconfig.py]]

## Top bridge nodes
- [[drift_detector.py]] - degree 7, connects to 5 communities
- [[dot-check_drift()]] - degree 5, connects to 2 communities
- [[dot-get_baseline()]] - degree 5, connects to 2 communities
- [[dot-from_dict()_5]] - degree 2, connects to 1 community
