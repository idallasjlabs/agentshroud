---
type: community
cohesion: 0.40
members: 5
---

# security/__init__.py

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[ClamAV (malware detection)]] - concept - gateway/security/__init__.py
- [[Falco (runtime security monitoring)]] - concept - gateway/security/__init__.py
- [[Trivy (container vulnerability scanning)]] - concept - gateway/security/__init__.py
- [[Wazuh (file integrity monitoring)]] - concept - gateway/security/__init__.py
- [[security__init__.py]] - code - gateway/security/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/security/__init__py
SORT file.name ASC
```
