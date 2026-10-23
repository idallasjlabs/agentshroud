---
type: community
cohesion: 0.11
members: 28
---

# _FakeUpstreamWS

**Cohesion:** 0.11 - loosely connected
**Members:** 28 nodes

## Members
- [[dot-test_any_error_since_boot_blocks_regardless_of_successes()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_below_threshold_not_soaked()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_empty_heartbeat_file_skip_alone_is_not_soaked()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_empty_heartbeat_file_skip_does_not_mask_a_real_error()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_empty_heartbeat_file_skip_is_benign_not_blocking()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_empty_job_list()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_missing_state_key_does_not_crash()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_no_runs_since_boot_not_soaked()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_one_success_since_boot_meets_default_threshold()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_other_skipped_status_counts_as_not_ok()]] - code - gateway/tests/test_soak_status.py
- [[dot-test_runs_before_boot_are_ignored()]] - code - gateway/tests/test_soak_status.py
- [[2026-09-19 root cause 'heartbeat skipped empty-heartbeat-file' is         Open]] - rationale - gateway/tests/test_soak_status.py
- [[A benign heartbeat skip must not hide an actual failing job.]] - rationale - gateway/tests/test_soak_status.py
- [[A job that last succeeded before this boot proves nothing about         THIS dep]] - rationale - gateway/tests/test_soak_status.py
- [[A skip for any OTHER reason (not the known-benign empty-heartbeat-         file]] - rationale - gateway/tests/test_soak_status.py
- [[An actively-failing job since redeploy must block soak even if         other job]] - rationale - gateway/tests/test_soak_status.py
- [[Any_47]] - code - scripts/soak_status.py
- [[OpenClaw isHeartbeatContentEffectivelyEmpty benign skip]] - concept - scripts/soak_status.py
- [[Return (soaked, message) for the given cron job list.      soaked=True only if a]] - rationale - scripts/soak_status.py
- [[TestClassify_2]] - code - gateway/tests/test_soak_status.py
- [[The benign skip alone proves nothing — still need a real success.]] - rationale - gateway/tests/test_soak_status.py
- [[_is_benign_skip]] - code - scripts/soak_status.py
- [[_is_benign_skip()]] - code - scripts/soak_status.py
- [[_job()]] - code - gateway/tests/test_soak_status.py
- [[classify()_2]] - code - scripts/soak_status.py
- [[main()_15]] - code - scripts/soak_status.py
- [[soak_status.py]] - code - scripts/soak_status.py
- [[test_soak_status.py]] - code - gateway/tests/test_soak_status.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_FakeUpstreamWS
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY__make_sanitizer()]]

## Top bridge nodes
- [[main()_15]] - degree 3, connects to 1 community
