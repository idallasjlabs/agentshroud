---
type: community
cohesion: 0.67
members: 3
---

# deploy.sh

**Cohesion:** 0.67 - moderately connected
**Members:** 3 nodes

## Members
- [[TrustManager._promotion_allowed]] - code - gateway/security/trust_manager.py
- [[TrustManager._update_score]] - code - gateway/security/trust_manager.py
- [[TrustManager.record_violation]] - code - gateway/security/trust_manager.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/deploysh
SORT file.name ASC
```
