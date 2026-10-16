---
type: community
cohesion: 0.10
members: 20
---

# ForwardRequest

**Cohesion:** 0.10 - loosely connected
**Members:** 20 nodes

## Members
- [[dot-test_approval_queue_enabled()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_container_hardening()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_drift_detector_enabled()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_egress_filter_enabled()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_encrypted_store_enabled()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_extensive_approval_actions()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_has_auth_token_placeholder()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_has_memory_limit()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_has_seccomp_profile()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_kill_switch_enabled()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_long_retention()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_pii_enabled()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_pii_engine_presidio()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_prompt_guard_enabled()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_rootless()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_ssh_requires_approval()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_telemetry_disabled()]] - code - gateway/tests/test_config_validation.py
- [[dot-test_trust_manager_enabled()]] - code - gateway/tests/test_config_validation.py
- [[TestParanoidConfig]] - code - gateway/tests/test_config_validation.py
- [[paranoid.env should enable ALL security features.]] - rationale - gateway/tests/test_config_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ForwardRequest
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AgentTarget]]

## Top bridge nodes
- [[TestParanoidConfig]] - degree 23, connects to 1 community
