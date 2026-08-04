---
type: community
cohesion: 0.16
members: 17
---

# Module Group 264

**Cohesion:** 0.16 - loosely connected
**Members:** 17 nodes

## Members
- [[.__init__()_51]] - code - gateway/security/config_integrity.py
- [[._hash_file()]] - code - gateway/security/config_integrity.py
- [[._load_baseline()]] - code - gateway/security/config_integrity.py
- [[._save_baseline()]] - code - gateway/security/config_integrity.py
- [[.check()_2]] - code - gateway/security/config_integrity.py
- [[.format_alert_text()]] - code - gateway/security/config_integrity.py
- [[.reset_baseline()]] - code - gateway/security/config_integrity.py
- [[Accept current file hashes as the new baseline (owner-acknowledged rebuild).]] - rationale - gateway/security/config_integrity.py
- [[Compare current file hashes against baseline.          Returns a list of change]] - rationale - gateway/security/config_integrity.py
- [[Computes and verifies SHA256 hashes of monitored bot config files.      At gatew]] - rationale - gateway/security/config_integrity.py
- [[ConfigIntegrityMonitor]] - code - gateway/security/config_integrity.py
- [[Format Telegram alert text for detected config changes.]] - rationale - gateway/security/config_integrity.py
- [[Load the last known baseline from disk. Returns empty dict if not found.]] - rationale - gateway/security/config_integrity.py
- [[Path_9]] - code - gateway/security/config_integrity.py
- [[Persist the current hashes as the new baseline.]] - rationale - gateway/security/config_integrity.py
- [[Return hex SHA256 of a file, or None if the file does not exist.]] - rationale - gateway/security/config_integrity.py
- [[config_integrity.py]] - code - gateway/security/config_integrity.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_264
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Gateway Config & Lifespan]]

## Top bridge nodes
- [[ConfigIntegrityMonitor]] - degree 11, connects to 1 community
