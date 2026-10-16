---
type: community
cohesion: 0.09
members: 56
---

# CronStateMonitor

**Cohesion:** 0.09 - loosely connected
**Members:** 56 nodes

## Members
- [[dot-__call__()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-__call__()_1]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-__init__()_20]] - code - gateway/security/cron_state_monitor.py
- [[dot-__init__()_21]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-__init__()_22]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-_dispatch_aggregate()]] - code - gateway/security/cron_state_monitor.py
- [[dot-_episode_id()]] - code - gateway/security/cron_state_monitor.py
- [[dot-_evaluate()]] - code - gateway/security/cron_state_monitor.py
- [[dot-_run()]] - code - gateway/security/cron_state_monitor.py
- [[dot-_safe_dispatch()]] - code - gateway/security/cron_state_monitor.py
- [[dot-check()_1]] - code - gateway/security/cron_state_monitor.py
- [[dot-parse_store()]] - code - gateway/security/cron_state_monitor.py
- [[dot-start()]] - code - gateway/security/cron_state_monitor.py
- [[dot-stop()]] - code - gateway/security/cron_state_monitor.py
- [[dot-test_alert_ids_stable_per_job_episode()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_corrupt_file_returns_empty()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_disabled_jobs_ignored()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_dispatch_failure_does_not_raise()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_first_sight_failing_alerts_once()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_flood_capped_with_aggregate_alert()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_hermes_jobs_reach_critical_via_observed_runs()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_job_name_capped_in_alert()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_malformed_consecutive_errors_does_not_blind_store()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_missing_file_returns_empty()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_multiple_stores_checked()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_ok_jobs_not_failing()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_ok_to_fail_dispatches_high_alert()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_oversized_store_skipped()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_parses_hermes_schema()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_parses_openclaw_schema()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_recovery_refail_realerts_through_real_dedup()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_recovery_resets_alerting()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_repeated_failure_escalates_to_critical()]] - code - gateway/tests/test_cron_state_monitor.py
- [[dot-test_start_is_idempotent()]] - code - gateway/tests/test_cron_state_monitor.py
- [[CronStateMonitor]] - code - gateway/security/cron_state_monitor.py
- [[Evaluate one job.  Returns 1 if a NEW episode was alerted.          Flood guard]] - rationale - gateway/security/cron_state_monitor.py
- [[JobState]] - code - gateway/security/cron_state_monitor.py
- [[Mimics AlertDispatcher's id-based 24h dedup — the real downstream.]] - rationale - gateway/tests/test_cron_state_monitor.py
- [[Normalized view of one bot cron job.]] - rationale - gateway/security/cron_state_monitor.py
- [[One poll pass over all stores.  Never raises.]] - rationale - gateway/security/cron_state_monitor.py
- [[Poll bot cron stores; dispatch AlertDispatcher alerts on failures.]] - rationale - gateway/security/cron_state_monitor.py
- [[Read one bot's cron store; tolerate absencecorruption.]] - rationale - gateway/security/cron_state_monitor.py
- [[Start the poll loop as an asyncio task (idempotent).]] - rationale - gateway/security/cron_state_monitor.py
- [[Task]] - code - gateway/security/cron_state_monitor.py
- [[TestAdversarial]] - code - gateway/tests/test_cron_state_monitor.py
- [[TestParsing]] - code - gateway/tests/test_cron_state_monitor.py
- [[TestTransitions]] - code - gateway/tests/test_cron_state_monitor.py
- [[_DedupDispatchFake]] - code - gateway/tests/test_cron_state_monitor.py
- [[_DispatchSpy]] - code - gateway/tests/test_cron_state_monitor.py
- [[_hermes_job()]] - code - gateway/tests/test_cron_state_monitor.py
- [[_hermes_store()]] - code - gateway/tests/test_cron_state_monitor.py
- [[_oc_job()]] - code - gateway/tests/test_cron_state_monitor.py
- [[_openclaw_store()]] - code - gateway/tests/test_cron_state_monitor.py
- [[cron_state_monitor.py]] - code - gateway/security/cron_state_monitor.py
- [[test_cron_state_monitor.py]] - code - gateway/tests/test_cron_state_monitor.py
- [[test_poll_loop_runs_and_stops()]] - code - gateway/tests/test_cron_state_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CronStateMonitor
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_AlertDispatcher]]

## Top bridge nodes
- [[CronStateMonitor]] - degree 36, connects to 2 communities
