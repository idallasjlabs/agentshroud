---
type: community
cohesion: 0.29
members: 7
---

# Credential Injector

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.test_get_all_loaded_values_method()]] - code - gateway/tests/test_credential_injector.py
- [[.test_returns_empty_when_dir_missing()]] - code - gateway/tests/test_credential_injector.py
- [[.test_returns_values_meeting_min_len()]] - code - gateway/tests/test_credential_injector.py
- [[.test_strips_trailing_newline()]] - code - gateway/tests/test_credential_injector.py
- [[CredentialInjector.get_all_loaded_values returns all loaded credential values.]] - rationale - gateway/tests/test_credential_injector.py
- [[TestLoadAllSecretFileValues]] - code - gateway/tests/test_credential_injector.py
- [[load_all_secret_file_values reads all Docker secret files for scrubbing.]] - rationale - gateway/tests/test_credential_injector.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Credential_Injector
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Credential Injector]]
- 1 edge to [[_COMMUNITY_Credential Isolation]]

## Top bridge nodes
- [[TestLoadAllSecretFileValues]] - degree 6, connects to 1 community
- [[.test_get_all_loaded_values_method()]] - degree 3, connects to 1 community