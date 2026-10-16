---
type: community
cohesion: 0.18
members: 12
---

# .check

**Cohesion:** 0.18 - loosely connected
**Members:** 12 nodes

## Members
- [[dot-__init__()_196]] - code - gateway/security/config_integrity.py
- [[dot-_hash_file()]] - code - gateway/security/config_integrity.py
- [[dot-_load_baseline()]] - code - gateway/security/config_integrity.py
- [[dot-_save_baseline()]] - code - gateway/security/config_integrity.py
- [[dot-check()_6]] - code - gateway/security/config_integrity.py
- [[dot-reset_baseline()]] - code - gateway/security/config_integrity.py
- [[Accept current file hashes as the new baseline (owner-acknowledged rebuild).]] - rationale - gateway/security/config_integrity.py
- [[Compare current file hashes against baseline.          Returns a list of change]] - rationale - gateway/security/config_integrity.py
- [[Load the last known baseline from disk. Returns empty dict if not found.]] - rationale - gateway/security/config_integrity.py
- [[Path_62]] - code - gateway/security/config_integrity.py
- [[Persist the current hashes as the new baseline.]] - rationale - gateway/security/config_integrity.py
- [[Return hex SHA256 of a file, or None if the file does not exist.]] - rationale - gateway/security/config_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/check
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_ConfigIntegrityMonitor]]

## Top bridge nodes
- [[dot-check()_6]] - degree 5, connects to 1 community
- [[dot-_hash_file()]] - degree 5, connects to 1 community
- [[dot-reset_baseline()]] - degree 4, connects to 1 community
- [[dot-_save_baseline()]] - degree 4, connects to 1 community
- [[dot-_load_baseline()]] - degree 3, connects to 1 community
