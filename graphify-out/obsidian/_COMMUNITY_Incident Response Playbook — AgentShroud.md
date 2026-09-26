---
type: community
cohesion: 0.15
members: 20
---

# Incident Response Playbook — AgentShroud

**Cohesion:** 0.15 - loosely connected
**Members:** 20 nodes

## Members
- [[.test_any_error_since_boot_blocks_regardless_of_successes()]] - code - gateway/tests/test_soak_status.py
- [[.test_below_threshold_not_soaked()]] - code - gateway/tests/test_soak_status.py
- [[.test_empty_heartbeat_file_skip_alone_is_not_soaked()]] - code - gateway/tests/test_soak_status.py
- [[.test_empty_heartbeat_file_skip_does_not_mask_a_real_error()]] - code - gateway/tests/test_soak_status.py
- [[.test_empty_heartbeat_file_skip_is_benign_not_blocking()]] - code - gateway/tests/test_soak_status.py
- [[.test_empty_job_list()]] - code - gateway/tests/test_soak_status.py
- [[.test_missing_state_key_does_not_crash()]] - code - gateway/tests/test_soak_status.py
- [[.test_no_runs_since_boot_not_soaked()]] - code - gateway/tests/test_soak_status.py
- [[.test_one_success_since_boot_meets_default_threshold()]] - code - gateway/tests/test_soak_status.py
- [[.test_other_skipped_status_counts_as_not_ok()]] - code - gateway/tests/test_soak_status.py
- [[.test_runs_before_boot_are_ignored()]] - code - gateway/tests/test_soak_status.py
- [[2026-09-19 root cause 'heartbeat skipped empty-heartbeat-file' is         Open]] - rationale - gateway/tests/test_soak_status.py
- [[A benign heartbeat skip must not hide an actual failing job.]] - rationale - gateway/tests/test_soak_status.py
- [[A job that last succeeded before this boot proves nothing about         THIS dep]] - rationale - gateway/tests/test_soak_status.py
- [[A skip for any OTHER reason (not the known-benign empty-heartbeat-         file]] - rationale - gateway/tests/test_soak_status.py
- [[An actively-failing job since redeploy must block soak even if         other job]] - rationale - gateway/tests/test_soak_status.py
- [[TestClassify_1]] - code - gateway/tests/test_soak_status.py
- [[The benign skip alone proves nothing — still need a real success.]] - rationale - gateway/tests/test_soak_status.py
- [[_job()]] - code - gateway/tests/test_soak_status.py
- [[test_soak_status.py]] - code - gateway/tests/test_soak_status.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Incident_Response_Playbook__AgentShroud
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_pytest.ini]]

## Top bridge nodes
- [[TestClassify_1]] - degree 14, connects to 1 community