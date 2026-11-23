---
type: community
members: 27
---

# classify

**Members:** 27 nodes

## Members
- [[dot-test_255_is_unreachable()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_any_error_since_boot_blocks_regardless_of_successes()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_below_threshold_not_soaked()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_empty_heartbeat_file_skip_alone_is_not_soaked()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_empty_heartbeat_file_skip_does_not_mask_a_real_error()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_empty_heartbeat_file_skip_is_benign_not_blocking()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_empty_job_list()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_missing_state_key_does_not_crash()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_no_runs_since_boot_not_soaked()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_nonzero_is_fail()]] - code - gateway/tests/test_multi_host_test.py
- [[dot-test_one_success_since_boot_meets_default_threshold()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_other_skipped_status_counts_as_not_ok()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_runs_before_boot_are_ignored()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_zero_is_pass()]] - code - gateway/tests/test_multi_host_test.py
- [[2026-09-19 root cause 'heartbeat skipped empty-heartbeat-file' is OpenClaw's…]] - rationale - gateway/tests/test_soak_status.py
- [[A benign heartbeat skip must not hide an actual failing job.]] - rationale - gateway/tests/test_soak_status.py
- [[A job that last succeeded before this boot proves nothing about THIS deploy —…]] - rationale - gateway/tests/test_soak_status.py
- [[A skip for any OTHER reason (not the known-benign empty-heartbeat- file case…]] - rationale - gateway/tests/test_soak_status.py
- [[An actively-failing job since redeploy must block soak even if other jobs…]] - rationale - gateway/tests/test_soak_status.py
- [[Map a runner exit code to a HostStatus.]] - rationale - gateway/tools/multi_host_test.py
- [[TestClassify_1]] - code - gateway/tests/test_multi_host_test.py
- [[TestClassify_2]] - code - gateway/tests/test_soak_status.py
- [[Tests for scriptssoak_status.py's classify() — the soak-period gate. This gate…]] - rationale - gateway/tests/test_soak_status.py
- [[The benign skip alone proves nothing — still need a real success.]] - rationale - gateway/tests/test_soak_status.py
- [[_job()]] - code - gateway/tests/test_soak_status.py
- [[classify()_2]] - code - gateway/tools/multi_host_test.py
- [[test_soak_status.py]] - code - gateway/tests/test_soak_status.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/classify
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_multi_host_test.py]]
- 2 edges to [[_COMMUNITY_test_multi_host_test.py]]
- 1 edge to [[_COMMUNITY_run_multi_host]]

## Top bridge nodes
- [[classify()_2]] - degree 19, connects to 3 communities
- [[TestClassify_1]] - degree 5, connects to 2 communities
