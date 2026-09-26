---
type: community
cohesion: 0.40
members: 5
---

# AgentShroud Data Assets (root)

**Cohesion:** 0.40 - moderately connected
**Members:** 5 nodes

## Members
- [[ClamAV (malware detection)]] - concept - gateway/security/__init__.py
- [[Falco (runtime security monitoring)]] - concept - gateway/security/__init__.py
- [[Trivy (container vulnerability scanning)]] - concept - gateway/security/__init__.py
- [[Wazuh (file integrity monitoring)]] - concept - gateway/security/__init__.py
- [[__init__.py_9]] - code - gateway/security/__init__.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Data_Assets_root
SORT file.name ASC
```
