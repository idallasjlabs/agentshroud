---
type: community
cohesion: 0.14
members: 14
---

# ._record_leakage()

**Cohesion:** 0.14 - loosely connected
**Members:** 14 nodes

## Members
- [[dot-_contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[dot-_looks_like_credential()]] - code - gateway/security/env_guard.py
- [[dot-_record_leakage()]] - code - gateway/security/env_guard.py
- [[dot-check_command_execution()]] - code - gateway/security/env_guard.py
- [[dot-check_file_access()]] - code - gateway/security/env_guard.py
- [[dot-scrub_command_output()]] - code - gateway/security/env_guard.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Scrub environment variables and API keys from command output.          Args]] - rationale - gateway/security/env_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_record_leakage
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_ContextGuard]]
- 2 edges to [[_COMMUNITY_check_command]]

## Top bridge nodes
- [[dot-check_command_execution()]] - degree 5, connects to 2 communities
- [[dot-_record_leakage()]] - degree 6, connects to 1 community
- [[dot-scrub_command_output()]] - degree 4, connects to 1 community
- [[dot-check_file_access()]] - degree 3, connects to 1 community
- [[dot-_contains_env_access_patterns()]] - degree 3, connects to 1 community
