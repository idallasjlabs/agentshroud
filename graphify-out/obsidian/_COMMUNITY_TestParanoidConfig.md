---
type: community
cohesion: 0.11
members: 19
---

# TestParanoidConfig

**Cohesion:** 0.11 - loosely connected
**Members:** 19 nodes

## Members
- [[.test_approval_queue_enabled()_2]] - code - gateway/tests/test_config_validation.py
- [[.test_container_hardening()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_drift_detector_enabled()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_egress_filter_enabled()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_encrypted_store_enabled()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_extensive_approval_actions()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_has_auth_token_placeholder()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_has_memory_limit()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_has_seccomp_profile()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_kill_switch_enabled()_2]] - code - gateway/tests/test_config_validation.py
- [[.test_long_retention()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_pii_enabled()_2]] - code - gateway/tests/test_config_validation.py
- [[.test_pii_engine_presidio()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_prompt_guard_enabled()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_rootless()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_ssh_requires_approval()_2]] - code - gateway/tests/test_config_validation.py
- [[.test_telemetry_disabled()_1]] - code - gateway/tests/test_config_validation.py
- [[.test_trust_manager_enabled()_1]] - code - gateway/tests/test_config_validation.py
- [[TestParanoidConfig_1]] - code - gateway/tests/test_config_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestParanoidConfig
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_config_validation.py]]
- 1 edge to [[_COMMUNITY_TestParanoidConfig]]
- 1 edge to [[_COMMUNITY__parse_env_file()]]

## Top bridge nodes
- [[TestParanoidConfig_1]] - degree 21, connects to 3 communities