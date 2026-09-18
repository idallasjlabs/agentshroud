---
type: community
cohesion: 0.26
members: 12
---

# TestKillSwitchVerification

**Cohesion:** 0.26 - loosely connected
**Members:** 12 nodes

## Members
- [[._make_monitor()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_dry_run_true_does_not_kill()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_duration_is_non_negative()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_overall_status_is_valid_value()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_result_has_required_fields()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_script_exists_test_is_present()]] - code - gateway/tests/test_observatory_mode.py
- [[.test_verification_log_written()]] - code - gateway/tests/test_observatory_mode.py
- [[Automated verification that verify_killswitch() returns required fields.]] - rationale - gateway/tests/test_observatory_mode.py
- [[Path_29]] - code - gateway/tests/test_observatory_mode.py
- [[TestKillSwitchVerification]] - code - gateway/tests/test_observatory_mode.py
- [[dry_run=True must never trigger actual kill switch execution.]] - rationale - gateway/tests/test_observatory_mode.py
- [[verify_killswitch() must write a log entry for auditability.]] - rationale - gateway/tests/test_observatory_mode.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestKillSwitchVerification
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_ModeRequest]]
- 1 edge to [[_COMMUNITY_test_observatory_mode.py]]

## Top bridge nodes
- [[TestKillSwitchVerification]] - degree 13, connects to 4 communities
- [[Path_29]] - degree 5, connects to 3 communities
- [[._make_monitor()]] - degree 10, connects to 1 community