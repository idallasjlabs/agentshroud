---
type: community
members: 14
---

# PIIHit

**Members:** 14 nodes

## Members
- [[dot-_deduplicate()]] - code - gateway/security/differential_pii_detector.py
- [[dot-_detect_pii()]] - code - gateway/security/differential_pii_detector.py
- [[dot-_detect_presidio()]] - code - gateway/security/differential_pii_detector.py
- [[dot-_detect_regex()]] - code - gateway/security/differential_pii_detector.py
- [[dot-from_confidence()]] - code - gateway/security/differential_pii_detector.py
- [[A single PII detection result.]] - rationale - gateway/security/differential_pii_detector.py
- [[IntEnum]] - code
- [[PIIHit]] - code - gateway/security/differential_pii_detector.py
- [[PIIHitSeverity]] - code - gateway/security/differential_pii_detector.py
- [[Regex-based PII detection (Presidio fallback).]] - rationale - gateway/security/differential_pii_detector.py
- [[Relative risk of a detected PII entity.]] - rationale - gateway/security/differential_pii_detector.py
- [[Remove overlapping hits, preferring higher confidence.]] - rationale - gateway/security/differential_pii_detector.py
- [[Run PII detection, returning hits at or above floor.]] - rationale - gateway/security/differential_pii_detector.py
- [[Use Presidio (entity-restricted) unioned with the core regex. Two guarantees…]] - rationale - gateway/security/differential_pii_detector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/PIIHit
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_DifferentialPIIDetector]]
- 4 edges to [[_COMMUNITY_differential_pii_detector.py]]
- 2 edges to [[_COMMUNITY_test_differential_pii_detector.py]]

## Top bridge nodes
- [[PIIHit]] - degree 9, connects to 3 communities
- [[PIIHitSeverity]] - degree 6, connects to 3 communities
- [[dot-_detect_pii()]] - degree 6, connects to 2 communities
- [[dot-_detect_presidio()]] - degree 7, connects to 1 community
- [[dot-_detect_regex()]] - degree 7, connects to 1 community
