---
type: community
members: 50
---

# discover_upstream_versions.py

**Members:** 50 nodes

## Members
- [[dot-test_gives_up_after_attempts_and_reraises_last_error()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_hermes_failure_is_reported_as_unknown_after_exhaustion()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_hermes_recovers_from_one_transient_failure()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_hung_hub_fetch_is_cut_by_deadline_and_retried()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_openclaw_recovers_from_one_transient_failure()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_passes_zero_based_attempt_index()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_propagates_fn_exception()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_raises_timeout_when_fn_hangs()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_retry_attempt_runs_with_ipv4_forced()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_returns_result_after_transient_failures()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_returns_value_when_fn_finishes_in_time()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[dot-test_single_attempt_never_sleeps()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[A fetch that never returns must not hang the unattended run. 2026-10-16 the…]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Any_7]] - code
- [[Call ``fn(attempt)`` up to ``attempts`` times; re-raise the last error if all…]] - rationale - scripts/discover_upstream_versions.py
- [[Discover the latest upstream releases of the tools AgentShroud wraps. WHY THIS…]] - rationale - scripts/discover_upstream_versions.py
- [[One attempt of ``fetch`` hard-bounded, IPv4-only after the first failure.]] - rationale - scripts/discover_upstream_versions.py
- [[Resolve the latest stable release of each wrapped tool. Each entry is…]] - rationale - scripts/discover_upstream_versions.py
- [[Run ``fn`` in a daemon thread; raise ``TimeoutError`` if it outlives…]] - rationale - scripts/discover_upstream_versions.py
- [[Tag records for a Docker Hub repository, newest first.]] - rationale - scripts/discover_upstream_versions.py
- [[TestCallWithDeadline]] - code - gateway/tests/test_discover_upstream_versions.py
- [[TestDiscoverRetries]] - code - gateway/tests/test_discover_upstream_versions.py
- [[TestRetry]] - code - gateway/tests/test_discover_upstream_versions.py
- [[Tests for scriptsdiscover_upstream_versions.py — latest-release discovery.…]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[The 2026-10-16 CLOSE_WAIT hang attempt 1 never returns; the hard deadline must…]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[Upstream fetches must survive a transient blip. 2026-10-16, dev host marvin…]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[_call_with_deadline()]] - code - scripts/discover_upstream_versions.py
- [[_digest_for_tag()]] - code - scripts/discover_upstream_versions.py
- [[_guarded_fetch()]] - code - scripts/discover_upstream_versions.py
- [[_retry()]] - code - scripts/discover_upstream_versions.py
- [[_run()]] - code - scripts/discover_upstream_versions.py
- [[always_fails()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[boom()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[discover()]] - code - scripts/discover_upstream_versions.py
- [[discover() applies the retry to both sources, independently.]] - rationale - gateway/tests/test_discover_upstream_versions.py
- [[discover_upstream_versions.py]] - code - scripts/discover_upstream_versions.py
- [[fetch_dockerhub_tags()]] - code - scripts/discover_upstream_versions.py
- [[flaky()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[fn()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[hub()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[hub()_1]] - code - gateway/tests/test_discover_upstream_versions.py
- [[hub()_2]] - code - gateway/tests/test_discover_upstream_versions.py
- [[hub()_3]] - code - gateway/tests/test_discover_upstream_versions.py
- [[is_stable]] - code - scripts/discover_upstream_versions.py
- [[main()]] - code - scripts/discover_upstream_versions.py
- [[npm()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[pick_latest_hermes_tag]] - code - scripts/discover_upstream_versions.py
- [[pick_latest_stable]] - code - scripts/discover_upstream_versions.py
- [[recorder()]] - code - gateway/tests/test_discover_upstream_versions.py
- [[test_discover_upstream_versions.py]] - code - gateway/tests/test_discover_upstream_versions.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/discover_upstream_versionspy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_UserSessionManager (4)]]
- 5 edges to [[_COMMUNITY_colima-health-check.sh]]
- 4 edges to [[_COMMUNITY_pick_latest_stable]]
- 3 edges to [[_COMMUNITY_egress_filter.py (4)]]
- 3 edges to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 2 edges to [[_COMMUNITY_UserSessionManager (5)]]
- 1 edge to [[_COMMUNITY_dockerbotshermesrun-standalone.sh (docker run launcher for Hermes)]]
- 1 edge to [[_COMMUNITY_plan_remediation]]

## Top bridge nodes
- [[discover_upstream_versions.py]] - degree 20, connects to 7 communities
- [[test_discover_upstream_versions.py]] - degree 13, connects to 4 communities
- [[discover()]] - degree 14, connects to 2 communities
- [[_guarded_fetch()]] - degree 9, connects to 2 communities
- [[_retry()]] - degree 9, connects to 1 community
