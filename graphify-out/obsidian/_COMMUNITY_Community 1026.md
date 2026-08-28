---
type: community
cohesion: 0.29
members: 7
---

# Community 1026

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[._create_detection_patterns()]] - code - gateway/security/output_canary.py
- [[._create_invisible_canary()]] - code - gateway/security/output_canary.py
- [[.generate_canary()]] - code - gateway/security/output_canary.py
- [[Create an invisible version of the canary using various techniques.          Arg]] - rationale - gateway/security/output_canary.py
- [[Create regex patterns to detect the canary in responses.          Args]] - rationale - gateway/security/output_canary.py
- [[Generate and store a canary for this session.          Args             session]] - rationale - gateway/security/output_canary.py
- [[Pattern_2]] - code - gateway/security/output_canary.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1026
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Memory Lifecycle & Egress Filtering]]

## Top bridge nodes
- [[._create_detection_patterns()]] - degree 4, connects to 1 community
- [[.generate_canary()]] - degree 4, connects to 1 community
- [[._create_invisible_canary()]] - degree 3, connects to 1 community