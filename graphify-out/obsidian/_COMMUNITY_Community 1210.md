---
type: community
members: 12
---

# Community 1210

**Members:** 12 nodes

## Members
- [[.__init__()_78]] - code - gateway/security/config_integrity.py
- [[._hash_file()]] - code - gateway/security/config_integrity.py
- [[._load_baseline()]] - code - gateway/security/config_integrity.py
- [[._save_baseline()]] - code - gateway/security/config_integrity.py
- [[.check()_2]] - code - gateway/security/config_integrity.py
- [[.reset_baseline()]] - code - gateway/security/config_integrity.py
- [[Accept current file hashes as the new baseline (owner-acknowledged rebuild).]] - rationale - gateway/security/config_integrity.py
- [[Compare current file hashes against baseline.          Returns a list of change]] - rationale - gateway/security/config_integrity.py
- [[Load the last known baseline from disk. Returns empty dict if not found.]] - rationale - gateway/security/config_integrity.py
- [[Path_12]] - code - gateway/security/config_integrity.py
- [[Persist the current hashes as the new baseline.]] - rationale - gateway/security/config_integrity.py
- [[Return hex SHA256 of a file, or None if the file does not exist.]] - rationale - gateway/security/config_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_1210
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 241]]

## Top bridge nodes
- [[._hash_file()]] - degree 5, connects to 1 community
- [[.check()_2]] - degree 5, connects to 1 community
- [[._save_baseline()]] - degree 4, connects to 1 community
- [[.reset_baseline()]] - degree 4, connects to 1 community
- [[._load_baseline()]] - degree 3, connects to 1 community