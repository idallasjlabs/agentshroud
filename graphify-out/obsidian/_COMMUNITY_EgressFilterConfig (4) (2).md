---
type: community
members: 12
---

# EgressFilterConfig (4) (2)

**Members:** 12 nodes

## Members
- [[dot-_make_monitor()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_dry_run_true_does_not_kill()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_duration_is_non_negative()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_overall_status_is_valid_value()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_result_has_required_fields()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_script_exists_test_is_present()]] - code - gateway/tests/test_observatory_mode.py
- [[dot-test_verification_log_written()]] - code - gateway/tests/test_observatory_mode.py
- [[Automated verification that verify_killswitch() returns required fields.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Path_65]] - code - gateway/tests/test_observatory_mode.py
- [[TestKillSwitchVerification]] - code - gateway/tests/test_observatory_mode.py
- [[dry_run=True must never trigger actual kill switch execution.]] - rationale - gateway/tests/test_observatory_mode.py
- [[verify_killswitch() must write a log entry for auditability.]] - rationale - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig_4_2
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_EgressFilterConfig (4)]]
- 3 edges to [[_COMMUNITY_AgentTarget (3)]]
- 2 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 2 edges to [[_COMMUNITY_AsyncMock]]

## Top bridge nodes
- [[TestKillSwitchVerification]] - degree 13, connects to 4 communities
- [[Path_65]] - degree 5, connects to 4 communities
- [[dot-_make_monitor()]] - degree 10, connects to 2 communities
