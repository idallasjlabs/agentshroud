---
type: community
cohesion: 0.10
members: 20
---

# Community 457

**Cohesion:** 0.10 - loosely connected
**Members:** 20 nodes

## Members
- [[.test_auto_revert_timer_logic()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_get_module_mode_pinned_modules()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_get_module_mode_respect_global_override()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_module_mode_resolution()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_observatory_mode_state_initialization()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_observatory_mode_validation()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_pinned_modules_validation()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_security_pipeline_set_global_mode()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_security_pipeline_set_global_mode_missing_components()]] - code - gateway/tests/test_observatory_mode.py
- [[Test Observatory Mode configuration and endpoints.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test SecurityPipeline.set_global_mode method.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test auto-revert timer functionality.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test module mode resolution with pinned modules.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test set_global_mode handles missing components gracefully.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test that get_module_mode respects AGENTSHROUD_MODE env var.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test that observatory mode state is properly initialized.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test that pinned modules always return enforce even in monitor mode.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test validation of observatory mode parameters.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Test validation of pinned module names.]] - rationale - gateway/tests/test_observatory_mode.py
- [[TestObservatoryMode]] - code - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_457
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_PII Sanitizer & E2E Tests]]
- 2 edges to [[_COMMUNITY_Community 25]]
- 1 edge to [[_COMMUNITY_Community 157]]
- 1 edge to [[_COMMUNITY_Community 156]]
- 1 edge to [[_COMMUNITY_Community 29]]

## Top bridge nodes
- [[TestObservatoryMode]] - degree 15, connects to 4 communities
- [[.test_get_module_mode_respect_global_override()]] - degree 3, connects to 1 community
- [[.test_security_pipeline_set_global_mode()]] - degree 3, connects to 1 community
- [[.test_security_pipeline_set_global_mode_missing_components()]] - degree 3, connects to 1 community